#!/usr/bin/env python3
"""產生 README 用的動態終端機示範（純 SVG，內嵌 CSS 動畫，不需要外部工具）。

GitHub README 會把 SVG 當一般 <img> 嵌進頁面，瀏覽器會照樣播放 SVG 內建的 CSS 動畫，
所以不用錄影、不用外部工具（VHS／asciinema／ffmpeg），純文字生成就有「動態介紹」的效果。
這是 aider（Aider-AI/aider）screencast.svg 用的同一招。

產生兩組、共四個檔：

1. `assets/demo-compare-{en,zh}.svg` — 左右對比：沒裝 vv vs 裝了 vv。
   左邊每次都要重打一長串背景，AI 還是要反問；右邊只打兩個字 `vv`，
   直接接上次進度。兩邊用同一個版面格線，左邊輸入區塞滿、右邊幾乎空白，
   那個「空白」本身就是重點。
2. `assets/demo-{en,zh}.svg` — 單一情境：紅燈攔截。示範 vv 的第二個價值：
   會動的事情先問過你，不是悶頭做完才說。

用法：
    python3 scripts/make-demo-svg.py

改內容請改下面 COMPARE / SAFETY 這兩個字典，不要手改產出的 svg
——手改的東西下次跑這支腳本會被蓋掉。
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

# ---- 色票，跟 docs/index.html 落地頁同一套（副駕領航員視覺）----
ASPHALT = "#14171f"
ASPHALT_2 = "#1c202b"
LINE = "#333a4d"
FOG = "#9aa1b2"
FOG_DIM = "#6b7284"
MIST = "#f4f1e8"
AMBER = "#e8a33d"

FONT = 15
# 等寬字在 font-size 15 的字元寬度。只在對比版的 right_input 逐字定位與游標定位用到。
# ⚠️ 這個估算只對 ASCII 成立：中日韓字在同一個字級大約是兩倍寬，會排到重疊。
# 所以 COMPARE 的 right_input 必須維持純 ASCII（現在是 "vv"）。要改成中文的話，
# 得改走「整行一次浮現」那條路（build_safety 的做法），不能逐字。
ADV = 9.0

# ── 左右對比版 ────────────────────────────────────────────────────────────
COMPARE = {
    "en": {
        "out": ASSETS / "demo-compare-en.svg",
        "left_title": "without vv",
        "right_title": "with vv",
        "left_input": [
            "I run an online store. Last week I was",
            "rewriting the fall campaign copy, got",
            "halfway, and the client deck still isn't",
            "done either. Can you help me...",
        ],
        "left_label": "AI",
        "left_reply": [
            "Sure — can you tell me more about",
            "your product and who the client is?",
        ],
        "right_input": "vv",
        "right_label": "vv",
        "right_reply": [
            "You're back. Fall campaign copy is",
            "on draft 3 — next up is scheduling.",
            "[Client deck] is still waiting on them.",
            "Which one first?",
        ],
    },
    "zh": {
        "out": ASSETS / "demo-compare-zh.svg",
        "left_title": "沒裝 vv",
        "right_title": "裝了 vv",
        "left_input": [
            "我是做電商的，上週在改秋季",
            "檔期文案，改到一半，客戶提案",
            "簡報也還沒做完，你可以幫我…",
        ],
        "left_label": "AI",
        "left_reply": [
            "好的，可以再多說一點你的",
            "產品和客戶背景嗎？",
        ],
        "right_input": "vv",
        "right_label": "vv",
        "right_reply": [
            "你回來了。秋季檔期文案寫到",
            "第 3 版，下一步是排上架時間。",
            "［客戶提案］還卡在等對方回覆。",
            "要先接哪一個？",
        ],
    },
}

# ── 單一情境版：紅燈攔截 ──────────────────────────────────────────────────
SAFETY = {
    "en": {
        "out": ASSETS / "demo-en.svg",
        "title": "vv — claude",
        "typed": "vv can I just ship this?",
        "label": "vv",
        "reply": [
            "This one's a red light — it messages real",
            "customers. I'll prep the list and the copy",
            "for you to look at; I only send after you",
            "say go.",
        ],
    },
    "zh": {
        "out": ASSETS / "demo-zh.svg",
        "title": "vv — claude",
        "typed": "vv 這個可以直接上線嗎？",
        "label": "vv",
        "reply": [
            "這步是紅燈：會發訊息給真的客人。",
            "我先把名單和文案準備好給你看，",
            "你按過我才送出。",
        ],
    },
}


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def chrome(pid: str, x: int, y: int, w: int, h: int, title: str, title_color: str) -> str:
    """一個終端機視窗的外框：圓角底、標題列、三顆燈、分隔線。"""
    return f'''
    <clipPath id="clip-{pid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" ry="14"/></clipPath>
    <g clip-path="url(#clip-{pid})">
      <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{ASPHALT}"/>
      <rect x="{x}" y="{y}" width="{w}" height="40" fill="{ASPHALT_2}"/>
      <line x1="{x}" y1="{y + 40}" x2="{x + w}" y2="{y + 40}" stroke="{LINE}" stroke-width="1"/>
      <circle cx="{x + 22}" cy="{y + 20}" r="5.5" fill="#ff5f56"/>
      <circle cx="{x + 40}" cy="{y + 20}" r="5.5" fill="#ffbd2e"/>
      <circle cx="{x + 58}" cy="{y + 20}" r="5.5" fill="#27c93f"/>
      <text class="chrome-title" x="{x + w / 2}" y="{y + 25}" text-anchor="middle" font-size="12.5" fill="{title_color}">{esc(title)}</text>
    </g>'''


def anim_line(cls: str, x: float, y: float, content: str, size: float, fill: str, weight: str = "") -> str:
    w = f' font-weight="{weight}"' if weight else ""
    return f'<text class="reveal {cls}" x="{x:.0f}" y="{y:.0f}" font-size="{size}" fill="{fill}"{w}>{esc(content)}</text>'


def base_style(cycle: float, hold_until: float, rules: list) -> str:
    """所有動畫共用的 CSS：整段循環淡出、逐行浮現、游標閃爍。

    hold_until 在這裡夾制，呼叫端不用各自記得 min()——忘記夾的話淡出關鍵影格會
    落在 100% 之後，整段就不會淡出，循環變成硬切。
    """
    hold_until = max(0.0, min(hold_until, cycle - 0.5))
    fade_pct = hold_until / cycle * 100
    return f'''  <style>
    text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Noto Sans TC", sans-serif; }}
    .chrome-title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC", sans-serif; }}
    .cycle {{ animation: cyclefade {cycle}s linear infinite; }}
    @keyframes cyclefade {{
      0% {{ opacity: 1; }}
      {fade_pct:.1f}% {{ opacity: 1; }}
      99.9% {{ opacity: 0; }}
      100% {{ opacity: 0; }}
    }}
    .reveal {{ opacity: 0; animation: revealin {cycle}s ease-out infinite; }}
    @keyframes revealin {{
      0% {{ opacity: 0; }}
      0.4% {{ opacity: 1; }}
      99.9% {{ opacity: 1; }}
      100% {{ opacity: 0; }}
    }}
    .caret {{ animation: caretblink 1.05s steps(1) infinite; }}
    @keyframes caretblink {{ 0%,49% {{ opacity: 1; }} 50%,100% {{ opacity: 0; }} }}
{chr(10).join("    " + r for r in rules)}
  </style>'''


# ══════════════════════════════════════════════════════════════════════════
def build_compare(cfg: dict) -> str:
    W, H = 1040, 356
    PW, GAP = 500, 40
    PY, PH = 6, 344
    LX, RX = 0, PW + GAP

    cycle = 11.0
    pad = 24
    y_cmd = PY + 72          # `$ claude`
    y_in = PY + 110          # 使用者輸入第一行
    line_h = 24
    y_reply = PY + 240       # 回覆區（兩邊對齊同一條格線，左滿右空＝重點）

    rules, body = [], []

    # ---- 左：沒裝 vv ----
    body.append(chrome("l", LX, PY, PW, PH, cfg["left_title"], FOG_DIM))
    left = [f'<text x="{LX + pad}" y="{y_cmd}" font-size="{FONT}" fill="{FOG_DIM}">$ claude</text>']
    left.append(f'<text x="{LX + pad}" y="{y_in}" font-size="{FONT}" fill="{FOG_DIM}">&gt;</text>')

    t = 0.9
    for i, ln in enumerate(cfg["left_input"]):
        cls = f"li{i}"
        rules.append(f".{cls}{{animation-delay:{t:.2f}s;}}")
        left.append(anim_line(cls, LX + pad + 24, y_in + i * line_h, ln, FONT, MIST))
        t += 0.42

    t += 0.55
    rules.append(f".llab{{animation-delay:{t:.2f}s;}}")
    left.append(anim_line("llab", LX + pad, y_reply, cfg["left_label"], FONT, FOG, "700"))
    for i, ln in enumerate(cfg["left_reply"]):
        cls = f"lr{i}"
        rules.append(f".{cls}{{animation-delay:{(t + i * 0.38):.2f}s;}}")
        left.append(anim_line(cls, LX + pad + 46, y_reply + i * line_h, ln, FONT, FOG))
    left_end = t + len(cfg["left_reply"]) * 0.38

    # ---- 右：裝了 vv ----
    body.append(chrome("r", RX, PY, PW, PH, cfg["right_title"], AMBER))
    right = [f'<text x="{RX + pad}" y="{y_cmd}" font-size="{FONT}" fill="{FOG_DIM}">$ claude</text>']
    right.append(f'<text x="{RX + pad}" y="{y_in}" font-size="{FONT}" fill="{AMBER}">&gt;</text>')

    typed = cfg["right_input"]
    tx = RX + pad + 24
    for i, ch in enumerate(typed):
        d = 0.9 + i * 0.16
        cls = f"rc{i}"
        rules.append(f".{cls}{{animation-delay:{d:.2f}s;}}")
        right.append(anim_line(cls, tx + i * ADV, y_in, ch, FONT, MIST))
    typed_end = 0.9 + len(typed) * 0.16
    # 游標要跟著打字一起出現，所以包一層 reveal（延遲＝開始打字的時間），
    # 內層才做閃爍；直接把 caret 放外面的話它從第 0 秒就在閃。
    rules.append(".rcaret{animation-delay:0.90s;}")
    right.append(
        f'<g class="reveal rcaret"><rect class="caret" x="{tx + len(typed) * ADV:.0f}" y="{y_in - 12}" width="8" height="16" fill="{AMBER}"/></g>'
    )

    t = typed_end + 0.5
    rules.append(f".rlab{{animation-delay:{t:.2f}s;}}")
    right.append(anim_line("rlab", RX + pad, y_reply, cfg["right_label"], FONT, AMBER, "700"))
    for i, ln in enumerate(cfg["right_reply"]):
        cls = f"rr{i}"
        rules.append(f".{cls}{{animation-delay:{(t + i * 0.38):.2f}s;}}")
        right.append(anim_line(cls, RX + pad + 46, y_reply + i * line_h, ln, FONT, MIST))
    right_end = t + len(cfg["right_reply"]) * 0.38

    style = base_style(cycle, max(left_end, right_end) + 3.4, rules)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Side by side: without vv you retype your background every time and the AI still asks for more; with vv you type two letters and it picks up where you left off.">
{style}
  {"".join(body)}
  <g class="cycle">
    {"".join(left)}
    {"".join(right)}
  </g>
</svg>
'''


# ══════════════════════════════════════════════════════════════════════════
def build_safety(cfg: dict) -> str:
    W, H = 760, 300
    PY, PH = 6, 288
    cycle = 10.0
    pad = 30
    y_cmd = PY + 74
    y_in = PY + 112
    y_reply = PY + 172
    line_h = 27

    rules = []
    body = chrome("s", 0, PY, W, PH, cfg["title"], FOG)

    content = [f'<text x="{pad}" y="{y_cmd}" font-size="16" fill="{FOG_DIM}">$ claude</text>']
    content.append(f'<text x="{pad}" y="{y_in}" font-size="16" fill="{AMBER}">&gt;</text>')

    typed_start = 0.9
    rules.append(f".styped{{animation-delay:{typed_start:.2f}s;}}")
    content.append(anim_line("styped", pad + 26, y_in, cfg["typed"], 16, MIST))
    typed_end = typed_start + 0.4  # 整行一次浮現，不做逐字，所以固定給一個「讀完」的間隔

    t = typed_end + 0.6
    rules.append(f".slab{{animation-delay:{t:.2f}s;}}")
    content.append(anim_line("slab", pad, y_reply, cfg["label"], 16, AMBER, "700"))
    for i, ln in enumerate(cfg["reply"]):
        cls = f"sr{i}"
        rules.append(f".{cls}{{animation-delay:{(t + i * 0.42):.2f}s;}}")
        content.append(anim_line(cls, pad + 56, y_reply + i * line_h, ln, 16, MIST))
    end = t + len(cfg["reply"]) * 0.42

    style = base_style(cycle, end + 3.2, rules)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Terminal demo: asking vv to ship something, and vv stopping to ask first because it would message real customers.">
{style}
  {body}
  <g class="cycle">
    {"".join(content)}
  </g>
</svg>
'''


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    for cfg in COMPARE.values():
        svg = build_compare(cfg)
        cfg["out"].write_text(svg, encoding="utf-8")
        print(f"wrote {cfg['out'].relative_to(ROOT)} ({len(svg)} bytes)")
    for cfg in SAFETY.values():
        svg = build_safety(cfg)
        cfg["out"].write_text(svg, encoding="utf-8")
        print(f"wrote {cfg['out'].relative_to(ROOT)} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
