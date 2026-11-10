# Ecotopia posters

| Folder | What's in it |
|---|---|
| `posters/` | One PDF per poster, to look at and print. `Print all ten A4.pdf` = the A4 series in one go. |
| `lasercutter/` | One LightBurn file per poster (black = engrave, red = cut). `All ten A4 on one sheet.svg` = the A4 series on one 1200×600 board. |
| `_build/` | Working files made by the script (editable masters, previews, bitmaps). No need to open. |

**01–06** are the large pieces (A3, trophy, crest). **07–16** are the A4 slogan series.

## Print on the Brother

    lp -d Brother-HL-2150N-series -o media=A4 "posters/posters/Print all ten A4.pdf"

The large pieces are true size; add `-o fit-to-page` to print them on A4.

## Lasercut in LightBurn

1. File → Import the `.svg` from `lasercutter/`; check the size (A4 = 210 × 297 mm).
2. Black layer → **Fill** (start ~300 mm/s, 20–30 %, 0.1 mm interval — test on scrap).
   Red layer → **Line**, 100 % @ 8 mm/s.
3. Black layer above red, so it engraves before it cuts. Keep *Cut inner shapes first* on.

## Changing a poster

Edit `scripts/make_posters.py` (slogans are in the `SERIES` list), then rebuild everything:

    .venv/bin/python scripts/make_posters.py
