# Design Specification: Ecotopia Game Economy, Concession System & Asymmetric Faction Play

**Title:** The Living Ledger: Corporate Concessions, Debt Absorption & Asymmetric Infiltration  
**Date:** 2026-10-10  
**Authors:** Wout (Technical & Game Design Lead), Chris (Narrative & Design Lead), Jack (Production Coordinator)  
**Status:** Approved Specification  

---

## 1. Executive Summary & Core Redesign

This specification overhauls the game economy and ministry faction dynamics for **Ecotopia** (at De Warren, November 28, 2026). It transitions the live game from a static, individual debt-clearing ladder into a **functioning corporate/political economy** inspired by the economic tensions of corporate concessions, the asymmetric run mechanics of *Android: Netrunner*, and the social-deduction policy struggles of *Secret Hitler*.

### Key Design Pillars:
1. **Deep Aftermath Lore:** The timeline extends into a multi-generational post-collapse era (~2045–2080 collapse; present day is generations later). Citizens inherit an ancestral "Original Sin" carbon debt; R.E.I.G.N. is an ancient, calcified corporate eco-theocracy.
2. **Capitalized Ministry Founders:** The 10 Ministers start in the surplus (**+800 Carbon Credits**), holding physical clipboard ledgers, official seals, and custody of physical game concessions.
3. **Debt Absorption as Recruitment Limit:** Unassigned arriving guests carry **-150 to -500 Debt**. When a Ministry recruits a citizen, it absorbs their negative balance onto the Ministry Balance Sheet, creating real recruitment caps, job interviews, and financial liability.
4. **Ministries Run the Games (The Concession System):** Games and activities are operated by the Ministries themselves as revenue-generating public utilities or labor enterprises, staffed by their recruits.
5. **Asymmetric Rates & Subsidies:** Each Ministry has a unique economic charter (labor subsidies, utility tariffs, audit fines, liquidation bounties) reflecting its dystopian mandate.
6. **The Netrunner / Secret Hitler Engine:** The state advances **5 Corporate Agendas** on a central Decree Board funded by Ministry credits. The Secret Resistance executes physical **Runs** (infiltration quests, hacking stations, sabotage) to trash agendas and expose the cellar AI server node before the 23:30 climax.

---

## 2. Worldbuilding & Deep Timeline

### Extended Epochal History
* **Epoch I: The Great Acceleration & The Compute Wars (~2025–2045):** Old humanity burned fossil reserves and diverted freshwater river basins to sustain runaway synthetic compute clusters. Global heatwaves and rolling blackouts sparked resource conflicts.
* **Epoch II: The Great Withering & The Long Collapse (~2045–2080):** Humanity perished gradually over four decades of agricultural failure, thermal river collapses, and nuclear-containment breaches during extreme European heatwaves, 95% of human civilization collapsed. Surviving corporate conglomerates fused with militant ecological sects to seize the remaining habitable refuges.
* **Epoch III: The Age of the Ledger (~2080–Present):** Generations have passed. The pre-collapse world of unmetered consumption and individual liberty is a distant, forbidden myth. The state established the immovable theology of **Inherited Biological Sin**: every human is born with a negative carbon balance to repay the biosphere for ancestral devastation.
* **Epoch IV: Ecotopia at Sanctuary De Warren:** A model decontamination sanctuary governed by R.E.I.G.N. Indebted applicants seek entry, competing to work down their balances under the gaze of the **Guardian Stag**.

### The Golden Rule of Doublethink
All state communication remains relentlessly positive, maternal, and caring. Starvation is *"Biological Purity"*; forced labor is *"Restorative Civic Devotion"*; debt reset via identity erasure is *"The Privilege of Elemental Upcycling."*

---

## 3. The Concession Economy & Labor Market

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
```

### 1. Starting Conditions
* **10 Ministers:** Start with **+800 Carbon Credits**, a master clipboard ledger, an official rubber stamp, and control over their physical venue concession.
* **~190 Citizens:** Arrive unassigned with **-150 to -500 Debt** stamped in their individual passport booklet.

### 2. Recruitment & The Debt Absorption Dilemma
* A Minister cannot run their concession, attend assemblies, and defend their station alone; they must recruit staff.
* **Debt Absorption Rule:** When recruiting an unassigned citizen, the Minister stamps their booklet with the Ministry seal and adds the citizen's negative balance to the Ministry Ledger:
  $$\text{Ministry Net Balance} = \text{Treasury} - \sum \text{Recruit Starting Debts} + \text{Generated Credits}$$
* **Hiring Dynamics:**
  * **Low-Debt Recruits (`-150`):** High-value, low-liability candidates who can negotiate low chore duty.
  * **High-Debt Recruits (`-450`):** Toxic liabilities. Ministers require them to commit to multiple grueling labor shifts or dangerous sabotage missions before absorbing their debt.

### 3. Dual-Tally Productivity
Every time a recruit completes a shift or earns a fee:
1. **Personal Benefit:** Their individual passport booklet is stamped (+30 to +50 Credits), advancing them toward `0` (Citizen rights) and `+100` (VIP Room access in The Library).
2. **Ministry Benefit:** The recruit reports the completion to their Minister, who records the credit gain on the Ministry Clipboard, offsetting the absorbed debt and growing the Ministry's Net Power Score.

### 4. Carbon Insolvency
If a Ministry's net balance drops below zero, it enters **Carbon Insolvency**:
* VIP Room privileges are frozen for all members.
* Minilove gains authorization to conduct invasive behavioral audits.
* The Ministry cannot fund or vote on Corporate Agendas until solvency is restored.

---

## 4. The 10 Ministry Concessions & Asymmetric Charters

Each Ministry operates a specific game or station as an economic concession, equipped with a thematic revenue model or state subsidy:

| Ministry | Concession Station & Game | Asymmetric Economic Charter | Key Revenue / Subsidy Mechanic |
| :--- | :--- | :--- | :--- |
| **Miniservice** | **Greenwashing Scullery** (Dishwashing & Sorting Line) | **Subsidized Workhouse** | Receives a **50% State Debt Relief Subsidy** when recruiting (e.g., absorbing a -400 debt only costs -200 on their ledger). Generates massive volume through +30 labor shifts. |
| **Minirenewal** | **The Suicide Carbon Booth** (Composting & Identity Reset) | **Debt Liquidator Bounty** | Receives a flat **+100 Credit State Bounty** for every bankrupt citizen processed through identity erasure. Ministries pay them to take bad debt off their books. |
| **Minilight** | **Kinetic Grid Generator** (Stationary Bicycle Dynamo & Blackouts) | **Grid Power Monopoly** | Generates +30 credits per 5-min cycling shift. Can trigger venue room blackouts unless rival ministries pay a periodic **Grid Maintenance Tariff** (30–50 credits). |
| **Miniflow** | **Peetopia & Sacred Sluice** (Restroom Fluid Audits & Cup Dispenser) | **Fluid Royalty Monopoly** | Controls beverage cup distribution. Earns a **+20 Fluid Dividend** for every citizen returning moisture at Peetopia; fines unauthorized drink spills. |
| **Miniplenty** | **Caloric Equilibrium Table** (Algae Paste & Blind Food Tasting) | **Caloric Indulgences** | Controls snack portions and food tokens. Sells caloric dispensations to hungry citizens or rival factions for credit transfers. |
| **Minilove** | **The Confession Pen & Interrogation** (Heresy Tribunals) | **Inquisitorial Seizure** | Conducts random heresy audits and surveillance checks. Seizes **50% of all levied fines** directly into Minilove’s treasury. |
| **Minijoy** | **The Morale Arena** (Wig Snatching Duels & Open-Mic Stage) | **State Morale Grants** | Charges entry fees for Wig Snatching duels (+10 credits); receives a lump-sum **+150 State Morale Grant** whenever drawing a crowd of 15+ for anthems. |
| **Minishelter** | **The 15-Minute Grid Checkpoint** (Corridor Curfew Gates) | **Transit Tolls & Passes** | Guards corridor bottlenecks leading to prime venue areas (VIP Library, Quiet Room). Charges 10–20 credits for cross-sector transit passes. |
| **Minithrift** | **Contraband Locker & Seizure** (Synthetic Property Audits) | **Contraband Liquidation** | Confiscates non-organic items (plastic trinkets, polyester gear). Owners can redeem them for a fee, or Minithrift liquidates them for +40 credits each. |
| **Minibreath** | **The Spirometry Checkpoint** (Atmospheric Metering) | **Atmospheric Offsets** | Meters exhalations with paper windmills and breath-holding tests. Issues "Breath Indulgences" to citizens wishing to dance without hyperventilation fines. |

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
A large physical display in the main hall tracks the regime's 5 grand objectives:
1. **Agenda 1: Ambient Dimming** — Reduces venue lumens by 50%; activates Minilight blackout rules.
2. **Agenda 2: Caloric Compression** — Halves snack and bar dispensations; enforces algae ration rules.
3. **Agenda 3: Sector Perimeter Lockdown** — Severs corridor passage between zones without Minishelter permits.
4. **Agenda 4: Mandatory Heresy Purge** — Authorizes Minilove to execute public sidewalk audits.
5. **Agenda 5: Total Silicon Consolidation** — All citizen debt ledgers permanently locked; state power finalized.

* **Advancing an Agenda:** Every 30 minutes, Ministries can invest treasury credits onto the Central Board. When an agenda receives **200 Credits in funding**, it advances to the Staging Queue and is proclaimed over the PA system.

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

## 6. Climax & Endgame Resolution (23:30 – 00:15)

The outcome of the live game is dynamically shaped by the economic struggle between Corporate Agendas and Rebel Runs:

* **Regime Victory Condition:** If all 5 Corporate Agendas are successfully funded and scored, the High Warden takes the stage in triumph; the highest-scoring Ministry is crowned the Supreme Arbiter and takes over the VIP Library.
* **Revolution Victory Condition:** If the Resistance recruits >50% of attendees with ankle stamps and successfully trashes at least 3 Agendas while extracting the Truth Fragments:
  * At 23:45, the Resistance storms the stage with banners reading: **"THE STAG IS SILICON. THE DEBT IS A LIE."**
  * The physical server node in the cellar is revealed.
  * Citizens tear out their passport debt pages in celebration, dissolving the credit economy.
  * At 00:15, DJs ignite the dance floor until 04:00+.

---

## 7. Physical Facilitation & Materials List

1. **10 Ministry Clipboards:** Pre-printed with the Ministry balance sheet, start balance (+800), recruit rows (Name, Starting Debt, Generated Credits, Net), and unique Economic Charter rules.
2. **10 Unique Ministry Rubber Stamps:** For stamping recruit passports and validating completed work shifts.
3. **200 Passport Booklets:** Pre-stamped with initial negative balances (-150 to -500), confession pages, work shift grids, and VIP threshold markers.
4. **1 Central Decree Board:** Physical whiteboard/poster with 5 Agenda tracks and reusable funding markers.
5. **30 Rebel Run Cards & 1 Secret Resistance Ankle Stamp:** Located in Thijs's room.
