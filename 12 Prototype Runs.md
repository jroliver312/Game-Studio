# Prototype Runs

Oct 15, 2026 · @Jack · Draft for the Owner to confirm (S-34)

*How the studio turns an Idea Brief or a seed pack into a playable throwaway prototype in a single unattended run — "press a button, play it the next day". A prototype run is a **test instrument**: it answers named questions with pass or fail. It is never the start of the real codebase.*

## 1. What a run is

One unattended session that:

1. picks 1–3 **questions** to answer (spikes from the seed pack, or "is the repeated decision interesting?" for an Inbox idea), each with a pass line;
2. builds the smallest playable thing that answers them, in a fixed throwaway stack (§4);
3. runs it headless many times with fixed seeds and measures what happened;
4. checks it loads and plays in a real browser;
5. delivers a **playable page**, the code, and a **report** with pass/fail per question.

Triggered by saying "prototype run for <idea or game>" (the run happens in that session), or by "prototype it too" in lunch mode (11 §10). It can also be scheduled for a set time as a one-off scheduled task when the computer will be on.

## 2. When a run is allowed — Proposed

| Stage of the idea | Allowance | Aimed at |
| --- | --- | --- |
| **Inbox** (cooling off) | **One run per idea**, without needing a slot. Owner time: playing it, under an hour | The core loop: is the decision the player repeats interesting? |
| **Setup / Test** (Stage 4) | As many as the Strategy Tests call for; each is a named test | The test plan's spikes and the hook test |
| **Build** | Only for a spike that blocks a backlog item | One technical or design question |

A run never needs the Build slot and never displaces the game in it (02 §3). This amends the WIP limits for this one, cheap activity (S-34).

## 3. Sizing: what one run can build

| Idea size (brief 1.13) | What a run builds | What it can't prove |
| --- | --- | --- |
| **S** | The whole core loop, playable start to a lose or win state | Long-term depth, content variety |
| **M** | The core loop of one system cluster (2–3 connected systems) | How the rest of the game feeds it |
| **L** (e.g. Sovereign) | 1–2 spikes: a headless simulation of the riskiest interaction with charts, plus a minimal view | The game itself. It answers a question, not "is this fun?" |

If the questions don't fit, the run narrows to the single most important one. It never expands.

## 4. The throwaway stack

Whatever the real game's stack, prototypes are built the same way so they run anywhere, including a phone, with no install:

- **One HTML file** with plain JavaScript (canvas or page elements). No frameworks, no build step, no network calls.
- **Shapes, colour and text only.** No generated or downloaded art, music or fonts, so there's nothing to license and no AI disclosure question. Fictional names only.
- **A seeded random number generator**; the seed is shown on screen and copyable, so a tester's run can be reproduced exactly.
- **A debug panel**, hidden by default, showing every system's key values, so the Owner can see why things happened.
- **A headless harness** (`harness.js`, run with Node) that plays N seeded games with a simple bot or random policy and reports how often key events happen. This is the "too much or too little" check from Pfeifer's connected-systems playable.

## 5. Verification before delivery

A run isn't delivered until all of these are true:

- [ ] The harness runs its seeded games with no errors, and the same seed produces the same result twice
- [ ] The page loads in a headless browser with no console errors, and a scripted play-through reaches a lose or win state (or N turns)
- [ ] Screenshots of the start, mid-game and end are taken
- [ ] Every question has a pass, fail or "couldn't tell" result, with the evidence
- [ ] The page states at the top: *Prototype — throwaway — <date> — answers: <questions>*

## 6. Delivery

| What | Where |
| --- | --- |
| `index.html`, `harness.js`, `report.md`, screenshots | `Games/<Game>/prototypes/YYYY-MM-DD run-N/`, or `Inbox/prototypes/<idea>/YYYY-MM-DD run-N/` for an Inbox idea, when the computer is reachable; otherwise sent as files |
| The playable page | Published as a **private** artifact, so it opens on the phone. Sharing it with testers is the Owner's choice |
| The report | Also saved to the Claude Project beside the brief |

The report (template `Templates/Prototype Report.md`) leads with: the questions and their results; **three things to try first** when playing; the harness numbers; what the run does **not** prove; and the suggested next run.

## 7. Rules

1. **Throwaway by default.** Prototype code goes into the real repository only under `prototypes/`, never into the game's source, unless a later review against the TDD says a piece is worth keeping, recorded as a Decision Log row.
2. **Questions first.** No run starts without written questions and pass lines. Unattended, the Assistant proposes them and says so in the report.
3. **Nothing public.** The artifact stays private; no store pages, posts or uploads.
4. **No spending.** A run uses no paid service or asset.
5. **Results feed the record.** In Setup/Test, results go into the Strategy Tests results log; in the Inbox, into the brief, where triage reads them.
6. **Time box.** One session. A run that can't finish delivers what it has, with "couldn't tell" results, rather than running on.

## 8. Changing this document

By Decision Log row. After each game, record which prototype results predicted later outcomes, and drop anything runs keep producing that nobody uses. Sections are appended, never renumbered.
