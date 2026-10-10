# Ecotopia Website Action Plan: Copy, Flow & UX
**Distilled Implementation Specifications for Jack & Web Development**  
*Authors: Chris (Storytelling, Narrative & Design Lead), Jack (Coordinator & Production Lead)*  
*Date: 2026-10-09*

> **Document Purpose & Scope:**  
> This document contains **only actionable website specifications**: direct copy replacements, application flow updates, form questionnaire options, and technical UI fixes for **`https://staging.join-ecotopia.org/`**.  
> All physical venue logistics, live LARP mechanics, printed booklet production, and long-form narrative worldbuilding have been intentionally stripped out and separated into dedicated documentation.

---

## 1. Executive Summary

The public website serves three core technical functions for the November 28 party at De Warren:
1. **Intake & Onboarding (`/apply`):** Authenticates guests, captures their starting carbon confessions, and assigns their initial carbon debt.
2. **Legal & Safety Compliance (`/terms`, `/privacy`):** Clarifies financial contributions, GDPR compliance, and non-negotiable safety/opt-out mechanics ("OZONE" safeword and Observer badges).
3. **World Presentation (`/ministries`):** Sets the tone through the 10 Ministries of R.E.I.G.N. without confusing guests about physical venue operations.

---

## 2. Onboarding & Authentication Flow (`/apply`)

### The Friction Issue
Currently, navigating to `/apply` without an active session shows an abrupt authentication barrier:
> *"Citizenship begins with identification — Sign in to continue. It is the first step of your application."*  
> `[SIGN IN WITH YOUR OLD-WORLD IDENTITY]`

**Risk:** Directing casual partygoers to create a Tonomy ID account without atmospheric framing causes unnecessary drop-off.

### Actionable Solution: Atmospheric Airlock Banner
Keep the authentication requirement, but add an atmospheric preamble directly above the sign-in button:

> **THE THRESHOLD OF ADMISSION**  
> *"Before you may confess, you must exist in the ledger. You were born into debt. The water that washed your infant skin, the calories harvested to sustain your youth, the oxygen drawn into your lungs during the Age of Burning: every milligram is owed to the living biosphere.*  
>  
> *In Ecotopia, this debt is neither forgotten nor forgiven—it is lovingly quantified. Authenticate your old-world identity to begin the Five Confessions, calculate your starting balance, and be drafted into your Ministry."*  
>  
> **Button CTA:** `[AUTHENTICATE IDENTITY TO BEGIN CONFESSION]`

---

## 3. The Carbon Debt Questionnaire (`CARBON_QUESTIONS`)

The 5 questions on `/apply` should be updated from generic carbon calculator metrics to liturgical state audits that reflect the satirical premise.

### Question Specifications

| Field ID | Label | Hint Text | Dropdown / Radio Options |
| :--- | :--- | :--- | :--- |
| **`flights`** | **Recreational Kerosene Combustion** | *Every altitude kilometer burned ozone belonging to unborn generations. Return trips double your debt.* | • `f0`: *Zero. My feet have never left the living soil.*<br>• `f1`: *1 to 2: A temporary lapse of atmospheric discipline.*<br>• `f2`: *3 to 5: Habitual leisure transit.*<br>• `f3`: *6 to 10: Chronic airborne defiance.*<br>• `f4`: *More than 10: I treated the stratosphere as personal exhaust.* |
| **`car`** | **Complicity with the Internal Combustion Engine** | *The bitumen martyrs tore their skin on the highway to stop this madness. Where were you?* | • `c0`: *I am unmotorized. My transit is biological.*<br>• `c1`: *I shared or borrowed an engine when biological will failed.*<br>• `c2`: *I owned a private machine of kinetic vanity.*<br>• `c3`: *I maintained multiple engines while the ice shelves cracked.* |
| **`meat`** | **Flesh Extraction & Caloric Carnivory** | *Miniplenty provides algae and pulse paste. How deeply were you attached to animal suffering?* | • `m0`: *Purely botanical. My teeth are free of blood.*<br>• `m1`: *Occasional extraction (A few times a month).*<br>• `m2`: *Weekly animal harvest (A few times a week).*<br>• `m3`: *Daily flesh ration (Every day).*<br>• `m4`: *Total caloric carnivory (At every meal).* |
| **`ai`** | **Inquiries Directed to the Silicon Mind (Daily AI Compute)** | *Hyperscale compute drained rivers before the grid failed. Every prompt boiled freshwater. R.E.I.G.N. remembers.* | • `a0`: *Zero. My thoughts are manual, slow, and human.*<br>• `a1`: *1 to 5 prompts: A modest theft of river water (a glass per day).*<br>• `a2`: *6 to 20 prompts: A commercial drain on the watershed (a bucket per day).*<br>• `a3`: *More than 20 prompts: Continuous algorithmic reliance (a full bath).*<br>• `a4`: *A synthetic intelligence is currently calculating this confession.* |
| **`devices`** | **Parasitic Lithium & Listening Hardware** | *Every battery required brine evaporation; every sensor transmitted your compliance to corporate servers.* | • `d0`: *1 or 2: Ascetic survival essentials.*<br>• `d1`: *3 to 5: Standard consumer complicity.*<br>• `d2`: *6 to 10: Heavy hardware entanglement.*<br>• `d3`: *More than I can count: I was surrounded by glowing screens.* |

### Mathematical Debt Calculation
Update the backend scoring formula on submission:

$$\text{Starting Carbon Balance} = -100 - \sum(\text{Confession Weights})$$

* **Base Gestational Debt:** `-100` Credits (inherent biological debt).
* **Confession Score Penalty:** Each option index (`0` to `4`) adds between `-10` and `-80` Credits.
* **Output Range:** Every registered citizen receives an initial balance between **`-150`** and **`-500 Carbon Credits`**.
* **Display on Completion Screen:**
  > *"Confession Recorded. Your Initial Balance: -285 Carbon Credits (Indebted Citizen). Report to the Garage Induction Desk on November 28 to begin restitution."*

---

## 4. The Sacramental Surrender Field (`INTAKE_SURRENDER`)

In the application form, update the single-choice surrender question:

**Field Label:** *"Which would you surrender first, for the good of all?"*

| Option Key | Option Text | Stored Profile Tag |
| :--- | :--- | :--- |
| `surname` | **My Surname** | `TAG_NAME_STRIKE` |
| `opinions` | **My Opinions** | `TAG_HERESY_RISK` |
| `weekends` | **My Weekends & Leisure** | `TAG_LABOR_DRAFT` |
| `hotwater` | **Hot Water & Physical Comfort** | `TAG_COLD_RATION` |
| `bedtime` | **My Bedtime & Circadian Freedom** | `TAG_NIGHT_SHIFT` |
| `secrets` | **My Secrets & Privacy** | `TAG_SURVEILLANCE_FOCUS` |

*Note for Web Devs:* Store this value in the guest record so it can be exported to CSV/Excel for the door check-in staff.

---

## 5. Drop-In Copy Replacements

Copy and paste the exact blocks below into the staging site templates.

### Route: `/terms` (Terms & Safety)

```markdown
### Financial Contribution & Entry Voucher
Participation in Ecotopia requires an advance contribution of **€15.00** (sliding scale €10.00 – €25.00 based on means). This contribution directly offsets venue hiring at De Warren, communal food, beverage reserves, and recycled passport cardstock. 

Advance contributions are processed via the secure event payment link provided upon application approval, or via card/cash at the garage intake checkpoint. No one is turned away for lack of funds; contact the Organizing Committee at citizens@join-ecotopia.org for a subsidized carbon grant.

### House Rules, Safety & Game Step-Out Mechanics
1. **Age Requirement:** Ecotopia is strictly an 18+ event. Age verification takes place at the garage threshold.
2. **The Universal Safe-Word ("OZONE"):** If at any point the theatrical roleplay, interrogation, or environment becomes uncomfortable or overwhelming, any attendee or performer may speak the word **"OZONE"**. 
   * Upon hearing *"OZONE"*, all nearby participants and actors must immediately drop character.
   * Step back, provide space, and ask: *"How can I help you?"*
   * A designated, non-costumed Safety Marshal will be available to assist you.
3. **The Observer / Free Citizen Option:** Attendees who wish to enjoy the music, visual installations, and drinks without engaging in character interrogation, carbon audits, or ministry labor chores may request an **Observer Wristband** at the door. Wardens and actors are strictly forbidden from conscripting Observer wristband wearers into state chores.
4. **The Sanctuary (Off-Game Safe Zone):** The library on the second floor is designated as a permanent, non-theatrical Safe Zone. No roleplay, propaganda enforcement, or loudspeaker broadcasting is permitted inside this room.
```

---

### Route: `/privacy` (Privacy Policy & GDPR)

```markdown
### 1. Data Controller & Organizing Entity
This service is operated by the **Ecotopia Organizing Committee** in partnership with the **De Warren Living Cooperative** (De Warren, Archipel 1, 1095 KJ Amsterdam, The Netherlands). For any data privacy inquiries or access requests, contact the Data Steward at **citizens@join-ecotopia.org**.

### 2. Legal Basis for Processing (GDPR Article 6)
We process citizen application data under the following legal bases:
* **Contractual Necessity (Article 6(1)(b)):** Processing your name, contact email, dietary preferences, and event responses is strictly necessary to assign your event role, administer your physical passport, and grant entry to De Warren.
* **Legitimate Interests (Article 6(1)(f)):** Maintaining event capacity limits, fire safety headcounts, and preventing ticket duplication.

### 3. Absolute Data Retention & Deletion Schedule
All personal data collected through this portal (including names, contact details, quiz responses, and carbon metrics) will be permanently purged from all production databases and automated backups on **19 December 2026** (exactly 21 days following the conclusion of the event). No data is retained, sold, or shared with third parties.
```

---

### Route: `/ministries` (The 10 State Ministries)

```markdown
# The Ten Ministries of R.E.I.G.N.
*Serving the Ecological Equilibrium through Devotion and Sacrifice*

1. **Miniplenty (Ministry of Ecological Bounty)**  
   *Mandate:* Rationing and caloric distribution.  
   *The Masquerade:* "Celebrating the beauty of self-imposed austerity and measured survival."  

2. **Minilove (Ministry of Ecological Harmony)**  
   *Mandate:* Biometric surveillance, behavioral interrogation, and social audit.  
   *The Masquerade:* "Ensuring all souls exist in loving, gentle compliance with Earth's limits."  

3. **Minijoy (Ministry of Morale & State Celebration)**  
   *Mandate:* Mandatory celebration, kinetic power generation, and stamina testing.  
   *The Masquerade:* "Releasing pure human kinetic joy for the collective grid."  

4. **Minirenewal (Ministry of Elemental Reclamation)**  
   *Mandate:* Involuntary recycling, identity erasure, character death, and physical composting.  
   *The Masquerade:* "The sublime honor of surrendering one's physical form back to the humus."  

5. **Minilight (Ministry of Luminescence & Grid Harmony)**  
   *Mandate:* Rolling blackouts, kilowatt rationing, and penal generator conscription.  
   *The Masquerade:* "Protecting our precious night sky and celebrating the spiritual depth of darkness."  

6. **Miniflow (Ministry of Hydrological Purity)**  
   *Mandate:* Moisture metering, strict graywater recovery, and drought simulations.  
   *The Masquerade:* "Honoring every sacred drop of Earth's circulating lifeblood."  

7. **Minibreath (Ministry of Atmospheric Rectitude)**  
   *Mandate:* Breath taxation, respiratory pacing, and carbon quota enforcement.  
   *The Masquerade:* "Harmonizing human exhalation with the delicate photosynthetic lung of the planet."  

8. **Minishelter (Ministry of Domestic Confinement)**  
   *Mandate:* Thermostat freezes, corridor curfew, and cubic meter optimization.  
   *The Masquerade:* "Maximizing thermal fellowship through cozy communal compression."  

9. **Miniservice (Ministry of Restorative Labor)**  
   *Mandate:* Penal dishwashing, waste sorting, and perpetual decontamination work.  
   *The Masquerade:* "Purifying the soul through the sacred, selfless rhythm of physical devotion."  

10. **Minithrift (Ministry of Material Confiscation)**  
    *Mandate:* Seizure of petroleum fabrics, plastic trinkets, and unauthorized possessions.  
    *The Masquerade:* "Liberating citizens from the toxic burden of non-biodegradable vanity."  
```

---

## 6. Actionable UI, Responsive & Technical Fixes

### 1. Floating Button Viewport Collision (CSS Fix)
* **Issue:** The floating `"VOICE A CONCERN"` sticky button overlaps footer text, submit buttons, and card borders on viewports narrower than 400px (e.g., iPhone SE / mobile Safari).
* **Fix:** Apply a mobile media query hiding or pinning the button to a static footer block when screen width is under 480px:
  ```css
  @media (max-width: 480px) {
    .floating-concern-btn {
      position: static;
      display: block;
      width: 100%;
      margin: 1rem 0;
    }
  }
  ```

### 2. Door Intake WAF / Rate Limiting Safeguard
* **Issue:** Up to 200 guests will connect to the local De Warren Wi-Fi at the door to retrieve their confirmation QR code or complete late intake. If multiple requests come from the same public venue IP, Vercel/Cloudflare WAF may trigger Captchas or rate-limit blocks.
* **Fix:** In the hosting provider (Vercel / Cloudflare), configure an IP whitelist or relaxed rate-limit rule for the event duration on the `/apply` and `/checkin` routes.

### 3. Missing Security Headers
* **Fix:** Add standard compliance headers to `next.config.js` or web server configuration:
  * `X-Content-Type-Options: nosniff`
  * `Referrer-Policy: strict-origin-when-cross-origin`
  * `X-Frame-Options: SAMEORIGIN`

---

## 7. Action Item Checklist for Jack & Web Team

| Task ID | Component / Route | Specific Action | Priority | Assigned Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **WEB-01** | `/terms` | Paste financial contribution text (€15 sliding scale, payment info). | **BLOCKER** | Jack / Finance | Ready to Paste |
| **WEB-02** | `/terms` | Paste house rules, 18+ limit, safe-word ("OZONE"), and Observer badge policy. | **BLOCKER** | Jack | Ready to Paste |
| **WEB-03** | `/privacy` | Paste GDPR Data Controller info and December 19 data purge commitment. | **BLOCKER** | Jack / Tech | Ready to Paste |
| **WEB-04** | `/ministries` | Replace draft ministries with the official 10 Newspeak Ministries copy. | **HIGH** | Web Dev | Ready to Paste |
| **WEB-05** | `/apply` | Insert "The Threshold of Admission" teaser before Tonomy login prompt. | **HIGH** | Web Dev | Ready to Paste |
| **WEB-06** | `/apply` (Form) | Update the 5 Carbon Confession questions and options in the form schema. | **HIGH** | Web Dev | Ready to Paste |
| **WEB-07** | `/apply` (Backend) | Update starting debt formula to output `-100` base minus confession penalties. | **MEDIUM** | Backend Dev | Ready to Code |
| **WEB-08** | CSS / Layout | Fix floating `"VOICE A CONCERN"` button overlapping on mobile screens. | **MEDIUM** | Frontend Dev | Ready to Code |
| **WEB-09** | DevOps / WAF | Add rate-limit exception / bypass for venue IP during event night. | **HIGH** | DevOps / Jack | Scheduled |
