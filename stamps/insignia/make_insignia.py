"""Generate the ten ministry insignia stamps (names as on the live site, Nov 2026).

Run: python3 make_insignia.py   -> writes NN_<name>.svg next to this file.
Then: inkscape converts text to paths (see bottom) so stamp makers get pure shapes.
"""
import math, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = 'font-family="Noto Sans Mono Black" font-weight="900"'


def star(cx, cy, r):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="#000"/>'


def rays(cx, cy, r1, r2, n, w):
    out = []
    for i in range(n):
        a = 2 * math.pi * i / n
        out.append(f'<line x1="{cx + r1*math.cos(a):.1f}" y1="{cy + r1*math.sin(a):.1f}" '
                   f'x2="{cx + r2*math.cos(a):.1f}" y2="{cy + r2*math.sin(a):.1f}" '
                   f'stroke="#000" stroke-width="{w}" stroke-linecap="round"/>')
    return "".join(out)


def gear(cx, cy, r, teeth=10):
    pts = []
    for i in range(teeth * 4):
        a = 2 * math.pi * i / (teeth * 4)
        rr = r if (i % 4) in (1, 2) else r * 0.78
        pts.append(f"{cx + rr*math.cos(a):.1f},{cy + rr*math.sin(a):.1f}")
    return (f'<polygon points="{" ".join(pts)}" fill="#000"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*0.32:.1f}" fill="#fff"/>')


C = 100, 104  # icon centre
ICONS = {
    # Purity: water drop with a check mark
    "PURITY": '<path d="M100 66 C100 66 74 98 74 114 A26 26 0 0 0 126 114 C126 98 100 66 100 66 Z" fill="#000"/>'
              '<path d="M87 113 L97 123 L114 103" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>',
    # Radiance: sun
    "RADIANCE": '<circle cx="100" cy="104" r="15" fill="#000"/>' + rays(100, 104, 21, 34, 12, 5),
    # Breath: three wind strokes
    "BREATH": '<path d="M70 88 H112 A10 10 0 1 0 102 78" fill="none" stroke="#000" stroke-width="6" stroke-linecap="round"/>'
              '<path d="M66 104 H128 A10 10 0 1 1 118 114" fill="none" stroke="#000" stroke-width="6" stroke-linecap="round"/>'
              '<path d="M74 120 H104 A9 9 0 1 1 95 129" fill="none" stroke="#000" stroke-width="6" stroke-linecap="round"/>',
    # Flow: three waves
    "FLOW": "".join(f'<path d="M68 {y} q8 -9 16 0 t16 0 t16 0 t16 0" fill="none" stroke="#000" stroke-width="6" stroke-linecap="round"/>'
                    for y in (90, 106, 122)),
    # Light: lightning bolt
    "LIGHT": '<path d="M108 68 L80 110 H98 L90 140 L122 94 H103 Z" fill="#000"/>',
    # Industry: gear
    "INDUSTRY": gear(100, 104, 32),
    # Humus: sprout from a soil mound
    "HUMUS": '<path d="M66 132 Q100 112 134 132 Z" fill="#000"/>'
             '<line x1="100" y1="124" x2="100" y2="92" stroke="#000" stroke-width="6" stroke-linecap="round"/>'
             '<path d="M100 98 Q80 98 76 78 Q96 76 100 98 Z" fill="#000"/>'
             '<path d="M100 92 Q118 90 124 72 Q104 70 100 92 Z" fill="#000"/>',
    # Service: crossed broom and spade
    "SERVICE": '<line x1="76" y1="78" x2="124" y2="132" stroke="#000" stroke-width="6" stroke-linecap="round"/>'
               '<path d="M118 120 L134 136 L126 144 L110 128 Z" fill="#000"/>'
               '<line x1="124" y1="78" x2="78" y2="128" stroke="#000" stroke-width="6" stroke-linecap="round"/>'
               '<path d="M70 72 H84 V80 H70 Z" fill="#000"/>'
               '<path d="M84 120 L70 134 Q66 142 74 140 L90 128 Z" fill="#000"/>',
    # Vigilance: the all-seeing eye
    "VIGILANCE": '<path d="M64 104 Q100 68 136 104 Q100 140 64 104 Z" fill="none" stroke="#000" stroke-width="6"/>'
                 '<circle cx="100" cy="104" r="13" fill="#000"/><circle cx="104" cy="100" r="4" fill="#fff"/>'
                 + rays(100, 104, 44, 50, 0, 4),
    # Joy: mandatory smile
    "JOY": '<circle cx="100" cy="104" r="32" fill="none" stroke="#000" stroke-width="6"/>'
           '<circle cx="89" cy="96" r="4.5" fill="#000"/><circle cx="111" cy="96" r="4.5" fill="#000"/>'
           '<path d="M84 112 Q100 128 116 112" fill="none" stroke="#000" stroke-width="6" stroke-linecap="round"/>',
}
# Official icons from the live site (staging.join-ecotopia.org/ministries), 48x48 glyphs.
import json as _json
_SITE = _json.load(open(os.path.join(HERE, "site_icons.json")))
for _n, _g in _SITE.items():
    ICONS[_n] = f'<g transform="translate(64 68) scale(1.5)" fill="#000" color="#000">{_g}</g>'
ORDER = ["PURITY", "RADIANCE", "BREATH", "FLOW", "LIGHT", "INDUSTRY", "HUMUS", "SERVICE", "VIGILANCE", "JOY"]


def arc_text(s, r, fs, spacing, top=True, cx=100, cy=104):
    step = (0.62 * fs + spacing) / r  # radians per character
    total = step * (len(s) - 1)
    out = []
    for i, ch in enumerate(s):
        if ch == " ":
            continue
        if top:
            a = -math.pi / 2 - total / 2 + i * step
            rot = math.degrees(a) + 90
        else:
            a = math.pi / 2 + total / 2 - i * step
            rot = math.degrees(a) - 90
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        out.append(f'<text {FONT} font-size="{fs}" fill="#000" stroke="#000" stroke-width="1.1" stroke-linejoin="round" text-anchor="middle" dominant-baseline="central" '
                   f'transform="translate({x:.2f} {y:.2f}) rotate({rot:.2f})">{ch}</text>')
    return "".join(out)


def insignia(name):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
  <circle cx="100" cy="100" r="95" fill="none" stroke="#000" stroke-width="6"/>
  <circle cx="100" cy="100" r="86" fill="none" stroke="#000" stroke-width="2.5"/>
  <circle cx="100" cy="104" r="46" fill="none" stroke="#000" stroke-width="3"/>
  {arc_text("MINISTRY OF " + name, 70, 14 if len(name) < 8 else 12.5, 1.5)}
  {arc_text("R.E.I.G.N.", 70, 13, 3, top=False)}
  {star(34, 104, 7)}{star(166, 104, 7)}
  {ICONS[name]}
</svg>
'''


for i, n in enumerate(ORDER, 1):
    path = os.path.join(HERE, f"{i:02d}_{n.lower()}.svg")
    with open(path, "w") as f:
        f.write(insignia(n))
    # text -> paths, so MakerWorld / slicers don't need the font
    out = path.replace(".svg", "_paths.svg")
    # text -> paths, then every stroke -> filled outline (stamp makers read fills only)
    subprocess.run(["inkscape", path, "--export-text-to-path", "--export-plain-svg",
                    "--export-filename", out], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["inkscape", out, "--actions=select-all;object-stroke-to-path;export-plain-svg;"
                    f"export-filename:{out};export-do"], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("done")
