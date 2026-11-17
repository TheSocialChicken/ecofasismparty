# Ecotopia: Citizen Passport & Documentation Booklet Production Guide
**A6 Passport Booklet Suite (Standard A4 Print, Cut & Fold Imposition Specifications)**  
*Authors: Wout (Technical & Game Design Lead), Chris (Narrative & Design Lead), Jack (Production Coordinator)*  
*Date: 2026-10-14*

> **Fabrication Purpose:**  
> This guide details how to print, cut, fold, and bind the entire suite of **5 physical A6 Passport Booklets** for Sanctuary De Warren on November 28, 2026.  
> Using standard double-sided A4 duplex printing:
> - **8-Page Booklets:** 1 printed A4 sheet = 1 complete 8-page A6 booklet.
> - **16-Page Booklets:** 2 printed A4 sheets = 1 complete 16-page A6 booklet.

---

## 1. The 6 A6 Passport Booklets Suite

| # | Booklet Title | File Name | Pages | Sheets | Key In-Universe / Clinical Function |
| :-: | :--- | :--- | :---: | :---: | :--- |
| **1** | **Citizen Passport** | [`print_passport_a6_booklet.html`](print_passport_a6_booklet.html) | 8 | 1 A4 Duplex | Guest ID, debt ledger, shift stamps, 10 concessions audit, tear-out bond |
| **2** | **Broadcast Scripts & Liturgy** | [`print_broadcast_scripts_a6_booklet.html`](print_broadcast_scripts_a6_booklet.html) | 8 | 1 A4 Duplex | Hanna PA decrees, Matriarch speech, Resistance manifesto, martyr relics |
| **3** | **Lore & Narrative Bible** | [`print_lore_bible_a6_booklet.html`](print_lore_bible_a6_booklet.html) | 16 | 2 A4 Duplex | 4 epochs, Doublethink lexicon, sacred hagiography, 10 ministries, cellar secret |
| **4** | **Game Design & Economics** | [`print_game_design_a6_booklet.html`](print_game_design_a6_booklet.html) | 16 | 2 A4 Duplex | Concession loop, debt absorption formula, Netrunner/Secret Hitler engine |
| **5** | **Quest Cards & Facilitator** | [`print_quest_cards_a6_booklet.html`](print_quest_cards_a6_booklet.html) | 16 | 2 A4 Duplex | Minister clipboard powers, 10 seeded moles, 5 Netrunner runs, climax script |

*Note: All booklets include both **🖨️ A4 Imposition Print View** (for physical fabrication) and **📖 Sequential Reading View** (for screen reading).*

---

## 2. Specifications & Materials

* **Final Booklet Dimensions:** **A6 Portrait** (105 mm wide × 148.5 mm tall) — standard international passport size.
* **Paper Stock Recommendation:**
  * **Best:** Heavy 120–160 gsm cream, ivory, or kraft paper. (Holds rubber stamp ink without bleeding through).
  * **Standard:** 80–100 gsm standard paper works fine if using quick-drying pigment ink pads.
* **Print Ratio & Quantities for 200 Guests:**
  * **Citizen Passports:** 220 A4 sheets (200 guests + 20 spares for character rebirths at Minirenewal).
  * **Facilitator & Minister Documentation Packs:** 10–20 copies of Booklets 2, 3, 4, and 5 for Hosts, Ministers, Audio Engineers, and Actors.
* **Tools Required:**
  1. Paper Guillotine / Rotary Trimmer (or scissors/ruler + hobby knife).
  2. Standard Long-Reach Stapler (or saddle-stitch booklet stapler).
  3. Perforation Cutter Wheel (optional, for scoring Page 7 of the Citizen Passport).

---

## 3. Printing Instructions (All Booklets)

1. Open any of the booklet HTML files in Chrome, Firefox, Safari, or Edge.
2. Press **Ctrl + P** (Windows/Linux) or **Cmd + P** (Mac) to open the print dialog.
3. Configure these exact settings:
   * **Destination:** Your printer (or *Save as PDF*).
   * **Paper Size:** `A4`
   * **Layout:** `Portrait`
   * **Two-Sided (Duplex):** **ON**, set to **Flip on Short Edge** (or tumble).
   * **Margins:** `None` (or `Minimum`).
   * **Options:** Check **"Background graphics"** so all dark covers and frames print cleanly.

---

## 4. Fabrication: 8-Page Booklets (1 A4 Sheet)

*Applies to: Booklet 1 (Citizen Passport) & Booklet 2 (Broadcast Scripts)*

```
Step 1: The A4 Sheet           Step 2: The Cut               Step 3: Nest & Fold
┌──────────────────────┐       ┌──────────────────────┐      ┌──────────┐
│   Sheet 1 (A5)       │       │   Sheet 1 (A5)       │      │ Page 1   │
│ [Page 8]  [Page 1]   │       │ [Page 8]  [Page 1]   │      │ (Cover)  │
├──────────────────────┤  ──►  └──────────────────────┘ ──► ├──────────┤
│   Sheet 2 (A5)       │       ┌──────────────────────┐      │ Staple   │
│ [Page 6]  [Page 3]   │       │   Sheet 2 (A5)       │      │  Spine   │
└──────────────────────┘       │ [Page 6]  [Page 3]   │      └──────────┘
 (Side A of printed A4)        └──────────────────────┘
                                (Stacked & Folded)
```

1. **The Cut (1 Cut):** Cut straight across the middle dashed line at **148.5 mm** to create two A5 halves:
   - **Sheet 1 (Top half):** Pages 8 & 1 on Side A; Pages 2 & 7 on Side B.
   - **Sheet 2 (Bottom half):** Pages 6 & 3 on Side A; Pages 4 & 5 on Side B.
2. **Nesting:** Lay Sheet 1 face down (Pages 2 & 7 facing up). Place Sheet 2 on top of it (Pages 4 & 5 facing up).
3. **Folding & Binding:** Fold in half along the vertical spine line (105 mm). Drive 2 staples through the spine.
   - Page order: **1 (Cover)** → **2 & 3** → **4 & 5 (Centerfold)** → **6 & 7** → **8 (Back Cover)**.

---

## 5. Fabrication: 16-Page Booklets (2 A4 Sheets)

*Applies to: Booklet 3 (Lore Bible), Booklet 4 (Game Design), Booklet 5 (Quest Cards)*

1. **Print 2 Sheets Duplex:** Print Paper 1 and Paper 2 with Duplex set to **Flip on Short Edge**.
2. **Cut Both Sheets in Half at 148.5 mm:** Produces 4 separate A5 folded leaves:
   - **Leaf 1 (Paper 1 Top):** Front: Pages 16 & 1 | Back: Pages 2 & 15
   - **Leaf 2 (Paper 1 Bottom):** Front: Pages 14 & 3 | Back: Pages 4 & 13
   - **Leaf 3 (Paper 2 Top):** Front: Pages 12 & 5 | Back: Pages 6 & 11
   - **Leaf 4 (Paper 2 Bottom):** Front: Pages 10 & 7 | Back: Pages 8 & 9 (Centerfold)
3. **Nesting Stack:**
   - Place **Leaf 1** on the table (Pages 2 & 15 facing up).
   - Place **Leaf 2** on top (Pages 4 & 13 facing up).
   - Place **Leaf 3** on top (Pages 6 & 11 facing up).
   - Place **Leaf 4** on top (Pages 8 & 9 facing up — this is the centerfold spread).
4. **Centerfold Stapling:** Fold the nested stack in half at 105 mm and drive 2 staples through the spine.
   - Page order: **1 to 16 in exact, flawless sequential numerical order!**

---

## 6. Live Party Gameplay Guide for Passports

1. **Intake (Garage):** Citizen arrives unassigned. Auditor stamps Starting Debt (`-150` to `-500 CC`) in the Page 2 box.
2. **Ministry Recruitment:** Minister signs citizen, stamps Page 3 with their Ministry Rubber Stamp, and logs absorbed debt onto Ministry Clipboard.
3. **Shift & Game Logging:** Facilitators stamp boxes on Page 4 (`+25 CC` or `+50 CC`). Each stamp directly advances 1 or 2 blocks on the Page 5 Visual Carbon Ladder (no manual math needed during the party).
4. **Tiers & VIP Speakeasy Clearance:** Crossing `0 CC` unlocks Assembly speaking/voting rights and audit immunity. Reaching `+100 CC` unlocks the secret VIP Library Speakeasy; the Bar Warden stamps the official gold/black seal on Page 5 and pours Single Malt Scotch.
5. **The 00:05 Climax:** When Thijs reveals the cellar AI server, all citizens tear out Page 7 and throw it as confetti.
