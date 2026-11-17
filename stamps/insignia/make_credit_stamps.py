"""Credit stamps (+/-10, 20, 50) for the passport boxes. Print size: 16 mm square."""
import os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
for v in (10, 20, 50):
    for sign, sym in (("plus", "+"), ("min", "−")):
        path = os.path.join(HERE, f"credit_{sign}{v}.svg")
        open(path, "w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160">
<rect x="6" y="6" width="148" height="148" rx="14" fill="none" stroke="#000" stroke-width="10"/>
<text x="80" y="94" font-family="Archivo Black, DejaVu Sans" font-weight="900" font-size="56" text-anchor="middle" fill="#000">{sym}{v}</text>
<text x="80" y="136" font-family="Archivo Black, DejaVu Sans" font-weight="900" font-size="26" letter-spacing="4" text-anchor="middle" fill="#000">CC</text>
</svg>''')
        out = path.replace(".svg", "_paths.svg")
        subprocess.run(["inkscape", path, "--export-text-to-path", "--export-plain-svg", "--export-filename", out], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["inkscape", out, f"--actions=select-all;object-stroke-to-path;export-plain-svg;export-filename:{out};export-do"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("done")
