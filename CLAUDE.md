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

## End every session
A five-line retro (`13 Learning System.md` §2) saved to `Studio/Learning/Sessions/`, then commit and push.

## Never commit
Secrets, keys, passwords, Steam keys, or anything from `.env`. `Studio/Dashboard/` is generated and ignored.
