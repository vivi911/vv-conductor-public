#!/usr/bin/env python3
"""發布前一致性檢查。

這包的同一條規矩會出現在好幾個檔案裡（SKILL.md 給 AI 讀、指揮家.md 給人讀、
onboarding.md 是首次流程、references/ 是補充）。手改其中一份、忘了另一份，
規則就會互相矛盾，而且不會有任何錯誤訊息——AI 只是選到不一樣的做法。

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
SKILL = ROOT / "skills" / "vv-conductor"

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
    """規則檔全體（母體），不是「我改過的檔案」；跳過 gitignore 掉的本機筆記。"""
    found = list(ROOT.glob("*.md")) + list(SKILL.rglob("*.md"))
    return sorted(p for p in found if not _is_git_ignored(p))


def scripts():
    return sorted((ROOT / "scripts").glob("*.py"))


# ── 跨檔規矩：同一條規矩，任何檔案都不准出現「舊的／相反的」講法 ──────────────
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
        "答完 7 題立即存檔",
        r"請把我剛剛回答的 7 題整理成 vv memory。」",  # leak-pattern
        "使用者已經說過要建立 Vault。問完卻要他再下一次指令，等於什麼都沒建。",
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

MUST_EXIST = {
    "固定開場白": "嗨，我是 vv——Vivi 老師為你打造的 AI 陪跑教練。",
    "官網": "https://goaskvivi.com/",
    "台灣 LINE": "https://lin.ee/ZgPigfa",
    "小紅書號": "940160605",
    "禁止自編 7 題": "Never invent your own questions",
    "Vault 位置章節": "## Vault Location",
    "存檔章節": "### Save the Vault",
    "更新檢查章節": "## Update Check",
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
    "SKILL.md", "指揮家.md", "vv-老闆視角.md", "README.md",
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
    print("【跨檔規矩】同一條規矩，有沒有檔案還留著相反的講法")
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


def check_must_exist(failures):
    print("\n【必留項】公開包原本就有的東西，有沒有被改掉或弄丟")
    path = SKILL / "SKILL.md"
    if not path.exists():
        failures.append(f"找不到 {rel(path)}，這不是檢查失敗，是包壞了或路徑錯了")
        print(f"  ❌ 找不到 {rel(path)}")
        return
    text = path.read_text(encoding="utf-8")
    for name, needle in MUST_EXIST.items():
        if needle in text:
            print(f"  ✅ {name}")
        else:
            failures.append(f"必留項不見了：{name}")
            print(f"  ❌ {name}")


def check_leak(failures):
    print("\n【洩漏】客戶名、真人名、內部路徑、內部基建、金鑰")
    rx = re.compile(LEAK)
    report(failures, "零洩漏", scan(docs() + scripts(), lambda l: bool(rx.search(l))))


def collect_refs(path: Path):
    text = path.read_text(encoding="utf-8")
    for rx in REF_PATTERNS:
        for m in rx.findall(text):
            if m in EXTERNAL_REFS or m.startswith(("~", "/")) or "YYYY" in m or "待填" in m:
                continue
            yield m


def check_refs(failures):
    print("\n【斷鏈】skill 裝到別台電腦後，檔案引用還找得到嗎")
    bad, total = [], 0
    for p in SKILL.rglob("*.md"):
        for ref in collect_refs(p):
            total += 1
            if not ((p.parent / ref).exists() or (SKILL / ref).exists()):
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

    新做法：搭一個假規則資料夾（暫存目錄，用完即刪），塞一份「乾淨樣本」和
    一份「已知踩了全部五類問題的壞樣本」，把全域 ROOT／SKILL 指過去，
    直接呼叫真正的四個 check_* 函式蒐集 failures，再拆封驗證：
    乾淨樣本要零 failure、壞樣本五類問題要五個都被點名。
    任何一個 check_* 被掏空或改壞，這裡都會抓到。
    """
    global ROOT, SKILL

    orig_root, orig_skill = ROOT, SKILL
    tmp = Path(tempfile.mkdtemp(prefix="vv-selftest-"))
    try:
        skill = tmp / "skills" / "vv-conductor"
        skill.mkdir(parents=True)

        clean_skill_md = "\n".join(
            [
                "嗨，我是 vv——Vivi 老師為你打造的 AI 陪跑教練。",
                "https://goaskvivi.com/",
                "https://lin.ee/ZgPigfa",
                "940160605",
                "Never invent your own questions",
                "## Vault Location",
                "### Save the Vault",
                "## Update Check",
                "See `README.md` for details.",
            ]
        )
        (skill / "SKILL.md").write_text(clean_skill_md, encoding="utf-8")
        (tmp / "README.md").write_text("clean readme, nothing to see here.", encoding="utf-8")

        with contextlib.redirect_stdout(io.StringIO()):
            ROOT, SKILL = tmp, skill
            clean_failures = []
            check_forbidden(clean_failures)
            check_must_exist(clean_failures)
            check_leak(clean_failures)
            check_refs(clean_failures)

            # 疊在乾淨樣本上加壞內容、同時拿掉一個必留項，五類問題一次到齊：
            # 違禁講法、漏防覆蓋、必留項不見、洩漏字串、引用斷鏈。
            bad_skill_md = clean_skill_md.replace(
                "嗨，我是 vv——Vivi 老師為你打造的 AI 陪跑教練。\n", ""
            ) + "\n" + "\n".join(
                [
                    "這裡寫了自動退版",  # leak-pattern
                    "路徑是 /Users/someone/x",  # leak-pattern
                    "See `不存在的檔案.md` for details.",
                    "cp -R x/memory-templates/*.md ~/vv-memory/",  # leak-pattern
                ]
            )
            (skill / "SKILL.md").write_text(bad_skill_md, encoding="utf-8")

            bad_failures = []
            check_forbidden(bad_failures)
            check_must_exist(bad_failures)
            check_leak(bad_failures)
            check_refs(bad_failures)
    finally:
        ROOT, SKILL = orig_root, orig_skill
        shutil.rmtree(tmp, ignore_errors=True)

    bad_joined = "\n".join(bad_failures)
    cases = {
        "跨檔規矩(check_forbidden)": not clean_failures and "退版一律要使用者拍板" in bad_joined,
        "防覆蓋(check_forbidden)": "複製空白原稿一定要防覆蓋" in bad_joined,
        "必留項(check_must_exist)": "必留項不見了" in bad_joined,
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
    print(f"檢查 {len(all_docs)} 份規則檔 + {len(scripts())} 支腳本\n")

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
