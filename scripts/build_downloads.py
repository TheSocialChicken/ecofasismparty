#!/usr/bin/env python3
"""Generate downloads.qmd: a page of direct download links for everything we made.

Links point at github.com/<repo>/raw/main/<path>, which serves both normal
files and Git LFS files (STL/zip), so the Pages site itself stays small.

Run from the repo root:  python3 scripts/build_downloads.py
"""
from pathlib import Path
from urllib.parse import quote

REPO = "TheSocialChicken/ecofasismparty"
RAW = f"https://github.com/{REPO}/raw/main/"
ROOT = Path(__file__).resolve().parent.parent

# (section title, blurb, list of globs)
SECTIONS = [
    ("Print-ready booklets & decks",
     "PDFs ready to print. A6 booklets are HTML: open in a browser and print (duplex, short edge).",
     ["print_*.pdf", "passport_v2/passport_v2.pdf", "print_*.html", "passport_v2/passport_v2.html"]),
    ("Game & lore documents", "The full design docs.",
     ["game_design_and_activities.pdf", "lore_and_narrative_bible.pdf",
      "quest_cards_and_facilitator_pack.pdf", "broadcast_scripts_and_liturgy.pdf",
      "cheat_card_ch4.html"]),
    ("Posters (print)", "A-size propaganda posters.", ["posters/posters/*.pdf"]),
    ("Posters (laser cutter)", "SVG cut/engrave files.", ["posters/lasercutter/*.svg"]),
    ("Props: laser & vinyl", "Desk placards, decals and other prop files.",
     ["props/**/*.svg", "props/**/*.pdf", "props/**/*.png"]),
    ("Ministry seals (stamps)", "Vector and PNG seals for the 10 ministries.",
     ["stamps/*.svg", "stamps/vectorized/*.svg", "stamps/png/*.png"]),
    ("Insignia", "Ministry insignia artwork.", ["stamps/insignia/*.svg", "stamps/insignia/*.png"]),
    ("3D-printable stamps (STL)", "Ready-to-print stamp heads, full size and small.",
     ["stamps/stampmaker_stl/*.stl", "stamps/stampmaker_stl_small/*.stl",
      "stamps/stampmaker_base/*.scad"]),
    ("Images & artwork", "Propaganda art, engravings and mockups.",
     ["images/*.png", "images/bw/*", "images/engravings/*"]),
]


def human(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024


def main() -> None:
    out = [
        "---",
        'title: "DOWNLOADS"',
        'subtitle: "Everything the Ministries have produced. Take it, print it, make it."',
        "---",
        "",
        f"Want it all? [Download the whole archive (zip)]"
        f"(https://github.com/{REPO}/archive/refs/heads/main.zip){{.btn .btn-success}}",
        "",
        f"Source and history: [github.com/{REPO}](https://github.com/{REPO})",
        "",
    ]
    seen: set[Path] = set()
    for title, blurb, globs in SECTIONS:
        files = []
        for g in globs:
            for p in sorted(ROOT.glob(g)):
                if p.is_file() and p not in seen and "_build" not in p.parts:
                    seen.add(p)
                    files.append(p)
        if not files:
            continue
        out += [f"## {title}", "", blurb, "", "| File | Type | Size |", "|---|---|---|"]
        for p in files:
            rel = p.relative_to(ROOT).as_posix()
            url = RAW + quote(rel)
            out.append(f"| [{p.name}]({url}) | {p.suffix.lstrip('.').upper()} | {human(p.stat().st_size)} |")
        out.append("")
    (ROOT / "downloads.qmd").write_text("\n".join(out), encoding="utf-8")
    print(f"downloads.qmd: {len(seen)} files")


if __name__ == "__main__":
    main()
