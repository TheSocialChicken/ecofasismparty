"""Text-free stamps for small (19.5 / 15 mm) StampMaker stamps.

Ministry: official site icon inside a ring.  Credit: value only (+10, -20 ...) in a frame.
Output: icon_only/<name>.svg (single filled shapes, ready for StampMaker / make_discs).
"""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "icon_only")
os.makedirs(OUT, exist_ok=True)
ICONS = json.load(open(os.path.join(HERE, "site_icons.json")))
ORDER = ["PURITY", "RADIANCE", "BREATH", "FLOW", "LIGHT", "INDUSTRY", "HUMUS", "SERVICE", "VIGILANCE", "JOY"]


def flatten(src, dst):
    subprocess.run(["inkscape", src, "--export-text-to-path", "--export-plain-svg", "--export-filename", dst],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["inkscape", dst, "--actions=select-all:groups;selection-ungroup;select-all:groups;selection-ungroup;"
                    "select-all:no-groups;object-stroke-to-path;object-to-path;path-union;"
                    f"export-plain-svg;export-filename:{dst};export-do"],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


for i, n in enumerate(ORDER, 1):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
<path fill="#000" fill-rule="evenodd" d="M100 2a98 98 0 1 0 0.01 0zM100 12a88 88 0 1 1 -0.01 0z"/>
<g transform="translate(38 38) scale(2.583)" fill="#000" color="#000">{ICONS[n]}</g>
</svg>'''
    src = os.path.join(OUT, f"_{i:02d}.svg")
    open(src, "w").write(svg)
    os.replace(src, os.path.join(OUT, f"{i:02d}_{n.lower()}.svg"))  # no union: keeps icon details

for v in (10, 20, 50):
    for sign, sym in (("plus", "+"), ("min", "−")):
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
<path fill="#000" fill-rule="evenodd" d="M30 1H130A29 29 0 0 1 159 30V130A29 29 0 0 1 130 159H30A29 29 0 0 1 1 130V30A29 29 0 0 1 30 1ZM34 13H126A21 21 0 0 1 147 34V126A21 21 0 0 1 126 147H34A21 21 0 0 1 13 126V34A21 21 0 0 1 34 13Z"/>
<text x="80" y="100" font-family="DejaVu Sans Condensed" font-weight="bold" font-size="56" text-anchor="middle" fill="#000">{sym}{v}</text>
</svg>'''
        src = os.path.join(OUT, f"_c.svg")
        open(src, "w").write(svg)
        subprocess.run(["inkscape", src, "--export-text-to-path", "--export-plain-svg", "--export-filename",
                        os.path.join(OUT, f"credit_{sign}{v}.svg")], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.remove(src)
print("done")
