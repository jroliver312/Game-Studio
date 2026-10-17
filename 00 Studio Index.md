# Studio Index

Oct 15, 2026 · @Jack

*The front page of the studio's records: what each document is for, its state, the order to read and confirm them, and what is still to write. The Assistant keeps this current.*

**Studio Board:** the pinned dashboard in claude.ai ("Studio Board") shows games, decisions due, hours, lessons, calibration and upcoming events, built from `studio.py dashboard` (04 A-34).

## 1. The studio set

| # | Document | Answers | State |
| --- | --- | --- | --- |
| 00 | Studio Index | Where is everything? | Current |
| 01 | Studio Charter | What is the studio, why does it exist, what does success look like? | Draft — purpose and success numbers await the Owner (S-12, S-13) |
| 02 | Operating Model | Who does what, the life of a game, WIP limits, rhythm, capacity, where records live | Draft — S-05, S-15, S-17 |
| 03 | Idea Pipeline and Portfolio | How ideas are captured, cooled, scored and promoted; where each game stands | Draft — S-06, S-19 |
| 04 | Automation Map | What gets systemized, how far, in what order | Draft — S-07, S-08 |
| 05 | Launch and Live Ops Playbook | From Gate B to launch to sunset, on Steam's rules | Draft — Steam rules read 15 Oct 2026 |
| 06 | Olive Boundary | What Olive does for the studio and what it doesn't | Draft — restates decisions already made in Olive |
| 07 | Risk and Legal Register | What could hurt the studio and what is done about it | Draft — R-01, R-02, R-04 need action before any store page |
| 08 | Studio Decision Log | Every studio decision and its status | 41 rows (S-41 added 2026-10-16 by the agency): 5 Confirmed, 30 Proposed, 5 Open; first review logged |
| 09 | Accounts and Assets Register | Every account and asset, how it is protected and recovered | Template — to fill |
| 10 | Production Playbook | From Gate B to a finished, successful game: the three tracks, every studio job, milestones P1–P5, Sovereign's route, lessons from other studios | Draft — S-24 to S-30 |
| 11 | Idea Onboarding Survey | Three rounds of questions (Spark, Shape, Course) that turn a new idea into an Idea Brief, then an engineering seed pack; lunch mode for capturing on the phone (§10) | Draft — S-31 to S-33 |
| 12 | Prototype Runs | Unattended throwaway prototypes that answer named questions with pass/fail; playable on the phone | Draft — S-34 |
| 13 | Learning System | Retros, lessons, predictions and calibration — how each session and each game gets better than the last | Draft — S-35; register seeded with 7 real lessons |
| 14 | Marketing and Sales Playbook | Pointers only since 2026-10-16: the method moved to Marketing Dept's 06 Marketing Method (K-1 to K-9, Games playbook G-1 to G-8) | Moved — S-41; Tactica's next steps (§6) until the agency's campaign plan replaces them |
| 15 | Audience and Channels | Each game's audience research — Tactica (§6, FM27 window) and Sovereign (§7); the procedure moved to Marketing Dept 06 K-1 to K-3, K-8 | Research current; procedure moved — S-41 |
| 16 | Existing Game Audit | Bringing a game that already exists in code onto the route: reconstruct its documents (labelled), place it on P1–P5, find risks, build the work list to 1.0 | Draft — S-40; Tactica first |
| — | Research: Solo studio route to launch | The sourced research behind 10 | Report, 15 Oct 2026, `Research/` |
| — | New Game Setup Procedure | How one idea becomes a tested foundation | Written 15 Oct 2026 from Sovereign — S-14 |

## 2. How the pieces fit

```
                    01 Charter  (why, what, success)
                         │
        ┌────────────────┼──────────────────┐
   03 Pipeline      02 Operating Model    07 Risk / 09 Accounts
   (which idea)     (how the week runs)   (what could break)
        │                │
        ▼                ▼
 New Game Setup  ──►  Build  ──►  05 Launch & Live Ops
   Procedure          (game repo)        │
                                         ▼
                         06 Olive  (money, sales, keys, feedback)

   04 Automation Map runs under all of it.   08 Decision Log records all of it.
```

## 3. Order of work for the Owner

1. **Read 01 and rewrite §2 in your own words.** Then confirm or change S-12.
2. **Go down 08 and set a status on every Proposed row** dated 2026-10-29. Each takes a minute; the reasons are in the row.
3. **This week, outside the documents:** check Tactica is in a repository with a remote (R-12); find the Thunderbuilt agreement (R-01).
4. **Before any store page:** S-01 name, run the trademark search on "Tactica" (R-04), S-10 agreement read, S-11 entity decision, S-18 the two professional hours.
5. **Start logging hours** every session: `python Automation/studio.py log 2 Tactica Engineering "what you did"`. On review day, `python Automation/studio.py weekly` drafts the note. Fill the blanks on `Games/Tactica/README.md` (machine, repo, Project).
6. **Fill 09** within a month, including §4 (if Jack is unavailable).

## 4. Still to write, and when

| Document | Write when | Why it matters |
| --- | --- | --- |
| Studio brand and press kit (name, logo, one-paragraph bio, screenshots folder, fact sheet) | After S-01 | Every store page, festival and press email reuses it |
| Studio website and mailing list plan | After S-01 | The one audience channel the studio owns (07 R-10) |
| Contractor agreement template (work for hire / assignment of rights) | Before paying anyone for art, music or code | Without a written assignment, the contractor owns what they made |
| Community and support policy (where players report bugs, reply times, code of conduct) | Before the first demo | Expands 05 §6 into a public page |
| Studio repository and backup of `C:\Game Studio` | Repository created 2026-10-17 (jroliver312/Game-Studio); done once the first push lands | Until then the studio's records exist on one machine and in the Project only (07 R-09) |
| Per-game platform decisions: languages, Steam Deck, accessibility | L−7 months for each game (05 §4) | They change the store page and the scope |
| Studio annual review | Each January | The charter's success measures, year over year |
| Studio post-mortem rollup | After the second launch | What held across games; feeds the charter and the procedure |

## 5. Housekeeping

- The Claude Project "Game Studio Entity" holds copies of this set; the folder is the working copy until a studio repository exists.
- The procedure's §8 says it belongs in the studio's own Project and repository and is linked from every game Project on day one — this set follows the same rule.

## 6. The working folders (built 2026-10-15, S-23)

| Folder | Holds |
| --- | --- |
| `Templates/` | Idea Card, Idea Brief, Seed Pack (TDD proposals, spikes, backlog CSV, data sources), Prototype Report, Beat Plan, Channel Map, Audit Report, Weekly Note, Launch Checklist, Post-mortem |
| `Inbox/` | One idea card per file, `YYYY-MM-DD title.md` |
| `Shelf/`, `Shelf/Killed/` | Shelved and killed ideas, with the reason |
| `Games/<Game>/README.md` | One page per game: stage, machine, repo, Project, what's owed |
| `Studio/hours.csv` | The hours log (A-04) |
| `Studio/Reviews/` | Weekly, monthly and quarterly notes |
| `Studio/Dashboard/` | The Studio Board's data files, rebuilt by `studio.py dashboard` |
| `Studio/Marketing/` | Festival Calendar (Steam events seeded), links.csv (UTM link register) |
| `Studio/Learning/` | Lessons Register, Standing Lessons (read by every skill), predictions.csv, Sessions/ retros |
| `Automation/` | `studio.py` (log, hours, due, inbox, weekly, backlog, predict, actual, calibration, link, dashboard) and `config.json` (hours budget, cooling-off days) |
