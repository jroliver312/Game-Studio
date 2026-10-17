# Operating Model

Oct 15, 2026 · @Jack · Draft for the Owner to confirm

*How the studio runs: who does what, the life of a game, how many things can be in flight, the weekly and monthly rhythm, how capacity is budgeted, and where every kind of record lives.*

## 1. Roles

The four roles from the New Game Setup Procedure (§1) are studio roles, not just setup roles.

| Role | Who | Does | Never does |
| --- | --- | --- | --- |
| **Owner** | Jack | Decides, confirms, passes gates, ships builds to players, speaks for the studio in public | Skips a gate because it feels done |
| **Assistant** | Claude | Drafts documents, researches, writes and runs automation, keeps the index, brief and logs current, prepares reviews | Confirms a decision, passes a gate, publishes anything to players or the public, spends money |
| **Reviewer** | An agent or person who did not draft the work | Reads finished documents and builds against a checklist; files findings | Reviews work it wrote |
| **Outside readers and testers** | Named people and communities | Play tests, read pitches, answer the questions the Strategy Tests ask | — |

The Owner wears six hats. Naming them makes it obvious when one is being neglected at a weekly review.

| Hat | Covers | Main documents |
| --- | --- | --- |
| Design | GDD, pillars, scope | Per-game GDD, Scope Ledger |
| Engineering | Code, builds, tests, tools | TDD, repo `CLAUDE.md` |
| Production | Calendar, hours, milestones, gates | Production calendar, hours log |
| Marketing | Store page, wishlists, festivals, devlogs, press | 05 Launch and Live Ops |
| Business | Money, tax, entity, legal, accounts | Olive, 07, 09 |
| Community and support | Reviews, bug reports, players | 05 §6 |

## 2. The life of a game

Every game is in exactly one stage. The stage is shown on the portfolio table (03 §5).

| # | Stage | Enters when | Leaves when | Governed by |
| --- | --- | --- | --- | --- |
| 0 | **Inbox** | An idea card is written | Monthly triage promotes, shelves or kills it | 03 |
| 1 | **Shelf** | Triage or a gate shelves it | A quarterly review sends it back to the Inbox (03 §3.4) | 03 |
| 2 | **Setup** | A setup slot is free and triage promotes it | Gate A passed | Procedure Stages 1–3.5 |
| 3 | **Test** | Gate A | Gate B: kill, pivot or go | Procedure Stage 4 |
| 4 | **Build** | Gate B go, and the build slot is free | Release candidate passes the launch checklist | Procedure Stage 5, the game's TDD and calendar |
| 5 | **Launch** | Launch checklist begins (L−30 days) | L+30 days | 05 |
| 6 | **Live** | L+30 | Owner declares maintenance | 05 §6 |
| 7 | **Maintenance** | Declared | Owner declares sunset | 05 §7 |
| 8 | **Post-mortem** | Written within 30 days of launch, and again at sunset | — | Procedure §5, §8 |

A **kill** at any stage is a Decision Log row; the documents stay as the record.

## 3. Work-in-progress limits — Proposed (S-05)

- **One game in Build or Launch.** The studio's main slot.
- **One game in Setup or Test.** Desk work and cheap tests can run beside a build, capped at a share of weekly hours (§5).
- **Live and Maintenance games** take only the support time in 05 §6; they do not occupy a slot.
- **Inbox and Shelf are unlimited.**

A new idea never displaces a game in a slot. If the Owner wants to switch, it is a Decision Log row that names what is paused and why.

## 4. Rhythm

| Cadence | Time box | What happens | Output |
| --- | --- | --- | --- |
| **Each work session** | 2–4 minutes | Log hours (with the backlog id in the note when there is one) and one line in the game's build log; five-line retro at the end (13 §2) | Hours log, build log, session retro |
| **Weekly review** (pick a fixed day) | 30 minutes | Hours vs plan; milestone progress; inbox — file new ideas, no triage; Proposed decisions near their decide-by date; reviews and bug digest; one hat that got no time | Five-line weekly note |
| **Monthly review** (first weekend) | 90 minutes | Money close for the game entity in Olive; idea triage (03 §3); risk register (07); accounts register spot-check (09); automation backlog (04 §5) — pick the next thing to automate | Monthly note, updated risk and triage scores |
| **Quarterly review** | Half a day | Charter success measures (01 §7); portfolio — anything to shelve or promote; re-read the charter; licensing re-checks; procedure "Took" lines | Quarterly note, any charter or procedure changes as Decision Log rows |
| **Per gate** | As the gate says | Gate checklist, ticked by the Owner | Gate row in the game's Decision Log |
| **Per launch** | — | 05 timeline | Post-mortem |

The weekly and monthly notes are short and go in `Studio/Reviews/` as `YYYY-MM-DD weekly.md`. The Assistant drafts them from the logs before the review; the Owner corrects and closes them. This is the first thing to automate (04 §5).

## 5. Capacity

The studio shares one person's week with a full-time job, Olive, the rental and the homestead.

- **The studio budget is set by the Owner** as hours per week, written in the resources block of each game's context brief and here: ______ hours per week (assumption until measured).
- **Setup/Test work is capped at a third of studio hours** while a game is in Build, so desk work does not starve the build.
- **Olive** has 10–20 hours per week through mid-January 2027; studio hours are on top of that, not taken from it, unless a Decision Log row moves them.
- **Measured beats typed.** After four weeks of logging, the measured average replaces the assumption everywhere, and calendars are re-dated from it.
- **Overload rule:** two months running above budget triggers a cut from the Scope Ledger's cut order or a date move — never "work harder".

## 6. Where everything lives

| Kind of record | Source of truth | Copies |
| --- | --- | --- |
| Studio documents (this set, procedure, templates) | `C:\Game Studio` (studio folder) | The "Game Studio Entity" Claude Project; the studio repo once it exists |
| Per-game design and reference docs | Claude Docs in the game's own Claude Project | Exported into the game repo's `docs/` (procedure Gate A) |
| Code, build log, `CLAUDE.md` | The game's GitHub repository (private), with a remote before any code | Local clones |
| Money, taxes, sales, ad spend, keys register, build register | Olive, game entity | CSV exports for the CPA |
| Store page, builds, the keys themselves, financial reports | Steamworks | Reports imported into Olive |
| Accounts, logins, recovery codes | Password manager (location in 09) | Sealed paper copy of recovery codes |
| Idea cards and shelf | `C:\Game Studio\Inbox`, `C:\Game Studio\Shelf` | — |

### 6.1 Folder layout — Proposed (S-15)

```
C:\Game Studio\
  00 Studio Index.md
  01 Studio Charter.md … 09 Accounts and Assets Register.md
  New Game Setup Procedure.md
  Templates\        idea card, weekly note, launch checklist, post-mortem
  Inbox\            one idea card per file
  Shelf\            shelved ideas with the reason
  Games\<Game>\     pointer file: Project link, repo link, stage, Olive entity
  Studio\Reviews\   weekly, monthly, quarterly notes
  Automation\       scripts the studio runs (04)
```

Game code does not live in this folder; each game has its own repository. Tactica is built on a different computer; its `Games\` pointer file records which machine and which remote.

## 7. Studio-wide engineering standards

Defaults every new game starts from; a game's TDD can override with a logged reason.

- A private GitHub repository with a remote **before** the first line of code; pushes at the end of every session.
- `CLAUDE.md` at the repo root holding the TDD's standing rules.
- Tests run on every push (04, item A-07); a red build is fixed before new work.
- Deterministic simulation core, stable ids, versioned saves with a migration ladder (procedure rule 8).
- Secrets (Steam keys, API keys, signing keys) never in a repository or a document.
- Commit messages in a fixed form (`fix:`, `feat:`, `content:`, `docs:`) so patch notes can be drafted from them.
- Studio work only on Jack's own machines and accounts (07 §R-01).

## 8. Changing this document

By Decision Log row only. Re-read at each quarterly review. Sections are appended, never renumbered.
