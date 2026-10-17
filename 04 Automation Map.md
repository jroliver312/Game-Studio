# Automation Map

Oct 15, 2026 · @Jack · Draft for the Owner to confirm

*Which repetitive studio tasks get systemized, how far each is automated, in what order, and the rules that keep automation from making decisions it should not. The goal is that a new idea or a new release runs on rails, and the Owner's hours go into the game.*

## 1. Rules

1. **Rule of three (S-07).** Do it by hand once. The second time, write it down as a checklist or template. The third time, automate it. Automating something done once automates a guess.
2. **Automation drafts; the Owner decides.** No automation passes a gate, confirms a decision, publishes to players or the public, spends money, or promotes a build to the default branch (S-08).
3. **Every automation has four lines written down:** trigger, what it reads, where its output goes, and how failure is noticed. An automation that can fail silently is not done.
4. **Secrets stay out.** Steam keys, API keys and signing keys live in the password manager or on the Beelink's environment file, never in a repo, a document, a scheduled task's prompt, or a Claude Project.
5. **Measure the payoff.** Each automation records the minutes per run it saves; the monthly review picks the next one by hours saved and risk removed.

## 2. Levels

| Level | Name | What it is | Example |
| --- | --- | --- | --- |
| L0 | Manual | Done from memory | — (the state to leave) |
| L1 | Checklist / template | A written list or a file to copy | Idea card, launch checklist |
| L2 | Assistant skill | A saved Claude skill the Owner invokes ("run the weekly review") | Patch notes from commits |
| L3 | Script / CI | Code that runs on a push or a command | Tests on every push; upload build to Steam beta branch |
| L4 | Scheduled task | Runs on a schedule unattended and reports | Weekly Steam review digest |

Most tasks should stop at L1 or L2. L3 and L4 are for things that run often, are checkable, and hurt when forgotten.

## 3. Catalog

| ID | Task | Stage | How often | Target level | Notes |
| --- | --- | --- | --- | --- | --- |
| A-01 | Capture an idea | Inbox | Any time | L1 | Template in 03 §2 |
| A-02 | Pre-score ideas for triage | Inbox | Monthly | L2 | Assistant fills the 03 §3.2 draft scores with reasons |
| A-03 | Draft the weekly and monthly notes | All | Weekly | L3 → L4 | **Built 2026-10-15:** `python Automation/studio.py weekly` drafts `Studio/Reviews/YYYY-MM-DD weekly.md` from the hours log, decide-by watcher, Inbox and game pages. Monthly note still by hand |
| A-04 | Hours log and summary | All | Every session | L3 | **Built 2026-10-15:** one file, `Studio/hours.csv` (`date, game, hat, hours, note`); `studio.py log 2 Tactica Engineering "note"` appends and checks game and hat; `studio.py hours` shows this week, the 4-week average, and hats with no time |
| A-05 | Decide-by watcher | Setup, Build | Weekly | L3 → L4 | **Built 2026-10-15:** `studio.py due` reads every Markdown table in the studio folder with "Decide by" and "Status" columns — Decision Logs, the Risk Register and Idea Brief open questions alike — and lists Proposed/Open rows as overdue, due within 3 days, later, or undated. Game Decision Logs are seen once exported into the folder or a game repo's `docs/` is added |
| A-06 | New game setup | Setup | Per game | L2 | Skill that runs the procedure: Project files, document skeletons from §5 templates, Stage 1 walk-through. Per procedure §8, built **after the second game** has been set up by hand |
| A-07 | Tests on every push | Build | Every push | L3 | GitHub Actions: unit tests, determinism replay, save round-trip. Red stops new work |
| A-08 | Build and upload to Steam | Build, Live | Each release | L3 | SteamPipe (steamcmd) script: build → version stamp → upload to a **beta** branch → record the build as an Event in Olive's build register (06 §2). Promoting to default is a manual step in Steamworks (S-08) |
| A-09 | Patch notes and Steam event post | Live | Each release | L2 | Drafted from commit messages since the last tag (02 §7 prefixes); Owner edits and posts |
| A-10 | Steam review digest | Launch, Live | Weekly (daily in launch month) | L4 | Pulls public reviews from Steam's review endpoint, sorts into bug / request / praise / other, links duplicates, writes a digest; bug items feed A-11; summary feeds Olive's feedback loop (06) |
| A-11 | Bug report to issue | Live | As reported | L2 | Turns a review, email or forum post into a GitHub issue with repro steps, version, label and severity |
| A-12 | Sales and wishlists into Olive | Launch, Live | Weekly / monthly | L3 | From Steamworks reports into Olive's game entity. Method decided once the Steamworks account exists; the reporting key lives only on the Beelink |
| A-13 | Discount and price calendar check | Live | Before each sale | L3 | Checks a planned sale against Steam's rules (05 §1): 30 days after release, 30 days between discounts, 30 days after a price increase; seasonal sales are exempt from the between-discounts rule only, not from the release or price-increase cooldowns |
| A-14 | Devlog and social drafts | Build, Launch | Fortnightly | L2 | Drafted from the build log and screenshots; Owner edits and posts. No auto-posting |
| A-15 | Licensing re-check | All | Quarterly | L4 | Re-reads every source in each game's Data and Licensing Register for licence changes; reports differences only |
| A-16 | Export docs into the repo | Setup onward | Each Confirmed change | L3 | Claude Docs → Markdown in the game repo's `docs/` (procedure Gate A) |
| A-17 | Post-mortem draft | Post-mortem | Per launch, per sunset | L2 | Drafted from the Decision Log, hours log, build log, review digests and Strategy Tests results; Owner writes the judgments |
| A-18 | Store page asset check | Launch | Per game, per update | L1 | Capsule sizes, screenshots, trailer, descriptions, tags; checked against Steamworks' current graphical asset rules when the page is built |
| A-19 | Launch checklist | Launch | Per game | L1 | 05 §4 as a copyable checklist |
| A-20 | Backup watch | All | Daily | L3 / L4 | Repos pushed in the last 7 days; studio folder backed up; alert by the same ntfy channel Olive already uses |
| A-21 | Press and creator keys | Launch, Live | Per request | L1 | Requests logged in Olive's key register (recipient, batch, purpose, embargo, outcome); keys themselves stay in Steamworks |
| A-22 | Idea Brief to engineering seed pack | Setup | Per promoted idea | L2 | The onboarding skill writes `Games/<Game>/seed/` (TDD proposals, spikes, P1 backlog CSV, data sources) from the brief (11 §9). Everything Proposed |
| A-23 | Seed backlog to GitHub issues | Setup, Build | Per game, then as the backlog grows | L3 | **Built 2026-10-15:** `studio.py backlog <Game>` checks the CSV (unique ids, types, acceptance present, dependencies exist, estimates well-formed) and totals the unmeasured estimate; `--apply --repo OWNER/NAME` creates labelled issues through the GitHub CLI and writes each URL back |
| A-24 | Lunch mode | Inbox | Per idea | L2 | The onboarding skill takes an 8-question phone Round 1, then unattended: Round 1 research and playback, a drafted Round 2, systems map, licence checks, size estimate, draft seed pack, and a "Waiting for you" list (11 §10) |
| A-25 | Prototype run | Inbox, Setup/Test, Build | Per question | L2 (or L4 when scheduled) | `game-prototype-run` skill: questions with pass lines → one-file HTML/JS throwaway with seeded RNG and debug panel → headless harness over N seeds → browser check and screenshots → private playable artifact + report (12) |
| A-26 | Session retro and briefing | All | Every working session | L2 | `studio-learning` skill: at session start, reads Standing Lessons and calibration and flags the ones that apply; at session end, drafts the five-line retro and raises lesson candidates into the Lessons Register (13 §2–3) |
| A-27 | Predictions and calibration | All | When estimating; weekly | L3 | **Built 2026-10-15:** `studio.py predict` / `actual` / `calibration [--write]` — median actual÷predicted per kind, a correction factor once 5 are closed, backlog estimates vs hours logged with `[F-03]`-style notes; written into Standing Lessons and the weekly note (13 §4) |
| A-28 | UTM link builder | Market phases | Every outside link | L3 | **Built 2026-10-15:** `studio.py link <Game> <appid> <source> <campaign> [content]` builds a Steam UTM link, validates the names and records it in `Studio/Marketing/links.csv` (14 M-13). **From 2026-10-16 (S-41):** new links come from Marketing Dept's `agency.py link`, recorded in its `Agency/links.csv` with utm_medium added; `studio.py link` still works but is no longer the register |
| A-29 | Festival and event watch | Market phases | Monthly | L4 | Scheduled check of Steam's Upcoming Events page and `Studio/Marketing/Festival Calendar.md`; lists new events and deadlines in the next 60 days (14 M-7). Not yet scheduled. **From 2026-10-16:** `agency.py calendar` reads this festival calendar beside every client's beats (deadlines 60 days ahead); the scheduled check of Steam's page itself is still to do |
| A-30 | Creator and curator list research | P2 onward | Per beat | L2 | Assistant builds the target list (YouTube 10k–500k, Twitch 50–2,000 average viewers, genre curators, played the comparables recently) and drafts the top-20 notes; Owner sends (14 M-5) |
| A-31 | Beat kit and beat report | Market phases | Per beat | L2 | From `Templates/Beat Plan.md`: Assistant drafts every asset text and the channel table at B−14, and the B+7 report with UTM sources and the prediction closed (14 M-3). **From 2026-10-16:** Marketing Dept's `Templates/Beat Plan.md` and `agency.py beat add / predict / actual / decide` (06 K-5 to K-8) |
| A-32 | Channel map research | Position, P2 | Per game; refreshed per beat | L2 | Assistant finds and sizes candidate communities, creators and publications (dated, confirmed to exist) and drafts scores; Owner reads each community's rules before posting (15 C-2 to C-4) |
| A-33 | Home-channel rules re-check | Market phases | Every six months | L4 | Reminder to re-read the rules pages of each home channel and update the channel map (15 §4 rule 5). Not yet scheduled |
| A-34 | Studio Board | All | On request; weekly with the review | L3 + L2 | **Built 2026-10-15:** `studio.py dashboard` writes nine JSON files to `Studio/Dashboard/` (summary, portfolio, decisions, hours by week, calibration, open predictions, lessons, inbox, upcoming events). The "Studio Board" dashboard in claude.ai shows them; to refresh, ask Claude to "refresh the Studio Board" (runs the export, re-uploads the files, updates each source's date). Sources go stale after 8 days |
| A-35 | Existing game audit | Any game built before the procedures | Once per game | L2 | `game-audit` skill: inventory, reconstructed Idea Brief and v0 documents with Confirmed / Evidence / Inferred / Unknown labels, milestone placement, risk scan, seed pack to 1.0, market setup, report with "Waiting for you" (16) |

## 4. What stays manual on purpose

- Every gate, every Decision Log status, every price and discount decision.
- Promoting a build to the default branch.
- Anything posted publicly under the studio's name, and any reply to a player.
- Choosing the next idea.
- The judgment half of a post-mortem.

## 5. Build order — Proposed

Picked by hours saved and risk removed. Revisited monthly.

| Order | Item | Why first | Rough effort |
| --- | --- | --- | --- |
| 1 | A-04 hours log + A-03 weekly note (L2) | Measured hours drive every calendar; the weekly review is what keeps the studio honest | 1–2 hours |
| 2 | A-05 decide-by watcher | Sovereign already has 7 Proposed rows; stale proposals are the procedure's commonest failure | 1–2 hours |
| 3 | A-07 tests on every push | Protects the foundation before more is built on it | 2–4 hours per repo |
| 4 | A-08 Steam upload to beta | First needed for the first Steam build; easy to get wrong by hand | 2–3 hours once the Steamworks app exists |
| 5 | A-10 review digest | Needed from launch day; feeds bug fixing and Olive | 2–3 hours |
| Later | A-06 new-game setup skill | After the second game is set up by hand (procedure §8) | — |

## 6. Where automation runs

| Kind | Runs on | Notes |
| --- | --- | --- |
| L2 skills | Claude, in the studio or game Project | Saved as skills; the Owner invokes them |
| L3 CI | GitHub Actions | Free tier is enough for private repos at this size; confirm minutes when set up |
| L3 local scripts | The Owner's own machines (the Beelink or the game machine) | Never a Thunderbuilt machine (07 §R-01) |
| L4 scheduled tasks | Claude scheduled tasks; local ones only when they need files on the Owner's machine | Each one's output goes to `Studio\Reviews\` or the game's issue tracker |

## 7. Changing this document

New automations are added as new rows (next free A- number). An automation that is retired keeps its row with "Retired" and the date. Sections are appended, never renumbered.
