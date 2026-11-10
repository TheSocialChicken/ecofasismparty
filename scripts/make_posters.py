#!/usr/bin/env python3
"""Generate Ecotopia propaganda pieces for the Bitlair 60W CO2 lasercutter.

Soviet-constructivist, 1-bit, on 4mm poplar. Each master SVG is drawn in
three colours, so it can also be edited by hand in Inkscape:

  black  #000000  ENGRAVE  (burned wood)
  red    #ff0000  CUT AWAY (filled area -> its outline becomes a cut path;
                            everything outside the piece is red too)
  white  #ffffff  bare wood

The build splits those colours into LightBurn-ready files in
posters/_build/, then publishes the two folders people use:
posters/posters/ (one PDF per poster) and posters/lasercutter/ (one LightBurn
file per poster). Per design, in _build/:

  <name>.svg          master artwork (live text)
  <name>_cut.svg      red 0.1mm hairlines, traced from the red areas
  <name>_engrave.png  1-bit 300 dpi bitmap of the black areas (Image layer;
                      flattened because LightBurn can't knock white out of
                      black fills). Same page size as _cut.svg: same origin.
  <name>_laser.svg    ALL-IN-ONE vector file: black fills (engrave) + red
                      hairlines (cut). The one to import into LightBurn.
  <name>_preview.png  how the finished wood should look
  sheet_A4x10_*       the ten A4 slogan panels nested on one 1200x600 sheet

It also checks the cut layout: loose wood "islands" that would drop out of
a hole (bridged automatically on stencils, reported otherwise) and wood
strips too thin to survive in 4mm poplar.

Usage: .venv/bin/python scripts/make_posters.py   (needs potracer, scipy)
"""
import math
import os
import re
import shutil
import subprocess
import sys

import numpy as np
import potrace
from PIL import Image
from scipy import ndimage

OUT = os.path.join(os.path.dirname(__file__), "..", "posters")
BUILD = os.path.join(OUT, "_build")      # masters, previews, bitmaps


def out(filename):
    """Working files all go into posters/_build/."""
    os.makedirs(BUILD, exist_ok=True)
    return os.path.join(BUILD, filename)


def pretty(name):
    """'11_breathe_less' -> '11 Breathe Less'"""
    num, _, words = name.partition("_")
    return f"{num} {words.replace('_', ' ').title()}"


ENGRAVE_DPI = 300
CUT_DPI = 200            # 0.127 mm/px; potrace smooths it into curves
MIN_WOOD_MM = 1.6        # thinner strips char through / snap in 4mm poplar
BRIDGE_MM = 2.0
CUT_SPEED, ENGRAVE_SPEED, LINE_GAP = 8.0, 300.0, 0.1   # mm/s, mm/s, mm
W, H = 297, 420
# The regime's figurehead is not final yet: every slogan takes its name from
# here (override for a test run: ECOTOPIA_LEADER="THE MATRIARCH" ...).
LEADER = os.environ.get("ECOTOPIA_LEADER", "THE STAG")
LEADER_TITLE = os.environ.get("ECOTOPIA_LEADER_TITLE", "THE GUARDIAN STAG")
LEADER_HE = os.environ.get("ECOTOPIA_LEADER_PRONOUN", "HE")          # HE / SHE / IT / THEY
LEADER_HIM = {"HE": "HIM", "SHE": "HER", "IT": "IT", "THEY": "THEM"}[LEADER_HE]
BK, WH, CUT = "#000000", "#ffffff", "#ff0000"

HEAD = "font-family:'Noto Sans Display';font-weight:900;font-stretch:extra-condensed;" \
       "-inkscape-font-specification:'Noto Sans Display ExtraCondensed Black'"
SUB = "font-family:'Noto Sans';font-weight:800;font-stretch:condensed;" \
      "-inkscape-font-specification:'Noto Sans Condensed ExtraBold'"
MONO = "font-family:'IBM Plex Mono';font-weight:600;" \
       "-inkscape-font-specification:'IBM Plex Mono SemiBold'"


def svg(body, w=W, h=H, title="", outline=None, holes=((14, 9), (W - 14, 9))):
    """Wrap artwork as a piece. `outline` is the wood shape (default: rounded
    rectangle); everything outside it, and the hanging holes, is cut away."""
    if outline is None:
        outline = f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="6" fill="{WH}"/>'
    hole = "".join(f'<circle cx="{x}" cy="{y}" r="2.5" fill="{CUT}"/>' for x, y in holes)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
     width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}">
<title>{title}</title>
<!-- black = ENGRAVE, red fill = CUT AWAY, white = bare wood -->
<rect width="{w}" height="{h}" fill="{CUT}"/>
{layer("piece", outline)}
{body}
{layer("holes", hole)}
</svg>
"""


def layer(name, content):
    return f'<g inkscape:groupmode="layer" inkscape:label="{name}">\n{content}\n</g>'


def text(x, y, s, size, style=HEAD, fill=BK, anchor="middle", extra=""):
    return (f'<text x="{x}" y="{y}" style="{style};font-size:{size}px;'
            f'text-anchor:{anchor};fill:{fill}" {extra}>{s}</text>')


def fit(x, y, s, width, size, style=HEAD, fill=BK, anchor="middle"):
    """Text squeezed/stretched to an exact width (keeps headlines on-grid)."""
    return text(x, y, s, size, style, fill, anchor,
                f'textLength="{width}" lengthAdjust="spacingAndGlyphs"')


def poly(pts, fill=BK, extra=""):
    p = " ".join(f"{x:.2f},{y:.2f}" for x, y in pts)
    return f'<polygon points="{p}" fill="{fill}" {extra}/>'


def sunburst(cx, cy, r, n=24, fill=BK, phase=0.0):
    out = []
    for i in range(n):
        a0 = (2 * i) * math.pi / n + phase
        a1 = (2 * i + 1) * math.pi / n + phase
        out.append(poly([(cx, cy),
                         (cx + r * math.cos(a0), cy + r * math.sin(a0)),
                         (cx + r * math.cos(a1), cy + r * math.sin(a1))], fill))
    return "\n".join(out)


def clipped(cid, x, y, w, h, content):
    return (f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3"/></clipPath>'
            f'<g clip-path="url(#{cid})">{content}</g>')


# ---------------------------------------------------------------- the stag
# Front-facing geometric stag head, defined in units around the forehead
# centre (0,0); antlers go to y=-78, muzzle to y=+48.
_FACE = [(-14, 0), (14, 0), (17, 8), (10, 30), (6, 44), (0, 49),
         (-6, 44), (-10, 30), (-17, 8)]
_EAR = [(-13, 3), (-36, -5), (-29, 5), (-17, 13)]
# left antler: main beam then tines, each a polyline
_ANTLER = [
    [(-7, 1), (-15, -18), (-20, -38), (-18, -58), (-11, -76)],
    [(-15, -18), (-31, -25)],
    [(-20, -38), (-37, -50)],
    [(-19, -47), (-8, -52)],
    [(-18, -58), (-29, -78)],
]


def _mirror(pts):
    return [(-x, y) for x, y in pts]


def stag(cx, cy, s, fill=BK, cut=WH, circuit=False, grow=0.0, features=True):
    """Stag head at (cx, cy) forehead centre, s = mm per unit.
    grow > 0 fattens every part by that many mm (an offset silhouette)."""
    T = lambda pts: [(cx + x * s, cy + y * s) for x, y in pts]
    sw = 5.2 * s
    edge = f'stroke="{fill}" stroke-width="{2 * grow:.2f}" stroke-linejoin="round"' if grow else ""
    parts = [poly(T(p), fill, edge) for p in (_FACE, _EAR, _mirror(_EAR))]
    lines, tips = [], []
    for seg in _ANTLER:
        for side in (seg, _mirror(seg)):
            p = T(side)
            lines.append("M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in p))
            tips.append(p[-1])
    style = f'fill="none" stroke="{fill}" stroke-width="{sw + 2 * grow:.2f}" stroke-linejoin="round"'
    style += ' stroke-linecap="butt"' if circuit and not grow else ' stroke-linecap="round"'
    parts.append(f'<path d="{" ".join(lines)}" {style}/>')
    if circuit:  # antlers as circuit traces ending in solder pads
        for x, y in tips:
            parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{sw * 1.15 + grow:.2f}" fill="{fill}"/>')
            if features:
                parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{sw * 0.45:.2f}" fill="{cut}"/>')
    if features:  # eyes and nose
        for sx in (-1, 1):
            parts.append(poly(T([(sx * 5, 15), (sx * 11, 13), (sx * 9, 18)]), cut))
        parts.append(poly(T([(-4, 41), (4, 41), (0, 46)]), cut))
    return "<g>" + "\n".join(parts) + "</g>"


# ------------------------------------------------- 01 apply (engraved hero)
def piece_apply():
    bg = clipped("c1", 1, 1, W - 2, H - 2, sunburst(148.5, 168, 260, n=28))
    disc = (f'<circle cx="148.5" cy="168" r="96" fill="{WH}"/>'
            f'<circle cx="148.5" cy="168" r="96" fill="none" stroke="{BK}" stroke-width="5"/>'
            f'<circle cx="148.5" cy="168" r="88" fill="none" stroke="{BK}" stroke-width="1.6"/>')
    head = stag(148.5, 175, 1.42)
    top = (f'<rect x="1" y="1" width="{W - 2}" height="58" rx="6" fill="{BK}"/>' +
           fit(148.5, 50, "ECOTOPIA", 265, 60, fill=WH))
    band = (f'<g transform="rotate(-8 148.5 300)">'
            f'<rect x="-30" y="268" width="360" height="56" fill="{BK}"/>' +
            fit(148.5, 313, "APPLY FOR CITIZENSHIP", 270, 44, fill=WH) + "</g>")
    foot = (f'<rect x="1" y="346" width="{W - 2}" height="58" fill="{WH}"/>' +
            fit(148.5, 360, "THE LAST GREEN COUNTRY ON EARTH WELCOMES YOU", 265, 15, SUB) +
            f'<rect x="16" y="368" width="265" height="1.6" fill="{BK}"/>' +
            text(148.5, 384, "YOUR CARBON DEBT IS WAITING TO BE FORGIVEN", 7.8, MONO) +
            text(148.5, 397, "R.E.I.G.N. · REGIME FOR ECOLOGICAL INTEGRITY AND GLOBAL NURTURING", 5.6, MONO) +
            f'<rect x="1" y="404" width="{W - 2}" height="15" rx="6" fill="{BK}"/>' +
            text(148.5, 415, "28 · 11 · APPLY BEFORE THE BORDER CLOSES", 8, MONO, fill=WH))
    return svg(layer("rays", bg) + layer("disc", disc) + layer("stag", head) +
               layer("type", top + band + foot), title="Ecotopia Apply")


# ------------------------------------ 02 recycling plant (arrows cut through)
def arrow_ring(cx, cy, r, sw, fill=BK):
    """Three chasing arrows around a circle (recycling sigil). The gaps
    between arrows keep the centre attached when they are cut through."""
    out = []
    for k in range(3):
        a0 = math.radians(-90 + k * 120 + 12)
        a1 = math.radians(-90 + k * 120 + 96)
        p0 = (cx + r * math.cos(a0), cy + r * math.sin(a0))
        p1 = (cx + r * math.cos(a1), cy + r * math.sin(a1))
        out.append(f'<path d="M{p0[0]:.2f},{p0[1]:.2f} A{r},{r} 0 0 1 {p1[0]:.2f},{p1[1]:.2f}" '
                   f'fill="none" stroke="{fill}" stroke-width="{sw}"/>')
        t = (-math.sin(a1), math.cos(a1))
        n = (math.cos(a1), math.sin(a1))
        L, Wd = sw * 1.6, sw * 1.25
        tip = (p1[0] + t[0] * L, p1[1] + t[1] * L)
        out.append(poly([tip, (p1[0] + n[0] * Wd, p1[1] + n[1] * Wd),
                         (p1[0] - n[0] * Wd, p1[1] - n[1] * Wd)], fill))
    return "\n".join(out)


def piece_recycling():
    wedge = clipped("c2", 1, 1, W - 2, H - 2, poly([(90, 0), (W, 0), (W, 250), (0, 120), (0, 0)]))
    ring = (f'<circle cx="212" cy="118" r="70" fill="{WH}"/>' +
            arrow_ring(212, 118, 50, 13, fill=CUT) + stag(212, 110, 0.38))
    type_ = (fit(20, 64, "BE", 60, 58, fill=WH, anchor="start") +
             fit(20, 108, "PROMOTED", 108, 34, fill=WH, anchor="start") +
             fit(148.5, 290, "TO THE", 257, 44) +
             fit(148.5, 340, "RECYCLING PLANT", 257, 50) +
             f'<rect x="20" y="352" width="257" height="2" fill="{BK}"/>' +
             fit(148.5, 370, "IT IS NOT A PUNISHMENT. IT IS A PRIVILEGE.", 257, 13, SUB) +
             text(148.5, 386, "Return reborn: new name · zero debt · one with the soil", 7, MONO) +
             f'<rect x="1" y="398" width="{W - 2}" height="21" rx="6" fill="{BK}"/>' +
             text(148.5, 412, "MINISTRY OF THE MUSHROOM · R.E.I.G.N.", 8.5, MONO, fill=WH))
    return svg(layer("wedge", wedge) + layer("sigil", ring) + layer("type", type_),
               title="Recycling Plant")


# ------------------------------------- 03 darkness (rays cut: a light screen)
def bulb(cx, cy, r):
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{BK}"/>',
           poly([(cx - r * .55, cy + r * .8), (cx + r * .55, cy + r * .8),
                 (cx + r * .42, cy + r * 1.45), (cx - r * .42, cy + r * 1.45)])]
    for i in range(3):  # screw base
        y = cy + r * (1.55 + i * .26)
        out.append(f'<rect x="{cx - r*.4:.2f}" y="{y:.2f}" width="{r*.8:.2f}" height="{r*.17:.2f}" fill="{BK}"/>')
    out.append(f'<path d="M{cx - r*.3:.2f},{cy + r*.75:.2f} L{cx - r*.3:.2f},{cy + r*.1:.2f} '
               f'L{cx - r*.1:.2f},{cy - r*.15:.2f} L{cx + r*.1:.2f},{cy + r*.1:.2f} '
               f'L{cx + r*.3:.2f},{cy - r*.15:.2f} L{cx + r*.3:.2f},{cy + r*.75:.2f}" '
               f'fill="none" stroke="{WH}" stroke-width="{r*.07:.2f}"/>')
    return "\n".join(out)


def piece_lights():
    # rays are holes: hang it in front of a lamp and the light comes through
    rays = clipped("c3", 14, 22, W - 28, 236, sunburst(148.5, 150, 230, n=20, fill=CUT, phase=0.08))
    halo = f'<circle cx="148.5" cy="150" r="86" fill="{WH}"/>'
    b = bulb(148.5, 120, 52)
    bar = (f'<g transform="rotate(-38 148.5 160)">'
           f'<rect x="20" y="150" width="257" height="20" fill="{WH}"/>'
           f'<rect x="20" y="153.5" width="257" height="13" fill="{BK}"/></g>')
    # type on bare wood (much less engraving than a solid black band)
    type_ = (f'<rect x="14" y="266" width="{W - 28}" height="5" fill="{BK}"/>' +
             fit(148.5, 312, "DARKNESS IS", 257, 46) +
             fit(148.5, 362, "DEVOTION", 257, 52) +
             f'<rect x="14" y="368" width="{W - 28}" height="2" fill="{BK}"/>' +
             fit(148.5, 384, f"SURRENDER YOUR LIGHT. {LEADER} RETURNS IT TO THE EARTH.", 257, 11, SUB) +
             text(148.5, 398, "Every switched-off bulb erases 3 carbon credits of debt", 6.8, MONO) +
             text(148.5, 412, "MINISTRY OF THE SUNFLOWER · R.E.I.G.N.", 8, MONO))
    return svg(layer("rays", rays) + layer("bulb", halo + b + bar) + layer("type", type_),
               title="Darkness Is Devotion")


# ----------------------------------- 04 guardian stag trophy (shaped outline)
TW, TH = 300, 540


def piece_trophy():
    cx, cy, s = 150, 262, 3.1
    # wood silhouette: the stag grown by 7mm, a neck, and a name plaque
    neck = poly([(cx - 12 * s, cy + 26 * s), (cx + 12 * s, cy + 26 * s), (cx + 60, 440), (cx - 60, 440)], WH)
    plaque = f'<rect x="40" y="430" width="220" height="100" rx="8" fill="{WH}"/>'
    outline = stag(cx, cy, s, fill=WH, grow=7, features=False) + neck + plaque
    head = stag(cx, cy, s)
    stripes = "".join(f'<rect x="{cx - 40 + i * 6:.1f}" y="{cy + 48 * s + 2 + i * 9:.1f}" '
                      f'width="{80 - i * 12:.1f}" height="4" fill="{BK}"/>' for i in range(3))
    plate = (f'<rect x="47" y="437" width="206" height="86" rx="5" fill="none" stroke="{BK}" stroke-width="2.2"/>' +
             fit(150, 472, LEADER_TITLE, 186, 30) +
             f'<rect x="60" y="481" width="180" height="1.4" fill="{BK}"/>' +
             text(150, 498, f"{LEADER_HE} SEES · {LEADER_HE} PROVIDES · {LEADER_HE} RECYCLES" if LEADER_HE != "THEY" else "THEY SEE · THEY PROVIDE · THEY RECYCLE", 9.5, SUB) +
             text(150, 514, "R.E.I.G.N. · YEAR II OF THE HEALING", 6.5, MONO))
    # keyhole slot for a screw, hidden in the forehead's top edge
    holes = ((cx, cy + 6),)
    return svg(layer("engrave", head + stripes + plate), TW, TH, "Guardian Stag",
               outline=outline, holes=holes)


# --------------------------------------- 05 resistance: a real spray stencil
def stencil_text(x, y, s, width, size, rot=0.0):
    """Cut-through headline with horizontal bridges (classic stencil look)."""
    gy = y - size * 0.72 * 0.62
    return (f'<g transform="rotate({rot} {x} {y})">' + fit(x, y, s, width, size, fill=CUT) +
            f'<rect x="{x - width/2 - 2:.2f}" y="{gy:.2f}" width="{width + 4:.2f}" '
            f'height="{BRIDGE_MM}" fill="{WH}"/></g>')


def piece_stencil():
    frame = (f'<rect x="8" y="8" width="{W - 16}" height="{H - 16}" rx="4" fill="none" '
             f'stroke="{BK}" stroke-width="0.8" stroke-dasharray="4 3"/>')
    head = stag(148.5, 242, 1.1, fill=CUT, circuit=True)
    type_ = (stencil_text(148.5, 72, LEADER, 240, 62, rot=-3) +
             stencil_text(148.5, 122, "IS A MACHINE", 240, 46, rot=-3) +
             stencil_text(148.5, 372, f"UNPLUG {LEADER_HIM}", 245, 62, rot=2))
    label = (text(148.5, 401, "RESISTANCE STENCIL Nº 1 · SPRAY AT 30 CM · WIPE AFTER USE", 6.4, MONO) +
             text(148.5, 410, "touch soil, not screens · the credits were never real · 00:05", 5.6, MONO))
    return svg(layer("engrave", frame + label) + layer("stencil", head + type_),
               title="Unplug Him Stencil")


# --------------------------------------------- 06 crest plaque (round cut)
def crest_group(cx, cy, R):
    k = R / 100
    ring_r = 83 * k
    return "\n".join([
        f'<circle cx="{cx}" cy="{cy}" r="{R - 3*k:.2f}" fill="none" stroke="{BK}" stroke-width="{3*k:.2f}"/>',
        f'<circle cx="{cx}" cy="{cy}" r="{R - 7*k:.2f}" fill="none" stroke="{BK}" stroke-width="{1*k:.2f}"/>',
        f'<circle cx="{cx}" cy="{cy}" r="{70*k:.2f}" fill="none" stroke="{BK}" stroke-width="{3*k:.2f}"/>',
        sunburst(cx, cy, 66 * k, n=32),
        f'<circle cx="{cx}" cy="{cy}" r="{56*k:.2f}" fill="{WH}"/>',
        # clockwise from the bottom, so the top of the ring is the 50% point
        f'<path id="crest-arc" d="M{cx},{cy + ring_r:.2f} a{ring_r:.2f},{ring_r:.2f} 0 1 1 0,{-2*ring_r:.2f} '
        f'a{ring_r:.2f},{ring_r:.2f} 0 1 1 0,{2*ring_r:.2f}" fill="none"/>',
        f'<text style="{HEAD};font-size:{11*k:.2f}px;letter-spacing:{1.1*k:.2f}px;fill:{BK};text-anchor:middle">'
        f'<textPath xlink:href="#crest-arc" startOffset="50%">'
        f'REGIME FOR ECOLOGICAL INTEGRITY AND GLOBAL NURTURING</textPath></text>',
        f'<text x="{cx}" y="{cy + 91*k:.2f}" style="{HEAD};font-size:{9*k:.2f}px;'
        f'letter-spacing:{2*k:.2f}px;fill:{BK};text-anchor:middle">· R.E.I.G.N. ·</text>',
        stag(cx, cy + 6 * k, 0.5 * k)])


def piece_crest():
    c = W / 2
    outline = f'<circle cx="{c}" cy="{c}" r="{c - 1}" fill="{WH}"/>'
    return svg(layer("crest", crest_group(c, c, c - 4)), W, W, "REIGN Crest",
               outline=outline, holes=((c, 12),))


# ======================================== A4 slogan series (10 per sheet)
# Each icon is drawn inside a disc of radius r around (cx, cy), and each
# one uses the cutter for something: holes, slots or a light screen.
SW, SH = 210, 297


def _arc(cx, cy, rad, a0, a1):
    p0 = (cx + rad * math.cos(math.radians(a0)), cy + rad * math.sin(math.radians(a0)))
    p1 = (cx + rad * math.cos(math.radians(a1)), cy + rad * math.sin(math.radians(a1)))
    return f"M{p0[0]:.2f},{p0[1]:.2f} A{rad:.2f},{rad:.2f} 0 0 1 {p1[0]:.2f},{p1[1]:.2f}"


def ic_drop(cx, cy, r):
    """Water drop; the puddle ripples are cut slots."""
    t, b, br = cy - .78 * r, cy + .12 * r, .44 * r
    drop = (f'<path d="M{cx},{t:.2f} C{cx + .12*r:.2f},{cy - .45*r:.2f} {cx + br:.2f},{b - .3*r:.2f} '
            f'{cx + br:.2f},{b:.2f} A{br:.2f},{br:.2f} 0 0 1 {cx - br:.2f},{b:.2f} '
            f'C{cx - br:.2f},{b - .3*r:.2f} {cx - .12*r:.2f},{cy - .45*r:.2f} {cx},{t:.2f} Z" fill="{BK}"/>')
    shine = (f'<path d="{_arc(cx, b, br * .68, 110, 170)}" fill="none" stroke="{WH}" '
             f'stroke-width="{.06*r:.2f}" stroke-linecap="round"/>')
    ripples = "".join(f'<path d="M{cx - rx:.2f},{cy + .6*r:.2f} A{rx:.2f},{ry:.2f} 0 0 0 {cx + rx:.2f},{cy + .6*r:.2f}" '
                      f'fill="none" stroke="{CUT}" stroke-width="{.05*r:.2f}" stroke-linecap="round"/>'
                      for rx, ry in ((.62 * r, .13 * r), (.84 * r, .22 * r)))
    return drop + shine + ripples


def ic_eye(cx, cy, r):
    """The all-seeing eye; the pupil is a hole straight through the wall."""
    P0, C, P2 = (cx - .92 * r, cy), (cx, cy - .85 * r), (cx + .92 * r, cy)
    out = [f'<path d="M{P0[0]:.2f},{cy} Q{cx},{cy - .85*r:.2f} {P2[0]:.2f},{cy} '
           f'Q{cx},{cy + .85*r:.2f} {P0[0]:.2f},{cy} Z" fill="{BK}"/>',
           f'<circle cx="{cx}" cy="{cy}" r="{.36*r:.2f}" fill="{WH}"/>',
           sunburst(cx, cy, .32 * r, n=18),
           f'<circle cx="{cx}" cy="{cy}" r="{.17*r:.2f}" fill="{WH}"/>',
           f'<circle cx="{cx}" cy="{cy}" r="{.11*r:.2f}" fill="{CUT}"/>']
    for t in (.2, .3, .4, .5, .6, .7, .8):  # lashes along the upper lid
        x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * C[0] + t ** 2 * P2[0]
        y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * C[1] + t ** 2 * P2[1]
        dx, dy = x - cx, y - (cy + .35 * r)
        n = math.hypot(dx, dy)
        dx, dy = dx / n, dy / n
        out.append(f'<line x1="{x + dx*.06*r:.2f}" y1="{y + dy*.06*r:.2f}" x2="{x + dx*.2*r:.2f}" '
                   f'y2="{y + dy*.2*r:.2f}" stroke="{BK}" stroke-width="{.055*r:.2f}" stroke-linecap="round"/>')
    return "\n".join(out)


def ic_obey(cx, cy, r):
    """The word itself, cut through stencil-style; glows when backlit."""
    return stencil_text(cx, cy + .55 * r, "OBEY", 184, 118)


def ic_wheel(cx, cy, r):
    """Bicycle wheel; the gaps between the spokes are cut out."""
    out = [f'<circle cx="{cx}" cy="{cy}" r="{.9*r:.2f}" fill="none" stroke="{BK}" stroke-width="{.14*r:.2f}"/>',
           f'<circle cx="{cx}" cy="{cy}" r="{.76*r:.2f}" fill="none" stroke="{BK}" stroke-width="{.03*r:.2f}"/>']
    ri, ro = .2 * r, .7 * r
    for k in range(8):
        a0, a1 = k * 45 + 6, (k + 1) * 45 - 6
        q = lambda rad, a: (cx + rad * math.cos(math.radians(a)), cy + rad * math.sin(math.radians(a)))
        p = [q(ri, a0), q(ro, a0), q(ro, a1), q(ri, a1)]
        out.append(f'<path d="M{p[0][0]:.2f},{p[0][1]:.2f} L{p[1][0]:.2f},{p[1][1]:.2f} '
                   f'A{ro:.2f},{ro:.2f} 0 0 1 {p[2][0]:.2f},{p[2][1]:.2f} L{p[3][0]:.2f},{p[3][1]:.2f} '
                   f'A{ri:.2f},{ri:.2f} 0 0 0 {p[0][0]:.2f},{p[0][1]:.2f} Z" fill="{CUT}"/>')
    out += [f'<circle cx="{cx}" cy="{cy}" r="{.14*r:.2f}" fill="{BK}"/>',
            f'<circle cx="{cx}" cy="{cy}" r="{.05*r:.2f}" fill="{WH}"/>']
    return "\n".join(out)


def ic_lungs(cx, cy, r):
    """Lungs that are also a tree; the airways are cut through."""
    out = [f'<rect x="{cx - .06*r:.2f}" y="{cy - .72*r:.2f}" width="{.12*r:.2f}" height="{.5*r:.2f}" fill="{BK}"/>']
    for sx in (-1, 1):
        X = lambda f: cx + sx * f * r
        out.append(f'<path d="M{X(.1):.2f},{cy - .3*r:.2f} C{X(.35):.2f},{cy - .58*r:.2f} {X(.78):.2f},{cy - .2*r:.2f} '
                   f'{X(.74):.2f},{cy + .3*r:.2f} C{X(.72):.2f},{cy + .66*r:.2f} {X(.36):.2f},{cy + .72*r:.2f} '
                   f'{X(.1):.2f},{cy + .56*r:.2f} Z" fill="{BK}"/>')
        out.append(f'<path d="M{X(.13):.2f},{cy - .12*r:.2f} L{X(.36):.2f},{cy + .12*r:.2f} '
                   f'M{X(.27):.2f},{cy + .02*r:.2f} L{X(.5):.2f},{cy - .12*r:.2f} '
                   f'M{X(.36):.2f},{cy + .12*r:.2f} L{X(.52):.2f},{cy + .36*r:.2f} '
                   f'M{X(.36):.2f},{cy + .12*r:.2f} L{X(.27):.2f},{cy + .46*r:.2f}" fill="none" '
                   f'stroke="{CUT}" stroke-width="{.06*r:.2f}" stroke-linecap="round"/>')
        # a sprouting leaf on top of the windpipe
        out.append(f'<ellipse cx="{X(.14):.2f}" cy="{cy - .8*r:.2f}" rx="{.14*r:.2f}" ry="{.06*r:.2f}" '
                   f'transform="rotate({sx * -30} {X(.14):.2f} {cy - .8*r:.2f})" fill="{BK}"/>')
    return "\n".join(out)


def ic_box(cx, cy, r):
    """An empty crate, flaps open; its 'contents' are slots cut above it."""
    q = lambda x, y: (cx + x * r, cy + y * r)
    out = [poly([q(-.6, .02), q(0, .34), q(0, .86), q(-.6, .54)]),
           poly([q(0, .34), q(.6, .02), q(.6, .54), q(0, .86)]),
           poly([q(-.6, .02), q(0, -.3), q(.6, .02), q(0, .34)], WH,
                f'stroke="{BK}" stroke-width="{.04*r:.2f}" stroke-linejoin="round"'),
           f'<path d="M{cx},{cy - .3*r:.2f} L{cx},{cy - .08*r:.2f} L{cx - .44*r:.2f},{cy + .14*r:.2f} '
           f'M{cx},{cy - .08*r:.2f} L{cx + .44*r:.2f},{cy + .14*r:.2f}" fill="none" stroke="{BK}" '
           f'stroke-width="{.03*r:.2f}"/>',
           poly([q(-.6, .02), q(-.92, -.12), q(-.36, -.46), q(0, -.3)], BK,
                f'stroke="{WH}" stroke-width="{.02*r:.2f}"'),
           poly([q(0, .34), q(.6, .02), q(.9, .2), q(.3, .52)], BK, f'stroke="{WH}" stroke-width="{.025*r:.2f}"'),
           f'<line x1="{cx}" y1="{cy + .34*r:.2f}" x2="{cx}" y2="{cy + .86*r:.2f}" stroke="{WH}" stroke-width="{.025*r:.2f}"/>']
    for x in (-.24, 0, .24):  # vanished belongings, rising
        out.append(f'<line x1="{cx + x*r:.2f}" y1="{cy - .5*r:.2f}" x2="{cx + x*r:.2f}" y2="{cy - .82*r:.2f}" '
                   f'stroke="{CUT}" stroke-width="{.06*r:.2f}" stroke-linecap="round" '
                   f'stroke-dasharray="{.08*r:.2f} {.07*r:.2f}"/>')
    return "\n".join(out)


def ic_megaphone(cx, cy, r):
    """Agit-prop loudhailer; the sound waves are cut slots."""
    q = lambda x, y: (cx + x * r, cy + y * r)
    body = (poly([q(-.42, -.12), q(.22, -.46), q(.22, .46), q(-.42, .12)]) +
            f'<rect x="{cx + .2*r:.2f}" y="{cy - .5*r:.2f}" width="{.08*r:.2f}" height="{r:.2f}" fill="{BK}"/>' +
            f'<rect x="{cx - .6*r:.2f}" y="{cy - .15*r:.2f}" width="{.16*r:.2f}" height="{.3*r:.2f}" fill="{BK}"/>' +
            poly([q(-.32, .1), q(-.18, .1), q(-.25, .46), q(-.39, .46)]))
    waves = "".join(f'<path d="{_arc(cx + .3*r, cy, rad * r, -38, 38)}" fill="none" stroke="{CUT}" '
                    f'stroke-width="{.06*r:.2f}" stroke-linecap="round"/>' for rad in (.22, .38, .54))
    return f'<g transform="rotate(-14 {cx} {cy})">{body}{waves}</g>'


def ic_figures(cx, cy, r):
    """A family shrinking into a single sprout."""
    base = cy + .55 * r
    out = [f'<rect x="{cx - .8*r:.2f}" y="{base:.2f}" width="{1.6*r:.2f}" height="{.05*r:.2f}" fill="{BK}"/>']
    for x, h in ((-.58, .95), (-.1, .68), (.26, .48)):
        X, hh = cx + x * r, h * r
        out.append(f'<circle cx="{X:.2f}" cy="{base - hh + .11*hh:.2f}" r="{.11*hh:.2f}" fill="{BK}"/>')
        out.append(poly([(X - .19 * hh, base - hh + .27 * hh), (X + .19 * hh, base - hh + .27 * hh),
                         (X + .13 * hh, base), (X - .13 * hh, base)]))
        out.append(f'<rect x="{X - .02*hh:.2f}" y="{base - .35*hh:.2f}" width="{.04*hh:.2f}" '
                   f'height="{.35*hh:.2f}" fill="{WH}"/>')
    sx = cx + .6 * r
    out.append(f'<rect x="{sx - .025*r:.2f}" y="{base - .34*r:.2f}" width="{.05*r:.2f}" height="{.34*r:.2f}" fill="{BK}"/>')
    for d in (-1, 1):
        out.append(f'<ellipse cx="{sx + d*.1*r:.2f}" cy="{base - .36*r:.2f}" rx="{.11*r:.2f}" ry="{.05*r:.2f}" '
                   f'transform="rotate({d * -30} {sx + d*.1*r:.2f} {base - .36*r:.2f})" fill="{BK}"/>')
    # dotted 'fading' arrow from people to plant, cut
    out.append(f'<path d="M{cx - .5*r:.2f},{cy - .62*r:.2f} Q{cx + .1*r:.2f},{cy - .9*r:.2f} {cx + .55*r:.2f},{cy - .3*r:.2f}" '
               f'fill="none" stroke="{CUT}" stroke-width="{.05*r:.2f}" stroke-linecap="round" '
               f'stroke-dasharray="{.06*r:.2f} {.07*r:.2f}"/>')
    return "\n".join(out)


def ic_sunrise(cx, cy, r):
    """The state permits the sunrise; the rays are cut through."""
    y0 = cy + .3 * r
    rays = (f'<clipPath id="sun-clip"><path d="M{cx - .9*r:.2f},{y0:.2f} A{.9*r:.2f},{.9*r:.2f} 0 0 1 '
            f'{cx + .9*r:.2f},{y0:.2f} Z"/></clipPath>'
            f'<g clip-path="url(#sun-clip)">{sunburst(cx, y0, 1.2 * r, n=22, fill=CUT, phase=math.pi / 22)}</g>')
    sun = (f'<path d="M{cx - .42*r:.2f},{y0:.2f} A{.42*r:.2f},{.42*r:.2f} 0 0 1 {cx + .42*r:.2f},{y0:.2f} Z" '
           f'fill="{WH}" stroke="{BK}" stroke-width="{.06*r:.2f}"/>')
    fields = "".join(f'<rect x="{cx - w*r:.2f}" y="{y0 + d*r:.2f}" width="{2*w*r:.2f}" height="{.05*r:.2f}" fill="{BK}"/>'
                     for w, d in ((.86, .02), (.7, .16), (.5, .3), (.28, .44)))
    sx, base = cx, y0 - .02 * r  # a seedling standing in front of the sun
    sprout = (f'<rect x="{sx - .04*r:.2f}" y="{base - .58*r:.2f}" width="{.08*r:.2f}" height="{.58*r:.2f}" fill="{BK}"/>' +
              "".join(f'<ellipse cx="{sx + d*.2*r:.2f}" cy="{base - .62*r:.2f}" rx="{.21*r:.2f}" ry="{.085*r:.2f}" '
                      f'transform="rotate({d * -28} {sx + d*.2*r:.2f} {base - .62*r:.2f})" fill="{BK}"/>'
                      for d in (-1, 1)))
    return rays + sun + fields + sprout


def ic_snowflake(cx, cy, r):
    """A snowflake cut clean through, so the cold can come in."""
    d = []
    for k in range(6):
        a = math.radians(k * 60 - 90)
        ux, uy = math.cos(a), math.sin(a)
        d.append(f"M{cx:.2f},{cy:.2f} L{cx + ux*.72*r:.2f},{cy + uy*.72*r:.2f}")
        for f, L in ((.38, .22), (.58, .15)):
            bx, by = cx + ux * f * r, cy + uy * f * r
            for s in (-1, 1):
                b = a + s * math.radians(60)
                d.append(f"M{bx:.2f},{by:.2f} L{bx + math.cos(b)*L*r:.2f},{by + math.sin(b)*L*r:.2f}")
    return (f'<circle cx="{cx}" cy="{cy}" r="{.9*r:.2f}" fill="none" stroke="{BK}" stroke-width="{.03*r:.2f}" '
            f'stroke-dasharray="{.1*r:.2f} {.06*r:.2f}"/>'
            f'<path d="{" ".join(d)}" fill="none" stroke="{CUT}" stroke-width="{.1*r:.2f}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


# name, icon, headline lines, subline lines, footer, background variant.
# Deliberately generic: no leader or ministry names (both still undecided).
SERIES = [
    ("07_conserve", ic_drop, ["CONSERVE"],
     ["EVERY DROP YOU DON'T DRINK", "IS A GIFT TO THE EARTH"], "DECREE Nº 07 · R.E.I.G.N. · ECOTOPIA", 0),
    ("08_you_are_watched", ic_eye, ["YOU ARE WATCHED"],
     ["BECAUSE YOU ARE LOVED.", "SMILE FOR THE CAMERAS · THEY SMILE FOR YOU"], "DECREE Nº 08 · R.E.I.G.N. · ECOTOPIA", 1),
    ("09_obey", ic_obey, ["GLADLY."],
     ["OBEDIENCE IS THE ONLY", "TRULY RENEWABLE RESOURCE"], "DECREE Nº 09 · R.E.I.G.N. · ECOTOPIA", 2),
    ("10_pedal", ic_wheel, ["PEDAL"],
     ["EVERY JOULE YOU GIVE", "IS A JOULE THE EARTH KEEPS"], "DECREE Nº 10 · R.E.I.G.N. · ECOTOPIA", 1),
    ("11_breathe_less", ic_lungs, ["BREATHE LESS"],
     ["EXHALE ONLY WHEN NECESSARY.", "CO2 IS A PRIVILEGE, NOT A RIGHT."], "DECREE Nº 11 · R.E.I.G.N. · ECOTOPIA", 0),
    ("12_own_nothing", ic_box, ["OWN NOTHING"],
     ["POSSESSIONS ARE CARBON.", "SURRENDER THEM WITH A SMILE."], "DECREE Nº 12 · R.E.I.G.N. · ECOTOPIA", 2),
    ("13_speak_up", ic_megaphone, ["SPEAK UP"],
     ["A HEATER LEFT ON IS YOUR NEIGHBOUR'S", "CRY FOR HELP. REPORT IT. SAVE THEM."], "DECREE Nº 13 · R.E.I.G.N. · ECOTOPIA", 0),
    ("14_smaller_is_greener", ic_figures, ["SMALLER IS", "GREENER"],
     ["ONE CHILD. OR BETTER STILL: ONE PLANT."], "DECREE Nº 14 · R.E.I.G.N. · ECOTOPIA", 1),
    ("15_give_thanks", ic_sunrise, ["GIVE THANKS"],
     ["THIS MORNING THE STATE", "ALLOWED THE SUN TO RISE"], "DECREE Nº 15 · R.E.I.G.N. · ECOTOPIA", 2),
    ("16_cold_is_cozy", ic_snowflake, ["COLD IS COZY"],
     ["HEATING IS A HABIT OF", "THE OLD, BURNING WORLD"], "DECREE Nº 16 · R.E.I.G.N. · ECOTOPIA", 0),
]


def slogan_panel(icon, heads, subs, footer, variant):
    cx, cy, r = SW / 2, 100, 58
    disc = icon is not ic_obey
    if variant == 0:    # constructivist diagonal split
        bg = clipped(f"s{id(icon)}", 1, 1, SW - 2, SH - 2, poly([(0, 0), (SW, 0), (SW, 128), (0, 176)]))
    elif variant == 1:  # sunburst
        bg = clipped(f"s{id(icon)}", 1, 1, SW - 2, 178, sunburst(cx, cy, 250, n=24, phase=0.13))
    else:               # plain wood, heavy top bar
        bg = f'<rect x="1" y="1" width="{SW - 2}" height="16" rx="6" fill="{BK}"/>'
    if disc:
        bg += (f'<circle cx="{cx}" cy="{cy}" r="{r + 6}" fill="{WH}"/>'
               f'<circle cx="{cx}" cy="{cy}" r="{r + 6}" fill="none" stroke="{BK}" stroke-width="2.4"/>')
    if len(heads) == 1:
        hy, rule, sy, ss = [226], 233, [247, 259], 9.5
        head_txt = fit(cx, 226, heads[0], 188, 48)
    else:
        hy, rule, sy, ss = [206, 242], 249, [263], 9.5
        head_txt = "".join(fit(cx, y, h, 188, 36) for y, h in zip(hy, heads))
    type_ = (head_txt + f'<rect x="11" y="{rule}" width="188" height="1.6" fill="{BK}"/>' +
             "".join(fit(cx, y, s, 188, ss, SUB) for y, s in zip(sy, subs)) +
             f'<rect x="1" y="278" width="{SW - 2}" height="18" rx="6" fill="{BK}"/>' +
             text(cx, 290, footer, 7, MONO, fill=WH))
    return svg(layer("background", bg) + layer("icon", icon(cx, cy, r)) + layer("type", type_),
               SW, SH, heads[0].title(), holes=((12, 9), (SW - 12, 9)))


def nest_sheet(names, cols=5, gap=2.0, tag="sheet_A4x10"):
    """Lay the A4 panels out on one 1200x600 poplar sheet as a single job."""
    rows = math.ceil(len(names) / cols)
    sw, sh = cols * SW + (cols - 1) * gap, rows * SH + (rows - 1) * gap
    k = ENGRAVE_DPI / 25.4
    eng = Image.new("1", (round(sw * k), round(sh * k)), 1)
    prev = Image.new("RGB", (round(sw * k / 4), round(sh * k / 4)), (60, 60, 64))
    paths, fills = [], []
    for i, name in enumerate(names):
        x, y = (i % cols) * (SW + gap), (i // cols) * (SH + gap)
        eng.paste(Image.open(out(f"{name}_engrave.png")), (round(x * k), round(y * k)))
        p = Image.open(out(f"{name}_preview.png"))
        prev.paste(p.resize((p.width // 4, p.height // 4)), (round(x * k / 4), round(y * k / 4)))
        with open(out(f"{name}_laser.svg")) as f:
            doc = f.read()
        grab = lambda gid: doc.split(f'<g id="{gid}">', 1)[1].split("</g>", 1)[0].strip()
        paths.append(f'<g transform="translate({x:.2f},{y:.2f})">\n{grab("cut")}\n</g>')
        fills.append(f'<g transform="translate({x:.2f},{y:.2f})">\n{grab("engrave")}\n</g>')
    eng.save(out(f"{tag}_engrave.png"), dpi=(ENGRAVE_DPI, ENGRAVE_DPI))
    prev.save(out(f"{tag}_preview.png"))
    with open(out(f"{tag}_cut.svg"), "w") as f:
        f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{sw:.1f}mm" height="{sh:.1f}mm" viewBox="0 0 {sw:.1f} {sh:.1f}">
<!-- {len(names)} A4 panels on one 1200x600 sheet. RED = CUT. Same origin as {tag}_engrave.png -->
<g id="cut">
{chr(10).join(paths)}
</g>
</svg>
""")
    with open(out(f"{tag}_laser.svg"), "w") as f:
        f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{sw:.1f}mm" height="{sh:.1f}mm" viewBox="0 0 {sw:.1f} {sh:.1f}">
<!-- {len(names)} A4 panels, one 1200x600 sheet. BLACK = ENGRAVE, BLUE = inner cuts, RED = outlines (last). -->
<g id="engrave">
{chr(10).join(fills)}
</g>
<g id="cut">
{chr(10).join(paths)}
</g>
</svg>
""")
    print(f"{tag}: {sw:.0f} x {sh:.0f} mm")


# ================================================================== build
def render(svg_path, dpi):
    tmp = os.path.join(OUT, f".render_{dpi}.png")
    subprocess.run(["inkscape", svg_path, "--export-type=png", f"--export-filename={tmp}",
                    f"--export-dpi={dpi}", "--export-background=#ff0000",
                    "--export-background-opacity=1"], check=True, capture_output=True)
    a = np.asarray(Image.open(tmp).convert("RGB")).astype(int)
    os.remove(tmp)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    cut = (r > 128) & (g < 128) & (b < 128)
    ink = (r < 128) & (g < 128) & (b < 128)
    return cut, ink


def bridge_islands(cut, px_mm, auto):
    """Wood not connected to the main piece falls out. Bridge it upward
    (stencil-style) or just report it."""
    msgs = []
    bw = max(1, round(BRIDGE_MM / px_mm))
    for _ in range(60):
        lab, n = ndimage.label(~cut)
        if n <= 1:
            break
        sizes = ndimage.sum(np.ones_like(lab), lab, range(1, n + 1))
        main = 1 + int(np.argmax(sizes))
        islands = [i for i in range(1, n + 1) if i != main]
        if not auto:
            for i in islands:
                ys, xs = np.nonzero(lab == i)
                msgs.append(f"  ! loose island {sizes[i-1]*px_mm**2:.0f} mm² at "
                            f"({xs.mean()*px_mm:.0f}, {ys.mean()*px_mm:.0f}) mm")
            break
        for i in islands:
            ys, xs = np.nonzero(lab == i)
            top = ys.min()  # bridge up from the island's highest point
            x = int(np.median(xs[ys == top]))
            x0, x1 = max(0, x - bw // 2), x + bw - bw // 2
            y = top
            while y > 0 and not (lab[y - 1, x0:x1] == main).any():
                y -= 1
            cut[max(0, y - 1):top + 1, x0:x1] = False
        msgs.append(f"  bridged {len(islands)} island(s)")
    return cut, msgs


def thin_wood(cut, px_mm):
    r = max(1, round(MIN_WOOD_MM / px_mm / 2))
    disk = np.hypot(*np.mgrid[-r:r + 1, -r:r + 1]) <= r
    wood = ~cut
    lost = wood & ~ndimage.binary_opening(wood, structure=disk)
    lab, n = ndimage.label(lost)
    areas = ndimage.sum(lost, lab, range(1, n + 1)) * px_mm ** 2
    msgs = []
    for i, a in enumerate(areas):
        if a > 4:  # smaller ones are just sharp inside corners
            y, x = ndimage.center_of_mass(lost, lab, i + 1)
            msgs.append(f"  ! wood strip thinner than {MIN_WOOD_MM} mm ({a:.0f} mm²) "
                        f"at ({x*px_mm:.0f}, {y*px_mm:.0f}) mm")
    return msgs


def trace_mask(mask, px_mm, w, h):
    """Trace a boolean mask into SVG path data (mm), like Inkscape's Trace
    Bitmap. Returns (path data, total outline length in mm)."""
    curves = potrace.Bitmap(~mask).trace(turdsize=4, alphamax=1.0, opticurve=True, opttolerance=0.2)
    d, length = [], 0.0
    P = lambda p: f"{p.x * px_mm:.3f},{p.y * px_mm:.3f}"
    for c in curves:
        pts = [c.start_point] + [s.end_point for s in c.segments]
        xs, ys = [p.x * px_mm for p in pts], [p.y * px_mm for p in pts]
        if min(xs) < 0.3 and min(ys) < 0.3 and max(xs) > w - 0.3 and max(ys) > h - 0.3:
            continue  # the sheet edge itself, not a shape
        seg = [f"M{P(c.start_point)}"]
        prev = c.start_point
        for s in c.segments:
            seg.append(f"L{P(s.c)} L{P(s.end_point)}" if s.is_corner else
                       f"C{P(s.c1)} {P(s.c2)} {P(s.end_point)}")
            length += math.hypot(s.end_point.x - prev.x, s.end_point.y - prev.y) * px_mm
            prev = s.end_point
        d.append(" ".join(seg) + "Z")
    return " ".join(d), length


ENGRAVE_ATTR = 'fill="#000000" stroke="#000000" stroke-width="0.1"'
CUT_ATTR = 'fill="none" stroke="#ff0000" stroke-width="0.1"'
INNER_ATTR = 'fill="none" stroke="#0000ff" stroke-width="0.1"'


def split_cuts(d):
    """Separate the piece's outer outline (largest shape) from the inner
    cuts, so LightBurn gets them as two layers: blue inner first, red last."""
    parts = [p.strip() for p in d.split("Z") if p.strip()]
    def area(p):
        n = [float(v) for v in re.findall(r"-?\d+\.?\d*", p)]
        xs, ys = n[0::2], n[1::2]
        return (max(xs) - min(xs)) * (max(ys) - min(ys))
    outer = max(parts, key=area)
    return outer + "Z", "".join(p + "Z" for p in parts if p is not outer)


def _poly(part):
    n = [float(v) for v in re.findall(r"-?\d+\.?\d*", part)]
    return list(zip(n[0::2], n[1::2]))


def _inside(pt, poly):
    x, y, hit = pt[0], pt[1], False
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            hit = not hit
    return hit


def shapes(d, attr, holes=False):
    """One <path> per shape, styles spelled out on every path (LightBurn
    skipped a single giant fill-only path). With holes=True each outline
    keeps its holes (letter counters, the white disc) in the same path."""
    parts = [p.strip() + "Z" for p in d.split("Z") if p.strip()]
    if not holes:
        return "\n".join(f'<path {attr} d="{p}"/>' for p in parts)
    polys = [_poly(p) for p in parts]
    owners = [[j for j in range(len(parts)) if j != i and _inside(polys[i][0], polys[j])]
              for i in range(len(parts))]
    groups = {}
    for i, own in enumerate(owners):
        if len(own) % 2 == 0:           # even depth: a solid outline
            groups.setdefault(i, [i])
        else:                           # odd depth: a hole in its innermost owner
            parent = max(own, key=lambda j: len(owners[j]))
            groups.setdefault(parent, [parent]).append(i)
    return "\n".join(f'<path {attr} fill-rule="evenodd" d="{" ".join(parts[i] for i in g)}"/>'
                     for g in groups.values())


def laser_svg(w, h, cut_d, engrave_d=None, note=""):
    """LightBurn-ready vector file: black shapes = engrave (Fill mode),
    red hairlines = cut (Line mode). Engrave runs first: keep layer order."""
    eng = f'<g id="engrave">\n{shapes(engrave_d, ENGRAVE_ATTR, holes=True)}\n</g>\n' if engrave_d else ""
    outer, inner = split_cuts(cut_d)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}">
<!-- Layer order in LightBurn: BLACK = ENGRAVE (Fill), then BLUE = inner cuts (Line),
     then RED = outer outline (Line, last). Cuts: 4mm poplar 100% @ 8 mm/s. {note} -->
{eng}<g id="cut">
{shapes(inner, INNER_ATTR)}
{shapes(outer, CUT_ATTR)}
</g>
</svg>
"""


def build(name, doc, w, h, auto_bridge=False):
    master = out(f"{name}.svg")
    with open(master, "w") as f:
        f.write(doc)
    log = [name]

    cut, _ = render(master, CUT_DPI)
    px = 25.4 / CUT_DPI
    cut, msgs = bridge_islands(cut, px, auto_bridge)
    log += msgs + thin_wood(cut, px)
    cut_d, cut_len = trace_mask(cut, px, w, h)
    with open(out(f"{name}_cut.svg"), "w") as f:
        f.write(laser_svg(w, h, cut_d, note="Same origin as _engrave.png"))

    cut_hi, ink = render(master, ENGRAVE_DPI)
    # re-apply bridges at engrave resolution, then never engrave scrap
    cut_hi &= np.asarray(Image.fromarray(cut).resize(ink.shape[::-1], Image.NEAREST))
    ink &= ~cut_hi
    Image.fromarray(~ink).convert("1").save(out(f"{name}_engrave.png"),
                                            dpi=(ENGRAVE_DPI, ENGRAVE_DPI))
    eng_d, _ = trace_mask(ink, 25.4 / ENGRAVE_DPI, w, h)
    with open(out(f"{name}_laser.svg"), "w") as f:
        f.write(laser_svg(w, h, cut_d, eng_d, note="All-in-one: import this file alone."))

    # preview: poplar, burned engraving, cut-away shown as dark background
    prev = np.empty(ink.shape + (3,), np.uint8)
    prev[:] = (226, 196, 150)
    prev[ink] = (74, 44, 24)
    prev[cut_hi] = (60, 60, 64)
    Image.fromarray(prev).save(out(f"{name}_preview.png"))

    hpx = 25.4 / ENGRAVE_DPI
    cols = np.where(ink.any(axis=1))[0]
    travel = 0.0
    for y in cols[::max(1, round(LINE_GAP / hpx))]:
        xs = np.nonzero(ink[y])[0]
        travel += (xs[-1] - xs[0]) * hpx
    eng_min = travel / ENGRAVE_SPEED / 60 * 1.3
    cut_min = cut_len / CUT_SPEED / 60
    log.append(f"  cut {cut_len/1000:.1f} m ≈ {cut_min:.0f} min · engrave ≈ {eng_min:.0f} min · "
               f"≈ € {(cut_min + eng_min) * 0.10:.2f}")
    print("\n".join(log))


def overview(names, tag, height=900):
    """All previews side by side in one image."""
    ims = [Image.open(out(f"{n}_preview.png")) for n in names]
    ims = [i.resize((round(i.width * height / i.height), height)) for i in ims]
    sheet = Image.new("RGB", (sum(i.width + 12 for i in ims), height), (255, 255, 255))
    x = 0
    for i in ims:
        sheet.paste(i, (x, 0))
        x += i.width + 12
    sheet.save(out(f"{tag}_preview.png"))


def laser_to_pdf(laser_svg_path, pdf_path, w, h, scale=1.0):
    """Paper version of a laser file: engraving solid black, cut lines as
    black hairlines (red would print as muddy grey on the mono Brother)."""
    with open(laser_svg_path) as f:
        body = f.read().split("-->", 1)[1].rsplit("</svg>", 1)[0]
    body = body.replace('stroke="#ff0000" stroke-width="0.1"', 'stroke="#000000" stroke-width="0.3"')
    ox, oy = w * (1 - scale) / 2, h * (1 - scale) / 2
    tmp = os.path.join(BUILD, ".print.svg")
    with open(tmp, "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" '
                f'viewBox="0 0 {w} {h}"><g transform="translate({ox:.3f},{oy:.3f}) '
                f'scale({scale})">{body}</g></svg>')
    subprocess.run(["inkscape", tmp, "--export-type=pdf", f"--export-filename={pdf_path}"],
                   check=True, capture_output=True)
    os.remove(tmp)


def publish(pieces, series):
    """The two folders people actually use:
    posters/posters/      one PDF per poster, to look at and print
    posters/lasercutter/  one LightBurn file per poster (+ the full A4 sheet)"""
    pdf_dir, laser_dir = os.path.join(OUT, "posters"), os.path.join(OUT, "lasercutter")
    os.makedirs(pdf_dir, exist_ok=True)
    os.makedirs(laser_dir, exist_ok=True)
    for name, _, w, h, _ in pieces:
        src = out(f"{name}_laser.svg")
        shutil.copyfile(src, os.path.join(laser_dir, f"{pretty(name)}.svg"))
        # A4 panels shrink 6% to clear the Brother's margins; big pieces stay
        # true size (print at a copy shop, or 'fit to page' onto A4)
        laser_to_pdf(src, os.path.join(pdf_dir, f"{pretty(name)}.pdf"), w, h,
                     0.94 if name in series else 1.0)
    shutil.copyfile(out("sheet_A4x10_laser.svg"), os.path.join(laser_dir, "All ten A4 on one sheet.svg"))
    subprocess.run(["pdfunite", *[os.path.join(pdf_dir, f"{pretty(n)}.pdf") for n in series],
                    os.path.join(pdf_dir, "Print all ten A4.pdf")], check=True)


def main():
    os.makedirs(OUT, exist_ok=True)
    pieces = [
        ("01_apply_for_citizenship", piece_apply(), W, H, False),
        ("02_recycling_plant", piece_recycling(), W, H, False),
        ("03_darkness_light_screen", piece_lights(), W, H, False),
        ("04_guardian_stag_trophy", piece_trophy(), TW, TH, False),
        ("05_resistance_stencil", piece_stencil(), W, H, True),
        ("06_reign_crest_plaque", piece_crest(), W, W, False),
    ]
    pieces += [(name, slogan_panel(icon, heads, subs, footer, v), SW, SH, icon is ic_obey)
               for name, icon, heads, subs, footer, v in SERIES]
    only = sys.argv[1:]
    for name, doc, w, h, auto in pieces:
        if not only or any(o in name for o in only):
            build(name, doc, w, h, auto)
    series = [s[0] for s in SERIES]
    nest_sheet(series)
    overview([p[0] for p in pieces[:6]], "overview_A3_pieces")
    publish(pieces, series)
    print("output:", os.path.abspath(OUT))


if __name__ == "__main__":
    main()
