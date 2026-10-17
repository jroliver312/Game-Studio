# Idea Pipeline and Portfolio

Oct 15, 2026 · @Jack · Draft for the Owner to confirm

*How a game idea is captured in two minutes, cooled off, judged against the others once a month, and either promoted into the New Game Setup Procedure, shelved with a reason, or killed. Plus the portfolio: every game the studio has, and where it stands.*

## 1. Why a pipeline

Ideas are cheap and arrive at the worst times — usually in the middle of a build. The pipeline exists so that no idea is lost and no idea interrupts the work in a slot. Writing it down is the release valve; the monthly triage is where it is judged.

## 2. Capture: the idea card

One file per idea in `Inbox\`, named `YYYY-MM-DD <working title>.md`. Two minutes, no research. Any field can say "don't know".

```markdown
# <Working title>
Captured: YYYY-MM-DD

**One line:** <a stranger could repeat it back>
**The fantasy:** <what the player gets to be or do that they can't elsewhere>
**Pillar guesses:** <3 words or phrases>
**Target player and session length:** <who, and how long one sitting lasts>
**Nearest games:** <up to 3, and what each leaves out>
**Why me:** <what Jack knows or has built that makes this easier for him>
**Reuse:** <code, data, tools from existing games it can use>
**Size guess:** S (≤ 6 months part-time) / M (6–18) / L (18+)
**Hook test idea:** <the cheapest way to find out if anyone wants it>
**Excitement now:** 1–5
```

### 2.1 Going further: the onboarding survey

Any idea worth more than a card goes through the Idea Onboarding Survey (11): Rounds 1–2 at intake, Round 3 at promotion. Its Idea Brief replaces the card and gives triage much better answers to score.

## 3. Triage — Proposed (S-06)

### 3.1 The cooling-off rule

An idea must sit in the Inbox **30 days** before it can be promoted. It can be killed or shelved any time. During the cooling-off it may get **one prototype run** (12 §2); its results go into the brief for triage to read. Most ideas lose their shine in a month; the ones that do not are the ones worth the procedure's Stage 1.

### 3.2 Monthly scoring

At the monthly review, each idea older than 30 days is scored 1–5 on six questions. The Assistant pre-fills a draft score with one line of reasoning; the Owner sets the final number.

| # | Question | Weight |
| --- | --- | --- |
| 1 | **Charter fit** — does it sit inside 01 §3 and outside 01 §4? (a 1 here ends the scoring) | gate |
| 2 | **Solo feasibility** — can one person finish it at the studio's measured hours? | ×2 |
| 3 | **Market signal** — do the nearest games sell, and is there a visible gap? (a quick look, not the full Competitive Analysis) | ×2 |
| 4 | **Reuse** — how much existing code, data, tooling or knowledge carries over? | ×1 |
| 5 | **Still excited after 30 days** — re-rated, not copied from capture | ×1 |
| 6 | **Hook cheapness** — can the hook be tested for under a weekend and under $50? | ×1 |

Score out of 35. Ideas ranked; the scores and reasons go into the idea card.

### 3.3 Outcomes

- **Promote** — only if the Setup/Test slot is free (02 §3) and the idea scores highest. It moves to `Games\<Game>\` and the procedure's Stage 1 begins.
- **Hold** — stays in the Inbox, re-scored next month. An idea held three months without promotion is shelved.
- **Shelve** — moved to `Shelf\` with one line: why, and what would change the answer.
- **Kill** — moved to `Shelf\Killed\` with the reason. Never deleted.

### 3.4 The shelf

Re-read at each quarterly review. A shelved idea comes back only through the Inbox (it gets a fresh 30-day clock unless the shelf note named the condition and that condition is now met).

## 4. Promotion into the procedure

Promotion is the procedure's Stage 1 entry ("an idea worth more than a weekend"). Before Stage 1 starts, the idea completes Round 3 of the onboarding survey (11 §5), whose Idea Brief carries Stage 1's resources block. The idea card gives Stage 1 a head start: one line, pillars, target player and session length, and nearest games are drafts of Stage 1's first four steps; the hook test idea seeds the Strategy Tests. The procedure's Stage 1 time box (4 hours) still applies.

## 5. Portfolio

The Assistant keeps this table current; the Owner confirms stage changes. Stages are from 02 §2.

| Game | Stage | Where | Next gate or milestone | Notes |
| --- | --- | --- | --- | --- |
| **Tactica** (formerly the FC26 Career Sim working title) | Build | Single-file HTML; separate computer | Release candidate; launch date not anchored | Version 113+, ~25,000 players, 70 leagues (as of the Sep 2026 notes). Entered Build before the procedure existed (S-20); gets the Existing Game Audit (16) first. Renamed from FC26 on 2026-10-15 (S-22); name still needs the R-03 clearance search (07 R-04). Its Lessons document already feeds Sovereign's TDD. Business side set up in Olive's game entity. |
| **Sovereign** | Setup — Stage 3 done; Gate A not passed | Its own Claude Project | Gate A: 7 Proposed decisions awaiting the Owner | The procedure was extracted from this run. Stage 3.5 review not yet run. |
| *Inbox* | — | `Inbox\` | Monthly triage | Empty |

**Slot check today:** Build slot — Tactica. Setup/Test slot — Sovereign. Both slots full: new ideas go to the Inbox and wait. (If Sovereign is in fact the main focus, that is a Decision Log row saying Tactica is paused.)

## 6. Changing this document

By Decision Log row. Sections are appended, never renumbered.
