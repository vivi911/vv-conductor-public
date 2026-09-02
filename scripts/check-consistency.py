#!/usr/bin/env python3
"""發布前一致性檢查。

這包的同一條規矩會出現在好幾個檔案裡（SKILL.md 給 AI 讀、conductor.md/指揮家.md 給人讀、
onboarding.md 是首次流程、references/ 是補充），而且現在有**兩個語言樹**：英文（repo 根目錄，
預設語言）與 zh-TW（Traditional Chinese，`zh-TW/` 底下）。手改其中一份、忘了另一份 —— 不管是
忘了同一語言的另一個檔案，還是忘了另一個語言樹 —— 規則就會互相矛盾，而且不會有任何錯誤訊息，
AI 只是選到不一樣的做法。

這支腳本就是攔這件事的。發布前跑，不綠不推。

    python3 scripts/check-consistency.py

⚠️ 寫新檢查時的鐵律：**用「禁止出現的講法」去掃全部檔案，不要用「我改過哪幾句」
去對答案。** 從自己的修改清單推導檢查項，必然漏掉你沒想到的地方——這支腳本
存在的原因，就是有人這樣驗過然後漏了。
"""

import contextlib
import io
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "vv-conductor"              # English track (default, repo root)
ROOT_ZH = ROOT / "zh-TW"
SKILL_ZH = ROOT_ZH / "skills" / "vv-conductor"          # Traditional Chinese track

# 這一行以下的樣式定義本身含有要偵測的字串，掃自己時要跳過
SELF_EXEMPT = "# leak-pattern"


def _is_git_ignored(path: Path) -> bool:
    """gitignore 掉的檔案永遠不會被發布，掃它只會製造擋不掉的假警報。

    在非 git 環境（例如 self_test() 的暫存資料夾）裡 `git check-ignore`
    會直接失敗，這時當作「沒被忽略」處理，行為退回舊版（照掃不誤），
    不會因為抓不到 git 而漏掉真正該擋的東西。
    """
    try:
        result = subprocess.run(
            ["git", "check-ignore", "-q", str(path)],
            cwd=ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return result.returncode == 0
    except OSError:
        return False


def docs():
    """規則檔全體（母體），涵蓋英文（預設，repo 根目錄）與 zh-TW 兩個語言樹；
    不是「我改過的檔案」；跳過 gitignore 掉的本機筆記。"""
    found = (
        list(ROOT.glob("*.md"))
        + list(SKILL.rglob("*.md"))
        + list(ROOT_ZH.glob("*.md"))
        + list(SKILL_ZH.rglob("*.md"))
    )
    return sorted(p for p in found if not _is_git_ignored(p))


def scripts():
    return sorted((ROOT / "scripts").glob("*.py"))


# ── 跨檔規矩：同一條規矩，任何檔案（任何語言樹）都不准出現「舊的／相反的」講法 ──
# 每條 = (規矩名, 禁止出現的 regex, 為什麼這樣寫會出事)
FORBIDDEN = [
    (
        "退版一律要使用者拍板",
        r"自動退版|任一項失敗就退版|automatic rollback is fine|any fail triggers rollback",  # leak-pattern
        "退版就是動正式流量。新手分不出乾淨退版與會弄髒資料的退版，而退版都發生在慌張的時候。",
    ),
    (
        "卡住時給三種回法",
        r"你回我這 4 句任一即可|4\. 我看一下再回",  # leak-pattern
        "四選項跟「只給一個推薦、不列選項」打架，且第四句沒有資訊量。",
    ),
    (
        "答完 6 題立即存檔",
        r"請把我剛剛回答的 6 題整理成 vv memory。」",  # leak-pattern
        "使用者已經說過要建立 Vault。問完卻要他再下一次指令，等於什麼都沒建。",
    ),
    (
        "不再詢問替教練改名",
        r"rename vv|want to give (?:me|the coach) a name|想幫(?:我|教練)取(?:個)?名字|替 vv 改名|你想怎麼叫這位陪跑教練",  # leak-pattern
        "教練固定叫 vv；導入只需要問 AI 應該怎麼稱呼使用者。",
    ),
    (
        "導入題數只能是 6 題",
        r"7[- ]question|7 questions|7 Vault questions|7 題|7 個問題|七題|第 7 題",  # leak-pattern
        "v1.7.2 的導入題數已定案；任何舊題數殘字都會讓公開說明互相矛盾。",
    ),
    (
        "唯一例外是卡住求拍板，不是 onboarding 收尾",
        r"onboarding closing list is the one|onboarding 收尾.{0,12}例外|the onboarding closing list in SKILL\.md",  # leak-pattern
        "onboarding 收尾已改成只給一句推薦，不再是選單，所以不再是例外。",
    ),
    (
        "同一必過項連三輪不過才停",
        r"The same gate fails twice|同一關失敗兩次",  # leak-pattern
        "停損門檻各檔不一致，AI 會選到不同的收手時機。",
    ),
]

# 複製空白原稿到使用者記憶庫，一定要有 no-clobber。
# 單獨處理是因為它要看「整行有沒有防護旗標」，不是單純比對字串。
COPY_LINE = re.compile(r"^\s*cp\b.*memory-templates.*~/vv-memory")  # leak-pattern
NO_CLOBBER = re.compile(r"(^|\s)(-[a-zA-Z]*n[a-zA-Z]*|--no-clobber)(\s|$)")

# 安裝 skill 的 cp：目標端必須先被 rm -rf 掉，否則第二次執行（＝更新動作）
# 在 macOS 上會複製到「已存在的同名資料夾裡面」變成 vv-conductor/vv-conductor，
# 舊版還在當家而且完全不報錯 —— 使用者以為更新了，其實沒有。2026-08-21 實測踩到。
INSTALL_CP = re.compile(r"\bcp\s+-[a-zA-Z]*[Rra][a-zA-Z]*\s+.*\bskills/vv-conductor\b.*~/\.(codex|claude)/skills")  # leak-pattern
RM_TARGET = re.compile(r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*\s+~/\.(codex|claude)/skills/vv-conductor\b")  # leak-pattern

# 兩個語言樹共用的必留項（語言無關：網址、ID、已經是英文的固定小節標題）
MUST_EXIST_COMMON = {
    "官網": "https://goaskvivi.com/",
    "台灣 LINE": "https://lin.ee/ZgPigfa",
    "小紅書號": "940160605",
    "禁止自編 6 題": "Never invent your own questions",
    "Vault 位置章節": "## Vault Location",
    "存檔章節": "### Save the Vault",
    "更新檢查章節": "## Update Check",
}
# 各語言樹自己的固定開場白（這句話兩邊必須是各自語言的版本，不是同一句）
MUST_EXIST_EN_ONLY = {
    "固定開場白（英文）": "Hi, I'm vv — the AI co-pilot coach Vivi built for you.",
}
MUST_EXIST_ZH_ONLY = {
    "固定開場白（中文）": "嗨，我是 vv——Vivi 老師為你打造的 AI 陪跑教練。",
}

LEAK = (
    r"美力|bebetterone|小巴黎|debalets|adflow|凱惠|"  # leak-pattern
    r"\bAndy\b|柏寰|祥哥|潘總|Jaxson|俊毅|oliveliao|"  # leak-pattern
    r"/Users/|~/小總|ROUTER\.md|vv-profile|接手憲法|"  # leak-pattern
    r"memory-api|gen-lang-client|Secret Manager|Firestore|"  # leak-pattern
    r"AIza[0-9A-Za-z_-]{20,}|sk-[0-9A-Za-z]{20,}"  # leak-pattern
)

EXTERNAL_REFS = {
    "AGENTS.md", "CLAUDE.md", "HANDOFF-LATEST.md",
    "SKILL.md", "README.md",
    "conductor.md", "boss-view.md",       # English track human-readable docs
    "指揮家.md", "vv-老闆視角.md",         # zh-TW track human-readable docs
}

# 反引號寫法與 markdown 連結寫法都要抓，只抓一種會漏
REF_PATTERNS = [
    re.compile(r"`([A-Za-z0-9_一-鿿][A-Za-z0-9_./一-鿿-]*\.(?:md|yaml))`"),
    re.compile(r"\]\(([A-Za-z0-9_一-鿿][A-Za-z0-9_./一-鿿-]*\.(?:md|yaml))\)"),
]


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def scan(paths, predicate):
    """回傳 [(檔案:行號, 行內容)]，自動跳過帶豁免標記的樣式定義行。"""
    out = []
    for p in paths:
        try:
            lines = p.read_text(encoding="utf-8").split("\n")
        except OSError as e:
            out.append((rel(p), f"<讀不到：{e}>"))
            continue
        for i, line in enumerate(lines, 1):
            if SELF_EXEMPT in line:
                continue
            if predicate(line):
                out.append((f"{rel(p)}:{i}", line.strip()[:70]))
    return out


def report(failures, name, hits, why=None):
    if hits:
        detail = "\n     ".join(f"{loc}  {txt}" for loc, txt in hits)
        failures.append(f"{name}" + (f"\n     原因：{why}" if why else "") + f"\n     {detail}")
        print(f"  ❌ {name}")
        for loc, txt in hits:
            print(f"       {loc}  {txt}")
    else:
        print(f"  ✅ {name}")


def check_forbidden(failures):
    print("【跨檔規矩】同一條規矩，有沒有檔案還留著相反的講法（兩個語言樹一起掃）")
    targets = docs() + scripts()
    for name, pattern, why in FORBIDDEN:
        rx = re.compile(pattern)
        report(failures, name, scan(targets, lambda l, rx=rx: bool(rx.search(l))), why)

    report(
        failures,
        "複製空白原稿一定要防覆蓋",
        scan(targets, lambda l: bool(COPY_LINE.search(l)) and not NO_CLOBBER.search(l)),
        "沒有 -n / --no-clobber 的 cp 會把使用者累積的記憶庫換成空白原稿，且救不回來。",
    )

    report(
        failures,
        "安裝 skill 的 cp 前面要先 rm -rf 目標端",
        _unguarded_install_cp(),
        "macOS 上 cp -R 到「已存在的同名資料夾」會複製進它裡面，變成 "
        "vv-conductor/vv-conductor。更新動作＝重跑安裝，所以少了 rm -rf 就是"
        "「使用者以為更新了、其實還在跑舊版」，而且不報錯。",
    )


def _unguarded_install_cp():
    """找出「前面沒有先 rm -rf 目標端」的安裝 cp 行。

    只看同一個 ``` 程式碼區塊內、這一行之前的內容——rm 寫在別的區塊或別的段落
    對照著貼的人不會執行到，等於沒有保護。
    """
    hits = []
    for p in docs():
        try:
            lines = p.read_text(encoding="utf-8").split("\n")
        except OSError as e:
            hits.append((rel(p), f"<讀不到：{e}>"))
            continue
        guarded_since_fence = False
        for i, line in enumerate(lines, 1):
            if line.lstrip().startswith("```"):
                guarded_since_fence = False       # 換區塊，保護重新計算
                continue
            if SELF_EXEMPT in line:
                continue
            if RM_TARGET.search(line):
                guarded_since_fence = True
            if INSTALL_CP.search(line) and not guarded_since_fence:
                hits.append((f"{rel(p)}:{i}", line.strip()[:70]))
    return hits


def _check_must_exist_one(failures, skill_root, label, needles):
    path = skill_root / "SKILL.md"
    if not path.exists():
        failures.append(f"找不到 {rel(path)}，這不是檢查失敗，是包壞了或路徑錯了")
        print(f"  ❌ 找不到 {rel(path)}")
        return
    text = path.read_text(encoding="utf-8")
    for name, needle in needles.items():
        if needle in text:
            print(f"  ✅ [{label}] {name}")
        else:
            failures.append(f"必留項不見了（{label}）：{name}")
            print(f"  ❌ [{label}] {name}")


def check_must_exist(failures):
    print("\n【必留項】公開包原本就有的東西，有沒有被改掉或弄丟（英文＋zh-TW 各自檢查）")
    en_needles = {**MUST_EXIST_COMMON, **MUST_EXIST_EN_ONLY}
    zh_needles = {**MUST_EXIST_COMMON, **MUST_EXIST_ZH_ONLY}
    _check_must_exist_one(failures, SKILL, "英文", en_needles)
    _check_must_exist_one(failures, SKILL_ZH, "zh-TW", zh_needles)


def check_leak(failures):
    print("\n【洩漏】客戶名、真人名、內部路徑、內部基建、金鑰")
    rx = re.compile(LEAK)
    report(failures, "零洩漏", scan(docs() + scripts(), lambda l: bool(rx.search(l))))


def collect_refs(path: Path):
    text = path.read_text(encoding="utf-8")
    for rx in REF_PATTERNS:
        for m in rx.findall(text):
            if m in EXTERNAL_REFS or m.startswith(("~", "/")) or "YYYY" in m or "待填" in m or "TBD" in m:
                continue
            yield m


def check_refs(failures):
    print("\n【斷鏈】skill 裝到別台電腦後，檔案引用還找得到嗎（英文＋zh-TW 各自檢查）")
    bad, total = [], 0
    for skill_root in (SKILL, SKILL_ZH):
        for p in skill_root.rglob("*.md"):
            for ref in collect_refs(p):
                total += 1
                if not ((p.parent / ref).exists() or (skill_root / ref).exists()):
                    bad.append((rel(p), ref))
    if bad:
        failures.append("引用斷鏈：\n     " + "\n     ".join(f"{a} → {b}" for a, b in bad))
        print(f"  ❌ {len(bad)} 條斷鏈（共檢查 {total} 條）")
        for a, b in bad:
            print(f"       {a} → {b}")
    else:
        print(f"  ✅ {total} 條引用零斷鏈")


def self_test():
    """反向自檢：真的跑一遍 check_forbidden／check_must_exist／check_leak／check_refs，
    不是只測正則字串本身。

    舊版的做法是拿正則直接對一個字串做 re.search，這只證明正則寫得出來，
    完全沒證明那個正則真的被掛進 check_* 函式的執行路徑——把 check_forbidden
    整支換成 `pass`，舊版自檢照樣全線通過。

    新做法：搭一個假規則資料夾（暫存目錄，用完即刪），塞英文與 zh-TW 兩個語言樹
    各一份「乾淨樣本」，把全域 ROOT／SKILL／ROOT_ZH／SKILL_ZH 指過去，直接呼叫
    真正的四個 check_* 函式蒐集 failures，先驗證兩個語言樹的乾淨樣本都是零 failure；
    再疊上「已知踩了全部五類問題的壞樣本」（並同時拿掉兩個語言樹各自的固定開場白），
    驗證五類問題＋兩個語言樹的必留項都被點名。任何一個 check_* 被掏空或改壞，這裡都會抓到。
    """
    global ROOT, SKILL, ROOT_ZH, SKILL_ZH

    orig = (ROOT, SKILL, ROOT_ZH, SKILL_ZH)
    tmp = Path(tempfile.mkdtemp(prefix="vv-selftest-"))
    try:
        skill_en = tmp / "skills" / "vv-conductor"
        skill_en.mkdir(parents=True)
        root_zh = tmp / "zh-TW"
        skill_zh = root_zh / "skills" / "vv-conductor"
        skill_zh.mkdir(parents=True)

        common_lines = [
            "https://goaskvivi.com/",
            "https://lin.ee/ZgPigfa",
            "940160605",
            "Never invent your own questions",
            "## Vault Location",
            "### Save the Vault",
            "## Update Check",
            "See `README.md` for details.",
        ]
        opening_en = "Hi, I'm vv — the AI co-pilot coach Vivi built for you."
        opening_zh = "嗨，我是 vv——Vivi 老師為你打造的 AI 陪跑教練。"

        # 乾淨樣本也放一組「有先 rm -rf 才 cp」的安裝指令，證明正確寫法不會被誤報
        guarded_install = [
            "```bash",
            "rm -rf ~/.codex/skills/vv-conductor",
            "cp -R x/skills/vv-conductor ~/.codex/skills/vv-conductor",
            "```",
        ]
        clean_en_md = "\n".join([opening_en] + common_lines + guarded_install)
        clean_zh_md = "\n".join([opening_zh] + common_lines + guarded_install)
        (skill_en / "SKILL.md").write_text(clean_en_md, encoding="utf-8")
        (skill_zh / "SKILL.md").write_text(clean_zh_md, encoding="utf-8")
        (tmp / "README.md").write_text("clean readme, nothing to see here.", encoding="utf-8")
        (root_zh / "README.md").write_text("clean readme zh, nothing to see here.", encoding="utf-8")

        with contextlib.redirect_stdout(io.StringIO()):
            ROOT, SKILL, ROOT_ZH, SKILL_ZH = tmp, skill_en, root_zh, skill_zh
            clean_failures = []
            check_forbidden(clean_failures)
            check_must_exist(clean_failures)
            check_leak(clean_failures)
            check_refs(clean_failures)

            # 疊在乾淨樣本上加壞內容、同時拿掉兩個語言樹各自的固定開場白，
            # 六類問題一次到齊：違禁講法、漏防覆蓋、英文必留項不見、zh-TW 必留項
            # 不見、洩漏字串、引用斷鏈。
            bad_en_md = clean_en_md.replace(opening_en + "\n", "") + "\n" + "\n".join(
                [
                    "這裡寫了自動退版",  # leak-pattern
                    "路徑是 /Users/someone/x",  # leak-pattern
                    "See `不存在的檔案.md` for details.",
                    "cp -R x/memory-templates/*.md ~/vv-memory/",  # leak-pattern
                    "```bash",
                    "cp -R x/skills/vv-conductor ~/.codex/skills/vv-conductor",  # leak-pattern
                    "```",
                ]
            )
            bad_zh_md = clean_zh_md.replace(opening_zh + "\n", "")
            (skill_en / "SKILL.md").write_text(bad_en_md, encoding="utf-8")
            (skill_zh / "SKILL.md").write_text(bad_zh_md, encoding="utf-8")

            bad_failures = []
            check_forbidden(bad_failures)
            check_must_exist(bad_failures)
            check_leak(bad_failures)
            check_refs(bad_failures)
    finally:
        ROOT, SKILL, ROOT_ZH, SKILL_ZH = orig
        shutil.rmtree(tmp, ignore_errors=True)

    bad_joined = "\n".join(bad_failures)
    cases = {
        "乾淨樣本零 failure": not clean_failures,
        "跨檔規矩(check_forbidden)": "退版一律要使用者拍板" in bad_joined,
        "防覆蓋(check_forbidden)": "複製空白原稿一定要防覆蓋" in bad_joined,
        "安裝cp要先rm(check_forbidden)": "安裝 skill 的 cp 前面要先 rm -rf 目標端" in bad_joined,
        "英文必留項(check_must_exist)": "必留項不見了（英文）" in bad_joined,
        "zh-TW必留項(check_must_exist)": "必留項不見了（zh-TW）" in bad_joined,
        "洩漏(check_leak)": "零洩漏" in bad_joined,
        "斷鏈(check_refs)": "引用斷鏈" in bad_joined,
    }
    bad = [k for k, v in cases.items() if not v]
    if bad:
        print(f"\n【反向自檢】❌ 這幾種檢查失去作用：{'、'.join(bad)}")
        return False
    print(f"\n【反向自檢】✅ {len(cases)} 種檢查都確認有效（跑的是真正的 check_* 函式，不是只測正則）")
    return True


def main():
    if not self_test():
        print("🔴 腳本自檢沒過，不要相信這支腳本現在的任何結果，先別往下跑")
        return 2

    all_docs = docs()
    if not all_docs:
        print("🔴 找不到任何規則檔，路徑可能錯了")
        return 2
    print(f"檢查 {len(all_docs)} 份規則檔（英文＋zh-TW）+ {len(scripts())} 支腳本\n")

    failures = []
    check_forbidden(failures)
    check_must_exist(failures)
    check_leak(failures)
    check_refs(failures)

    print()
    if failures:
        print(f"🔴 {len(failures)} 項未過，不可發布：\n")
        for f in failures:
            print(f"  ・{f}\n")
        return 1
    print("🟢 全部通過，可以發布")
    return 0


if __name__ == "__main__":
    sys.exit(main())
