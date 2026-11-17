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


# ---------------------------------------------------------------------------
# Front-page product grid (_products.qmd, included by index.qmd).
# Each product lists every format that exists on disk as a button.
# Files are served from the Pages site itself (see `resources:` in _quarto.yml).
# ---------------------------------------------------------------------------
from html import escape

FORMATS = [  # (suffix, label)
    (".pdf", "PDF"), (".docx", "DOCX"), (".md", "MD"), (".html", "WEB"),
]

PRODUCTS = [
    ("🛂 PASSPORT", [
        ("Passport v2", ["passport_v2/passport_v2"]),
        ("Passport A6 booklet", ["print_passport_a6_booklet"]),
        ("Passport production guide", ["passport_production_guide"]),
    ]),
    ("📜 LORE", [
        ("Lore booklet A4", ["print_lore_a4_booklet"]),
        ("Lore & narrative bible", ["lore_and_narrative_bible", "print_lore_bible_a6_booklet"]),
        ("Lore A6 booklet", ["print_lore_a6_booklet"]),
        ("Broadcast scripts & liturgy", ["broadcast_scripts_and_liturgy", "print_broadcast_scripts_a6_booklet"]),
    ]),
    ("🎲 GAMES & CARDS", [
        ("Card deck", ["print_cards_deck"]),
        ("Games codex A4", ["print_games_codex_a4"]),
        ("Quest cards & facilitator pack", ["quest_cards_and_facilitator_pack", "print_quest_cards_a6_booklet"]),
        ("Game design & activities", ["game_design_and_activities", "print_game_design_a6_booklet"]),
        ("Cheat card ch.4", ["cheat_card_ch4"]),
    ]),
    ("🔏 STAMPS & PROPS", [
        ("Stamp preview sheet", ["stamps_preview"]),
        ("Prop fabrication guide", ["BITLAIR_PROP_FABRICATION_GUIDE"]),
    ]),
]


def fmt_links(bases: list[str]) -> str:
    chips = []
    for i, base in enumerate(bases):
        for suf, label in FORMATS:
            p = ROOT / f"{base}{suf}"
            if p.is_file():
                tag = label if i == 0 or suf != ".html" else "A6 WEB"
                chips.append(f'<a class="chip" href="{quote(base + suf)}">{tag}</a>')
    return "".join(chips)


def build_products() -> None:
    h = ['```{=html}', '<div class="dl-grid">']
    for section, items in PRODUCTS:
        h.append(f'<div class="dl-card"><h4>{escape(section)}</h4>')
        for name, bases in items:
            links = fmt_links(bases)
            if links:
                h.append(f'<div class="dl-row"><span>{escape(name)}</span><span>{links}</span></div>')
        if section.startswith("🔏"):
            h.append('<div class="dl-row"><span>Seals, insignia, 3D STL</span><span>'
                     '<a class="chip" href="downloads.html#ministry-seals-stamps">SVG/PNG</a>'
                     '<a class="chip" href="downloads.html#insignia">INSIGNIA</a>'
                     '<a class="chip" href="downloads.html#d-printable-stamps-stl">STL</a></span></div>')
        h.append('</div>')
    h.append('</div>')

    # Posters: one row per poster, print PDF + laser SVG(s)
    pdfs = {p.stem: p for p in sorted((ROOT / "posters/posters").glob("*.pdf"))}
    svgs = sorted((ROOT / "posters/lasercutter").glob("*.svg"))
    h.append('<div class="dl-card dl-wide"><h4>🪧 POSTERS (16)</h4><div class="poster-grid">')
    for stem, pdf in pdfs.items():
        chips = [f'<a class="chip" href="{quote(pdf.relative_to(ROOT).as_posix())}">PDF</a>']
        num = stem.split(" ")[0]
        for s in svgs:
            if s.stem.split(" ")[0] == num and num.isdigit():
                lab = "SVG SIMPLE" if "SIMPLE" in s.stem else "LASER SVG"
                chips.append(f'<a class="chip" href="{quote(s.relative_to(ROOT).as_posix())}">{lab}</a>')
        if stem.startswith("Print all"):
            sheet = ROOT / "posters/lasercutter/All ten A4 on one sheet.svg"
            if sheet.is_file():
                chips.append(f'<a class="chip" href="{quote(sheet.relative_to(ROOT).as_posix())}">LASER SHEET</a>')
        h.append(f'<div class="dl-row"><span>{escape(stem)}</span><span>{"".join(chips)}</span></div>')
    h.append('</div></div>', )
    h.append('```')
    (ROOT / "_products.qmd").write_text("\n".join(h), encoding="utf-8")
    print(f"_products.qmd: {sum(len(i) for _, i in PRODUCTS)} products, {len(pdfs)} posters")


build_products()
