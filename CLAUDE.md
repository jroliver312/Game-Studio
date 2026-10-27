# Game Studio — instructions for Claude sessions

This repository is Jack's game studio: the documents that define how the studio runs, its templates, its records and its tooling. Game code does **not** live here; each game has its own repository (Tactica is on another computer — see `Games/Tactica/README.md`).

## Start every session
1. Read `00 Studio Index.md` (what each document is for) and `Studio/Learning/Standing Lessons.md` (lessons and calibration factors). Say in one line which lessons apply to today's task, if any.
2. For a game, read its page in `Games/<Game>/README.md`.

## Conventions
- Jack (the Owner) decides; Claude drafts. New choices go in `08 Studio Decision Log.md` as **Proposed** with a decide-by date (YYYY-MM-DD). Never set a row to Confirmed on Jack's behalf.
- Sections are appended, never renumbered; other documents cite them by number.
- Every figure carries a date and a source; anything assumed is labelled (Confirmed / Evidence / Inferred / Unknown — `16 Existing Game Audit.md` §3).
- Nothing is published, posted, sent or paid for without Jack.
- Marketing work now lives in the agency (see `14` and `15` for the pointers).

## Tooling
`python Automation/studio.py <command>` — `log`, `hours`, `due`, `inbox`, `weekly`, `backlog`, `predict`, `actual`, `calibration`, `link`, `dashboard`. Run from the repository root.

## Studio map

The studio's skills (game-idea-onboarding, game-prototype-run, game-audit, studio-learning) are
written generally in the Workshop and name these places and rules; this is where they are for this
studio. This section goes in `C:\Game Studio\CLAUDE.md` and in the Game Studio Entity Project's
instructions.

| Place | Where |
| --- | --- |
| studio folder | `C:\Game Studio` |
| studio Project | the "Game Studio Entity" Claude Project: documents in `studio/`, learning copies in `studio/learning/`, Idea Briefs in `ideas/`, reports in `games/<Game>/` |
| documents | in the studio folder: `01` charter (§3–4 is the fit check), `03` triage, `10` milestone route (§3 exit lines P1–P5), `11 Idea Onboarding Survey.md` (§9 seed pack, §10 lunch mode), `12 Prototype Runs.md`, `13 Learning System.md`, `14` and `15` marketing (now pointers: the method moved to the agency, `C:\Projects\Marketing Dept\06 Marketing Method.md`; a game's positioning is the agency's `Clients\Game Studio\<Game>\positioning.md`, 06 K-4; its channel map stays in `Games\<Game>\marketing\channel-map.md`), `16 Existing Game Audit.md` (§2 steps, §3 labels, §4 risk checklist, §5 season harness) |
| templates folder | `C:\Game Studio\Templates\`: `Idea Brief.md`, `Seed Pack\`, `Prototype Report.md`, `Audit Report.md` |
| learning folder | `C:\Game Studio\Studio\Learning\`: `Standing Lessons.md`, `Lessons Register.md`, `predictions.csv`, `Sessions\` |
| ideas inbox | `C:\Game Studio\Inbox\` (inbox prototypes in `Inbox\prototypes\<idea>\`, draft seed packs in `Inbox\seed\<title>\`) |
| games folder | `C:\Game Studio\Games\<Game>\` (Tactica, Sovereign, and each promoted idea) |
| studio's board | the "Studio Board" dashboard, fed by `studio.py dashboard` (`Studio/Dashboard/`, generated, never committed) |
| studio script | `python Automation/studio.py <command>`, run in the studio folder; backlog push: `backlog <Game> --apply --repo OWNER/NAME` (Jack's call) |

### The studio's rules the skills read here

- Charter, in short: premium single-player, complete at launch, original IP, fictional names; no
  loot boxes or required studio servers.
- Known patterns from the studio's research: era × region (or any combinatorial content) multiplies
  scope; Early Access rarely pays off; political themes face ad-platform blocks; real places invite
  accuracy disputes; simulation games prove connected systems (P1) before any polished slice.
- Store: Steam (nearest games, tags, title check, Steam Deck target, the Steam SDK path for a web
  game). Milestone names: P1 is the connected-systems playable; Gate B ends the seed pack's
  Proposed status.
- Lessons the skills used as examples: L-002 (check outside terms against the studio's names) and
  L-004 (licence-check the data in Round 2).
- The 30-day cooling-off and the monthly triage (`03`) apply to every idea.
- Audit step A-2, as the old skill put it: "answer the 11 Onboarding Survey questions".
- Hour notes: `studio.py log <hours> <Game> <area> "[<id>] <note>"`, e.g. `log 2 Sovereign Engineering "[F-03] economy prices"`.

## End every session
A five-line retro (`13 Learning System.md` §2) saved to `Studio/Learning/Sessions/`, then commit and push.

## Never commit
Secrets, keys, passwords, Steam keys, or anything from `.env`. `Studio/Dashboard/` is generated and ignored.
