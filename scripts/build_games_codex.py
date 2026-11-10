#!/usr/bin/env python3
"""Build print_games_codex_a4.html: the gothic Facilitator Codex + Book of Games (pick list).

Edit the data below (GAMES, sheets) and re-run:
    python3 scripts/build_games_codex.py
Then print the HTML from Chrome (A4, margins: default, background graphics on) or render to PDF.
"""
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "print_games_codex_a4.html"
e = html.escape

# --------------------------------------------------------------------------- BOOK II: GAME CATALOGUE
# Each game: name, ministry, host, where, size (players · minutes), props, play (steps), reward, twist, heat
# heat = intensity for the player: Low / Medium / High (High = only with explicit opt-in)

CATEGORIES = [
  {
    "key": "interrogation",
    "title": "The Interrogation",
    "sub": "Minilove intake for those who did not apply for citizenship · Lead: Eric",
    "plate": ("martyrs.jpg", "Plate · The Tribunal of the Unregistered"),
    "intro": "Guests without an application are pulled from the garage queue into a small, dim room: one chair, one lamp, "
             "two officers. Every interrogation ends the same way — with a debt stamped in the passport and a ministry "
             "assignment — but the route there can be chosen per guest and per mood. Keep each session under four minutes "
             "so the queue keeps moving.",
    "games": [
      dict(name="Good Cop / Bad Cop Carbon Audit", ministry="Minilove", host="2 Interrogation Officers",
           where="Garage interrogation room", size="1 guest · 3–4 min", heat="Medium",
           props="Desk lamp, single chair, clipboard, Audit Card with 5 questions, debt stamp",
           play=["Bad Cop reads the Audit Card: flights taken, meat eaten, age of phone, length of shower, number of chargers owned.",
                 "Every honest answer adds debt (+50 CC per sin); every evasive answer adds double.",
                 "Good Cop slides over a cup of algae water and offers a 100 CC 'discount' for a sincere apology to the biosphere.",
                 "Total is stamped into the passport (−150 to −500 CC) and a ministry is assigned."],
           reward="Debt set at −150 to −500 CC", twist="Guests who apologise to the lamp instead of the officers get a 'Sincerity Discount' of 50 CC."),
      dict(name="The Prisoner's Ledger", ministry="Minilove", host="2 Officers in separate booths",
           where="Two booths or two corners of the garage", size="2 guests · 3 min", heat="Medium",
           props="Two chairs back-to-back behind a curtain, 2 verdict cards, egg timer",
           play=["Two arriving guests are separated and each told the other has 'already confessed'.",
                 "Each secretly chooses SILENCE or DENOUNCE on a verdict card.",
                 "Both silent: −150 each. One denounces: denouncer −100, the other −400. Both denounce: −300 each.",
                 "Reveal the cards together; read the outcome aloud like a court verdict."],
           reward="Debt per outcome table", twist="A classic prisoner's dilemma: the room learns who trusts whom before the party even starts."),
      dict(name="The Breath Polygraph", ministry="Minilove × Minibreath", host="1 Officer + 1 hidden Buzzer Operator",
           where="Interrogation room", size="1 guest · 2–3 min", heat="Low",
           props="'Lie detector' (lamp + paper windmill + cables), hidden buzzer or bell",
           play=["Guest holds the windmill to their lips; every answer must be breathed onto it.",
                 "Officer asks 6 yes/no questions ('Have you ever left a tap running?').",
                 "The hidden operator buzzes at random. Each buzz = 'LIE DETECTED', +40 CC debt.",
                 "Guest may retract any answer by confessing a bigger sin instead."],
           reward="Debt +40 CC per buzz", twist="The machine is obviously rigged — and the officer insists it is the most objective instrument in Ecotopia."),
      dict(name="The 24-Hour Carbon Receipt", ministry="Minilove", host="1 Auditor with calculator",
           where="Intake desk", size="1 guest · 3 min", heat="Low",
           props="Receipt pad, absurd Carbon Price List (A5), adding machine or calculator",
           play=["Guest reconstructs the last 24 hours out loud: travel, meals, screens, showers.",
                 "Auditor prices every item from the Carbon Price List ('one selfie: 12 CC').",
                 "Guest must total the receipt themselves within 60 seconds.",
                 "Arithmetic errors are fined as 'ledger fraud' (+50 CC)."],
           reward="Debt = receipt total", twist="Hand the receipt over as a souvenir; it doubles as proof of debt at other stations."),
      dict(name="State Tongue Drill", ministry="Minilove", host="1 Officer with flash cards",
           where="Interrogation room", size="1 guest · 2 min", heat="Low",
           props="10 flash cards from the Doublethink Lexicon (old word → state word)",
           play=["Officer shows an old-world word ('holiday', 'freedom', 'steak').",
                 "Guest must answer with the State Tongue equivalent within 5 seconds.",
                 "Each old-world word spoken = +20 CC debt; each correct answer = −10 CC.",
                 "Ten cards, then the passport is stamped."],
           reward="Debt ±10/20 CC per card", twist="Teaches the vocabulary the rest of the night runs on."),
      dict(name="The Ancestral Multiplier", ministry="Minilove", host="1 Genealogist Officer",
           where="Interrogation room", size="1 guest · 3 min", heat="Low",
           props="Family-tree form, one large die, ink pad",
           play=["Guest names three ancestors and one bad habit each (a car, a cruise, a barbecue).",
                 "Each habit gets a base debt of 50 CC.",
                 "Guest rolls the Ancestral Multiplier die: the total is multiplied by the roll (cap at −500).",
                 "Thumbprint the family tree; it is filed 'for eternity'."],
           reward="Debt 50–500 CC", twist="Inherited Biological Sin made literal: you are fined for your grandmother's caravan."),
      dict(name="Denounce a Neighbour", ministry="Minilove", host="1 Officer",
           where="Intake desk", size="1 guest · 1–2 min", heat="Medium",
           props="Pre-printed Denunciation Slips, box with slot",
           play=["Officer offers 100 CC off the guest's debt for naming another guest who 'looks unsustainable'.",
                 "The guest writes a description (never a real name) on a Denunciation Slip.",
                 "Slips go in the box; Minilove patrols draw slips during the night and audit whoever matches.",
                 "Guests who refuse to denounce get a small 'Integrity' sticker — which the resistance looks for."],
           reward="−100 CC debt for denouncing", twist="The refusers become the easiest recruits for Thijs's resistance later."),
      dict(name="The Soft Interrogation (opt-out route)", ministry="Minilove", host="1 Friendly Clerk",
           where="Side desk, lights up", size="1 guest · 1 min", heat="Low",
           props="Simple form, pen, debt stamp",
           play=["For guests who look uncomfortable or say they'd rather not: no officers, no lamp.",
                 "A friendly clerk asks three light questions and apologises for the bureaucracy.",
                 "Standard debt of −250 CC is stamped; passport handed over with a smile.",
                 "Guest continues to the ministry desk like everyone else."],
           reward="Debt −250 CC", twist="Always available. Nobody needs to explain why they chose it."),
    ],
  },
  {
    "key": "inburgering",
    "title": "The Inburgering",
    "sub": "The Civic Integration Programme for new citizens · Lead: Inge & Lexi",
    "plate": ("babel.jpg", "Plate · The Confusion of Tongues · The Integration Exam"),
    "intro": "Every new citizen must integrate. Modelled on the Dutch inburgering: an exam, a participation declaration, "
             "a knowledge-of-society test and a ceremony — all in Ecotopian form. These games work at intake, at a fixed "
             "Integration Desk during the night, or as a scheduled ceremony on the hour.",
    "games": [
      dict(name="The Civic Integration Exam", ministry="Minilove × Miniservice", host="1 Examiner, 1 Invigilator",
           where="Integration Desk", size="4–8 guests · 5 min", heat="Low",
           props="A6 exam sheets with 10 multiple-choice questions, pencils, a loud timer",
           play=["Guests sit in a row; the invigilator reads the rules in a stern voice.",
                 "10 absurd questions ('A neighbour uses two napkins. You: a) report b) report twice c) compost the neighbour').",
                 "Examiner marks on the spot. 7+/10 = pass, below = remedial class (sing the anthem once).",
                 "Pass stamps 'INGEBURGERD' in the passport."],
           reward="+30 CC on pass", twist="Every answer is technically correct; the examiner marks according to mood."),
      dict(name="The Participation Declaration", ministry="Minilove", host="1 Notary",
           where="Integration Desk", size="1–6 guests · 3 min", heat="Low",
           props="Long contract on a scroll, quill or fountain pen, wax-seal stamp",
           play=["The notary reads the Participation Declaration out loud, very fast.",
                 "Hidden in the middle: 'I hereby donate my spare neural cycles to the Guardian Stag.'",
                 "Guests must sign. Anyone who asks 'wait, what was that line?' is quietly given a resistance contact slip.",
                 "Everyone else receives a wax seal on Page 3."],
           reward="+20 CC for signing", twist="Plants the AI-server twist early: attentive guests become the resistance."),
      dict(name="Knowledge of Ecotopian Society", ministry="Miniservice", host="1 Examiner + 1 actor",
           where="Integration Desk or corridor", size="1–2 guests · 3 min", heat="Low",
           props="Scenario cards, a minister's hat for the actor",
           play=["Guest draws a scenario card: greet a Minister, refuse a second ration, report a light left on, apply for a shower permit.",
                 "The actor plays the other side of the scene.",
                 "Examiner scores politeness, obedience and correct use of State Tongue (0–10).",
                 "Score ≥ 7 earns a 'Society Knowledge' stamp."],
           reward="+25 CC for ≥ 7", twist="Parody of the KNM exam; guests learn the social rules of the evening by playing them."),
      dict(name="The State Tongue Speaking Test", ministry="Minijoy", host="1 Examiner with posh accent",
           where="Integration Desk", size="1 guest · 2 min", heat="Low",
           props="Decree cards to read aloud, microphone optional",
           play=["Guest reads a short decree aloud in the official voice of Hanna (posh, polite, horrific).",
                 "The examiner grades accent, tone of calm menace and correct pauses.",
                 "Grades A–F stamped on the passport.",
                 "Grade A may be invited to read an announcement over the PA later."],
           reward="+15 to +40 CC by grade", twist="Gives you a pool of guest announcers for the night."),
      dict(name="The Integration Buddy", ministry="Miniservice", host="Integration Desk staff",
           where="Anywhere", size="2 guests · 30 min", heat="Low",
           props="Buddy cards in pairs (matching numbers), stamp sheet",
           play=["Each new citizen is paired with a veteran citizen (someone who arrived earlier).",
                 "Together they must collect 3 ministry stamps within 30 minutes.",
                 "Return to the desk with the completed buddy card.",
                 "Both receive the reward; the fastest pair of the hour is announced by Hanna."],
           reward="+30 CC each", twist="Mixes friend groups and gets new arrivals into the game fast."),
      dict(name="Anthem & State Gesture Certification", ministry="Minijoy", host="1 Choreographer",
           where="Integration Desk / dance floor edge", size="1–10 guests · 3 min", heat="Low",
           props="Speaker with the Ecotopia anthem, gesture poster",
           play=["The choreographer teaches the 4 State Gestures (Stag Antlers, Ledger Bow, Breath Hold, Gratitude Palm).",
                 "Guests perform them to 30 seconds of the anthem.",
                 "Pass = gestures in the right order; certification stamp issued.",
                 "Certified citizens must perform the gestures whenever Hanna says 'Gratitude'."],
           reward="+20 CC", twist="Sets up crowd moments for the Grand Assembly at 23:30."),
      dict(name="The Naturalisation Ceremony", ministry="All ministries", host="High Warden + Hanna (PA)",
           where="Main stage", size="10–40 guests · 8 min, on the hour", heat="Low",
           props="Seed packets or sapling stickers, ceremonial ledger, gong",
           play=["Every hour, everyone who passed an integration game gathers at the stage.",
                 "Mass oath: 'I compost my old self. I return my nitrogen. I accept my debt with gratitude.'",
                 "Names are read out; each new citizen receives a seed packet and the gong is struck.",
                 "Applause is mandatory and metered."],
           reward="+25 CC + seed packet", twist="A satisfying public beat each hour that also drives crowds to the stage."),
      dict(name="The Labour Market Orientation", ministry="Miniservice", host="3–4 Ministers",
           where="Corridor 'job fair' table", size="6–12 guests · 6 min", heat="Low",
           props="Ministry recruitment flyers, a bell",
           play=["Speed-dating, but for jobs: ministers sit on one side, unassigned citizens on the other.",
                 "60-second pitches each way; bell rings, citizens move one seat.",
                 "At the end, ministers bid for citizens with treasury credits.",
                 "Hired citizens get a ministry stamp and their first shift."],
           reward="Hiring bonus 20–60 CC", twist="Turns the concession hiring mechanic into a visible, funny moment."),
    ],
  },
  {
    "key": "stations",
    "title": "Ministry Stations",
    "sub": "Concession games that run all night at fixed locations",
    "plate": ("famine.jpg", "Plate · The Stations of Daily Labour"),
    "intro": "Station games are short, repeatable and give each ministry a reason to recruit labour. Choose two or three "
             "per ministry, at most.",
    "games": [
      dict(name="The Recycling Plant Sorting Line", ministry="Minirenewal", host="1 Plant Supervisor",
           where="Recycling plant / garage corner", size="1–2 guests · 60 s", heat="Low",
           props="Crate of clean 'trash' (cans, cartons, cork, fabric), 7 bins with absurd labels",
           play=["Bins are labelled things like 'Repentant Plastic', 'Former Luxuries', 'Nitrogen-Positive', 'Heresy'.",
                 "Guest sorts 20 items in 60 seconds.",
                 "Supervisor checks against a secret (and changing) sorting chart.",
                 "Each correct item +2 CC; each wrong item −2 CC."],
           reward="Up to +40 CC", twist="The sorting chart changes every hour by decree; old rules become heresy."),
      dict(name="Second Life Pawnshop", ministry="Minithrift", host="1 Pawnbroker",
           where="Minithrift table", size="1 guest · 90 s", heat="Low",
           props="Box of random objects (a sock, a CD, a spoon, a lampshade), bell",
           play=["Guest draws a random object.",
                 "They have 30 seconds to pitch three new uses for it.",
                 "Pawnbroker rings the bell for each convincing use.",
                 "3 bells = the object is 'reborn' and the guest is paid."],
           reward="+10 CC per bell", twist="The reusable-objects idea from the committee list, as a quick improv game."),
      dict(name="Pedal Power Vigil", ministry="Minilight", host="1 Dynamo Warden",
           where="Bike dynamo by the bar", size="1–2 guests · 3 min shifts", heat="Low",
           props="Stationary bike with dynamo or light, leaderboard",
           play=["The bar's 'sacred lamp' must stay lit; when nobody pedals, the warden switches it off.",
                 "Guests pedal 3-minute shifts.",
                 "If the lamp goes out, the bar stops serving until it's relit (for 30 seconds — keep it light).",
                 "Fastest shift of the hour goes on the leaderboard."],
           reward="+30 CC per shift", twist="Makes Minilight's grid monopoly physical and loud."),
      dict(name="Blind Tasting: The Most Sustainable Bite", ministry="Miniplenty", host="1 Sommelier of Scarcity",
           where="Miniplenty snack table", size="1–4 guests · 2 min", heat="Low",
           props="Blindfolds, 5 numbered cups (seaweed, cricket crisps, lentils, oat drink, one normal crisp)",
           play=["Blindfolded guests taste 5 samples.",
                 "They must rank them from 'most sustainable' to 'most sinful'.",
                 "The normal crisp is always the sinner; spotting it pays a bonus.",
                 "Check allergies before blindfolding — offer a no-food version (smell only)."],
           reward="+25 CC (pass 3/5), +35 CC (5/5)", twist="Whoever enjoys the crisp too visibly is fined for nostalgia."),
      dict(name="The Sensory Sanctum: Smell Your Way to Sustainability", ministry="Minibreath", host="1 Olfactory Priest",
           where="Sensory blocking room", size="1–3 guests · 3 min", heat="Low",
           props="8 opaque jars (pine, soil, coffee, petrol-scented marker, rain, rubber…), blindfolds, soft light",
           play=["Guests are led blindfolded into a quiet, dim room.",
                 "They smell each jar and say whether it is 'Sanctioned' or 'Heretical'.",
                 "The priest whispers the official verdict after each jar.",
                 "Guests leave with a breath stamp."],
           reward="+20 CC", twist="Good low-energy station; also a calm place to send overwhelmed guests."),
      dict(name="Ecococktail Indulgences", ministry="Miniplenty × Miniflow", host="Bartenders",
           where="Bar", size="Any · ongoing", heat="Low",
           props="Cocktail menu with CC prices, 'Neutralised' stamp",
           play=["Every drink has a Carbon Price on the menu.",
                 "A drink becomes 'Carbon-Neutral' if the guest performs a deed first: a compliment to a minister, 10 seconds of pedalling, a recited slogan.",
                 "Neutralised drinks get a stamp on the cup.",
                 "Guests who forget their deed are gently shamed by the bartender."],
           reward="Discount or stamp", twist="Not a separate game: a layer over the existing bar."),
      dict(name="Peetopia Flush Permits", ministry="Miniflow", host="1 Fluid Auditor (outside restrooms)",
           where="Restroom corridor", size="Any · 10 s", heat="Low",
           props="Flush permit tickets, clipboard, hydration chart poster",
           play=["The auditor offers a 'Flush Permit' as guests head to the restroom.",
                 "Returning moisture to the collective earns a stamp on the way out.",
                 "Guests who skip the auditor are written up (just a joke citation).",
                 "Never block the restroom or delay anyone in a hurry."],
           reward="+20 CC per return", twist="Keeps the existing Peetopia idea light and fast."),
      dict(name="Greenwashing: The Rebranding Desk", ministry="Miniservice", host="1 Brand Steward",
           where="Scullery table", size="1–2 guests · 2 min", heat="Low",
           props="Empty product packaging, green markers, leaf stickers",
           play=["Guest picks a 'sinful' product package (crisps, a shampoo bottle, a phone box).",
                 "In 90 seconds they must greenwash it: new name, leaf stickers, a slogan.",
                 "The steward hangs the best ones on the Wall of Purified Products.",
                 "Pairs with the existing Greenwashing Dishes shift."],
           reward="+20 CC, +40 CC if hung on the wall", twist="The wall becomes a funny art piece by midnight."),
    ],
  },
  {
    "key": "stage",
    "title": "Stage & Crowd",
    "sub": "Scheduled moments for the main stage, the PA and the whole room",
    "plate": ("trumpets.jpg", "Plate · The Seven Trumpets of Morale"),
    "intro": "Big moments to pull the room together between the station games. One every 30–45 minutes is plenty.",
    "games": [
      dict(name="The Ecotopia Anthem & State Dance", ministry="Minijoy", host="Morale Officer + DJ",
           where="Dance floor", size="Everyone · 4 min", heat="Low",
           props="Anthem track, gesture poster, megaphone",
           play=["At 22:00 and 23:30 the DJ fades into the anthem.",
                 "The Morale Officer leads the State Gestures from the stage.",
                 "Ministers 'spot-check' devotion and hand out +10 CC to the most sincere dancers.",
                 "Ends with the whole room shouting 'Born into debt! Repaid in devotion!'"],
           reward="+10 CC spot rewards", twist="Learned during the Inburgering, performed by everyone later."),
      dict(name="The Ministry Rally", ministry="All ministries", host="High Warden as judge",
           where="Main stage", size="3–5 ministries · 15 min", heat="Low",
           props="Prompt cards, cardboard banners, markers, applause meter (or a judge with a sign)",
           play=["Each competing ministry gets 10 minutes to prepare a 60-second rally speech and chant.",
                 "Prompts: 'Why your ministry deserves more power', 'Why the rival ministry is a fire hazard'.",
                 "Each ministry performs; the crowd is the applause meter.",
                 "Winner receives a treasury grant and may fund a decree."],
           reward="+150 CC treasury grant", twist="Drives the Central Decree Board and gives ministries a reason to recruit loud citizens."),
      dict(name="The Sustainability Pageant", ministry="Minijoy", host="2 hosts + 3 judges",
           where="Main stage", size="5–6 contestants · 15 min", heat="Low",
           props="Sash for the winner, judges' scorecards, a runway (taped line)",
           play=["Round 1, Lowest-Footprint Outfit: walk the runway explaining what your outfit gave up.",
                 "Round 2, Talent: 30 seconds of a sustainable talent (silent gratitude, composting mime…).",
                 "Round 3, Q&A: 'How would you end the world as sustainably as possible?'",
                 "Judges score; winner crowned Citizen of the Ledger."],
           reward="+100 CC + sash", twist="Ideal for guests who came in full costume."),
      dict(name="ABC: The Sustainability Gameshow", ministry="Minijoy × Minilove", host="Quizmaster in Hanna voice",
           where="Stage or side room", size="4 teams of 3 · 15 min", heat="Low",
           props="Buzzers or bells, question cards, scoreboard",
           play=["Rounds: Carbon Prices, Doublethink, Pre-Collapse History (all wrong on purpose), Name That Ministry.",
                 "Teams buzz in; correct answers per the State, not reality.",
                 "Joker: once per game a team may 'Denounce' another team to steal their points.",
                 "Winning team splits the prize."],
           reward="+60 CC per winning team member", twist="A pub quiz where reality loses points."),
      dict(name="How the World Ends (Open-Mic)", ministry="Minijoy", host="Morale Officer",
           where="Mini-podium", size="Up to 4 contestants · 10 min", heat="Low",
           props="Megaphone, banners, ribbon",
           play=["Existing game: 60 seconds for the most melodramatic extinction monologue.",
                 "Rounds at 22:00, 22:45, 23:15.",
                 "Crowd applause picks the winner.",
                 "Winner receives the Order of Cathartic Hysteria."],
           reward="+100 CC + ribbon", twist="Already in the run sheet; listed here for completeness."),
      dict(name="Hanna Says (PA Broadcast Game)", ministry="Minilove", host="Hanna on the PA + floor wardens",
           where="Whole venue", size="Everyone · 1 min, several times a night", heat="Low",
           props="PA, scripted broadcasts",
           play=["Hanna's hourly bulletins include commands: 'Citizens will now hold their breath in gratitude.'",
                 "Commands that start with 'By decree' must be obeyed; others must be ignored.",
                 "Wardens fine the slowest or the wrong ones 10 CC (playfully).",
                 "Mix in genuinely useful info (bar times, schedule) the same way."],
           reward="Fines 10 CC", twist="Simon Says with a posh voice and horrific news in between."),
      dict(name="The Riot Drill", ministry="Minilove × Minishelter", host="4 Officers with cardboard shields",
           where="Dance floor edge, marked zone", size="Volunteers · 5 min", heat="Medium",
           props="Cardboard shields, tape for the zone, whistle",
           play=["A choreographed, no-contact drill: officers 'kettle' a taped zone that shrinks every 30 seconds.",
                 "Volunteers inside chant approved slogans and must stay in the zone.",
                 "Those squeezed out are 'processed' (a stamp) and become spectators.",
                 "Last citizen standing receives a Loyalty Medal."],
           reward="+40 CC to the last citizen", twist="Musical chairs as state theatre. Strict rule: no touching, volunteers only."),
      dict(name="The Wig Snatching Arena", ministry="Minijoy", host="Arena Referee",
           where="Clearing near the stage", size="2 duellists · 60 s", heat="Low",
           props="Neon wigs, bell, chalk circle",
           play=["Existing game: snatch the opponent's wig without touching their body.",
                 "Best of 3, hands start on knees.",
                 "Entry +10 CC to Minijoy; winner +25 CC.",
                 "Good distraction for rebel runs nearby."],
           reward="+25 CC", twist="Already in the run sheet; listed for completeness."),
    ],
  },
  {
    "key": "economy",
    "title": "Gambling & the Debt Economy",
    "sub": "Games that move carbon credits between citizens and ministries",
    "plate": ("pale_horse.jpg", "Plate · And Debt Rode Behind Him"),
    "intro": "Gambling makes the economy feel alive and lets players climb out of debt quickly or sink further. Cap stakes at "
             "50 CC so nobody is locked out of the night's game.",
    "games": [
      dict(name="Carbon Roulette", ministry="Minijoy", host="1 Croupier",
           where="Casino table", size="Up to 6 · 2 min per spin", heat="Low",
           props="Spinner or roulette wheel with the 10 ministry names + a black 'STAG' field, chips",
           play=["Players bet 10–50 CC on a ministry.",
                 "Winning ministry pays 5×; the STAG field takes all bets for the state.",
                 "The croupier announces each result as a state communiqué.",
                 "The winning ministry's treasury gets +10 CC every spin."],
           reward="5× stake", twist="Ministries start sending members to cheer for their own field."),
      dict(name="Liar's Ledger", ministry="Minilove", host="Self-run (rules card)",
           where="Any table", size="3–6 · 10 min", heat="Low",
           props="5 dice and a cup per player",
           play=["Liar's dice: players bid on how many dice across the table show a face ('four 3s').",
                 "Call 'AUDIT' to challenge the previous bid.",
                 "Loser of each audit pays 10 CC into the pot and loses a die.",
                 "Last player with dice wins the pot."],
           reward="The pot", twist="Bluffing as civic virtue."),
      dict(name="Debt Futures Auction", ministry="Minithrift", host="1 Auctioneer",
           where="Stage or bar", size="Room · 10 min, once per hour", heat="Medium",
           props="Gavel, 'debt bonds' cards (volunteers only)",
           play=["Volunteer citizens put a slice of their debt up for auction.",
                 "Others bid credits to 'buy' it; the buyer may assign the debtor one light task (fetch a drink, perform a gesture).",
                 "The auctioneer narrates each citizen's qualities like livestock at a fair.",
                 "Debt moves from seller to buyer on both passports."],
           reward="Debt transfer", twist="Only volunteers; tasks must stay light and consensual."),
      dict(name="The Carbon Confessional Price List", ministry="Minilove", host="1 Confessor",
           where="Confession booth", size="1 guest · 90 s", heat="Low",
           props="Price list of sins, curtain, small bell",
           play=["Guest confesses a pre-collapse sin; the confessor looks it up on the price list.",
                 "Pay the price in credits to receive absolution (a stamp).",
                 "Confessing someone else's sin costs double.",
                 "Minilove keeps 50% of every absolution."],
           reward="Absolution stamp", twist="The committee's Carbon Confessions idea, made into a shop."),
      dict(name="Indulgence Certificates", ministry="Miniplenty × Minilove", host="Pardoner with tray",
           where="Roaming", size="Any · 30 s", heat="Low",
           props="Pre-printed gothic certificates (e.g. 'Licence to shower 4 minutes')",
           play=["The pardoner roams the venue selling indulgences.",
                 "Each certificate permits one sin for one night: a second drink, a phone check, a hug.",
                 "Wardens may demand to see the certificate.",
                 "Unlicensed sinners are fined 20 CC."],
           reward="Costs 20–60 CC", twist="Medieval indulgences meet carbon offsets."),
      dict(name="The Ministry Stock Exchange", ministry="Minithrift", host="1 Broker at a board",
           where="Wall near the Decree Board", size="Room · all night", heat="Low",
           props="Whiteboard with 10 ministry 'share prices', share slips",
           play=["Citizens buy shares in ministries for 10 CC each.",
                 "Every 30 minutes the broker updates prices based on ministry treasuries and scandals.",
                 "Shares can be sold back at the current price.",
                 "Insider trading is a heresy (and therefore very popular)."],
           reward="Varies", twist="Gives spectators a reason to follow the ministry rivalries."),
    ],
  },
  {
    "key": "resistance",
    "title": "Resistance & the Machine",
    "sub": "Games that seed the AI-server twist and feed the revolution at 23:30",
    "plate": ("melencolia.jpg", "Plate · Melencolia of the Machine"),
    "intro": "These games tie into the secret that the Guardian Stag is an AI running on human brains. They should feel "
             "slightly off: too precise, too eager, glitching.",
    "games": [
      dict(name="Prove You Are Human", ministry="Minilove (the Machine)", host="1 Terminal Attendant",
           where="Terminal by the cellar door", size="1 guest · 2 min", heat="Low",
           props="Laptop or printed 'captcha' cards with absurd tests",
           play=["Before entering a sector, guests must pass a captcha: 'Select all images containing gratitude'.",
                 "The attendant marks every answer as wrong at least once.",
                 "On the third try they pass and receive a sector stamp.",
                 "One captcha card in ten shows a cellar server rack — the attendant panics and takes it back."],
           reward="Sector stamp", twist="Plants the AI clue in plain sight."),
      dict(name="The Prompt Confessional", ministry="Minilove (the Machine)", host="Hidden typist",
           where="Booth with screen", size="1 guest · 2 min", heat="Low",
           props="Laptop showing a chat window, hidden operator on another laptop",
           play=["Guests type a question or confession to 'the Guardian Stag'.",
                 "A hidden operator replies in an over-polite, slightly broken AI voice.",
                 "Every reply ends with a debt adjustment.",
                 "Occasionally the Stag 'leaks': 'Neural throughput insufficient. Please hydrate.'"],
           reward="±10–30 CC", twist="Answers the committee's 'Sustainable AI, how to do it?' line with the twist itself."),
      dict(name="The Whisper Chain", ministry="Resistance (Thijs)", host="Thijs's room",
           where="Whole venue", size="5 guests · 20 min", heat="Low",
           props="5 numbered cards, one secret phrase",
           play=["A rebel whispers a phrase to the first link; each link must find the next by a visual sign (ankle stamp, red ribbon).",
                 "The last link reports the phrase back to Thijs.",
                 "If it arrives intact, the chain gets a truth fragment.",
                 "Minilove patrols may intercept a link: 'You seem to be whispering.'"],
           reward="Truth fragment", twist="Telephone game meets underground cell structure."),
      dict(name="Truth Fragment Hunt", ministry="Resistance", host="Thijs + 2 rebels",
           where="Whole venue (hidden slips)", size="Teams of 2–4 · 45 min", heat="Low",
           props="10 hidden slips with server logs, cable photos, power bills",
           play=["Teams receive a cryptic map from Thijs's room.",
                 "Slips are hidden at ministry stations (under the compost bin, in the hollow book…).",
                 "Collect at least 5 fragments to unlock the cellar story.",
                 "Fragments are presented as evidence at 23:45."],
           reward="Revolution evidence", twist="Feeds directly into the 23:45 raid script."),
      dict(name="The Turing Tribunal", ministry="Minijoy", host="Moderator + 3 'ministers'",
           where="Stage", size="Room · 10 min", heat="Low",
           props="3 chairs, script for one 'bot' minister",
           play=["Three ministers answer questions from the crowd.",
                 "One of them only reads from a printed script (the 'bot').",
                 "The crowd votes on who is the machine.",
                 "If they guess right, every resistance member present earns a truth fragment."],
           reward="Truth fragment / +20 CC", twist="The audience practises spotting the machine before the reveal."),
      dict(name="Sabotage the Ledger", ministry="Resistance", host="Self-run, rules card",
           where="Central Decree Board", size="Rebels · ongoing", heat="Low",
           props="Removable stickers, sticky notes, decoy decree slips",
           play=["Rebels try to swap one decree slip on the Central Board without being seen.",
                 "Each successful swap removes 100 CC from an agenda.",
                 "Minilove guards the board; caught rebels are sent to the Interrogation room for a 'refresher'.",
                 "A swap counts only when Thijs confirms it."],
           reward="Trash 100 CC from an agenda", twist="A simpler, always-on version of the Netrunner runs."),
    ],
  },
]

# --------------------------------------------------------------------------- BOOK I: FACILITATOR CODEX (existing content)
OPERATING = [
  ("Starting Treasury", "Each ministry begins with +800 Carbon Credits."),
  ("Recruiting Citizens", "Stamp the passport with the official Ministry Seal. Log starting debt (−150 to −500 CC) on the clipboard ledger."),
  ("Concession Operation", "Assign recruits to station shifts (+30 CC) and guard against sabotage runs."),
  ("Dual-Tally Logging", "Stamp the recruit's passport AND record the gain on the ministry ledger."),
  ("Corporate Agendas", "Pool credits to enact decrees on the Central Board (200 CC to enact)."),
]
POWERS = [
  ("Miniservice", "Debt Relief", "50% state debt relief: absorbing −400 debt burdens the ledger by only −200. Rapid dishwashing shifts."),
  ("Minirenewal", "Bounty", "+100 CC state bounty whenever a bankrupt citizen is composted through the Suicide Carbon Booth."),
  ("Minilight", "Grid Monopoly", "May plunge zones into darkness unless paid a 30–50 CC Grid Maintenance Tariff."),
  ("Miniflow", "Fluid Dividends", "+20 CC every time a citizen returns moisture at Peetopia; fines unauthorised cup spills."),
  ("Miniplenty", "Indulgences", "Controls the snack table. Sells caloric dispensations for direct credit transfers."),
  ("Minilove", "Fine Seizure", "Carries citation pads. Keeps 50% of all fines levied on heretics."),
  ("Minijoy", "Morale Grants", "Charges +10 CC entry for wig duels; +150 grant for crowd rallies of 15+ guests."),
  ("Minishelter", "Transit Tolls", "Guards corridor bottlenecks; charges 10–20 CC for cross-sector transit passes."),
  ("Minithrift", "Liquidation", "Confiscates non-organic items; liquidates contraband for +40 CC each."),
  ("Minibreath", "Offsets", "Meters exhalations; sells Breath Indulgences to dancers and runners."),
]
MOLES = [
  ("01", "Miniflow", "Whisper to Citizen Jasper at the water cooler: “The Rhine does not belong to the algorithm.”", "Slip to Thijs's room"),
  ("02", "Miniplenty", "Deliver 3 algae paste cups to the coat check: “These calories cannot sustain a soul.”", "+30 CC & “Seek the red door”"),
  ("03", "Minilight", "Pedal the bike backward for 2 minutes humming a pre-collapse melody.", "Match packet with room code"),
  ("04", "Minilove", "Find the hollow copy of Silent Spring on the 3rd shelf in the library.", "Secret knock: 3 slow, 2 fast"),
  ("05", "Minirenewal", "Tell the recycling operator: “I am Citizen Unaccounted.”", "Resistance ankle stamp"),
  ("06", "Minibreath", "Exhale into the corridor sensor for 10 s reciting: “The forest does not ask for credits.”", "Cellar cable hatch access"),
  ("07", "Minishelter", "Bribe the checkpoint guard with a synthetic trinket.", "Corridor pass to Thijs's sector"),
  ("08", "Miniservice", "Hide a clean saucer under a towel during the wash shift; carry it to the tea station.", "Duplicate ankle stamp"),
  ("09", "Minithrift", "Retrieve the USB drive labelled CELLAR_AI_BACKUP_NODE from the locker.", "Induction into strike cadre"),
  ("10", "Minijoy", "End your open-mic speech: “Joy without truth is just an electric fence.”", "Resistance makes contact"),
]
RUNS = [
  ("01", "Grid Short-Circuit", "Minilight dynamo", "2 recruits & warden", "Attach an ungrounded wire clip to the terminal during a distraction.", "Trash 100 CC from an active decree"),
  ("02", "Flow Meter Inversion", "Miniflow Peetopia", "Restroom auditor", "Invert the moisture dial without being observed.", "Truth Fragment #1 (water telemetry)"),
  ("03", "Heresy Registry Purge", "Minilove holding pen", "Cameras & officers", "Swap the citation sheet with an ink-stained decoy.", "Trash 100 CC from an active decree"),
  ("04", "Composting Vault Extraction", "Minirenewal booth", "Lab technologists", "Retrieve folder HUMUS_DELETIONS_2080 from beneath the compost vat.", "Truth Fragment #2 (AI parameter feeding)"),
  ("05", "Contraband Vault Heist", "Minithrift locker", "Contraband guard", "Pick the latch during a staged scuffle; take the fibre cable.", "Truth Fragment #3 (fibre line to the cellar)"),
]
RIVALRIES = [
  ("Miniplenty", "Dehydration Audit", "Convince 3 Miniflow citizens that dry lentils beat kombucha.", "+30"),
  ("Minilove", "Nostalgia Sting", "Catch 2 Minijoy members discussing pre-collapse holidays.", "+40"),
  ("Minijoy", "Smiling Scullery", "Make the Miniservice dish squad sing the smiling song.", "+35"),
  ("Minirenewal", "Reclaim the Confiscated", "Steal 3 items from Minithrift to compost in the vat.", "+45"),
  ("Minilight", "Blackout Guide", "Kill the lights in Minishelter; guide everyone out with glowsticks.", "+30"),
  ("Miniflow", "Moisture Seizure", "Confiscate high-water vegetables from the Miniplenty table.", "+35"),
  ("Minibreath", "Hyperventilation Fine", "Cite 3 citizens pedalling the stationary bike.", "+25"),
  ("Minishelter", "Curfew Trap", "Trap a Minilove warden inside the phone booth for 3 minutes.", "+50"),
  ("Miniservice", "Perpetual Mop", "Mop the booth exit, forcing recycled citizens to remove boots.", "+25"),
  ("Minithrift", "Tabard Audit", "Seize non-organic lanyards from Minibreath officers.", "+30"),
]

# --------------------------------------------------------------------------- HTML helpers
def plate(img, cap, height="62mm", span=False):
    cls = "plate span" if span else "plate"
    return f'<figure class="{cls}"><img src="images/bw/{img}" style="height:{height}" alt=""><figcaption>{e(cap)}</figcaption></figure>'

def sheet(title, sub, body, label=None):
    lab = f' data-label="{e(label)}"' if label else ""
    return f'<section class="sheet"{lab}><h3 class="sh">{e(title)}</h3><div class="shs">{e(sub)}</div>{body}</section>'

def dl(rows):
    return "<dl class='kv'>" + "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in rows) + "</dl>"

def game_html(n, g):
    steps = "".join(f"<li>{e(s)}</li>" for s in g["play"])
    return f"""
<article class="game">
  <header>
    <span class="gnum">{n}</span>
    <h4>{e(g['name'])}</h4>
    <span class="pick">☐ PICK</span>
  </header>
  <div class="gmeta"><span>{e(g['ministry'])}</span><span>{e(g['size'])}</span><span>Intensity: {e(g['heat'])}</span></div>
  <dl class="kv small"><dt>Host</dt><dd>{e(g['host'])}</dd><dt>Where</dt><dd>{e(g['where'])}</dd><dt>Props</dt><dd>{e(g['props'])}</dd></dl>
  <ol class="steps">{steps}</ol>
  <div class="reward">Reward · {e(g['reward'])}</div>
  <p class="twist">{e(g['twist'])}</p>
  <div class="notes">Notes:</div>
</article>"""

# --------------------------------------------------------------------------- assemble
parts = []

# Cover
parts.append(f"""
<section class="cover">
  <div class="over">Ministry of Ecological Harmony · Sanctuary De Warren</div>
  {plate("michael.jpg", "Plate I · The Guardian Stag Casts Down the Dragon of Idleness", "115mm")}
  <h1>The Codex of Labour &amp; Play</h1>
  <div class="csub">Facilitator Sheets · The Book of Games</div>
  <p class="decree">“Every task earns credit. Every silence hides a runner.<br>Every game is a sacrament, and every sacrament is a debt repaid.”</p>
  <div class="pub">For Ministers, Wardens, Hosts &amp; Facilitators only<br>Sanctuary De Warren · 28 November 2026 · Year Zero</div>
</section>""")

# Book I
b1 = []
b1.append(f"""<section class="booktitle">
  <div class="bnum">Book the First</div><h2>The Facilitator Codex</h2>
  <div class="bsub">Operating sheets for those who keep the machine running</div>
  {plate("moses.jpg", "Plate II · The Tables of the Operating Law", "140mm")}
</section>""")

flow = []
flow.append(sheet("The Facilitator's Oath", "Safety first · read before the doors open", f"""
<p class="v dc">Facilitators are the guardians of immersion and of safety. The regime is fiction; the people are real. If any player shows discomfort, the roleplay stops for them immediately and you step out of character without fuss.</p>
<div class="decree-box" data-label="Emergency Safe-Word">Saying <b>OZONE</b> halts all gameplay, roleplay and performance around that person at once and brings organiser support, without question or penalty. Every host learns this before their first shift.</div>
<ul class="rules">
<li><b>Quiet Haven:</b> the second-floor quiet room is strictly out of character.</li>
<li><b>De-escalation:</b> drop the bureaucratic tone; offer water, tea, a seat.</li>
<li><b>No touching</b> in interrogations, riot drills or arena games unless the game says so and both people agree.</li>
<li><b>Fictional sins only:</b> never ask about health, relationships, money, religion or anything a guest wouldn't say in public.</li>
<li><b>Always an easy route:</b> every intake game has the Soft Interrogation as an alternative, no explanation needed.</li>
</ul>""", "Safety"))
flow.append(sheet("Minister Operating Sheet", "Clipboard rules & economic governance",
    "<ol class='rules'>" + "".join(f"<li><b>{e(k)}:</b> {e(v)}</li>" for k, v in OPERATING) + "</ol>"
    "<p class='fine'>Ministry clipboards are audited periodically by Minilove.</p>"))
flow.append(sheet("The Ten Economic Powers", "Asymmetric minister superpowers",
    "<table class='tbl'><tr><th>Ministry</th><th>Power</th><th>Effect</th></tr>" +
    "".join(f"<tr><td class='mn'>{e(a)}</td><td><b>{e(b)}</b></td><td>{e(c)}</td></tr>" for a, b, c in POWERS) + "</table>"))
flow.append(sheet("Station Sheet I · The Suicide Carbon Booth", "Minirenewal upcycling ritual", dl([
    ("Location", "Phone booth / Upcycling Portal"), ("Host", "Renewal Technologist (lab coat)")]) + """
<ol class="steps"><li>Citizen enters with heavy debt (−350 CC or worse).</li>
<li>Review: “Are you prepared to surrender your old self?”</li>
<li>Oath: “I compost my ego; I return my nitrogen.”</li>
<li>Strike out the surname with black marker; stamp the giant “CLEANSED TO HUMUS” seal.</li>
<li>Reset debt to 0 CC; assign a new name (e.g. Citizen Lichen-88). Minirenewal logs the +100 bounty.</li></ol>"""))
flow.append(sheet("Station Sheet II · How the World Ends", "Minijoy extinction open-mic", dl([
    ("Location", "Mini-podium stage"), ("Host", "The Morale Officer (megaphone)"),
    ("Rounds", "22:00 · 22:45 · 23:15 (up to 4 contestants)"),
    ("Rules", "60 seconds to deliver the most melodramatic, operatic extinction monologue."),
    ("Judging", "Synchronised audience applause."),
    ("Reward", "+100 CC & the Order of Cathartic Hysteria ribbon. Minijoy logs the crowd subsidy.")])))
flow.append(sheet("Station Sheet III · The Wig Snatching Arena", "Minijoy", """
<p class="v">Two duellists in neon wigs. Hands start on knees. On the bell, snatch your opponent's wig without touching their body. Best of 3, 60 seconds. Winner receives a +25 CC stamp.</p>"""))
flow.append(sheet("Station Sheet IV · Greenwashing Dishes", "Miniservice", """
<p class="v">Five-minute shift. One recycled sponge, a strictly metered spray bottle (“Account for every drop”). Cleaning 10 glasses earns a +30 CC stamp.</p>"""))
flow.append(sheet("The Ten Seeded Moles", "Discreet missions slipped into 10 passports",
    "<table class='tbl'><tr><th>#</th><th>Cover</th><th>Mission</th><th>Reward</th></tr>" +
    "".join(f"<tr><td>{a}</td><td class='mn'>{e(b)}</td><td>{e(c)}</td><td>{e(d)}</td></tr>" for a, b, c, d in MOLES) + "</table>", "Secret"))
flow.append(sheet("The Rebel Runs", "Netrunner infiltration missions from Thijs's room",
    "".join(f"<div class='run'><b>Run {a} · {e(b)}</b><br><i>Target:</i> {e(c)} · <i>Ice:</i> {e(d)}<br><i>Action:</i> {e(f)}<br><i>Breach:</i> {e(g)}</div>"
            for a, b, c, d, f, g in RUNS) +
    "<p class='fine'>Climax key: the three truth fragments prove the Guardian Stag is an AI server in the cellar.</p>", "Secret"))
flow.append(sheet("Civic Rivalries", "Inter-ministry friction quests",
    "<table class='tbl'><tr><th>Ministry</th><th>Quest</th><th>CC</th></tr>" +
    "".join(f"<tr><td class='mn'>{e(a)}</td><td><b>{e(b)}:</b> {e(c)}</td><td>{e(d)}</td></tr>" for a, b, c, d in RIVALRIES) + "</table>"))
flow.append(sheet("The Revolution · Run of Show", "23:30 Assembly → 00:15 Dance", """
<div class="cue"><b>CUE 01 · 23:30 · Grand Assembly</b><br><i>Audio:</i> low sub-bass drone and bells.<br><i>Hanna (PA):</i> “Citizens of R.E.I.G.N. The hour of accounting has arrived. By decree of the Guardian Stag, all ministries assemble at the podium. Bring your passports. Bring your devotion. Prepare to be weighed.”</div>
<div class="cue"><b>CUE 02 · 23:45 · Resistance Raid</b><br><i>Visual:</i> red alarm strobes; audio stutters.<br><i>Action:</i> ankle-stamped rebels blow whistles and drop black banners: “THE STAG IS SILICON. THE DEBT IS A LIE.”<br><i>Thijs at the mic:</i> “There is no Guardian Stag! Look at the cellar! An AI server is running in the basement!”</div>
<div class="cue"><b>CUE 03 · 00:05 · Liberation Ritual</b><br>Everyone tears out Page 7 of their passport (the Ancestral Debt Bond) and throws it as confetti. Performers drop character, embrace participants and rejoice.</div>
<div class="cue"><b>00:15 · Beat Drop</b><br>The siren fades into the DJ's opening bassline. The venue becomes an open dance floor until 04:00+. Confetti is cleaned up together at 04:00.</div>""", "Script"))
b1.append('<div class="flow">' + "".join(flow) + "</div>")
parts.append("".join(b1))

# Book II
total = sum(len(c["games"]) for c in CATEGORIES)
b2 = [f"""<section class="booktitle">
  <div class="bnum">Book the Second</div><h2>The Book of Games</h2>
  <div class="bsub">{total} suggestions · more than we need · tick ☐ PICK on the ones we run</div>
  {plate("leviathan.jpg", "Plate III · The Leviathan of Leisure", "115mm")}
  <p class="decree">How to use this book: each game has a ministry, a host, props and a reward. Tick the ones we choose,
  write the owner in the Notes line, and re-run <code>scripts/build_games_codex.py</code> after editing.</p>
</section>"""]
n = 0
for c in CATEGORIES:
    games = []
    for g in c["games"]:
        n += 1
        games.append(game_html(n, g))
    b2.append(f"""<section class="cat">
  <h2 class="ch">{e(c['title'])}</h2>
  <div class="chs">{e(c['sub'])}</div>
  <div class="flow">
    {plate(c['plate'][0], c['plate'][1], "58mm")}
    <p class="v dc">{e(c['intro'])}</p>
    {''.join(games)}
  </div>
</section>""")
parts.append("".join(b2))

# Pick summary
rows = []
n = 0
for c in CATEGORIES:
    rows.append(f"<tr class='grp'><td colspan='4'>{e(c['title'])}</td></tr>")
    for g in c["games"]:
        n += 1
        rows.append(f"<tr><td>☐</td><td>{n}</td><td>{e(g['name'])}</td><td>{e(g['ministry'])}</td></tr>")
parts.append(f"""<section class="cat summary">
  <h2 class="ch">The Selection Ledger</h2>
  <div class="chs">All {total} games on one sheet · tick, assign an owner, done</div>
  <table class="tbl pickl"><tr><th>Pick</th><th>#</th><th>Game</th><th>Ministry</th></tr>{''.join(rows)}</table>
</section>""")

CSS = """
@page { size: A4; margin: 10mm 8mm 11mm;
  @top-left { content: "The Codex of Labour & Play"; font-family: 'Cinzel', serif; font-size: 6.5pt; letter-spacing: .2em; text-transform: uppercase; }
  @top-right { content: "Sanctuary De Warren · Year Zero"; font-family: 'Cinzel', serif; font-size: 6.5pt; letter-spacing: .2em; text-transform: uppercase; }
  @bottom-center { content: "✦  " counter(page) "  ✦"; font-family: 'Cinzel', serif; font-size: 8pt; }
}
@page :first { @top-left { content: none } @top-right { content: none } @bottom-center { content: none } }
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { background: #444; }
body { background: #fff; color: #000; font-family: 'Grenze Gotisch', serif; font-size: 10.2pt; line-height: 1.3;
  max-width: 210mm; margin: 0 auto; padding: 10mm 8mm; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
@media print { html { background: #fff; } body { max-width: none; padding: 0; } }
img { filter: grayscale(1) contrast(1.15); }
code { font-family: 'Cinzel', serif; font-size: .8em; }

.booktitle { break-before: page; }
.cover, .booktitle { break-after: page; text-align: center; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 255mm; }
.over, .bnum { font-family: 'Cinzel', serif; letter-spacing: .45em; text-transform: uppercase; font-size: 8pt; margin-bottom: 5mm; }
.cover h1 { font-family: 'UnifrakturMaguntia', serif; font-weight: 400; font-size: 40pt; line-height: 1.05; margin-top: 6mm; }
.booktitle h2 { font-family: 'UnifrakturMaguntia', serif; font-weight: 400; font-size: 36pt; line-height: 1.05; }
.csub, .bsub { font-family: 'Cinzel', serif; letter-spacing: .2em; text-transform: uppercase; font-size: 9pt; margin: 3mm 0 7mm; }
.decree { font-size: 12pt; max-width: 130mm; border-top: .8px solid #000; border-bottom: .8px solid #000; padding: 4mm 6mm; margin-top: 6mm; }
.pub { font-family: 'Cinzel', serif; font-size: 7.5pt; letter-spacing: .25em; text-transform: uppercase; line-height: 2; margin-top: 8mm; }
.cover .plate img, .booktitle .plate img { width: auto; max-width: 100%; }

.flow { column-count: 2; column-gap: 6mm; column-rule: .8px solid #000; }
.cat { break-before: page; }
.ch { font-family: 'UnifrakturMaguntia', serif; font-weight: 400; font-size: 26pt; text-align: center; line-height: 1.1; }
.chs { font-family: 'Cinzel', serif; font-size: 7.5pt; letter-spacing: .22em; text-transform: uppercase; text-align: center; margin: 1mm 0 4mm; padding-bottom: 2mm; border-bottom: .8px solid #000; }

.plate { margin: 0 0 3mm; text-align: center; break-inside: avoid; }
.plate img { display: block; width: 100%; object-fit: cover; border: 1.4px solid #000; outline: .6px solid #000; outline-offset: 2px; margin: 0 auto; }
.plate figcaption { font-family: 'Cinzel', serif; font-size: 6.5pt; letter-spacing: .14em; text-transform: uppercase; margin-top: 1.6mm; }
p.v { text-align: justify; hyphens: auto; margin-bottom: 2.5mm; }
.dc::first-letter { font-family: 'UnifrakturMaguntia', serif; font-size: 3.4em; float: left; line-height: .78; margin: .05em .08em 0 0; }

.sheet { break-inside: avoid-column; margin-bottom: 5mm; padding-bottom: 3mm; border-bottom: .8px solid #000; }
.sheet:has(.tbl) { break-inside: auto; }
.sh { font-family: 'UnifrakturMaguntia', serif; font-weight: 400; font-size: 15pt; line-height: 1.1; }
.shs { font-family: 'Cinzel', serif; font-size: 6.6pt; letter-spacing: .18em; text-transform: uppercase; margin: .6mm 0 2.4mm; }
.rules { padding-left: 4.5mm; margin: 2mm 0; } .rules li { margin-bottom: 1.2mm; }
.fine { font-family: 'Cinzel', serif; font-size: 6.6pt; letter-spacing: .1em; text-transform: uppercase; margin-top: 2mm; }
.decree-box { border: 1px solid #000; border-left: 4px solid #000; padding: 3mm 3.5mm 2.5mm; margin: 4mm 0 3mm; position: relative; }
.decree-box::before { content: attr(data-label); position: absolute; top: -2.3mm; left: 3mm; background: #fff; padding: 0 1.4mm; font-family: 'Cinzel', serif; font-size: 6.4pt; letter-spacing: .25em; text-transform: uppercase; }
.kv { display: grid; grid-template-columns: auto 1fr; gap: .6mm 2.5mm; margin: 1.5mm 0; }
.kv dt { font-family: 'Cinzel', serif; font-weight: 700; font-size: .72em; letter-spacing: .08em; text-transform: uppercase; padding-top: .3mm; }
.kv.small { font-size: .95em; }
.steps { padding-left: 4.8mm; margin: 1.6mm 0; } .steps li { margin-bottom: .8mm; }
.tbl { width: 100%; border-collapse: collapse; font-size: .9em; margin: 1.5mm 0; }
.tbl th { background: #000; color: #fff; font-family: 'Cinzel', serif; font-weight: 700; font-size: .68em; letter-spacing: .12em; text-transform: uppercase; padding: 1mm 1.2mm; text-align: left; }
.tbl td { border-bottom: .5px solid #000; padding: .9mm 1.2mm; vertical-align: top; }
.tbl tr { break-inside: avoid; }
.tbl td.mn { font-family: 'Cinzel', serif; font-size: .74em; font-weight: 700; letter-spacing: .04em; }
.run, .cue { border: .8px solid #000; padding: 2mm 2.5mm; margin: 2mm 0; break-inside: avoid; }

.game { break-inside: avoid; border: 1.2px solid #000; outline: .5px solid #000; outline-offset: -1.4mm; padding: 2.6mm 3mm 2.4mm; margin: 0 0 4mm; }
.game header { display: flex; align-items: baseline; gap: 2mm; border-bottom: .8px solid #000; padding-bottom: 1mm; }
.gnum { font-family: 'Cinzel', serif; font-weight: 700; font-size: 8pt; background: #000; color: #fff; padding: .3mm 1.4mm; }
.game h4 { font-family: 'UnifrakturMaguntia', serif; font-weight: 400; font-size: 13.5pt; line-height: 1.05; flex: 1; }
.pick { font-family: 'Cinzel', serif; font-weight: 700; font-size: 7pt; letter-spacing: .08em; white-space: nowrap; }
.gmeta { display: flex; flex-wrap: wrap; gap: .4mm 2.5mm; font-family: 'Cinzel', serif; font-size: 6.4pt; letter-spacing: .08em; text-transform: uppercase; margin: 1.2mm 0; }
.gmeta span + span::before { content: "· "; }
.reward { background: #000; color: #fff; font-family: 'Cinzel', serif; font-weight: 700; font-size: 7pt; letter-spacing: .08em; text-transform: uppercase; text-align: center; padding: 1mm; margin: 1.6mm 0 1.4mm; }
.twist { font-weight: 600; border-left: 1.4px solid #000; padding-left: 2mm; }
.notes { font-family: 'Cinzel', serif; font-size: 6.6pt; letter-spacing: .1em; text-transform: uppercase; border-bottom: .6px dotted #000; padding-top: 3mm; }

.pickl td:first-child { width: 7mm; font-size: 1.15em; }
.pickl td:nth-child(2) { width: 8mm; }
.pickl tr.grp td { font-family: 'UnifrakturMaguntia', serif; font-size: 1.25em; border-bottom: 1px solid #000; padding-top: 2.4mm; }
.summary .pickl { column-span: all; }
"""

page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Codex of Labour &amp; Play — Facilitator Sheets &amp; Book of Games</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=UnifrakturMaguntia&family=Cinzel:wght@400;700&family=Grenze+Gotisch:wght@400;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{''.join(parts)}
</body>
</html>
"""
OUT.write_text(page, encoding="utf-8")
print(f"wrote {OUT.name}: {total} games")
