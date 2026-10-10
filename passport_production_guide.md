# Ecotopia: Citizen Passport Booklet Production & Fabrication Guide
**8-Page A6 Passport Booklet (Standard A4 Print, Cut & Fold Specification)**  
*Authors: Wout (Technical & Game Design Lead), Chris (Narrative & Design Lead), Jack (Production Coordinator)*  
*Date: 2026-10-10*

> **Fabrication Purpose:**  
> This guide details how to print, cut, fold, and bind the physical **Citizen Passports** for Sanctuary De Warren on November 28, 2026.  
> Using standard double-sided A4 printing, **1 printed sheet yields 1 complete 8-page A6 passport!**

---

## 1. Specifications & Materials

* **Final Booklet Dimensions:** **A6 Portrait** (105 mm wide × 148.5 mm tall) — standard international passport size.
* **Paper Stock Recommendation:**
  * **Best:** Heavy 120–160 gsm cream, ivory, or kraft paper. (Holds rubber stamp ink without bleeding through).
  * **Standard:** 80–100 gsm standard paper works fine if using quick-drying pigment ink pads.
* **Print Ratio:**
  * 1 A4 Double-Sided Sheet = 1 Complete 8-Page Passport Booklet.
  * For 200 guests: Print **220 A4 sheets** (200 guests + 20 spares for character rebirths at Minirenewal).
* **Tools Required:**
  1. Paper Guillotine / Rotary Trimmer (or scissors/ruler + hobby knife).
  2. Standard Long-Reach Stapler (or saddle-stitch booklet stapler).
  3. Perforation Cutter Wheel (optional, for scoring Page 7, or scissors notch).

---

## 2. Printing Instructions (`print_passport_a6_booklet.html`)

1. Open [print_passport_a6_booklet.html](file:///home/chris/Nextcloud/Github/ecofasismparty/print_passport_a6_booklet.html) in Chrome, Firefox, or Safari.
2. Press **Ctrl + P** (Windows/Linux) or **Cmd + P** (Mac) to open the print dialog.
3. Configure these exact settings:
   * **Destination:** Your printer (or *Save as PDF*).
   * **Paper Size:** `A4`
   * **Layout:** `Portrait`
   * **Two-Sided (Duplex):** **ON**, set to **Flip on Short Edge** (or tumble).
   * **Margins:** `None` (or `Minimum`).
   * **Options:** Check **"Background graphics"** so all dark covers and frames print cleanly.

---

## 3. Step-by-Step Cutting, Folding & Binding

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

1. **Step 1 — The Horizontal Cut (1 Cut per sheet):**
   * Take the printed double-sided A4 sheet.
   * Cut straight across the middle dashed line at **148.5 mm** (the exact center).
   * You now have two separate A5 sheets:
     * **Sheet 1 (Top half):** Pages 8 & 1 on Side A; Pages 2 & 7 on Side B.
     * **Sheet 2 (Bottom half):** Pages 6 & 3 on Side A; Pages 4 & 5 on Side B.
2. **Step 2 — The Nesting Stack:**
   * Lay **Sheet 1** face down (so Page 1 and Page 8 are facing the table, and Pages 2 & 7 are facing up).
   * Place **Sheet 2** on top of it (with Pages 4 & 5 facing up — this is the centerfold).
3. **Step 3 — The Center Fold:**
   * Fold the combined stack in half along the vertical spine line (at 105 mm).
   * Check your page sequence:
     * Front: **Page 1 (Front Cover)**
     * Open 1: **Page 2 (Identity & Debt)** on left | **Page 3 (Ministry Visa)** on right
     * Open 2: **Page 4 (Labor Shift Grid)** on left | **Page 5 (Ascent to Purity & VIP)** on right (Centerfold)
     * Open 3: **Page 6 (10 Concessions Audit)** on left | **Page 7 (Perforated Debt Bond)** on right
     * Back: **Page 8 (Back Cover / OZONE safe-word)**
4. **Step 4 — Staple the Spine:**
   * Drive 2 staples through the centerfold spine (from the outside in, or using a long-reach stapler).
5. **Step 5 — Score Page 7 (Optional):**
   * Use a dashed perforation wheel or small scissor nick along the dotted line of Page 7 to allow it to be easily torn out during the 00:05 Revolution climax!

---

## 4. Live Party Gameplay Guide for Passports

1. **Intake (Garage):**
   * Citizen arrives unassigned. Auditor stamps Starting Debt (`-150` to `-500 CC`) in the Page 2 box.
2. **Ministry Recruitment:**
   * Minister signs citizen, stamps Page 3 with their Ministry Rubber Stamp, and logs absorbed debt onto Ministry Clipboard.
3. **Shift Logging:**
   * Facilitators stamp boxes on Page 4 (+20, +30, +50 CC).
4. **VIP Speakeasy Clearance:**
   * When citizen reaches `+100 CC`, bar warden stamps the gold box on Page 5 and admits them to the VIP Library.
5. **The 00:05 Climax:**
   * When Thijs reveals the cellar AI server, all citizens tear out Page 7 and throw it as confetti.
