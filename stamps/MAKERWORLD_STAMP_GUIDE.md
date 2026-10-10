# ECOTOPIA 3D-PRINTED STAMP FABRICATION GUIDE
## Parametric Stamp Maker Integration for Bambu Lab / MakerWorld

This guide provides complete fabrication parameters for manufacturing the physical rubber stamps for the **Ecotopia** immersive theater party (De Warren, Nov 28, 2026), utilizing Koolm's [Customizable Stamp Maker on MakerWorld (Model #1037541)](https://makerworld.com/en/models/1037541-stamp-maker-customizable-stamps#profileId-1021711).

---

## 1. Inventory & Dimensional Specifications

All stamps in `stamps/` are engineered with bold vectors, thick stroke weights (≥0.8mm real-world minimum), and high contrast to ensure crisp 3D extrusion in TPU without ink pooling or blurred text.

| Stamp File | Stamp Role & Department | Shape | Target Size (mm) | Passport Page & Landing Zone | Recommended Ink Color |
|---|---|---|---|---|---|
| `01_miniservice_seal.svg` | Ministry of Restorative Labor | Round | **40 mm Ø** | Page 3 (Visa Seal, 44mm) & Desk Clipboard | Pigment Black / Rust |
| `02_minirenewal_seal.svg` | Ministry of Elemental Reclamation | Round | **40 mm Ø** | Page 3 (Visa Seal, 44mm) & Desk Clipboard | Forest Green / Black |
| `03_minilight_seal.svg` | Ministry of Energetic Austerity | Round | **40 mm Ø** | Page 3 (Visa Seal, 44mm) & Desk Clipboard | Amber / Bright Yellow |
| `04_miniflow_seal.svg` | Ministry of Hydraulic Rectitude | Round | **40 mm Ø** | Page 3 (Visa Seal, 44mm) & Desk Clipboard | Deep Navy / Blue |
| `05_miniplenty_seal.svg` | Ministry of Caloric Rationing | Round | **40 mm Ø** | Page 3 (Visa Seal, 44mm) & Desk Clipboard | Crimson Red / Black |
| `06_minilove_seal.svg` | Ministry of Biological Harmony | Round | **40 mm Ø** | Page 3 (Visa Seal, 44mm) & Desk Clipboard | Magenta / Scarlet |
| `07_minijoy_seal.svg` | Ministry of Morale & Celebration | Round | **40 mm Ø** | Page 3 (Visa Seal, 44mm) & Desk Clipboard | Hot Pink / Orange |
| `08_minishelter_seal.svg` | Ministry of 15-Minute Sanctuary | Round | **40 mm Ø** | Page 3 (Visa Seal, 44mm) & Desk Clipboard | Slate Grey / Black |
| `09_minithrift_seal.svg` | Ministry of Material Liberation | Round | **40 mm Ø** | Page 3 (Visa Seal, 44mm) & Desk Clipboard | Industrial Purple / Black |
| `10_minibreath_seal.svg` | Ministry of Atmospheric Rectitude | Round | **40 mm Ø** | Page 3 (Visa Seal, 44mm) & Desk Clipboard | Sky Blue / Black |
| `shift_plus_20.svg` | General Work Shift (+20 CC) | Square | **18 mm × 18 mm** | Page 4 (Labor Grid cells) | Black or Blue |
| `shift_plus_30.svg` | Heavy Work Shift (+30 CC) | Square | **18 mm × 18 mm** | Page 4 (Labor Grid cells) | Black or Blue |
| `shift_plus_50.svg` | Heroic / Concession Bonus (+50 CC) | Square | **18 mm × 18 mm** | Page 4 (Labor Grid cells) | Bright Red or Green |
| `vip_library_speakeasy.svg`| Citizen Class A Speakeasy Permit | Octagon / Rect | **38 mm × 16 mm** | Page 5 (VIP Library box, 18mm height) | Metallic Gold or Red |
| `cleansed_to_humus.svg` | Cadaveric Liquidation / Recycled | Rectangle | **34 mm × 13 mm** | Page 7 (Ancestral Debt Slip, 35×14mm) | Blood Red or Soil Brown |
| `resistance_ankle_stamp.svg`| Secret Underground Recruitment | Round | **18 mm Ø** | Citizen Skin (Ankle/Wrist) or Passport | Violet / Subversive Green |

---

## 2. MakerWorld Customizer Workflow

When opening the model on MakerWorld:

### Step 1: Generate the Flexible Stamp Face (TPU)
1. In the Customizer parameter panel:
   - **Stamp Type / Shape:** Choose `Round` (for Ministry Seals & Resistance), `Square` (for Shift stamps), or `Rectangle` (for VIP and Humus stamps).
   - **Outer Dimensions:** Enter the exact dimensions from the table above (e.g., `40` for round seals, `18` for shifts, `34 × 13` for Humus).
   - **Relief Height:** Set to **1.6 mm - 2.0 mm**. (This ensures ample clearance so the flat background of the stamp never accidentally touches the paper when pressing).
   - **Base Plate Thickness:** **2.0 mm**.
   - **Image Import:** Click `Upload SVG` and select the corresponding file from the `stamps/` folder.
   - **Image Mode:** Ensure mode is set to **Emboss / Raised** (the black vector shapes extrude upward to catch ink).
2. Export the generated 3D plate as `.step` or `.stl`.

### Step 2: Generate the Rigid Handle & Cap (PLA / PETG)
1. The Koolm model automatically generates a matching ergonomic handle, backing plate, and snap-fit protective cap scaled to your stamp face dimensions.
2. Select standard handle profile (e.g., round knob for circular stamps, rectangular grip for bars).
3. Export the handle and cap STLs.

---

## 3. Slicer & Print Settings (Bambu Studio / PrusaSlicer)

### Plate A: Stamp Face (Flexible Filament)
* **Filament:** **TPU 95A** (standard flexible) or **TPU 85A/90A** (softer, provides superior ink distribution like real vulcanized rubber).
* **Nozzle:**
  - **0.4 mm Nozzle:** Perfectly fine for all 40mm seals, shift stamps, and bold text.
  - **0.2 mm Nozzle (Optional / High-Detail):** Recommended for crispest micro-type on `cleansed_to_humus.svg` and `vip_library_speakeasy.svg`.
* **Layer Height:** **0.12 mm** (Fine) or **0.16 mm** optimal.
* **Top Surface Pattern:** **Concentric** (for circular stamps) or **Monotonic Line** (for square/rectangular). Concentric delivers ultra-smooth unbroken continuous perimeters that distribute stamp ink evenly.
* **Wall Loops:** **3 to 4 loops** to ensure letter walls are solid and don't collapse under stamping pressure.
* **Top Shell Layers:** **5 layers** or **100% Infill** (solid top prevents ink from absorbing into internal infill gaps).
* **Print Speed:** Reduce **Outer Wall Speed to 25–35 mm/s** for TPU. Slow printing guarantees razor-sharp edges on text glyphs.
* **Ironing:** **DISABLED**. (Ironing on TPU can cause stringing and rough burrs on fine typography).

### Plate B: Handle & Cap (Rigid Filament)
* **Filament:** **PLA Matte** or **PETG** (Black, Grey, or Wood-fill for historical bureaucratic immersion).
* **Layer Height:** **0.20 mm** (Standard).
* **Infill:** **15% Gyroid**.
* **Walls:** **3 loops** for a satisfying, durable heft in facilitators' hands.

---

## 4. Post-Processing & Assembly

1. **Mounting:**
   - Koolm’s model features a dedicated recess on the handle base.
   - Clean both bonding surfaces with isopropyl alcohol (IPA).
   - Affix the TPU stamp face into the handle recess using **thick cyanoacrylate (Super Glue / Gorilla Gel)** or **heavy-duty double-sided foam mounting tape** (carpet/VHB tape). Double-sided foam tape provides an extra 0.5mm of mechanical cushion, which further evens out hand-stamping pressure across uneven tabletops!
2. **Ink Testing & Priming:**
   - New 3D-printed TPU surfaces can initially repel water-based inks due to surface tension.
   - **Pro Tip:** Lightly buff the relief surface of the TPU stamp face with **800-grit sandpaper** or a melamine sponge, then wipe with rubbing alcohol. This micro-textures the TPU surface, allowing it to hold ink beautifully just like commercial vulcanized stamps.
   - Test on scrap paper before the event.

---

## 5. Party Station Deployment Pack

For smooth gameplay during the event, assemble the following physical kits:

* **Ministry Desks (10 Stations):**
  - 1× Ministry Seal Handle (40mm)
  - 1× Ink Stamp Pad (Black or Ministry Signature Color)
  - 1× Shift Stamp Handle (`+30 CC` or `+20 CC`)
* **Thijs’s Room (Underground Resistance):**
  - 2× Resistance Ankle Stamp (18mm)
  - 1× Violet / Subversive Green washable ink pad (cosmetic / skin-safe ink for ankles)
* **The High Warden / Vault Desk:**
  - 1× VIP Library Speakeasy Stamp (Gold ink pad)
  - 1× Cleansed to Humus Stamp (Red ink pad)
