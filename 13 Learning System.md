# Learning System

Oct 15, 2026 · @Jack · Draft for the Owner to confirm (S-35)

*How the studio learns from its own work, so every session starts better informed than the last and every game is better than the one before. Learning only counts once it has changed something: a document, a template, a skill, a checklist or a number. A lesson that is written down but changes nothing is a note, not learning.*

## 1. The loop

```
  Work ──► Evidence ──► Lesson (Proposed) ──► Review ──► Change ──► Next session reads it
   ▲         (retros,       (Lessons            (monthly   (doc, skill,      (Standing
   │          predictions,   Register)           review)    template,         Lessons)
   │          runs, gates)                                  script)              │
   └─────────────────────────────────────────────────────────────────────────────┘
```

Four kinds of evidence feed it, each captured where it happens:

| Evidence | Captured | Where it goes |
| --- | --- | --- |
| **Session retros** — what we set out to do, what happened, what worked, what didn't | End of every working session, ~2 minutes, the Assistant drafts | `Studio/Learning/Sessions/YYYY-MM-DD <topic>.md` |
| **Predictions vs actuals** — every estimate the studio makes, closed when the real number arrives | When an estimate is made; closed when known | `Studio/Learning/predictions.csv` |
| **Run and test results** — prototype runs, Strategy Tests, reviewer findings | At each run, test or review | Their own reports, linked from the retro |
| **Gate and game reviews** — gates, post-mortems, the annual review | At each gate and launch | The procedure's post-mortem; the annual review |

## 2. Session retros

At the end of any working session that produced or changed something, the Assistant drafts five lines and the Owner corrects them (or says "fine"):

1. **Goal** — what we set out to do.
2. **Result** — what exists now that didn't before, and what didn't get done.
3. **Worked** — one thing to do again.
4. **Didn't** — one thing that cost time, went wrong, or had to be redone, and why.
5. **Lesson candidate** — if 3 or 4 points at something that will happen again, one line in the form *"When X, do Y, because Z (evidence)."* Otherwise "none".

A candidate goes into the Lessons Register as **Proposed** with a decide-by date, so the weekly decide-by watcher shows it. A retro with no lesson is normal; forcing one produces noise.

## 3. The Lessons Register

`Studio/Learning/Lessons Register.md`, one row per lesson:

| Column | Meaning |
| --- | --- |
| ID | `L-001`, never reused |
| Date | When raised |
| Source | Retro, prediction, run, test, review, gate, post-mortem |
| Game | Or "Studio" |
| Lesson | "When X, do Y, because Z" |
| Evidence | Where it was seen, with a link or reference |
| Change | The exact document, template, skill or script change that puts it into practice |
| Seen | How many times the situation has come up (raised at 1; the Assistant increments it) |
| Decide by / Status | Proposed → **Adopted** (change made, Decision Log row) / **Rejected** (reason) / **Watching** (needs a second sighting) |

### 3.1 Rules for lessons

1. **A lesson names its change.** "Be more careful with licences" is rejected; "add a licence check to survey Round 2 (11 §4, 2.22)" is a lesson.
2. **One sighting is a note, two is a pattern.** A one-off becomes **Watching**; when it's seen again, it's proposed for adoption. Expensive or dangerous ones (lost work, legal, money) are adopted on the first sighting.
3. **Adoption goes through the Decision Log** like any other change, and the changed document's section is cited in the lesson's row.
4. **Repeat offenders.** If an Adopted lesson's situation happens again, the change didn't work. The row is reopened with Seen +1, and the fix is redesigned, not repeated.
5. **Retire lessons that never fire.** At the annual review, a Standing Lesson that hasn't been relevant in a year moves out of the Standing list (it stays in the register).

## 4. Predictions and calibration

Self-awareness, in numbers: how far off the studio's guesses run, by kind of guess.

Every estimate is logged when it is made — `python Automation/studio.py predict <Game> <kind> "<what>" <value> <unit>` — and closed with `studio.py actual <ID> <value>` when the real number arrives. Kinds:

| Kind | Examples |
| --- | --- |
| `hours` | A stage, a milestone, a backlog item, a prototype run |
| `weeks` | Calendar time for a phase |
| `size` | The S/M/L gut call vs what it turned out to be |
| `count` | Wishlists, reviews, units, testers recruited |
| `rate` | Hook test pass rate, conversion, win rate |
| `money` | Costs against the cash ceiling |

`studio.py calibration` reports, per kind, the median of actual ÷ predicted and how many predictions back it. It also compares each game's backlog estimates with the hours actually logged against those items (log hours with the item id in the note, e.g. `"[F-03] economy prices"`).

**How calibration is used:**
- Once a kind has **five or more** closed predictions, its median ratio becomes the studio's **correction factor**. New estimates of that kind are shown both raw and corrected ("12–20 h guessed, 22–37 h at your 1.8× factor").
- Calendars (procedure Stage 5, 10 §3) use corrected numbers.
- A factor moving toward 1.0 over time is the clearest sign the studio is getting better at knowing itself.

## 5. Standing Lessons: how future sessions get smarter

`Studio/Learning/Standing Lessons.md` holds the Adopted lessons that still matter — **at most 15**, one line each, grouped by stage (idea, setup, build, market, launch, working with the Assistant). Kept short on purpose: a list nobody reads teaches nothing.

- **Every studio skill reads it first** (onboarding, prototype runs, the learning skill itself) and checks the work in hand against it. When a lesson applies, the skill says so in one line: *"Standing lesson L-007: licence-check data sources in Round 2 — doing that now."*
- **Every game's Project instructions and repository `CLAUDE.md`** link to it, so engineering sessions inherit it too.
- **The calibration factors** sit at the top of the file, regenerated by the script, so every estimate in every session sees them.

## 6. Cadence

| When | What | Time |
| --- | --- | --- |
| End of a working session | Retro (§2) | ~2 min |
| When estimating | Log the prediction (§4) | seconds |
| Weekly review | Decide-by watcher shows Proposed lessons; calibration summary in the weekly note | inside the 30 min |
| Monthly review | Decide Proposed lessons (adopt, reject, watch); refresh Standing Lessons | ~15 min |
| Each gate | Close the gate's predictions; one gate retro | ~15 min |
| Post-mortem | Every lesson raised during the game is re-read; the Lessons half of the post-mortem comes from the register, not from memory | — |
| Annual review | Retire stale Standing Lessons; compare calibration year over year | ~1 hour |

## 7. What makes each game better than the last

Three measures, recorded per game in the post-mortem and compared across games:

1. **Calibration factor** for hours, moving toward 1.0.
2. **Repeat offenders** — Adopted lessons whose situation happened again — going toward zero.
3. **The procedure's own three numbers** (hours to Gate A; foundation decisions reversed after the first milestone; licensing problems found after build start) getting smaller.

## 8. What this is not

- **Not personal memory.** Claude's memory about Jack is separate and about him; studio lessons live in these files, where they can be read, corrected and versioned.
- **Not a blame log.** Lessons are about the system — documents, checklists, tools — never "try harder".
- **Not automatic adoption.** The Assistant raises and drafts; the Owner adopts (S-07).

## 9. Changing this document

By Decision Log row. Sections are appended, never renumbered.
