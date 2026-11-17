# Ecotopia: Game Activities, Concessions & Economic Engine Guide
**Comprehensive Game Design, Ministry Concessions & Asymmetric Run Mechanics**  
*Authors: Wout (Technical & Game Design Lead), Chris (Narrative & Design Lead), Jack (Production Coordinator)*  
*Date: 2026-10-10*

> **Target Audience & Document Scope:**  
> This guide is the master operating reference for **Wout (Game Design)**, **Ministry Leads (Ministers)**, **Game Facilitators**, and **Quest Writers**.  
> It consolidates the living concession economy, debt absorption mechanics, the 10-ministry game concessions, corporate agendas (Secret Hitler track), rebel infiltration runs (Netrunner mechanics), and the revolution endgame sequence.

---

## 1. The Core Gameplay Loop & Concession Economy

The interactive game runs for approximately **2 to 2.5 hours** (typically 21:30 to 00:00) before transitioning into the open dance celebration.

```
       [Arriving Unassigned Citizens: -150 to -500 Debt]
                              │
                              ▼
           [Labor Market & Ministry Interviews]
      Ministers evaluate debts, skills, and work willingness
                              │
                              ▼
            [Sponsorship & Contract Stamp]
      Ministry absorbs citizen's negative balance onto Ledger
                              │
      ┌───────────────────────┴───────────────────────┐
      ▼                                               ▼
[Worker Operates Ministry Concession]   [Worker Dispatched on Quests / Runs]
- Runs game shifts & labor              - Infiltrates rival ministries
- Collects customer tariffs & fees      - Sabotages corporate agendas
      │                                               │
      └───────────────────────┬───────────────────────┘
                              ▼
                  [Dual-Tally Resolution]
   Citizen passport climbs toward 0 / +100 (Personal VIP)
   Ministry Ledger builds Net Surplus (State Dominance)
                              │
                              ▼
        [Phase 3: The Revolution Climax (23:30 - 00:15)]
   5 Corporate Agendas locked OR Rebels expose Cellar Server
```

---

## 2. The Living Economy: Capital, Debt & Concessions

### 1. Starting Capital vs. Unassigned Labor
* **The 10 Ministers / Founders:** Pre-designated players or hosts who start in the surplus with **+800 Carbon Credits**, an official **Ministry Clipboard Ledger**, an official **Ministry Rubber Stamp**, and custody of their **Concession Station**.
* **The Indebted Citizens (~190 guests):** Enter intake with **-150 to -500 Debt** stamped in their physical passport booklet (calculated from intake applications or the interrogation pen). They arrive unassigned, with no civic rights or room access until sponsored.

### 2. The Hiring Dilemma: Debt Absorption
* **Why Ministries Must Hire:** A Minister cannot man a bike dynamo, scrub glassware, audit drinks, and conduct inquisitions alone for 2.5 hours. They *must* recruit staff to run shifts, solicit customer credits, and guard their station.
* **The Absorption Formula:** When a Minister recruits an unassigned citizen:
  1. The Minister stamps the citizen's passport with the official Ministry Seal.
  2. The Minister logs the recruit's starting debt directly onto the Ministry Clipboard Ledger:
     $$\text{Ministry Net Balance} = \text{Starting Treasury (+800)} - \sum \text{Recruit Starting Debts} + \text{Generated Credits}$$
* **Natural Hiring Limits & Negotiations:**
  * **Low-Debt Citizens (`-150`):** In high demand. Ministries compete to sign them, offering low labor duties.
  * **High-Debt Citizens (`-450`):** Regarded as toxic liabilities. Ministers conduct 60-second interviews: *"If we absorb 450 credits of your ancestral sin, you must run two 10-minute shifts at our station and execute one dangerous sabotage run on our rival."*

### 3. The Dual-Tally Productivity Loop
* When a recruit works a 5-minute shift, runs their station, or completes a quest:
  * **Individual Passport:** Receives a credit stamp (+30 to +50), moving the individual toward `0` (Citizen rights) and `+100` (VIP Room access in The Library).
  * **Ministry Clipboard:** The recruit reports back to their Minister to log the credit gain, offsetting the absorbed debt and driving the Ministry's Net Power Score toward state dominance.

### 4. Carbon Insolvency (`Net Balance < 0`)
* If a Ministry recklessly hires too many unproductive debtors, its net balance drops below zero.
* **Insolvency Penalties:** VIP Room access is frozen for all members, Minilove may conduct aggressive audits, and the Ministry cannot vote or fund Corporate Agendas until solvency is restored.
* **Defections & Liquidation:** Insolvent Ministries can sell high-performing recruits to wealthy rivals or dump unproductive debtors at **Minirenewal (The Recycling Plant)** to compost their debt contract.

---

## 3. The 10 Ministry Concessions & Asymmetric Business Models

Ministries do not just play games—**they operate them as economic concessions and state enterprises**. Each Ministry has an asymmetric economic charter:

| Newspeak Ministry | Physical Concession & Game | Asymmetric Economic Charter | Key Revenue & Subsidy Mechanic |
| :--- | :--- | :--- | :--- |
| **Miniservice** | **Greenwashing Scullery** (Dishwashing & Sorting Station) | **Subsidized Workhouse** | Receives a **50% State Debt Relief Subsidy** when recruiting (e.g. absorbing -400 debt only burdens ledger by -200). Generates massive credit volume through +30 labor shifts. |
| **Minirenewal** | **The Suicide Carbon Booth** (Composting & Identity Reset) | **Debt Liquidator Bounty** | Collects a flat **+100 Credit State Bounty** for every bankrupt citizen processed through identity erasure. Ministries pay them to take bad debt off their books. |
| **Minilight** | **Kinetic Grid Generator** (Stationary Bicycle Dynamo & Blackouts) | **Grid Power Monopoly** | Recruits generate +30 credits per 5-min cycling shift. Minilight can plunge rival zones into blackouts unless they pay a periodic **Grid Maintenance Tariff** (30–50 credits). |
| **Miniflow** | **Peetopia & Sacred Sluice** (Restroom Fluid Audits & Cup Dispenser) | **Fluid Royalty Monopoly** | Controls cup dispensing and hydration. Collects a **+20 Fluid Dividend** for every citizen returning moisture at Peetopia; fines unauthorized drink spills. |
| **Miniplenty** | **Caloric Equilibrium Table** (Algae Paste & Blind Food Tasting) | **Caloric Indulgences** | Controls snack distribution. Sells caloric dispensations to hungry citizens or rival factions for direct credit transfers. |
| **Minilove** | **The Confession Pen & Interrogation** (Heresy Tribunals) | **Inquisitorial Seizure** | Conducts random heresy audits and surveillance checks. Seizes **50% of all levied fines** directly into Minilove's treasury. |
| **Minijoy** | **The Morale Arena** (Wig Snatching Duels & Open-Mic Stage) | **State Morale Grants** | Charges entry fees for Wig Snatching duels (+10 credits); receives a lump-sum **+150 State Morale Grant** whenever drawing a crowd of 15+ for crowd rallies. |
| **Minishelter** | **The 15-Minute Grid Checkpoint** (Corridor Curfew Gates) | **Transit Tolls & Passes** | Guards corridor bottlenecks leading to prime venue areas (VIP Library, Quiet Room). Charges 10–20 credits for cross-sector transit passes. |
| **Minithrift** | **Contraband Locker & Seizure** (Synthetic Property Audits) | **Contraband Liquidation** | Confiscates non-organic items (plastic trinkets, polyester gear). Owners can redeem them for a fee, or Minithrift liquidates them for +40 credits each. |
| **Minibreath** | **The Spirometry Checkpoint** (Atmospheric Metering) | **Atmospheric Offsets** | Meters exhalations with paper windmills and breath-holding tests. Issues "Breath Indulgences" to citizens wishing to dance without hyperventilation fines. |

---

## 4. Master Concession Games Catalog

### Category A: Kinetic & Utility Concessions
* **Stationary Power Bicycle (Minilight Concession):**  
  * *Setup:* Rigged bicycle generator powering a bulb or sound feed.
  * *Mechanic:* Indebted citizens pedal 5-minute shifts to earn +30 credits. Minilight stores the generated wattage as Ministry treasury points.
* **Greenwashing the Dishes (Miniservice Concession):**  
  * *Setup:* Scullery station with metered spray bottles and recycled sponges.
  * *Mechanic:* Workers clean 10 glassware items under strict single-sponge rules (+30 credits). Generates high throughput for Miniservice.
* **Peetopia Fluid Balance (Miniflow Concession):**  
  * *Setup:* Hydration monitoring station outside restrooms.
  * *Mechanic:* Returning moisture to the collective facility grants a +20 credit stamp, while Miniflow collects an equal state fluid dividend.

### Category B: Competitive & Morale Concessions
* **Wig Snatching Elimination Arena (Minijoy Concession):**  
  * *Setup:* Two duelists wearing identical neon synthetic wigs face off in a clearing.
  * *Mechanic:* Fast elimination duel (best of 3, ~60 seconds). Winner receives +25 credits. Entry fees flow to Minijoy.
* **How the World Ends Open-Mic (Minijoy Concession):**  
  * *Setup:* Mini-podium with megaphone and banners.
  * *Mechanic:* Contestants have 60 seconds to deliver the most melodramatic extinction monologue. Crowd applauds to decide the winner (+100 credits and ribbon).

### Category C: Penal & Reclamation Concessions
* **The Suicide Carbon Booth (Minirenewal Concession):**  
  * *Setup:* Upcycling telephone booth staffed by Renewal Technologists in lab coats.
  * *Mechanic:* Bankrupt or defecting citizens undergo a composting ritual. Old identity is struck through; balance reset to `0`; citizen receives a new designation (*Citizen Lichen-88*). Minirenewal collects +100 bounty.
* **The Confession Pen & Interrogation (Minilove Concession):**  
  * *Setup:* Dimly lit holding pen with single chair and spotlight.
  * *Mechanic:* Citizens confess pre-collapse ecological crimes. Minilove issues absolutions or fines, retaining a 50% cut.

---

## 5. The Netrunner & Secret Hitler Engine

To unite the ministries, the economic engine, and the secret resistance into a dramatic climax, gameplay incorporates **Corporate Agendas (Secret Hitler policy tracks)** and **Rebel Infiltration Runs (Netrunner asymmetric attacks)**.

```
                    ┌───────────────────────────────┐
                    │     CENTRAL DECREE BOARD      │
                    │   5 Corporate State Agendas   │
                    └───────────────┬───────────────┘
                                    │
           ┌────────────────────────┴────────────────────────┐
           ▼                                                 ▼
[MINISTRIES: The Corporations]                    [REBELS: The Runners]
- Pool treasury credits to advance Agendas       - Infiltrate Ministry Concessions
- Enforce escalating authoritarian decrees       - Bypass Ministry "Ice" (Guards/Audits)
- Score Net Carbon Power for the Stag            - Execute "Runs" to Trash Agendas & Steal Truth
           │                                                 │
           └────────────────────────┬────────────────────────┘
                                    ▼
                [23:30 Grand Assembly & Climax]
      Agendas fully locked OR Resistance raids and exposes Cellar
```

### 1. The Central Decree Board (The 5 Agendas)
A large physical display in the main hall tracks the regime's 5 grand corporate objectives:
1. **Agenda 1: Ambient Dimming** — Reduces venue lumens by 50%; activates Minilight blackout rules.
2. **Agenda 2: Caloric Compression** — Halves snack and bar dispensations; enforces algae ration rules.
3. **Agenda 3: Sector Perimeter Lockdown** — Severs corridor passage between zones without Minishelter permits.
4. **Agenda 4: Mandatory Heresy Purge** — Authorizes Minilove to execute public sidewalk audits.
5. **Agenda 5: Total Silicon Consolidation** — All citizen debt ledgers permanently locked; state power finalized.

* **Advancing an Agenda:** Every 30 minutes, Ministries can invest treasury credits onto the Central Board. When an agenda receives **200 Credits in funding**, it advances to the Staging Queue and is proclaimed over the PA system by Hanna.

### 2. Rebel Infiltration Runs (Netrunner Mechanics)
The Secret Resistance (headquartered in **Thijs’s room**, identified via the **Ankle Stamp**) operates as Runners attempting to disrupt the corporate machine.

* **The Run Loop:**
  1. Operatives receive a discrete **Run Card** from Thijs’s room targeting a specific Ministry station (e.g., reversing Miniflow's meter, stealing Minithrift's backup drive, sabotaging Minilight's dynamo).
  2. **Overcoming Ice (Defenses):** The Runner must bypass station defenses (inquisitors, checkpoint guards, surveillance wardens) through stealth, distraction (e.g., triggering a wig duel nearby), or credit bribes.
  3. **Breaching & Trashing:** Successful completion of a Run allows the Runner to:
     * **Trash an Agenda:** Remove 100 credits of funding from an active Corporate Agenda on the Central Board.
     * **Extract a Truth Fragment:** Collect physical evidence slips proving the Guardian Stag is powered by a salvaged corporate AI server in the cellar.

### 3. The Secret Legislative Council (Secret Hitler Dynamics)
Every 45 minutes, the High Warden convenes the 10 Ministers for an Assembly. Two decree cards are drawn from the state deck. Hidden resistance moles within ministry ranks can use secret votes or procedural maneuvers to veto corporate decrees or slip through subversive resolutions (e.g., *Decree of General Amnesty*).

---

## 6. Climax & Endgame: The Revolution (23:30 – 00:15)

The live game outcome is dynamically determined by the economic struggle between Corporate Agendas and Rebel Runs:

```
23:30 ── State Assembly: Leader's Grand Spectacle & Ministry Showcases
23:45 ── Resistance Raid: Ankle-stamped rebels storm the podium
00:00 ── The Great Reveal: Cellar server node exposed; compliance proved a sham
00:15 ── Transition: The system falls; DJs take over for the dance party
```

1. **The State Assembly (23:30):** The loudspeaker orders all 10 Ministries to gather before the main stage. The supreme figurehead arrives amidst smoke and fanfare. Each ministry presents their chant, anthem, or synchronized formation.
2. **The Resistance Raid (23:45):** If the resistance has recruited over 50% of attendees with ankle stamps and trashed at least 3 Agendas, the moles signal the revolt. They storm the podium with black banners reading: **"THE STAG IS SILICON. THE DEBT IS A LIE."**
3. **The Big Reveal (00:00):** Revolutionaries reveal the truth: the entire carbon credit ledger, the surveillance cameras, and the Guardian Stag calculations were never ecological—they were running on a salvaged corporate AI server node in the cellar! The regime was simply running compliance theater to preserve power.
4. **Resolution (00:15):** The ministries dissolve their rivalries, citizens tear out their passport debt pages, and the stage converts immediately into an open celebration dance floor with DJs running until 04:00+.

---

## 7. Guidelines for Activity Creators & Ministers

1. **Always Word Positively:** Punishments are *"privileges"*; starvation is *"caloric purity"*; forced chores are *"joyful civic service."*
2. **Keep the Barrier to Entry Low:** Games must take under 3 minutes to learn and under 10 minutes to play.
3. **Always Award Credit Stamps:** Every completed activity must offer a tangible reward on the player's physical passport booklet (+10 to +50 credits) and clipboard ledger.
4. **Respect the Universal Safe-Word:** If any player utters **"OZONE"**, pause immediately, drop character, and ensure they are supported.
