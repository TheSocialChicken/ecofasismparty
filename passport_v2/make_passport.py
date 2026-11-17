"""Citizen Passport v2: practical stamp booklet (A6, 16 pages, 2 A4 sheets duplex).

Run: python3 make_passport.py  -> passport_v2.html (open in browser, print A4,
     100% scale, double-sided, flip on LONG edge). Cut each sheet in half
     horizontally, fold, and nest: sheet 1 top, sheet 1 bottom, sheet 2 top, sheet 2 bottom (centre).
Game names are deliberately absent: games are still in flux.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# The Great Seal of R.E.I.G.N., from the live site, converted to black & white
STAG = open(os.path.join(HERE, "great_seal_bw.svg")).read().replace("<svg ", '<svg class="crest" ', 1)


def ledger(n, first):
    boxes = "".join(f'<div class="box"><span>{first + i}</span></div>' for i in range(20))
    return f"""<h2>CREDITS</h2>
<p class="sub">Stamp every reward (+) and fine (&minus;)</p>
<div class="grid">{boxes}</div>
<div class="total">Page total: <span class="line"></span> CC</div>"""


# Ministry icons, shared with the insignia stamps (stamps/insignia/make_insignia.py)
_src = open(os.path.join(HERE, "..", "stamps", "insignia", "make_insignia.py")).read()
_ns = {"__file__": os.path.join(HERE, "..", "stamps", "insignia", "x.py")}
exec(_src[:_src.index("for i, n in enumerate(ORDER")], _ns)
ICONS, ORDER = _ns["ICONS"], _ns["ORDER"]


def icon(name):
    return f'<svg viewBox="60 64 80 80" class="micon">{ICONS[name]}</svg>'


MINISTRIES = "".join(f'<div class="min">{icon(n)}<span>{n.title()}</span></div>' for n in ORDER)

PAGES = {
    1: f"""<div class="cover">
<div class="big">REPUBLIC OF<br>ECOTOPIA</div>
{STAG}
<div class="title">CITIZEN<br>PASSPORT</div>
<div class="motto">R.E.I.G.N. decides,<br>so that citizens are free.</div>
</div>""",
    2: """<h2>CITIZEN</h2>
<div class="field">Name<span class="line"></span></div>
<div class="field">Ministry of<span class="line"></span></div>
<div class="startbox"><div>CARBON DEBT</div><div class="amount">&minus; <span class="line short"></span> CC</div></div>
<div class="seal-wrap"><div class="seal">MINISTRY<br>SEAL</div></div>
<p class="sub center">Written in at the door.<br>The night is your chance to repay it.</p>""",
    3: """<h2>R.E.I.G.N.</h2>
<div class="lore">
<p class="reign">Regime for<br>Ecological<br>Integrity and<br>Global<br>Nurturing</p>
<p class="quote">R.E.I.G.N. decides,<br>so that citizens are free.</p>
</div>""",
    4: """<h2>ARTICLES</h2>
<p class="sub">The Articles of Nurturing</p>
<ol class="articles">
<li><b>I.</b> Every citizen is placed where they will flourish.</li>
<li><b>II.</b> Questions are welcome. They have already been answered.</li>
<li><b>III.</b> Rest is a right of every citizen. It is scheduled.</li>
<li><b>IV.</b> R.E.I.G.N. hears every concern. Every single one.</li>
</ol>
<p class="sub center mt-auto">Adopted unanimously. Every vote was counted, including yours.</p>""",
    5: f"""<h2>MINISTRIES</h2>
<p class="sub">The machinery of care. Every citizen serves in one.</p>
<div class="mins">{MINISTRIES}</div>""",
    6: """<h2>HOW IT WORKS</h2>
<ol class="rules">
<li>Your carbon debt is written in at the door.</li>
<li>Serve, play and obey: earn <b>+</b> stamps.</li>
<li>Misbehave: get <b>&minus;</b> stamps.</li>
<li>Add up each page.</li>
<li>Reach <b>0</b>: your debt is repaid.</li>
</ol>
<p class="sub center mt-auto">CC = carbon credits.<br>Dancing counts as renewable energy.</p>""",
    7: ledger(1, 1),
    8: ledger(2, 21),
    9: ledger(3, 41),
    10: ledger(4, 61),
    11: ledger(5, 81),
    12: ledger(6, 101),
    13: """<h2>PERMITS</h2>
<p class="sub">Special access, granted by R.E.I.G.N.</p>
<div class="permits"><div class="permit"></div><div class="permit"></div></div>
<div class="startbox"><div>FINAL BALANCE</div><div class="amount"><span class="line short"></span> CC</div></div>
<div class="field">Officer<span class="line"></span></div>""",
    14: """<h2>DECREE</h2>
<div class="lore">
<p class="decree">By decree of R.E.I.G.N., artificial intelligence is banned in Ecotopia.</p>
<p>Citizens who did not apply are processed at the door: a longer wait, and further obligations.</p>
</div>""",
    15: """<h2>SAFETY</h2>
<div class="ozone">SAFE WORD<br><span>OZONE</span><small>stops all play at once</small></div>
<p class="sub center">Say it, and play stops.<br>No questions. No penalty.</p>
<p class="sub center mt-auto">Every citizen record is released back to nature on 19 December 2026.</p>""",
    16: f"""<div class="cover">
{STAG}
<div class="motto">Your arrival<br>has been noted.</div>
<div class="title small">BY ORDER OF<br>R.E.I.G.N.</div>
</div>""",
}

# Long-edge duplex imposition. 2 A4 sheets -> 4 folded A5 leaves, nested:
# sheet 1 top (outer), sheet 1 bottom, sheet 2 top, sheet 2 bottom (centre).
SHEETS = [
    ([[16, 1], [14, 3]], [[2, 15], [4, 13]]),
    ([[12, 5], [10, 7]], [[6, 11], [8, 9]]),
]


def page(n):
    return f'<div class="a6"><div class="frame">{PAGES[n]}<div class="pn">{n}</div></div></div>'


def side(rows, label):
    halves = "".join(f'<div class="half">{page(a)}{page(b)}</div>' for a, b in rows)
    return f'<div class="label">{label}</div><div class="a4">{halves}</div>'


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo:wght@500;700;800&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{background:#444;font-family:'Archivo','DejaVu Sans',sans-serif;color:#000;display:flex;flex-direction:column;align-items:center;padding:12px;
 -webkit-print-color-adjust:exact;print-color-adjust:exact}
.label{color:#fff;font:700 16px 'Archivo',sans-serif;margin:10px 0 6px}
.a4{width:210mm;height:297mm;background:#fff;padding:4mm;display:flex;flex-direction:column}
.half{flex:1;display:flex;border-bottom:1px dashed #999}
.half:last-child{border-bottom:none}
.a6{flex:1;padding:2mm;border-right:1px dashed #999}
.a6:last-child{border-right:none}
.frame{height:100%;border:2.5px solid #000;outline:1px solid #000;outline-offset:-2.2mm;padding:4.5mm 5mm;position:relative;display:flex;flex-direction:column}
h2{font-family:'Archivo Black',sans-serif;font-size:17pt;letter-spacing:1px;background:#000;color:#fff;text-align:center;padding:1mm 0}
h2.mt{margin-top:5mm}
.sub{font-size:10pt;font-weight:700;margin:1.5mm 0 2.5mm;text-align:center}
.center{text-align:center}
.pn{position:absolute;bottom:1.5mm;right:3mm;font-weight:800;font-size:9pt}
.line{display:inline-block;flex:1;border-bottom:2px solid #000;min-width:20mm;height:1em}
.line.short{width:28mm;flex:none}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.6mm;flex:1}
.box{border:1.5px dashed #000;position:relative;min-height:19mm}
.box span{position:absolute;top:.6mm;left:1mm;font-size:6.5pt;font-weight:700;color:#666}
.total{font-size:12pt;font-weight:800;display:flex;gap:2mm;align-items:end;margin-top:2.5mm;margin-right:4mm}
.cover{height:100%;display:flex;flex-direction:column;align-items:center;justify-content:space-between;text-align:center;padding:2mm 0 4mm}
.cover .big{font-family:'Archivo Black',sans-serif;font-size:20pt;line-height:1.05}
.cover .title{font-family:'Archivo Black',sans-serif;font-size:24pt;line-height:1;border-top:3px solid #000;border-bottom:3px solid #000;padding:2mm 4mm}
.crest{width:48mm;height:48mm}
.motto{font-size:11pt;font-weight:700;font-style:italic}
.field{font-size:13pt;font-weight:800;display:flex;gap:2mm;align-items:end;margin-top:5mm}
.startbox{border:2.5px solid #000;margin-top:5mm;padding:2mm;text-align:center;font-weight:800;font-size:11pt}
.startbox .amount{font-family:'Archivo Black',sans-serif;font-size:20pt;margin-top:1mm;display:flex;justify-content:center;align-items:end;gap:1mm}
.seal-wrap{flex:1;display:flex;align-items:center;justify-content:center}
.seal{width:44mm;height:44mm;border:2px dashed #000;border-radius:50%;display:flex;align-items:center;justify-content:center;text-align:center;font-weight:800;font-size:10pt;color:#777}
.bal{width:100%;border-collapse:collapse;margin-top:2mm;font-size:11pt}
.bal th{font-weight:800;border-bottom:2.5px solid #000;padding:1mm;text-align:left}
.bal td{border-bottom:1.2px solid #000;height:8.5mm}
.permits{flex:1;display:flex;flex-direction:column;gap:3mm;margin-bottom:1mm}
.permit{flex:1;border:2px dashed #000}
.rules{font-size:13pt;font-weight:700;line-height:1.35;margin:4mm 0 0 6mm}
.rules li{margin-bottom:2mm}
.ozone{border:3px solid #000;text-align:center;font-weight:800;font-size:11pt;padding:2.5mm;margin:5mm 0 3mm}
.ozone span{display:block;font-family:'Archivo Black',sans-serif;font-size:28pt;letter-spacing:3px;line-height:1.1}
.ozone small{display:block;font-size:10pt}
.mt-auto{margin-top:auto}
.lore{display:flex;flex-direction:column;gap:5mm;font-size:13pt;font-weight:700;line-height:1.3;margin-top:5mm;text-align:center}
.reign{font-family:'Archivo Black',sans-serif;font-size:17pt;line-height:1.15}
.quote{font-style:italic;border-top:2px solid #000;border-bottom:2px solid #000;padding:2mm 0}
.decree{font-family:'Archivo Black',sans-serif;font-size:16pt;line-height:1.2}
.articles{list-style:none;font-size:13pt;font-weight:700;line-height:1.3;margin-top:2mm}
.articles li{margin-bottom:4mm}
.mins{display:grid;grid-template-columns:1fr 1fr;gap:2mm 3mm;flex:1;align-content:space-evenly}
.min{display:flex;align-items:center;gap:2mm;font-size:12.5pt;font-weight:800}
.micon{width:13mm;height:13mm;flex:none}
.title.small{font-size:15pt}
@media print{body{background:none;padding:0}.label{display:none}.a4{page-break-after:always}
 @page{size:A4 portrait;margin:0}.half,.a6{border-color:#ccc}}
"""

html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Citizen Passport v2</title><style>{CSS}</style></head><body>
{"".join(side(fa, f"Sheet {i} front") + side(fb, f"Sheet {i} back") for i, (fa, fb) in enumerate(SHEETS, 1))}
</body></html>"""

out = os.path.join(HERE, "passport_v2.html")
open(out, "w").write(html)
print(out)
