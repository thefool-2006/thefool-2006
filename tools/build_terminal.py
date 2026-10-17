"""Builds assets/terminal.svg. Edit the INFO list / colors, then run:  python tools/build_terminal.py
If assets/portrait_dots.svg exists (from photo_to_dots.py) it is embedded; otherwise a placeholder silhouette is drawn."""
import os, math, random, re

INFO = [  # (key, value)
 ("Subject",        "Rachith Kumar M"),
 ("Role",           "Data Analyst / Scientist"),
 ("Focus",          "AI · Data Science · Python"),
 ("Education",      "B.Tech CSE (AI & DS)"),
 ("Status",         "Final Year, Parul Univ."),
 ("ToolChain",      "Python · Git · VS Code"),
]
STACK = [
 ("Core.Lang",      "Python, C++, Java"),
 ("Core.Frontend",  "HTML, CSS"),
 ("Core.Backend",   "Flask, Django"),
 ("Core.Database",  "MongoDB, SQL"),
 ("Core.Infra",     "Git, GitHub"),
]
GRID = [
 ("Grid.Mail",      "rachirachith8@gmail.com"),
 ("Grid.GitHub",    "github.com/rachi2006"),
 ("Grid.LinkedIn",  "add-your-linkedin"),
]
EMAIL = "rachirachith8@gmail.com"

CYAN, PURPLE, BG, TEXT, DIM = "#22d3ee", "#a855f7", "#0a0a1f", "#e0e7ff", "#64748b"

# ---- portrait panel (x 40..360, y 90..430) ----
if os.path.exists("assets/portrait_dots.svg"):
    inner = re.sub(r"</?svg[^>]*>", "", open("assets/portrait_dots.svg").read())
    portrait = f'<g transform="translate(40,90)">{inner}</g>'
else:
    random.seed(3); d = []
    for y in range(0, 340, 6):
        for x in range(0, 320, 6):
            hx, hy = (x-160)/62, (y-120)/78            # head ellipse
            head = hx*hx + hy*hy < 1
            sx = abs(x-160)/130                         # shoulders
            body = y > 215 and sx < 1 - ((y-215)/190)**2*0.35 and y < 340
            neck = 218 > y > 185 and abs(x-160) < 24
            if head or body or neck:
                if random.random() < 0.88:
                    d.append(f'<circle cx="{x+random.uniform(-1,1):.1f}" cy="{y+random.uniform(-1,1):.1f}" r="{random.uniform(.9,1.9):.1f}"/>')
    portrait = f'<g transform="translate(40,90)" fill="#a78bfa" opacity=".85">{"".join(d)}</g>'

rows, y, i = [], 150, 0
def line(k, v, hl=False):
    global y, i
    delay = 0.35 + i*0.18; i += 1
    vv = v.replace("&", "&amp;")
    rows.append(f'<g class="row" style="animation-delay:{delay:.2f}s"><text x="410" y="{y}" class="k">{k}</text>'
                f'<line x1="{410+len(k)*8.4+8}" y1="{y-4}" x2="640" y2="{y-4}" stroke="{DIM}" stroke-dasharray="1 4" stroke-linecap="round"/>'
                f'<text x="650" y="{y}" class="v">{vv}</text></g>')
    y += 24
for k, v in INFO:  line(k, v)
y += 8
for k, v in STACK: line(k, v)
y += 8
rows.append(f'<text x="410" y="{y}" class="k" fill="{CYAN}">- Contact -</text>'); y += 24
for k, v in GRID:  line(k, v)
cur_y = y

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{y+40}" viewBox="0 0 900 {y+40}">
<style>
 text{{font-family:'Courier New',ui-monospace,monospace}}
 .k{{fill:{CYAN};font-size:14px;font-weight:bold}}
 .v{{fill:{TEXT};font-size:13px}}
 .row{{animation:in .5s ease backwards}}
 @keyframes in{{from{{opacity:0;transform:translateX(-8px)}}to{{opacity:1;transform:none}}}}
 @keyframes glow{{0%,100%{{opacity:.55}}50%{{opacity:1}}}}
 @keyframes blink{{50%{{opacity:0}}}}
 @keyframes scan{{0%{{transform:translateY(0)}}100%{{transform:translateY(340px)}}}}
 .glow{{animation:glow 3s ease-in-out infinite}}
 .cur{{animation:blink 1s steps(1) infinite}}
 .scan{{animation:scan 4s linear infinite}}
</style>
<defs>
 <linearGradient id="bd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{PURPLE}"/></linearGradient>
 <filter id="gl" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter>
 <clipPath id="pc"><rect x="40" y="90" width="320" height="340"/></clipPath>
</defs>
<rect x="8" y="8" width="884" height="{y+24}" rx="16" fill="none" stroke="url(#bd)" stroke-width="3" filter="url(#gl)" class="glow"/>
<rect x="8" y="8" width="884" height="{y+24}" rx="16" fill="{BG}" stroke="url(#bd)" stroke-width="1.5"/>
<circle cx="36" cy="36" r="7" fill="#ff5f56"/><circle cx="58" cy="36" r="7" fill="#ffbd2e"/><circle cx="80" cy="36" r="7" fill="#27c93f"/>
<text x="860" y="41" text-anchor="end" font-size="12" fill="{DIM}">rachi2006.connect<tspan class="cur">_</tspan></text>
<line x1="8" y1="58" x2="892" y2="58" stroke="{CYAN}" stroke-opacity=".25"/>
<text x="40" y="82" font-size="11" fill="{DIM}" letter-spacing="3">VISUAL.MAP</text>
<rect x="40" y="90" width="320" height="340" fill="none" stroke="{CYAN}" stroke-opacity=".6"/>
<path d="M40 110V90h20M360 110V90h-20M40 410v20h20M360 410v20h-20" stroke="{CYAN}" stroke-width="3" fill="none"/>
{portrait}
<g clip-path="url(#pc)"><rect class="scan" x="40" y="90" width="320" height="3" fill="{CYAN}" opacity=".5"/></g>
<text x="410" y="82" font-size="11" fill="{DIM}" letter-spacing="3">SYSTEM.INFO</text>
<rect x="408" y="94" width="{len(EMAIL)*8.2+20}" height="24" rx="4" fill="{PURPLE}"/>
<text x="418" y="111" font-size="13" font-weight="bold" fill="#fff">{EMAIL}</text>
{"".join(rows)}
<text x="410" y="{cur_y+10}" font-size="12" fill="{DIM}">> More about me &amp; projects below in README</text>
</svg>'''
open("assets/terminal.svg", "w").write(svg)
print("built assets/terminal.svg")
