#!/usr/bin/env python3
"""
Generate LightBurn-ready SVG for 10 Ministry Desk Placards.
Red (#ff0000) = Laser CUT lines
Black (#000000) = Vector SCORE / Engraving lines
"""

ministries = [
    {
        "id": "01",
        "name": "MINISERVICE",
        "role": "MINISTRY OF RESTORATIVE LABOR",
        "concession": "CONCESSION: SCULLERY & GREASE RECLAMATION",
        "tariff": "LABOR RATE: +30 CC PER AUDITED SHIFT",
        "charter": "CHARTER: 50% ANCESTRAL DEBT ABSORPTION SUBSIDY"
    },
    {
        "id": "02",
        "name": "MINIRENEWAL",
        "role": "MINISTRY OF ELEMENTAL RECLAMATION",
        "concession": "CONCESSION: CADAVERIC COMPOSTING & NUTRIENT RETURN",
        "tariff": "BOUNTY: +100 CC PER LIQUIDATED BIOMASS BOND",
        "charter": "CHARTER: ZERO SOIL RESIDUE • CADAVERIC HARVEST RIGHTS"
    },
    {
        "id": "03",
        "name": "MINILIGHT",
        "role": "MINISTRY OF ENERGETIC AUSTERITY",
        "concession": "CONCESSION: HUMAN BICYCLE DYNAMO POWER GRID",
        "tariff": "LABOR RATE: +30 CC PER 100 JOULES GENERATED",
        "charter": "CHARTER: GRID ENERGIZATION TARIFFS & BLACKOUT EXEMPTION"
    },
    {
        "id": "04",
        "name": "MINIFLOW",
        "role": "MINISTRY OF HYDRAULIC RECTITUDE",
        "concession": "CONCESSION: PEETOPIA UREA EXTRACTION & PURITY METERING",
        "tariff": "LABOR RATE: +20 CC PER RETURNED STERILE VIAL",
        "charter": "CHARTER: EXCLUSIVE HYDRAULIC ROYALTIES ON LIQUID TOKENS"
    },
    {
        "id": "05",
        "name": "MINIPLENTY",
        "role": "MINISTRY OF CALORIC RATIONING",
        "concession": "CONCESSION: FERMENTED YEAST PASTE & CALORIC TRIAGE",
        "tariff": "DISTRIBUTION: 1 RATION WAFER PER 15 CC TICKET",
        "charter": "CHARTER: SOLE VENDOR OF STATE SACRAMENTAL NUTRITION"
    },
    {
        "id": "06",
        "name": "MINILOVE",
        "role": "MINISTRY OF BIOLOGICAL HARMONY",
        "concession": "CONCESSION: EUGENIC MATING INTERVIEWS & MORAL COMPLIANCE",
        "tariff": "SANCTION: +25 CC PER REPRODUCTIVE CLEARANCE CERTIFICATE",
        "charter": "CHARTER: 50% PROCEEDS FROM PUBLIC DECENCY CITATIONS"
    },
    {
        "id": "07",
        "name": "MINIJOY",
        "role": "MINISTRY OF MORALE & CELEBRATION",
        "concession": "CONCESSION: WIG DUEL ARENA & MANDATORY JOY RECREATION",
        "tariff": "WAGER: +25 CC PER ARENA COMBAT TRIUMPH",
        "charter": "CHARTER: AUTHORIZED DISTRIBUTOR OF STATE MORALE TONICS"
    },
    {
        "id": "08",
        "name": "MINISHELTER",
        "role": "MINISTRY OF 15-MINUTE SANCTUARY",
        "concession": "CONCESSION: CORRIDOR TOLL GATES & 15-MINUTE CURFEW AUDITS",
        "tariff": "TOLL: 10 CC PER PERIMETER TRANSIT PERMIT",
        "charter": "CHARTER: EXCLUSIVE BOUNDARY ENFORCEMENT & ENTRY CHARGES"
    },
    {
        "id": "09",
        "name": "MINITHRIFT",
        "role": "MINISTRY OF MATERIAL LIBERATION",
        "concession": "CONCESSION: CONTRABAND LOCKER & SYNTHETIC TEXTILE SEIZURE",
        "tariff": "SEIZURE: +40 CC LIQUIDATION TARIFF PER NON-ORGANIC ITEM",
        "charter": "CHARTER: SEIZURE & FORFEITURE OF PLASTIC ARTIFACTS"
    },
    {
        "id": "10",
        "name": "MINIBREATH",
        "role": "MINISTRY OF ATMOSPHERIC RECTITUDE",
        "concession": "CONCESSION: SPIROMETRY CHECKPOINT & DANCING INDULGENCES",
        "tariff": "OFFSET: +20 CC INDULGENCE FOR HYPERVENTILATION PERMIT",
        "charter": "CHARTER: COMMISSARY RIGHTS ON SURPLUS OXYGEN QUOTAS"
    }
]

sheet_w = 600
sheet_h = 550

svg_parts = [
    f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {sheet_w} {sheet_h}" width="{sheet_w}mm" height="{sheet_h}mm">
  <!-- LIGHTBURN LASER CUT TEMPLATE FOR BITLAIR 60W CO2 LASER -->
  <!-- RED (#ff0000) = CUT (Power 100%, Speed 8 mm/s on 4mm Plywood) -->
  <!-- BLACK (#000000) = SCORE / ENGRAVE (Power 25%, Speed 30 mm/s) -->
  <defs>
    <style>
      .cut {{ fill: none; stroke: #ff0000; stroke-width: 0.15; }}
      .score {{ fill: none; stroke: #000000; stroke-width: 0.2; }}
      .score-text {{ font-family: monospace, sans-serif; font-weight: 900; fill: #000000; }}
    </style>
  </defs>'''
]

col_w = 200
row_h = 105
margin_x = 10
margin_y = 10

card_w = 190
card_h = 95
tab_w = 20
tab_h = 4.2 # Thickness of 4mm plywood with clearance

for i, m in enumerate(ministries):
    col = i % 2
    row = i // 2
    x = margin_x + col * col_w
    y = margin_y + row * row_h

    # Card perimeter with two bottom tabs (for slotted feet)
    tab1_x1 = x + 35
    tab1_x2 = tab1_x1 + tab_w
    tab2_x1 = x + card_w - 35 - tab_w
    tab2_x2 = tab2_x1 + tab_w
    bottom_y = y + card_h
    tab_bottom = bottom_y + tab_h

    cut_path = (
        f"M {x} {y} "
        f"H {x + card_w} "
        f"V {bottom_y} "
        f"H {tab2_x2} V {tab_bottom} H {tab2_x1} V {bottom_y} "
        f"H {tab1_x2} V {tab_bottom} H {tab1_x1} V {bottom_y} "
        f"H {x} Z"
    )
    svg_parts.append(f'  <path d="{cut_path}" class="cut"/>')

    # Decorative inner scoring border
    inner_pad = 4
    svg_parts.append(f'  <rect x="{x + inner_pad}" y="{y + inner_pad}" width="{card_w - 2*inner_pad}" height="{card_h - 2*inner_pad}" class="score"/>')
    svg_parts.append(f'  <rect x="{x + inner_pad + 1.5}" y="{y + inner_pad + 1.5}" width="{card_w - 2*(inner_pad+1.5)}" height="{card_h - 2*(inner_pad+1.5)}" class="score"/>')

    # Header Bar
    svg_parts.append(f'  <line x1="{x + inner_pad}" y1="{y + 22}" x2="{x + card_w - inner_pad}" y2="{y + 22}" class="score"/>')
    svg_parts.append(f'  <line x1="{x + inner_pad}" y1="{y + 24}" x2="{x + card_w - inner_pad}" y2="{y + 24}" class="score"/>')

    # Ministry Name & Role
    cx = x + card_w / 2
    svg_parts.append(f'  <text x="{cx}" y="{y + 14}" text-anchor="middle" font-size="9" class="score-text" letter-spacing="1.5">{m["name"]}</text>')
    svg_parts.append(f'  <text x="{cx}" y="{y + 20}" text-anchor="middle" font-size="4.2" class="score-text" letter-spacing="0.8">{m["role"]}</text>')

    # Content Lines
    svg_parts.append(f'  <text x="{cx}" y="{y + 36}" text-anchor="middle" font-size="5" class="score-text">{m["concession"]}</text>')
    svg_parts.append(f'  <line x1="{x + 20}" y1="{y + 42}" x2="{x + card_w - 20}" y2="{y + 42}" class="score"/>')
    
    svg_parts.append(f'  <text x="{cx}" y="{y + 54}" text-anchor="middle" font-size="5.2" class="score-text">{m["tariff"]}</text>')
    svg_parts.append(f'  <text x="{cx}" y="{y + 65}" text-anchor="middle" font-size="4.2" class="score-text">{m["charter"]}</text>')

    # Footer
    svg_parts.append(f'  <line x1="{x + inner_pad}" y1="{y + 75}" x2="{x + card_w - inner_pad}" y2="{y + 75}" class="score"/>')
    svg_parts.append(f'  <text x="{cx}" y="{y + 83}" text-anchor="middle" font-size="3.5" class="score-text">OFFICIAL DESK PLACARD • AFFIX VERIFICATION STAMPS BELOW</text>')
    svg_parts.append(f'  <text x="{cx}" y="{y + 89}" text-anchor="middle" font-size="3" class="score-text">ECOTOPIA REIGN PROTOCOL // DE WARREN NOVEMBER 2026</text>')

# 20 Interlocking Base Feet (Right column x = 420..580)
foot_w = 40
foot_h = 24
slot_w = 20.2
slot_h = 4.2 # Thickness of 4mm plywood

foot_start_x = 425
foot_start_y = 15

for k in range(20):
    fx = foot_start_x + (k % 4) * 43
    fy = foot_start_y + (k // 4) * 27
    
    # Outer foot shape (rounded top or chamfered)
    poly = f"{fx},{fy+foot_h} {fx},{fy+8} {fx+8},{fy} {fx+foot_w-8},{fy} {fx+foot_w},{fy+8} {fx+foot_w},{fy+foot_h}"
    svg_parts.append(f'  <polygon points="{poly}" class="cut"/>')
    # Mortise slot in the center for tab
    slot_x = fx + (foot_w - slot_w) / 2
    slot_y = fy + 10
    svg_parts.append(f'  <rect x="{slot_x}" y="{slot_y}" width="{slot_w}" height="{slot_h}" class="cut"/>')
    svg_parts.append(f'  <line x1="{fx+4}" y1="{fy+4}" x2="{fx+foot_w-4}" y2="{fy+4}" class="score"/>')

svg_parts.append("</svg>")

with open("props/lasercutter/ministry_desk_placards.svg", "w") as f:
    f.write("\n".join(svg_parts))

print("props/lasercutter/ministry_desk_placards.svg successfully generated!")
