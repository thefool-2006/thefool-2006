"""Builds assets/projects.svg (neon repo cards). Edit REPOS, then: python tools/build_projects.py"""
CYAN, PURPLE, BG, TEXT, DIM = "#22d3ee", "#a855f7", "#0a0a1f", "#e0e7ff", "#64748b"
REPOS = [  # (name, description, language, color)
 ("learn_skills", "Growth system: learning, streaks, notes", "Python", "#3572A5"),
 ("python_code",  "Python practice programs and scripts",                     "Python", "#3572A5"),
 ("PYLIB",        "Python library experiments",                               "Python", "#3572A5"),
 ("java_code",    "Java programs and practice code",                          "Java",   "#b07219"),
 ("DDS-projects", "Data structure projects in C++",                           "C++",    "#f34b7d"),
 ("DDS-Codes",    "Data structure and algorithm code in C++",                   "C++",    "#f34b7d"),
]
cw, ch, gap = 430, 92, 16
rows = (len(REPOS)+1)//2
H = 60 + rows*(ch+gap)
out = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{H}" viewBox="0 0 900 {H}">
<style>text{{font-family:'Courier New',ui-monospace,monospace}}
.c{{animation:in .5s ease backwards}}@keyframes in{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
@keyframes pulse{{0%,100%{{opacity:.4}}50%{{opacity:1}}}}.p{{animation:pulse 2.5s infinite}}</style>
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{PURPLE}"/></linearGradient></defs>
<text x="10" y="28" font-size="13" fill="{DIM}" letter-spacing="3">PROJECTS.LIST <tspan fill="{CYAN}">~/projects.sh --all</tspan></text>''']
for n, (name, desc, lang, col) in enumerate(REPOS):
    x = 10 + (n%2)*(cw+14); y = 48 + (n//2)*(ch+gap)
    out.append(f'''<g class="c" style="animation-delay:{n*0.15:.2f}s">
<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="12" fill="{BG}" stroke="url(#g)" stroke-width="1.3"/>
<text x="{x+18}" y="{y+30}" font-size="11" fill="{DIM}">rachi2006/</text>
<text x="{x+18}" y="{y+52}" font-size="17" font-weight="bold" fill="{TEXT}">{name}</text>
<text x="{x+18}" y="{y+74}" font-size="12" fill="{DIM}">{desc}</text>
<circle class="p" cx="{x+cw-110}" cy="{y+30}" r="5" fill="{col}"/>
<text x="{x+cw-98}" y="{y+34}" font-size="12" fill="{TEXT}">{lang}</text></g>''')
out.append("</svg>")
open("assets/projects.svg","w").write("\n".join(out)); print("built assets/projects.svg")
