# Existing Game Audit

Oct 15, 2026 · @Jack · Draft for the Owner to confirm (S-40)

*How a game that already exists in code — built before the studio's procedures, or brought in from elsewhere — is brought onto the studio's route. It is the onboarding survey run backwards: instead of questions → documents → code, it reads the game and reconstructs the documents, places the game on the milestone route, finds the risks, and produces the work list to 1.0. Tactica is the first game it is for (S-20).*

## 1. Principles

1. **Read before writing.** The inventory (A-1) changes nothing in the game's files.
2. **Every reconstructed line carries a label** (§3). The audit may assume from context, but it says it is assuming, how confident it is, and why.
3. **Never infer commitments or law.** Hours, money, dates, price, entity and legal facts are left blank for the Owner.
4. **Reconstructed documents are v0.** They become the game's real documents only when the Owner has confirmed or corrected them; the corrections are recorded, not silently applied.
5. **Find the expensive surprises first.** A question that would be costly to discover late (how the game reaches Steam, save compatibility, licensing, the name) goes to the top of the report.

## 2. The steps

| # | Step | Reads | Produces | Time |
| --- | --- | --- | --- | --- |
| A-1 | **Inventory** (read-only) | The repository or folder: code, data files, name lists, libraries, fonts, sounds, saves, version history, any existing docs or post-mortems | Inventory table: what exists, size, where, last changed | ~30 min |
| A-2 | **Reconstruct the Idea Brief** | The game's screens, systems and data, plus earlier notes | The Idea Brief (11) answered from evidence; every answer labelled; unanswerable ones on the "Waiting for you" list | ~1 h |
| A-3 | **Place it on the route** | The code, against each exit line of P1–P5 (10 §3) | A milestone table with yes / no / partly and the evidence for each line; the stage the game is really at | ~45 min |
| A-4 | **Reconstruct the documents** | A-1 to A-3 | v0 of: Design Document (with systems map), Technical Design (as built, risky parts as proposals), Data and Licensing Register, Scope Ledger (1.0 vs later, cut order), Competitive Analysis seed | ~2 h |
| A-5 | **Risk scan** | Everything above | Risks added to the game's log and the studio register (07): name, real names in data, licences, single-copy code, performance, saves across versions, platform packaging | ~30 min |
| A-6 | **Seed pack from reality** | The gap between where the game is and 1.0 | `Games/<Game>/seed/`: spikes for the unknowns, a backlog to 1.0 with done-lines and estimates, data sources; every estimate logged as a prediction (13 §4) | ~1 h |
| A-7 | **Market setup** | Positioning (14 M-1), the channel map (15) | Positioning draft, channel map updated, store-page plan with dates | ~30 min |
| A-8 | **Report and confirm** | All of it | The Audit Report (`Templates/Audit Report.md`) with the "Waiting for you" list first; Decision Log rows for every inferred item; game page and Studio Board updated | Owner: ~45 min to review |

About one to two Assistant sessions, plus one Owner sitting to confirm.

## 3. Labels on every reconstructed line

| Label | Meaning | Rule |
| --- | --- | --- |
| **Confirmed** | The Owner said it | Quote or cite where he said it |
| **Evidence** | Seen in the game or its data | Give the location (file, function or line, screen) |
| **Inferred** | Reasoned from context | Give a confidence (High / Medium / Low) and the reason in one line; goes to the Decision Log as Proposed with a decide-by date |
| *Unknown* | Not determinable | Left blank and listed as an open question |

Inferred items with **Low** confidence are listed in "Waiting for you"; Medium and High ones are confirmed in bulk unless the Owner objects to a specific line.

## 4. What the audit looks for (checklist)

**Foundations**
- [ ] Code in a repository with a remote; pushed recently (R-12)
- [ ] Same seed gives the same result (determinism)
- [ ] Saves carry a version and old saves load (migration)
- [ ] Stable ids for entities (players, clubs, leagues)
- [ ] Data separate from code (moddable, translatable)
- [ ] Text separate from code (localization)
- [ ] Automated tests exist and run

**Platform**
- [ ] How the game reaches Steam (a web game needs a desktop wrapper; Steam features such as cloud saves and achievements need its SDK)
- [ ] Performance at Steam Deck size and power; controller navigation; text readable at 1280×800
- [ ] Offline play; no network calls

**Content and legal**
- [ ] Every library, font, sound and data source has a known licence
- [ ] No real people, clubs, crests, leagues or competitions by name; generated names checked against real ones
- [ ] The game's name cleared (07 R-03, R-04)
- [ ] AI-generated content that ships is known and disclosable (R-15)

**Design and scope**
- [ ] The core loop and the 3–5 repeated decisions are clear in the game
- [ ] Systems map: each system's inputs and outputs
- [ ] Onboarding: can a new player understand the first 10 minutes
- [ ] Feature list split into 1.0 and later; work in progress named
- [ ] Balance: a headless run of many seeded seasons shows nothing happening far too often or too rarely

**Market**
- [ ] The hook, comparables, tags; the screenshot that sells it
- [ ] The timing window (15 §6 for Tactica)

## 5. The headless season harness (the audit's biggest accelerator)

For a simulation that already exists, the most valuable thing the audit can set up is a harness around the game's **real** engine: run hundreds or thousands of seeded seasons without the interface and report what happened — goals per game, home advantage, promotion and relegation churn, transfer prices, player growth, club finances, how often each event fires. It turns balance work from hours of play into an overnight run, and seeded replays become regression tests so a new version can't silently change how the game plays. The audit scopes it (spike S-01 or S-02 in the seed pack); building it is the first backlog item if the code allows the engine to run headless.

## 6. Access

The audit needs to read the game's code: either a session linked to the computer where the game lives (with its folder connected), or the game pushed to a private GitHub repository the session can open. The second also closes the single-copy risk (R-12).

## 7. Changing this document

By Decision Log row. After each audit, note which checklist items found real problems and which never did. Sections are appended, never renumbered.
