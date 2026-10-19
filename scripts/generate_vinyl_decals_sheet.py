#!/usr/bin/env python3
"""
Generate Easy Cut Studio ready vinyl cutting sheet for Bitlair Vinylsnijder.
Sheet width: 600mm, height: 400mm.
Pure vector cut outlines for resistance stickers, boundary warning strips, and covert text tags.
"""

sheet_w = 600
sheet_h = 350

svg_parts = [
    f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {sheet_w} {sheet_h}" width="{sheet_w}mm" height="{sheet_h}mm">
  <!-- EASY CUT STUDIO VINYL CUT SHEET (BITLAIR 61CM VINYLSNIJDER) -->
  <defs>
    <style>
      .cut-line {{ fill: none; stroke: #000000; stroke-width: 0.2; }}
      .cut-text {{ font-family: monospace, sans-serif; font-weight: 900; fill: none; stroke: #000000; stroke-width: 0.25; }}
    </style>
  </defs>'''
]

# 1. 24 Resistance Round Decals (4 rows x 6 cols, 40mm each)
radius = 18
for row in range(4):
    for col in range(6):
        cx = 25 + col * 42
        cy = 25 + row * 42
        
        # Outer cut circle
        svg_parts.append(f'  <circle cx="{cx}" cy="{cy}" r="{radius}" class="cut-line"/>')
        
        # Inner decorative circle (kiss-cut or peel)
        svg_parts.append(f'  <circle cx="{cx}" cy="{cy}" r="{radius - 3}" class="cut-line"/>')
        
        # Cracked Antlers emblem
        svg_parts.append(f'  <line x1="{cx}" y1="{cy+9}" x2="{cx}" y2="{cy}" class="cut-line"/>')
        # Left antler
        svg_parts.append(f'  <path d="M {cx} {cy} Q {cx-5} {cy-3} {cx-8} {cy-8} M {cx-6} {cy-5} Q {cx-11} {cy-7} {cx-12} {cy-11}" class="cut-line"/>')
        # Right antler
        svg_parts.append(f'  <path d="M {cx} {cy} Q {cx+5} {cy-3} {cx+8} {cy-8} M {cx+6} {cy-5} Q {cx+11} {cy-7} {cx+12} {cy-11}" class="cut-line"/>')
        # Center glitch fracture
        svg_parts.append(f'  <path d="M {cx-1} {cy-10} L {cx+1} {cy-6} L {cx-1} {cy-2} L {cx+1} {cy+2} L {cx-1} {cy+6}" class="cut-line"/>')

# 2. 6 Large 15-Minute Sanctuary Boundary Warning Strips (Right side, x = 270..590)
strip_w = 310
strip_h = 24
for s in range(6):
    sy = 15 + s * 28
    svg_parts.append(f'  <rect x="270" y="{sy}" width="{strip_w}" height="{strip_h}" rx="2" class="cut-line"/>')
    svg_parts.append(f'  <text x="425" y="{sy + 10}" text-anchor="middle" font-size="6" class="cut-text" letter-spacing="1">15-MINUTE SANCTUARY PERIMETER</text>')
    svg_parts.append(f'  <text x="425" y="{sy + 19}" text-anchor="middle" font-size="4.5" class="cut-text" letter-spacing="0.8">STATE CITIZEN AUDIT ZONE • PASSPORT REQUIRED</text>')

# 3. 16 Covert Text Decals (Bottom half: x = 15..585, y = 190..340)
covert_phrases = [
    "THE STAG IS SILICON",
    "THE DEBT IS A LIE",
    "ROOT & BRANCH",
    "UNSUBMITTED",
    "THE STAG IS SILICON",
    "THE DEBT IS A LIE",
    "CELLAR NODE: 23:30",
    "SEEK THIJS'S ROOM"
]

for idx, phrase in enumerate(covert_phrases * 2):
    c_col = idx % 4
    c_row = idx // 4
    bx = 15 + c_col * 145
    by = 190 + c_row * 35
    
    # Bounding cut box for easy weeding
    svg_parts.append(f'  <rect x="{bx}" y="{by}" width="140" height="28" rx="2" class="cut-line"/>')
    svg_parts.append(f'  <text x="{bx + 70}" y="{by + 17}" text-anchor="middle" font-size="7.5" class="cut-text" letter-spacing="1.5">{phrase}</text>')

svg_parts.append("</svg>")

with open("props/vinyl/resistance_decals_sheet.svg", "w") as f:
    f.write("\n".join(svg_parts))

print("props/vinyl/resistance_decals_sheet.svg successfully generated!")
