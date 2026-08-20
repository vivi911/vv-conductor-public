#!/usr/bin/env python3
"""產生 README 最上面用的動態終端機示範（純 SVG，內嵌 CSS 動畫，不需要外部工具）。

GitHub README 會把 SVG 當一般 <img> 嵌進頁面，瀏覽器會照樣播放 SVG 內建的 CSS 動畫，
所以不用錄影、不用外部工具（VHS／asciinema／ffmpeg），純文字生成就有「動態介紹」的效果。
這是 aider（Aider-AI/aider）screencast.svg 用的同一招。

用法：
    python3 scripts/make-demo-svg.py

會覆寫 assets/demo-en.svg 與 assets/demo-zh.svg。改內容請改下面 DEMOS 這個字典，
不要手改產出的 svg 檔——手改的東西下次跑這支腳本會被蓋掉。
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

WIDTH = 880
HEIGHT = 360
CYCLE = 9.0  # 整個循環秒數，所有動畫都要在這個週期內對齊，才會同步重播

DEMOS = {
    "en": {
        "out": ASSETS / "demo-en.svg",
        "prompt": "claude",
        "typed": "hi",
        "vv_label": "vv",
        "lines": [
            "You're back. Landing page copy is done —",
            "next step: add the pricing section.",
            "[Pricing page] is stuck on your review,",
            "[Q3 roadmap] hasn't started. Which first?",
        ],
    },
    "zh": {
        "out": ASSETS / "demo-zh.svg",
        "prompt": "claude",
        "typed": "hi",
        "vv_label": "vv",
        "lines": [
            "你回來了。落地頁文案寫完了——",
            "下一步是加上定價區塊。",
            "［定價頁］卡在等你審核，",
            "［Q3 規劃］還沒開始。要先接哪一個？",
        ],
    },
}

# ---- 色票，跟 docs/index.html 落地頁同一套（副駕領航員視覺）----
ASPHALT = "#14171f"
ASPHALT_2 = "#1c202b"
LINE = "#333a4d"
FOG = "#9aa1b2"
MIST = "#f4f1e8"
AMBER = "#e8a33d"


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def typing_tspans(text: str, start: float, char_dur: float = 0.09):
    """把字串拆成一串 tspan，每個字元自己的 opacity keyframe，依序 reveal。"""
    out = []
    for i, ch in enumerate(text):
        delay = start + i * char_dur
        cls = f"ch ch-d{int(delay * 1000)}"
        out.append(f'<tspan class="{cls}">{esc(ch)}</tspan>')
    return "".join(out), start + len(text) * char_dur


def build_svg(cfg: dict) -> str:
    prompt = esc(cfg["prompt"])
    typed = cfg["typed"]
    vv_label = esc(cfg["vv_label"])
    lines = cfg["lines"]

    typed_tspans, typed_end = typing_tspans(typed, start=0.6)
    cursor_hide_at = typed_end + 0.15

    # response 區塊：每行自己的 fade+rise keyframe，用 animation-delay 依序出現
    resp_start = typed_end + 0.55
    line_gap = 0.42
    resp_svg_lines = []
    style_rules = []
    y0 = 210
    line_h = 30
    for i, line in enumerate(lines):
        delay = resp_start + i * line_gap
        line_cls = f"resp-line{i}"
        style_rules.append(
            f".{line_cls}{{animation-delay:{delay:.2f}s;}}"
        )
        resp_svg_lines.append(
            f'<text class="resp {line_cls}" x="150" y="{y0 + i * line_h}" font-size="17" fill="{MIST}">{esc(line)}</text>'
        )
    last_line_end = resp_start + (len(lines) - 1) * line_gap + 0.5

    fade_out_start = max(last_line_end + 2.4, CYCLE - 1.2)
    fade_out_dur = CYCLE - fade_out_start

    # 個別字元 keyframe（打字機效果用）要各自產生一條 CSS rule，因為 delay 各不同
    char_rules = []
    seen = set()
    for text, start in ((typed, 0.6),):
        for i, ch in enumerate(text):
            d = start + i * 0.09
            key = int(d * 1000)
            if key in seen:
                continue
            seen.add(key)
            char_rules.append(f".ch-d{key}{{animation-delay:{d:.2f}s;}}")

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}" role="img" aria-label="vv terminal demo">
  <defs>
    <clipPath id="rounded"><rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" rx="14" ry="14"/></clipPath>
  </defs>
  <style>
    text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }}
    .chrome-title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }}
    .fadegroup {{ animation: cyclefade {CYCLE}s ease-in-out infinite; }}
    @keyframes cyclefade {{
      0% {{ opacity: 1; }}
      {fade_out_start / CYCLE * 100:.1f}% {{ opacity: 1; }}
      {min(fade_out_start + fade_out_dur, CYCLE) / CYCLE * 100:.1f}% {{ opacity: 0; }}
      99.9% {{ opacity: 0; }}
      100% {{ opacity: 0; }}
    }}
    .ch {{ opacity: 0; animation: charin {CYCLE}s steps(1) infinite; }}
    @keyframes charin {{
      0% {{ opacity: 0; }}
      0.3% {{ opacity: 1; }}
      99.9% {{ opacity: 1; }}
      100% {{ opacity: 0; }}
    }}
    {"".join(char_rules)}
    .cursor {{ animation: cursorlife {CYCLE}s steps(1) infinite; animation-delay: {typed_end:.2f}s; }}
    @keyframes cursorlife {{
      0% {{ opacity: 1; }}
      {(resp_start - typed_end) / CYCLE * 100:.2f}% {{ opacity: 1; }}
      {(resp_start - typed_end) / CYCLE * 100 + 0.1:.2f}% {{ opacity: 0; }}
      99.9% {{ opacity: 0; }}
      100% {{ opacity: 0; }}
    }}
    .resp {{ opacity: 0; transform: translateY(6px); animation: respin {CYCLE}s ease-out infinite; }}
    @keyframes respin {{
      0% {{ opacity: 0; transform: translateY(6px); }}
      1% {{ opacity: 0; transform: translateY(6px); }}
      6% {{ opacity: 1; transform: translateY(0); }}
      99.9% {{ opacity: 1; transform: translateY(0); }}
      100% {{ opacity: 0; }}
    }}
    {"".join(style_rules)}
  </style>

  <g clip-path="url(#rounded)">
    <rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="{ASPHALT}"/>
    <rect x="0" y="0" width="{WIDTH}" height="44" fill="{ASPHALT_2}"/>
    <line x1="0" y1="44" x2="{WIDTH}" y2="44" stroke="{LINE}" stroke-width="1"/>
    <circle cx="26" cy="22" r="6.5" fill="#ff5f56"/>
    <circle cx="46" cy="22" r="6.5" fill="#ffbd2e"/>
    <circle cx="66" cy="22" r="6.5" fill="#27c93f"/>
    <text class="chrome-title" x="{WIDTH/2}" y="27" text-anchor="middle" font-size="13" fill="{FOG}">vv — claude</text>

    <g class="fadegroup">
      <text x="40" y="90" font-size="17" fill="{FOG}">$ {prompt}</text>

      <text x="40" y="140" font-size="17" fill="{AMBER}">&gt;</text>
      <text x="66" y="140" font-size="17" fill="{MIST}">{typed_tspans}</text>
      <rect class="cursor" x="{66 + len(typed) * 10.2:.0f}" y="126" width="9" height="18" fill="{AMBER}" style="animation-delay:{cursor_hide_at:.2f}s"/>

      <text x="40" y="{y0}" font-size="17" font-weight="700" fill="{AMBER}">{vv_label}</text>
      {"".join(resp_svg_lines)}
    </g>
  </g>
</svg>
'''
    return svg


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    for lang, cfg in DEMOS.items():
        svg = build_svg(cfg)
        cfg["out"].write_text(svg, encoding="utf-8")
        print(f"wrote {cfg['out'].relative_to(ROOT)} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
