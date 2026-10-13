import sys, json, os
from playwright.sync_api import sync_playwright

# Usage: render.py slides.json outdir
spec = json.load(open(sys.argv[1]))
out = sys.argv[2]
os.makedirs(out, exist_ok=True)

C = {"marine": "#002360", "profond": "#00183A", "terra": "#C1653D", "sauge": "#7A8B6F", "creme": "#F5F0E6"}

DROP = """<svg width="{s}" height="{h}" viewBox="0 0 64 88" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C1653D"/><stop offset="1" stop-color="#7A8B6F"/></linearGradient></defs>
<path d="M32 2 C32 2 4 38 4 58 C4 74 16.5 86 32 86 C47.5 86 60 74 60 58 C60 38 32 2 32 2 Z" fill="url(#g)"/>
<rect x="17" y="55" width="30" height="5" rx="2.5" fill="#F5F0E6"/></svg>"""

def drop(s):
    return DROP.format(s=s, h=int(s * 88 / 64))

THEMES = {
    "creme": dict(bg=C["creme"], title=C["marine"], text=C["profond"], muted="#6b6b6b", line=C["sauge"]),
    "marine": dict(bg=C["marine"], title=C["creme"], text=C["creme"], muted="#b9c3d6", line=C["sauge"]),
    "sauge": dict(bg=C["sauge"], title=C["creme"], text=C["creme"], muted="#e6e9e2", line=C["creme"]),
    "terra": dict(bg=C["terra"], title=C["creme"], text=C["creme"], muted="#f3dccf", line=C["creme"]),
}

CSS = """
@page {{ size: 1080px 1920px; margin: 0 }}
* {{ box-sizing: border-box; margin: 0; padding: 0 }}
body {{ width: 1080px; height: 1920px; background: {bg}; color: {text};
  font-family: 'Fraunces', serif; position: relative; overflow: hidden }}
.wrap {{ position: absolute; inset: 0; padding: 200px 110px 260px; display: flex; flex-direction: column; justify-content: center; gap: 56px }}
.kicker {{ font-family: 'Montserrat'; font-weight: 700; font-size: 30px; letter-spacing: 8px; text-transform: uppercase; color: {line} }}
h1 {{ font-family: 'Montserrat'; font-weight: 800; font-size: 104px; line-height: 1.05; color: {title}; letter-spacing: -1px }}
h2 {{ font-family: 'Montserrat'; font-weight: 800; font-size: 80px; line-height: 1.1; color: {title} }}
.accent {{ color: #C1653D }}
.on-dark .accent {{ color: #F5F0E6; border-bottom: 6px solid #C1653D }}
p {{ font-size: 50px; line-height: 1.4; color: {text} }}
p.it {{ font-style: italic }}
.big {{ font-family: 'Montserrat'; font-weight: 800; font-size: 260px; line-height: 1; color: #C1653D }}
.src {{ font-family: 'Montserrat'; font-size: 26px; color: {muted} }}
ul {{ list-style: none; display: flex; flex-direction: column; gap: 34px }}
li {{ font-size: 52px; line-height: 1.3; padding-left: 64px; position: relative }}
li:before {{ content: ''; position: absolute; left: 0; top: 34px; width: 36px; height: 3px; background: {line} }}
.rule {{ width: 120px; height: 3px; background: {line} }}
.foot {{ position: absolute; left: 110px; right: 110px; bottom: 150px; display: flex; align-items: center; justify-content: space-between;
  font-family: 'Montserrat'; font-weight: 700; font-size: 30px; color: {title} }}
.foot .brand {{ display: flex; align-items: center; gap: 16px; letter-spacing: 1px }}
.foot .n {{ font-weight: 500; color: {muted} }}
.on-dark .big {{ color: #F5F0E6 }}
.num {{ font-family: 'Montserrat'; font-weight: 800; font-size: 140px; line-height: 1; color: {line}; opacity: .9 }}
.center {{ align-items: center; text-align: center }}
.sig {{ font-family: 'Montserrat'; font-size: 26px; letter-spacing: 4px; text-transform: uppercase; color: {muted} }}
.sig b {{ display: block; margin-top: 10px; color: {title}; letter-spacing: 3px }}
"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    n = len(spec["slides"])
    for i, s in enumerate(spec["slides"], 1):
        t = THEMES[s.get("theme", spec.get("theme", "creme"))]
        dark = s.get("theme", spec.get("theme")) != "creme"
        body = s["html"].replace("{DROP_L}", drop(150)).replace("{DROP_S}", drop(34))
        foot = "" if s.get("nofoot") else f'<div class="foot"><span class="brand">{drop(34)} DOSE</span><span class="n">{"" if spec.get("nonum") else f"{i}/{n}"}</span></div>'
        html = f"<html><head><meta charset='utf-8'><style>{CSS.format(**t)}</style></head><body class='{'on-dark' if dark else ''}'><div class='wrap {s.get('cls','')}'>{body}</div>{foot}</body></html>"
        pg.set_content(html)
        pg.evaluate("document.fonts.ready")
        pg.screenshot(path=f"{out}/{i:02d}.png")
    b.close()
print("ok", n)
