# Idea Onboarding Survey

Oct 15, 2026 · @Jack · Draft for the Owner to confirm (S-31)

*The questions every new game idea is put through, in three rounds, so a development plan points in the right direction from the start. Each round sharpens the idea; between rounds the Assistant plays back what it heard, proposes the strongest version, and names what is still unclear, so the next round asks better questions. The output is an **Idea Brief** that becomes the starting draft for the New Game Setup Procedure's Stage 1 and seeds its Stage 2–3 documents.*

## 1. Why three rounds

| Round | Name | Settles | When | Time |
| --- | --- | --- | --- | --- |
| 1 | **The Spark** | *What* the game is and *why* it should exist | When the idea is introduced | ~20 minutes |
| 2 | **The Shape** | *How* it plays, looks, is built and what 1.0 contains | Straight after Round 1's playback, or within a week | ~40 minutes |
| 3 | **The Course** | *How we'll know*: riskiest assumption, the test, the resources, what success means, what gets cut first | At promotion out of the Inbox (03 §3) — or straight after Round 2 if the Owner wants the full brief now | ~30 minutes |

Rounds 1 and 2 cost little and give the 30-day cooling-off something solid to cool. Round 3 asks for commitments (hours, money, a kill-by date), which only make sense when the idea is actually getting a slot. If Round 3 runs early, its commitments are re-confirmed at promotion.

## 2. Rules for running it

1. **One round at a time.** Never ask Round 2 questions before Round 1's playback has been corrected.
2. **Don't re-ask.** Skip any question the Owner's earlier answers already cover; say "taking X as answered by Y".
3. **"Don't know" is a good answer.** It becomes an open question in the brief, never a guess dressed as an answer.
4. **Multiple choice where it speeds things up**, free text where the answer is the idea itself. Every multiple-choice question allows a custom answer.
5. **Tailor every round.** Each round has fixed core questions (§3–5) plus up to five follow-ups the Assistant writes from the previous playback, aimed at the biggest unknowns and contradictions.
6. **Playback after every round** (§6): what I heard, the sharpest version, contradictions, red flags, open questions. The Owner corrects it before the next round.
7. **The Assistant never decides.** It proposes pillars, a one-liner and scope splits; the Owner picks. Proposals stay marked Proposed in the brief.
8. **Look things up where it's cheap.** After Round 1, a quick look at the nearest games (price, reviews, release date, dated). After Round 2, a quick look at any data source or licence the idea depends on. Full research waits for Stage 2.
9. **Charter check every round.** Anything outside 01 §3 or inside 01 §4 is flagged immediately, not at the end.
10. **Answers are the Owner's words.** The brief quotes them; the Assistant's sharpening sits beside them, labelled.

## 3. Round 1 — The Spark

*Goal: a one-liner a stranger could repeat, the fantasy, who it's for, and whether it fits the studio.*

| # | Question | Format | Feeds |
| --- | --- | --- | --- |
| 1.1 | Describe the game in one or two sentences, however rough. | Free text | Pitch |
| 1.2 | What does the player get to **be** or **do** that they can't anywhere else? | Free text | Pitch, pillars |
| 1.3 | Where did the idea come from — a game you played, something you read, a problem you noticed, something you know well? | Free text | Why me |
| 1.4 | Genre, closest fit. | Choice: management / strategy / simulation / sports management / city or colony builder / narrative / tactics / other | Market, triage |
| 1.5 | Name up to three games it's closest to, and what each one gets wrong or leaves out. | Free text | Competitive Analysis seed |
| 1.6 | Who is the player? Pick the nearest, then say more. | Choice: deep-sim veteran / strategy fan who wants approachable / sports fan / history or politics enthusiast / casual-cozy / other | Target player |
| 1.7 | One sitting lasts about… | Choice: under 30 min / 30–90 min / 2+ hours / "one more turn" with no natural end | Session length |
| 1.8 | A full playthrough or campaign lasts about… | Choice: a few hours / 10–30 hours / 50+ hours / endless sandbox | Campaign length, content scope |
| 1.9 | Three words for how it should **feel**. | Free text | Pillars, art and audio direction |
| 1.10 | Setting: | Choice: fictional world / real places, present day / real places, historical / abstract, no setting | Licensing, sensitivity |
| 1.11 | Does it touch real people, real organizations, politics, religion, war, crime or other hard subjects? Which? | Free text | Risk register, rating, ad channels |
| 1.12 | Why are **you** the right person to make this? What do you already know or have built? | Free text | Why me, reuse |
| 1.13 | Size, gut feeling. | Choice: S (≤ 6 months part-time) / M (6–18) / L (18+) | Triage |
| 1.14 | Excitement right now, 1–5, and what excites you most. | Number + text | Triage |
| 1.15 | Anything it **must** have, or must never have? | Free text | Pillars, charter check |

**Assistant work before playback:** a quick dated look at the three named games (price, review score and count, release date); a charter check (01 §3–4); draft pillars.

## 4. Round 2 — The Shape

*Goal: how it plays, what it's made of, how it's built and presented, and what 1.0 is versus later. Questions marked (sim) are asked for systems-driven games; the Assistant drops what doesn't apply.*

### 4.1 Play

| # | Question | Format | Feeds |
| --- | --- | --- | --- |
| 2.1 | Walk through the first 10 minutes as a new player. | Free text | Onboarding, core loop |
| 2.2 | What are the 3–5 decisions the player makes over and over? | Free text | GDD §2 core choices |
| 2.3 | The loop at three scales: one moment, one session, one campaign. | Free text | GDD §3 |
| 2.4 | How does the player lose, and how do they win (or is there no win)? | Free text | GDD §3 |
| 2.5 | (sim) List the main systems. For each: what feeds into it, what it feeds out to. Rough is fine. | Free text / table | GDD §4, P1 connected-systems playable |
| 2.6 | Where do surprises come from: other systems, randomness, AI opponents, scripted events, the player's own mistakes? | Choice, multi | Design, determinism |
| 2.7 | Content: mostly handmade, mostly generated from rules or data, or both? What does one "unit" of content contain? | Choice + text | GDD §6–7, scope |
| 2.8 | Difficulty and depth: how does it teach itself, and how does it stay interesting at hour 50? | Free text | Onboarding, longevity |
| 2.9 | Progression or meta-progression between runs? | Choice: none / unlocks / persistent world / career | GDD §3 |

### 4.2 Presentation

| # | Question | Format | Feeds |
| --- | --- | --- | --- |
| 2.10 | Visual style. | Choice: 2D map and UI-led / 2D illustrated / 3D / text and UI only / other; plus one reference image or game | Art direction, cost |
| 2.11 | Who makes the art? | Choice: me / bought (which parts) / generated from data / mix | Budget, AI disclosure |
| 2.12 | Audio and music: | Choice: licensed library / commissioned / minimal | Budget |
| 2.13 | Main input: | Choice: mouse and keyboard / controller-first / both equally | UI, Steam Deck |
| 2.14 | Steam Deck target: | Choice: Verified is a goal / Playable is enough / not a target | Engineering, store page |
| 2.15 | Languages at 1.0, and later. | Free text | Localization budget, text externalization |
| 2.16 | Accessibility must-haves (remapping, text size, colour-blind safe, no time pressure…). | Choice, multi | UI, accessibility |

### 4.3 Build

| # | Question | Format | Feeds |
| --- | --- | --- | --- |
| 2.17 | Engine or stack, and why. | Choice: existing studio stack / Godot / Unity / custom / single-file web / other | TDD |
| 2.18 | What can be reused from Tactica, Sovereign or other projects (code, data, tools)? | Free text | TDD, estimate |
| 2.19 | (sim) Must runs be reproducible from a seed (replays, testing, sharing)? | Yes / no / don't know | TDD determinism |
| 2.20 | Save expectations: | Choice: anywhere / checkpoints / ironman option / one long save | TDD saves |
| 2.21 | Modding: | Choice: none / data files players can edit / full Workshop support from day one | TDD data formats, long tail |
| 2.22 | Outside data it depends on (maps, names, statistics, historical records) and where it would come from. | Free text | Licensing Register |
| 2.23 | Online features? (The charter rules out games that need studio servers.) | Choice: none / optional leaderboards or sharing / required | Charter check |

### 4.4 Scope and business shape

| # | Question | Format | Feeds |
| --- | --- | --- | --- |
| 2.24 | What **must** be in 1.0? What can wait for updates or DLC? | Free text, two lists | Scope Ledger |
| 2.25 | Price you imagine, and why. | Choice: under $10 / $10–15 / $15–20 / $20–25 / $25+ | CA, positioning |
| 2.26 | Release model: | Choice: complete at launch / Early Access / don't know | Strategy (10 §6: EA rarely pays off) |
| 2.27 | Life after launch: | Choice, multi: patches only / free updates / paid DLC / expansions / ports / sequel | Live ops, Olive |

**Assistant work before playback:** a systems map (boxes and arrows) if 2.5 was answered; a 1.0-versus-later split; a check of any data source from 2.22 against its licence page (dated); a rough size in hours, given as a range and labelled an estimate.

## 5. Round 3 — The Course

*Goal: the assumption that would kill it, the cheapest test of it, the resources it gets, what success means, and the first milestone. This round fills the procedure's Stage 1 resources block.*

| # | Question | Format | Feeds |
| --- | --- | --- | --- |
| 3.1 | Here are the three riskiest assumptions from the brief (Assistant proposes). Which one, if wrong, kills the game? | Choice + text | Strategy Tests §2 |
| 3.2 | What is the cheapest test of that assumption — paper prototype, spreadsheet model, a pitch shown to strangers, a one-week spike? | Choice + text | Strategy Tests §4 |
| 3.3 | What result would make you stop? Put a number on it if you can. | Free text | Kill criteria |
| 3.4 | The hook: the one screenshot, GIF or sentence that makes a stranger wishlist it. | Free text | Store page, hook test |
| 3.5 | Three or more Steam tags it would carry. | Free text | Store page, market check |
| 3.6 | Who tests it? Five named people or three named communities. | Free text | Stage 1 tester list |
| 3.7 | Hours per week you'll give it (an assumption until measured). | Number | Resources block, 02 §5 |
| 3.8 | Cash ceiling for setup and the first milestone (store fee, art, legal hour, tools). | Number | Resources block, Olive |
| 3.9 | Kill-by date: the date by which it passes Gate B or is shelved. | Date | Resources block, calendar |
| 3.10 | Which slot does it take, and what waits for it? (02 §3) | Choice | Portfolio, Decision Log |
| 3.11 | What does success look like for **this** game, at three levels: it paid for itself / it was worth it / it changed things? Units, revenue or reviews. | Free text, three lines | Strategy Tests §1 tiers, 01 §7 |
| 3.12 | If it runs long, what gets cut first, second and third? | Free text, ordered | Scope Ledger cut order |
| 3.13 | What does the first milestone (P1) look like when it's done? | Free text | 10 §3, GDD §12 |
| 3.14 | What will you buy rather than make (art, music, trailer, translation)? | Choice, multi | Budget, 10 §8 |
| 3.15 | Working title, and is it clear of existing games? (Assistant runs a quick check.) | Free text | 07 R-03, R-04 |

**Assistant work before final playback:** draft the Strategy Tests' first phase from 3.1–3.3; a quick check of the title (3.15) against Steam and an obvious-conflict search; assemble the Idea Brief.

## 6. The playback (after every round)

Five short parts, sent before the next round starts:

1. **What I heard** — the answers, condensed, in the Owner's words.
2. **The sharpest version** — a proposed one-liner, 3–5 pillars as a filter, and the target player, each marked Proposed.
3. **Contradictions** — where two answers pull against each other (e.g. "short sessions" and "50-hour campaigns"; "S size" and "full Workshop support"; "real places" and "no hard subjects").
4. **Red flags** — charter conflicts, licensing or real-world risks, scope that doesn't fit the size answer.
5. **Still unclear** — the questions the next round will add, in priority order.

The Owner corrects the playback; corrections are recorded in the brief as changes, not silent edits.

## 7. The output: the Idea Brief

One file per idea, `Inbox/YYYY-MM-DD <working title> — Idea Brief.md`, from the template in `Templates/Idea Brief.md`. It replaces the idea card for any idea that went through the survey. Its sections map onto the procedure:

| Brief section | Becomes |
| --- | --- |
| Pitch, fantasy, target player, session and campaign length, pillars | Stage 1 deliverables; GDD §1 |
| Nearest games with dated figures | Competitive Analysis seed (Stage 2) |
| Core choices, loop, systems map, content model | GDD §2–4, §6–7 |
| Presentation, input, Deck, languages, accessibility | GDD §9–10 |
| Stack, reuse, determinism, saves, modding | TDD seed (Stage 3) |
| Outside data and licences | Data and Licensing Register seed |
| 1.0 versus later, cut order | Scope Ledger seed |
| Riskiest assumption, test, kill result, hook, testers | Strategy Tests seed |
| Hours, cash ceiling, kill-by date, slot | Stage 1 resources block |
| Success at three levels | Strategy Tests §1 tiers |
| Every Proposed item and open question | Decision Log rows with decide-by dates |

A brief is **complete** when every core question has an answer or a logged "don't know", every playback was corrected, and no red flag is unaddressed. A complete brief lets Stage 1 finish well inside its 4-hour time box.

## 8. Improving the survey

After each game's post-mortem, ask: which question, if answered better at the start, would have saved the most time? Add or sharpen that question. Questions that never change the plan get cut. Changes go in the Decision Log; sections are appended, never renumbered.

## 9. From brief to engineering seed pack

*Runs once, when an idea is promoted (03 §4) and Round 3 is done. It turns the brief into engineering raw material, not an engineering plan: everything in it is **Proposed** until the Strategy Tests and Gate B have spoken. The real plan is written at Stage 5 from measured hours.*

### 9.1 What it produces

Four files in `Games/<Game>/seed/`, from `Templates/Seed Pack/`:

| File | Built from (brief) | Becomes later |
| --- | --- | --- |
| `tdd-proposals.md` | Build answers (2.17–2.23), systems map (2.5), saves, modding, input and Deck targets | TDD sections 1–14 skeleton; every item a Proposed row for TDD §14 |
| `spikes.md` | Riskiest assumptions (3.1–3.3), technical red flags from playbacks | Strategy Tests feasibility spikes: each has a question, method, time box, pass/fail line and failure action |
| `backlog.csv` | Systems map, P1 description (3.13), 1.0 list (2.24), cut order (3.12) | The P1 connected-systems playable backlog, pushed to GitHub Issues when the repo exists (04 A-23) |
| `data-sources.md` | Outside data (2.22), art and audio sourcing (2.11–2.12), languages (2.15) | Data and Licensing Register seed, one row per source with licence page and date read |

### 9.2 Rules

1. **Nothing in the seed pack is confirmed.** Each item carries its brief reference (e.g. `brief 2.19`) so a later change can be traced back to the answer it came from.
2. **Spikes come before backlog.** A backlog item that depends on an unproven spike lists it in `depends_on`; it isn't built until the spike passes.
3. **The backlog covers P1 only.** Later milestones are listed as one line each; detailing them now plans guesses.
4. **Every item has an acceptance line** that someone else could check: "seeded run of 100 turns reproduces byte-identical state", not "economy works".
5. **The backlog file is machine-readable** (§9.3) so it can be validated and pushed to issues without retyping.

### 9.3 Backlog format

`backlog.csv`, one row per item:

| Column | Meaning |
| --- | --- |
| `id` | `S-01` spike, `F-01` feature, `T-01` test, `X-01` tooling |
| `title` | Short, imperative |
| `system` | Which system from the map, or `core` / `tools` |
| `type` | spike / feature / test / tooling |
| `milestone` | `P1` (others only as one-line placeholders) |
| `acceptance` | The checkable done-line |
| `depends_on` | Other ids, separated by spaces |
| `estimate_hours` | A range, e.g. `4-8`, labelled an estimate until measured |
| `source` | The brief reference, e.g. `brief 2.5` |
| `issue` | Empty until pushed; filled with the issue URL by the script |

### 9.4 How it feeds automation

| Automation | What the seed pack makes possible |
| --- | --- |
| A-05 decide-by watcher | Brief §5 open questions carry Decide by and Status columns, so they appear in `studio.py due` alongside Decision Log rows |
| A-23 backlog to issues | `studio.py backlog <Game>` checks the CSV (ids unique, dependencies exist, acceptance present); `--apply` creates GitHub issues with labels and writes their URLs back |
| A-07 tests on push | Every `test` row and every acceptance line is a candidate automated test; seeded-replay acceptance lines become regression tests on day one |
| A-15 licensing re-check | Starts from `data-sources.md` instead of an empty register |
| A-04 hours log | Estimates in the backlog are compared with logged hours per item at the P1 gate; the gap calibrates the next game |
| A-17 post-mortem | Brief and seed pack predictions (size, hours, riskiest assumption, success tier) are compared with what happened |

## 10. Lunch mode: answer at lunch, review at home

*For when the Owner has an idea away from the desk. He answers a short, phone-friendly Round 1; the Assistant does the rest of the day's work unattended and leaves a reviewable brief. It speeds the survey up; it never replaces the Owner's answers.*

### 10.1 What the Owner does (about 10 minutes, on the phone)

Say "lunch mode" (or "quick idea, I'll be away") and answer eight questions, most of them tap-to-choose:

| From Round 1 | Question |
| --- | --- |
| 1.1 | The game in one or two sentences |
| 1.2 | What the player gets to be or do that they can't elsewhere |
| 1.5 | Up to three nearest games and what each gets wrong |
| 1.6 | Who the player is |
| 1.7 / 1.8 | Session length and campaign length |
| 1.10 / 1.11 | Setting, and any hard subjects or real people it touches |
| 1.13 | Size gut S / M / L |
| — | "Prototype it too?" yes / no (§10.4) |

### 10.2 What the Assistant does while he's away

1. The full Round 1 research and playback (§3 Assistant work, §6), with the unanswered Round 1 questions drafted from his answers.
2. **A drafted Round 2**: every answer written as the Assistant's best proposal, each marked *Drafted — not your answer*, with the reasoning in one line.
3. The systems map, licence checks for any data the idea needs, and a size estimate as a labelled range.
4. A **draft seed pack** (§9) marked DRAFT, built on proposed riskiest assumptions, because Round 3 hasn't happened.
5. If he said "prototype it too", a prototype run (12) aimed at the core loop.

### 10.3 What he comes home to

- The Idea Brief opens with a **"Waiting for you"** section: 5–10 decisions in priority order, each answerable in one line or one tap (pick a pillar set, confirm or change a drafted answer, resolve a contradiction).
- The brief is saved to the Claude Project (`ideas/YYYY-MM-DD <title> — Idea Brief.md`) so it reads on the phone, and to `Inbox/` when the computer is reachable. A short summary message says where it is and what matters most.
- Review takes about 30–40 minutes. Drafted answers become his only when he confirms them; unconfirmed ones stay Proposed.

### 10.4 Rules for lunch mode

1. Drafted answers never count as the Owner's answers: rounds done this way are marked `[~]` (drafted) in the brief header, not `[x]`, and triage scores (03 §3.2) use confirmed answers only.
2. Round 3's commitments (hours, cash, kill-by date) are never drafted. They are left blank.
3. The 30-day cooling-off starts on the capture date as usual. Lunch mode makes the brief better, not the idea faster to promote.
4. A prototype run from lunch mode uses the idea's one Inbox prototype allowance (12 §2).
