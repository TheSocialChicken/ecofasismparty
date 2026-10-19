# ECOTOPIA 2026 — BITLAIR PROP FABRICATION MASTER GUIDE
## Workshop Capabilities, Machine Workflows & Fabrication Plan (Amersfoort)

> **Hackerspace:** Bitlair (Nijverheidsweg-Noord 77, Amersfoort • [wiki.bitlair.nl](https://wiki.bitlair.nl))  
> **Target Event:** *Ecotopia* Immersive Theater Party (De Warren, Nov 28, 2026)  
> **Goal:** Transform the digital game design, passports, stamps, and quest assets into physical, high-immersion props using Bitlair's machines.

---

## 1. Machine Inventory vs. Ecotopia Props Matrix

Bitlair's workshop is uniquely equipped for all aspects of Ecotopia physical production. Below is the exact mapping of machines to event props:

| Bitlair Machine | Location | Specs & Software | Ecotopia Props to Fabricate | Cost / Policy |
|---|---|---|---|---|
| **Bambu Lab Fleet** (1× X1C + 3× P1S) | Flexlab | 0.4mm nozzle, PEI plates, AMS multi-material, **Bambu Studio** | • 10 Ministry Stamp handles & caps (PLA/PETG)<br>• Flexible TPU Stamp Faces (from `stamps/vectorized/`)<br>• Speakeasy tokens & Credential badge clips | **€ 0,03 / gram** filament |
| **60W CO2 Lasercutter** | Flexlab | **1260mm × 630mm bed**, Ruida DSP controller, **LightBurn** | • 10 Ministry Desk Placards & Clipboard Backers (4mm Poplar)<br>• The Grand Central Decree Board (Secret Hitler track)<br>• 5 Corporate Agenda token markers<br>• Laser-engraved natural rubber stamp alternative | **€ 0,10 / min** (members) / € 0,20 / min |
| **61cm Vinylsnijder** | Flexlab | 61cm roll width, infinite length, **Easy Cut Studio** | • Covert Resistance Stickers (*"THE STAG IS SILICON"* & Antlers)<br>• 15-Minute Sanctuary Boundary floor & door signs<br>• High Warden podium heraldry<br>• Spray-paint stencils for canvas banners | **Free machine**;<br>Vinyl **€ 0,75 / 10cm** (incl. transfer tape) |
| **Bernina B500 Borduurmachine** | Flexlab | Digital embroidery, USB input (`.exp` / `.dst`), multi-hoop | • 10 Official Ministry Armbands / Sashes<br>• Underground Resistance *"Root & Branch"* sew-on patches | RevBank donation ("borduurmachine") |
| **Shirtpers (Heat Press)** | Flexlab | High-temp flatbed heat press | • Miniservice Scullery Aprons (*"Restorative Labor"* branding)<br>• Facilitator & Warden high-contrast sashes | **Free** |
| **Fiberlaser** | Flexlab | Galvo fiber laser (metal marking) | • Library Speakeasy metal brass keys & VIP tokens<br>• High Warden ceremonial gavel plate | **Free** (Tuig adoption) |
| **Elektronica Werkplaats** | Hoofdruimte | Soldeerstation, oscilloscopen, componenten | • Bike Dynamo voltage display / wattage meter<br>• Cellar AI Server node flashing LED status lights<br>• Resistance UV blacklight pens / flashlights | Free / RevBank component costs |
| **Houtwerkplaats** | Houtwerkplaats | Tafelzaag, afkortzaag, lintzaag, bovenfrees, schuurmachines | • Central Decree Board standing easel / frame<br>• Bike Dynamo wooden mounting stand<br>• High Warden Assembly podium & gavel block | Free (bring own wood) |

---

## 2. Machine-Specific Fabrication Workflows

### A. Bambu Lab X1C & P1S — The 3D-Printed Stamps
* **Files:** All SVG vector files in [`stamps/vectorized/`](stamps/vectorized/) and 3D specs in [`stamps/MAKERWORLD_STAMP_GUIDE.md`](stamps/MAKERWORLD_STAMP_GUIDE.md).
* **Workflow:**
  1. Open Koolm's [MakerWorld Stamp Maker (#1037541)](https://makerworld.com/en/models/1037541-stamp-maker-customizable-stamps#profileId-1021711).
  2. Upload the vectorized SVGs:
     - 10 Ministry Seals: 40mm Ø Round (relief height: 1.8mm).
     - 3 Labor Shifts: 18mm × 18mm Square.
     - VIP Speakeasy: 38mm × 16mm Octagon.
     - Humus Liquidated: 34mm × 13mm Stencil.
     - Resistance Mark: 18mm Ø Round.
  3. Export handles/caps as STL and stamp faces as STL.
  4. **Printing Handles (PLA):** Load on any of the 4 Bambu printers in Flexlab. Slice in Bambu Studio with 15% gyroid infill. Can use AMS to print dual-color ministry labels on the handle caps!
  5. **Printing Stamp Faces (TPU 95A):** Mount TPU spool on the rear spool holder (do not feed TPU into the AMS). Set outer wall speed to 25–35 mm/s and top surface pattern to **Concentric**.

---

### B. 60W CO2 Lasercutter — Desk Placards & Central Decree Board
* **Work Area:** Massive **1260mm × 630mm** bed.
* **Software:** **LightBurn** (already installed and licensed on the PC right next to the laser).
* **Recommended Material:** 3mm or 4mm Poplar Plywood (*populieren multiplex*) — cheap, light, cuts cleanly.
* **Jobs to Run:**
  1. **10 Ministry Desk Placards (250mm × 120mm each):**
     - Cut wooden stand-up signs for the 10 stations (Miniservice, Minirenewal, Minilight, etc.) with slot-in interlocking feet.
     - **Speed/Power settings:**
       - Cutting (4mm poplar): **8 mm/s @ 100% power**.
       - Line Scoring (outlines & text): **30 mm/s @ 25% power** (vector scoring is 10× faster than raster engraving!).
  2. **The Grand Central Decree Board (800mm × 500mm):**
     - Sized to fit the stage. Features the 5 Corporate Agenda tracks (1 to 5 milestones) with laser-cut slots where acrylic or wooden tokens advance each round.
  3. **Alternative Laser-Cut Rubber Stamps:**
     - The CO2 laser can directly engrave A4 laser stamp rubber sheets at 500 dpi. If TPU prints are soft, laser-engraved rubber is an ultra-crisp 5-minute fallback!

---

### C. 61cm Vinyl Cutter — Signage & Resistance Decals
* **Machine:** 61cm wide plotter in Flexlab.
* **Software:** **Easy Cut Studio** (installed on the Bitlair PC above the machine; accepts `.svg` directly!).
* **Cost:** Machine is free; vinyl is € 0,75 per 10 linear cm (stocked in multiple colors under the bench, pay via RevBank `VINYL10CM`).
* **Jobs to Cut:**
  1. **Underground Resistance Stickers:**
     - Load `stamps/vectorized/resistance_ankle_stamp.svg`.
     - Cut 50× 30mm round decals on matte black and purple vinyl.
     - Rebels can peel and stick these on bathroom mirrors, corridor posts, and citizen dossiers.
  2. **15-Minute Sanctuary Boundary Tape / Decals:**
     - Cut floor arrows and wall boundary warnings: *"15-MINUTE SANCTUARY PERIMETER — PASSPORT AUDIT REQUIRED BEYOND THIS POINT"*.
  3. **Spray Paint Stencils:**
     - Cut stencil film for spray-painting *"THE STAG IS SILICON"* onto burlap banners.

---

### D. Bernina B500 Borduurmachine — Ministry Armbands & Badges
* **Machine:** Bernina B500 embroidery machine (located in Flexlab in the large Samla storage box).
* **Software:** Ink/Stitch (free Inkscape extension) or Bernina ArtLink to export `.exp` files to a USB thumb drive.
* **Setup:**
  - Standard pre-set settings: Foot #26, upper tension 3, lower tension 0, Jeans needle.
  - Fabric: Thick cotton canvas or felt armbands (green for Minirenewal, blue for Miniflow, red for Miniplenty, grey for Minishelter).
* **Production:**
  - Embroider the 10 circular ministry crests (using our SVGs) directly onto 100mm wide armbands with Velcro backing for the 10 facilitators.

---

### E. Electronics Station — Interactive Props
* **Bike Dynamo Wattage Monitor (Minilight Station):**
  - Use the soldering bench in the Hoofdruimte.
  - Wire an Arduino Nano / ESP32 with an analog voltage divider and a large 4-digit 7-segment display or an analog 1970s dial voltmeter.
  - When guests pedal the bike dynamo, the meter lights up and prints a verification tone when 100 Joules are contributed!
* **The Cellar AI Server Node (Resistance Climax):**
  - An old rack server chassis or enclosure with cycling green/red LEDs, a piezo buzzer, and an Ethernet cable run. Operatives must physically pull a jumper or insert a key to crash the Agenda engine!

---

## 3. Preparation Checklist Before Visiting Bitlair

### What to Bring:
- [ ] **USB Thumb Drive** loaded with:
  - `stamps/vectorized/*.svg` (for Bambu Studio & LightBurn)
  - `stamps/*.svg` (for Easy Cut Studio vinyl cutter)
  - `print_passport_a6_booklet.html` & `print_cards_deck.html`
- [ ] **Sheet Materials for Laser Cutting:**
  - 2 to 3 sheets of **4mm Poplar Plywood (1200 × 600 mm)** — available at Gamma / Hornbach / Praxis.
  - Optional: 1 sheet of 3mm tinted green or smoky acrylic for tokens/VIP passes.
- [ ] **Filament:**
  - 1 spool of **TPU 95A (Black or Grey)** for the stamp faces (check Bitlair Discord/wiki if space has TPU or bring your own).
  - PLA is readily available at Bitlair for € 0,03/g.
- [ ] **Fabric:**
  - Canvas / cotton straps for armbands, blank scullery aprons for heat-pressing.

### Bitlair Etiquette & Access:
- **Open Doors:** Typically **Sunday afternoons (from 14:00)** and **Wednesday evenings (from 19:00)**.
- **Instructors:** Ask in the space or on Bitlair Discord/IRC for:
  - *Lasercutter:* Vuurtorenjeroen / Linor / Hobbybob.
  - *Bambu Lab:* Elborro / Vuurtorenjeroen / ChillThijs.
  - *Vinyl Cutter:* Hobbybob / Elena.
  - *Borduurmachine:* Aranea / Elena.
- **Payment:** Setup a **RevBank** account at the bar terminal (add balance via iDeal/Wero) to pay for lasercutter time, vinyl, and snacks/club-mate!
