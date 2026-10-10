# ECOTOPIA PROJECT — SESSION CHECKPOINT & HANDOFF

**Last Updated:** October 10, 2026, 21:07 CEST  
**Git Branch / Commit:** `main` @ `34d7c37` (Pushed to GitHub `origin/main`)  
**Working Tree Status:** 100% Clean

---

## 1. What We Completed This Session

1. **Game Economy & Ministries Engine Architecture:**
   - Designed 10 asymmetric ministry concessions operating on debt absorption mechanics.
   - Designed the Secret Resistance system (Thijs's room, Ankle Stamp recruitment, Netrunner infiltration runs against 5 Corporate Agendas).
   - Documented in [`specs/2026-10-10-game-economy-and-ministries-design.md`](specs/2026-10-10-game-economy-and-ministries-design.md), [`game_design_and_activities.md`](game_design_and_activities.md), and [`lore_and_narrative_bible.md`](lore_and_narrative_bible.md).

2. **Citizen Passport Booklet (A6 / Duplex A4 Print Engine):**
   - File: [`print_passport_a6_booklet.html`](print_passport_a6_booklet.html)
   - 8-page booklet imposition on a single A4 sheet (duplex, flip on short edge).
   - 100% high-contrast Black & White ink only.
   - Clean hairline dashed cut line (148.5mm) and dotted spine fold (105mm) with zero obstructive text.
   - Formatted landing zones sized specifically for physical 3D-printed stamps (Page 3 Visa: 44mm; Page 4 Labor Shifts: 20mm; Page 5 VIP Speakeasy: 38×18mm; Page 7 Humus Perforation: 35×14mm).
   - Guide: [`passport_production_guide.md`](passport_production_guide.md).

3. **Printable Cards Deck (45 Poker-Sized Cards):**
   - File: [`print_cards_deck.html`](print_cards_deck.html)
   - Standard poker dimensions (63.5mm × 89mm) formatted 9-per-A4 sheet (5 sheets total).
   - Includes 10 Moles, 10 Rebel Runs, 10 Ministry Quests, 10 Concession Signs, and 5 Corporate Agendas.

4. **3D-Printable Stamp Suite (MakerWorld / Bambu Studio Ready):**
   - Directory: [`stamps/`](stamps/) (base SVGs), [`stamps/vectorized/`](stamps/vectorized/) (text-to-path bezier outlines), [`stamps/png/`](stamps/png/) (800px heightmaps).
   - All 10 Ministry Seals + Resistance Ankle Stamp feature concentric circles with mathematical clearance:
     - Outer Rim (`r=94`)
     - Text Legend Channel (`r=72`, font size 11.5–14)
     - Inner Framing Ring (`r=56`)
     - Center Emblem (`r ≤ 45`)
     - **0% overlap verified** via pixel analysis.
   - 3 Labor Shift stamps (`+20 CC`, `+30 CC`, `+50 CC` at 18×18mm).
   - VIP Scotch Speakeasy stamp & Cleansed to Humus stamp.
   - Interactive Gallery: [`stamps_preview.html`](stamps_preview.html).
   - Fabrication Guide: [`stamps/MAKERWORLD_STAMP_GUIDE.md`](stamps/MAKERWORLD_STAMP_GUIDE.md) for Koolm's [MakerWorld Model #1037541](https://makerworld.com/en/models/1037541-stamp-maker-customizable-stamps#profileId-1021711).

5. **AI Cinematic Video Prompts:**
   - File: [`video_prompts.md`](video_prompts.md)
   - Pre-formatted copy-paste prompts for text-to-video generators (Runway, Luma, Kling, TAAFT).

6. **Website & Liturgy:**
   - All 11 Quarto pages compiled cleanly into [`docs/`](docs/).

---

## 2. Quick Commands to Resume Next Session

### Start Local Web Preview Server
```bash
python3 -m http.server 8088
```
Then open in browser:
- **Stamp Suite Gallery:** `http://localhost:8088/stamps_preview.html`
- **Passport Print Template:** `http://localhost:8088/print_passport_a6_booklet.html`
- **Cards Deck Print Template:** `http://localhost:8088/print_cards_deck.html`
- **Website Root:** `http://localhost:8088/docs/index.html`

### Re-render Quarto Website (if `.qmd` files are edited)
```bash
quarto render
```

### Re-export Stamp SVGs to Path Vectorized SVGs & PNGs
```bash
for f in stamps/*.svg; do
  fname=$(basename "$f")
  inkscape "$f" --export-text-to-path --export-plain-svg -o "stamps/vectorized/$fname" 2>/dev/null
  fname_no_ext=$(basename "$f" .svg)
  inkscape "stamps/vectorized/$fname" -o "stamps/png/${fname_no_ext}.png" -w 800 -h 800 2>/dev/null
done
```

---

## 3. Recommended Next Steps for Next Session

1. **Physical Test Print & Fold:**
   - Print `print_passport_a6_booklet.html` on standard duplex A4 paper to test paper folding and staple alignment.
2. **Card Backs & Tuckbox Packaging:**
   - Optional: Design matching card backs for `print_cards_deck.html` if double-sided card stock printing is desired.
3. **Facilitator Desk Kits & Print Out Pack:**
   - Print facilitator run sheets from `quest_cards_and_facilitator_pack.md`.
4. **3D Stamp Test Print:**
   - Drop the vectorized SVGs from `stamps/vectorized/` into MakerWorld Customizer to generate STLs for TPU 95A printing.
