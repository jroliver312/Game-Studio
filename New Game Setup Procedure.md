# New Game Setup Procedure

Oct 15, 2026 · @Jack

*A repeatable procedure for taking a game idea from one line to a tested, documented foundation ready to build on. Written from the Sovereign setup; game-agnostic from here on. Every stage has an entry requirement, a deliverable and a done-when checklist, so the next idea starts by running this, not by remembering how the last one went.*

## 1. Purpose and when to use

Run this procedure whenever a game idea is serious enough to spend more than a weekend on. It produces, in order: a design document, a market analysis, a set of foundation documents (tests, engineering, licensing, scope and decisions), a tested verdict on the idea, and a dated plan for the first milestone. At the end the idea either has a foundation ready to build on, or it has been killed or pivoted for a stated reason, which is also a good outcome.

The one rule that runs through every stage: **the expensive thing is changing a foundation after things are built on it.** Every stage exists to settle something before the next stage builds on it. That is why documents come before tests, tests come before the plan, and the plan comes before code. Skipping a stage does not save its hours; it moves them to a worse time.

What the procedure is not: a design method. It does not say what makes a game good. It says what has to be true, in what order, so that the work done on the idea is not thrown away.

**Roles.** Four, and the procedure names which one acts at every step. The **Owner** (the studio's one developer) decides, confirms and passes gates. The **Assistant** drafts, researches, keeps the brief and index current, and never confirms a decision or passes a gate on the Owner's behalf. The **Reviewer** is an agent or person who has not seen the drafting and reads a finished document against a checklist (Stage 3.5). **Outside readers and testers** are the people the Strategy Tests name; they are recruited in Stage 1, not found later.

## 2. The procedure at a glance

&#91;embedded content: setup procedure · 5 stages, 2 gates\]

Five stages and two gates. Stages 1 to 3 are desk work and together took one working day for Sovereign once the design document existed; stage 4 is about a quarter of part-time hours; stage 5 begins the build. The gates are hard: Gate A is a checklist of documents and confirmed decisions, Gate B is the test plan's own kill, pivot or go rule. Each stage's exit is the next stage's entry, so there is no "partly done" between them.

## 3. Stage by stage

Each stage lists what must already be true to start it, what is done in it, what it produces, and the checklist that says it is finished. Hours are Sovereign's and are a first calibration, not a promise.

### Stage 1. Capture the idea and set up the project

**Entry:** an idea worth more than a weekend.

**Steps:** write the pitch in one sentence; name the three to five design pillars that every feature must serve; name the target player and session length; name the three closest existing games and what each leaves out. Create the Claude Project; write its instructions, a context brief and a reference-set index; let memory file the project.

**Resources, written down in the context brief before anything else is drafted:** the hours per week the Owner expects to give (an assumption until measured, and labelled so); a cash ceiling for the setup and the first milestone (store fees, an hour of legal review, contract art if the art test fails, tools); a tester list with at least five named people or three named communities for the hook and prototype tests; and a kill-by date, the calendar date by which the idea must have passed Gate B or be shelved.

**Deliverable:** Project instructions (pasted into the Project settings), `claude/<game>-context.md`, `claude/reference-set.md`.

**Done when:**

- [ ] One-sentence pitch a stranger can repeat back
- [ ] Pillars written as a filter ("a feature that fights one is cut")
- [ ] Target player and session length stated
- [ ] Three nearest games named with the gap each leaves
- [ ] Resources block filled: hours assumption, cash ceiling, tester list, kill-by date
- [ ] Project named for the game, instructions pasted, context brief and index exist

**Took:** about 2 hours.

**Time box:** 4 hours of working time. Over it, the idea is not ready to be a project; shelve it with its one-liner and pillars in a note.

### Stage 2. Define: design document and competitive analysis

**Entry:** Stage 1 done.

**Steps:** write the Game Design Document to the template in section 5, as a Claude Doc, canonical from the moment it exists. Then the Competitive Analysis: 8 to 12 comparables with price, reviews, sales and dates; what each does well; the recurring complaints; the gaps nobody fills; and an implications list of concrete changes to the GDD, each tied to evidence. The implications list is not applied yet; it is logged as pending.

**Deliverable:** two canonical Claude Docs.

**Done when:**

- [ ] Every GDD template section filled; no section is a heading alone
- [ ] Milestones have gates judged by someone other than the developer
- [ ] A cut list for 1.0 and the "no new system without a cut" rule are in the GDD
- [ ] The GDD's open questions are listed in one place
- [ ] Competitive Analysis figures carry the date they were read and link to the page
- [ ] The implications list exists and each item names its evidence and its GDD section

**Took:** the GDD and CA pre-date the procedure; budget 2 to 4 days part-time for both.

**Time box:** 5 working days part-time for both documents together. A GDD that is still growing past that is being polished instead of tested; stop at the template and let Stage 4 find what is missing.

### Stage 3. Foundation: the reference documents

**Entry:** Stage 2 done. Also bring in the post-mortem from the previous game if one exists (for Sovereign, Lessons from Tactica); it is an input to every document below.

**Steps, in this order, each a Claude Doc:**

1. **Strategy Tests.** Commercial tiers with numbers; the conditions that must be true; the questions; the tests, each with method, cost, pass criterion and failure action; four phases with gates; a results log; the kill, pivot, go rule.
2. **Technical Design Document.** Everything expensive to change after the first milestone: layers, platform interface, determinism, identity, saves, data formats, tools, gates, repo rules. Every choice made here for the first time is marked *proposed* and collected in its last section.
3. **Data and Licensing Register.** One row per dataset, font, sound and library, read from the publisher's own licence page; commercial use, derived works, redistribution, attribution, version. An attribution file template. Anything non-commercial or share-alike is rejected and replaced.
4. **Scope Ledger and Decision Log.** Protected scope; in and out of 1.0; the cut order if the first milestone runs long; the system swap log; the decision log with every decision's date, reason and status, seeded from the GDD and from the *proposed* items in the documents above.

**Deliverable:** four reference Claude Docs, linked from the project instructions and the index.

**Done when:**

- [ ] Each document's template sections are filled (section 5)
- [ ] Every proposal in the TDD and the Licensing Register has a row in the Decision Log marked Proposed
- [ ] The index lists every document with its state and nothing is "to write" before the build
- [ ] The context brief points at the Decision Log as the record

**Took:** about 6 hours of working time for all four, on one day.

**Time box:** 2 working days. These are reference documents drafted from the GDD and CA; if one needs more, the GDD is incomplete and the work goes back to Stage 2.

### Stage 3.5. Review

**Entry:** all four Stage 3 documents drafted.

**Steps:** a Reviewer who has not seen the drafting reads every document in the set against this checklist and files findings in a review log (a section at the end of the Decision Log document): contradictions between documents (gates in the Strategy Tests against GDD milestones; TDD against GDD §11; Licensing Register against the GDD's source table; Scope Ledger against the GDD's cut list and rules); claims with no source; figures with no date; proposals in any document that have no row in the Decision Log; sections that are headings alone. Then one outside human reads the GDD and the Strategy Tests and answers two questions: what would you build first, and what would you cut first. Their answers are compared with the Scope Ledger.

**Deliverable:** a review log with every finding either fixed (with the edit named) or logged as accepted (with the reason).

**Done when:**

- [ ] Every document has been read by a Reviewer who did not draft it
- [ ] Every cross-document check above was run and its result recorded
- [ ] Every finding is fixed or accepted, none open
- [ ] An outside human's first-build and first-cut answers are recorded and compared with the Scope Ledger

**Time box:** 1 working day. **Took:** not yet run for Sovereign; this stage was added after the first run found two contradictions by accident.

### Gate A. Foundation complete

Section 4 has the checklist. In short: the documents exist and are complete, every Proposed decision has been confirmed or changed by the owner, the GDD has been edited to match, and the housekeeping is done. Nothing is tested before this.

### Stage 4. Test

**Entry:** Gate A passed.

**Steps:** date the first phase two weeks ahead, start the hours log on day one, run the phase, log results in the Strategy Tests document, fold findings into the GDD in place, re-plan the next phase from measured hours. Repeat for each phase. Never date more than one phase ahead; the numbers are not real until they are measured.

**Deliverable:** a filled results log; GDD edits with their test number cited; a measured hours-per-week figure.

**At every phase gate, three things are updated before the next phase is dated:** the procedure's "Took" line for the stage or phase just finished; the next phase's plan, from measured hours; and any gate line that would have caught a problem the phase found. The procedure learns at each gate, not at the end of the game.

**Done when:**

- [ ] Every test in the plan has a result row, including "not run" with a reason
- [ ] Each phase gate was judged against its written criteria, not against how it felt
- [ ] Findings that changed the design are in the GDD, with the test cited
- [ ] Hours per week is a measured number from at least four weeks

**Took:** planned at 12 weeks and 150 to 200 hours; actual to be recorded here after Sovereign's run.

### Gate B. Kill, pivot or go

The Strategy Tests document's own rule, applied with its own numbers. A kill is recorded in the Decision Log with the result that caused it; the documents stay as the record of what was learned. A pivot re-enters Stage 2 for the sections that changed. A go proceeds.

### Stage 5. Plan and build

**Entry:** Gate B says go.

**Steps:** write the production calendar from measured hours (milestones with dates, the store page and demo at least six months before launch); draft the store page from the tested hook; create the repository with the TDD's repo rules as its `CLAUDE.md`, a remote before any code, and the previous game's day-one checklist worked through; start the first milestone.

**Deliverable:** production calendar, store page draft, a repository with its first pushed commit.

**Done when:**

- [ ] Calendar dates come from measured hours, not the GDD's estimate
- [ ] Store page draft names the hook the tests said was strongest
- [ ] Repository exists, remote set, `CLAUDE.md` in place, day-one checklist ticked
- [ ] First milestone's gate criteria copied into the repository's build log as the target

## 4. The two gates

A gate is a checklist, every line of which is a yes or a no. Nothing passes on "mostly". The owner ticks it; the assistant drafts and reminds but does not pass a gate on the owner's behalf.

### Gate A: foundation complete, tests may start

**Documents**

- [ ] Game Design Document complete to its template; no section is a heading alone
- [ ] Competitive Analysis complete; figures dated; implications list present
- [ ] Strategy Tests complete: tiers, conditions, questions, tests with pass criteria and failure actions, phases with gates, results log, kill/pivot/go rule
- [ ] Technical Design Document complete; proposals collected in its last section
- [ ] Data and Licensing Register complete; no Rejected dataset remains in any pipeline; attribution template written
- [ ] Scope Ledger and Decision Log complete; protected scope and cut order written; decision log seeded
- [ ] Previous game's post-mortem linked as a reference, or a note that none exists
- [ ] Reference-set index lists every document with its state

**Decisions**

- [ ] Every Proposed row in the Decision Log is Confirmed, changed or Rejected by the owner
- [ ] The GDD has been edited in place to match every Confirmed decision, including the Competitive Analysis implications the owner accepted
- [ ] The launch scope question (for Sovereign: launch eras) has either a decision or a named test that decides it

**Project**

- [ ] Project named for the game; instructions pasted into the Project settings and listing every document
- [ ] Context brief points at the Decision Log as the record and names the next step
- [ ] Any "Untitled" documents renamed

**Readiness**

- [ ] A start date for test Phase 0 and a two-week dated plan for its tests
- [ ] The hours log is ready to start on day one

**Review and safety**

- [ ] Stage 3.5 review log exists with no open finding
- [ ] Every Proposed row in the Decision Log carries a decide-by date; none is older than two weeks
- [ ] The repository exists with a remote, and every document in the set has been exported into its `docs/` folder; from here on, each Confirmed change is exported in the same sitting
- [ ] The resources block is filled and the kill-by date is in the calendar

### Gate B: kill, pivot or go

Taken verbatim from the Strategy Tests document for the game. For Sovereign:

- **Kill** if no pitch clears 40 percent in the hook test *and* paper-prototype players do not want another reign. Record the result in the Decision Log; the documents stay.
- **Pivot** if the hook and loop pass but a feasibility spike fails; apply the named scope change and re-enter Stage 2 for the sections it touches.
- **Go** when all four phase gates pass; fold results into the GDD, then Stage 5.

**A pivot is allowed once.** A second pivot is a kill, recorded as such; an idea that needs two pivots is a different idea and starts the procedure from Stage 1 with its own one-liner.

**Before any of the three is declared**

- [ ] Every test has a result row, including "not run" with a reason
- [ ] Hours per week is a measured number from at least four weeks
- [ ] The phase gates were judged against their written criteria by the people the criteria name (outside testers where the plan says so)
- [ ] The verdict and its deciding numbers are a row in the Decision Log

## 5. Document templates

The section list each document must contain. A new game's skeletons can be born from this table in one sitting; each section is then filled in order. Sections in italics are the ones that most often get skipped and most often cost later.

| Document | Sections | Owner of the content |
| --- | --- | --- |
| **Project instructions** (pasted into the Project) | What the game is in two sentences; platforms and what is out of scope here; source-of-truth docs with links; reference docs with links; how to work (ask-before-irreversible, short replies, pillars as filter, voice rules, no real people, foundations first, honest grading, dated figures, the milestone decision point) | Owner writes the rules, assistant drafts |
| **Context brief** (`claude/<game>-context.md`) | Doc links; current phase; pitch; platforms; decisions (pointer to the log); open questions; milestones; next steps; housekeeping; working rules | Assistant keeps current |
| **Reference-set index** (`claude/reference-set.md`) | What exists (doc, where, role, state); what is missing in the order needed, with entry conditions; order of work; housekeeping | Assistant keeps current |
| **Game Design Document** | 1 Vision and pillars · 2 The core choices the player makes · 3 Core loop (moment, session, campaign; losing; winning; difficulty) · 4 Simulation systems, each with inputs and outputs · 5 The rule systems that vary (for Sovereign, political systems) with a *fairness rule* · 6 Content packs: what one contains, the launch set in detail, the planned set · 7 Content pipeline (tools, sources, fairness rules) · 8 The spatial layer (map, buildings, ownership, disasters) · 9 Controls and UI, controller first if any console · 10 Presentation (art, UI style, audio, performance targets) · 11 Technical architecture outline · 12 Scope and milestones with gates, *what is cut from 1.0*, *rules for staying on scope* · 13 Risks, *approach to hard subject matter*, open questions · 14 Glossary and example data files | Owner |
| **Competitive Analysis** | 1 Summary · 2 The market with dated figures · 3 Direct competitors table (studio, date, price, reviews, critics, sales, overlap) · 4 Positioning map · 5 What to take from each · 6 What to avoid, with sources · 7 Gaps nobody fills · 8 *Implications for the design document*, each with evidence and section · 9 Sources, with what was not found | Assistant drafts, owner reads |
| **Strategy Tests** | 1 Purpose and commercial tiers with numbers · 2 What needs to be true, each mapped to tests · 3 Questions, grouped · 4 Tests: what, method, cost, pass, *failure action* · 5 Sequence with phase gates and *kill, pivot, go* · 6 Results log | Assistant drafts, owner runs |
| **Technical Design Document** | 1 Scope and rules (code wins, generated numbers, proposals marked) · 2 Repository layout · 3 Layers and the dependency rule · 4 Platform interface · 5 Simulation contract (tick, determinism, numeric type, RNG, replay test) · 6 Threads and handoff · 7 Memory · 8 *Entities and stable ids* · 9 Data formats and schemas · 10 *Saves: version, migration ladder, round trip* · 11 Tools · 12 Build, gates and tests · 13 Standing rules (the repo's `CLAUDE.md`) · 14 *Decisions proposed, questions for the first milestone* | Assistant drafts, owner confirms §14 |
| **Data and Licensing Register** | 1 Verdict · 2 The register (dataset, use, licence page read, commercial, derived, redistribute, attribution, version, status) · 3 Notes on the complicated ones · 4 Other inputs (fonts, audio, names, libraries) · 5 Rules for adding a source and the attribution file template · 6 Open items and re-check schedule | Assistant drafts from publisher pages, owner confirms |
| **Scope Ledger and Decision Log** | 1 Protected scope · 2 In 1.0 and cut from 1.0 · 3 *Cut order* with saves, costs, reversibility and the trigger rule · 4 System swap log · 5 Decision log (date, decision, reason, replaces, doc, status chip) · 6 How it is used | Assistant drafts, owner owns every status |
| **Lessons from the previous game** | The rules, short · Decide on day one · Surprises that cost us · Measuring honestly · The workflow that worked · Working with the assistant on a long build · *Day-one checklist* | Written at the end of each game, from its records |

Later documents (writing bible, art bible, production calendar, store page draft) are not part of the setup; their entry conditions are in the reference-set index and they are written when those are met.

## 6. Rules that apply at every stage

1. **Two documents are canonical; everything else is a reference.** The design document and the competitive analysis are edited in place and never re-summarized into a new doc. References point at them by section.
2. **A decision is proposed in a working doc, logged with a decide-by date, confirmed by the Owner, and only then applied to the canonical docs.** The Assistant never edits a canonical doc on its own judgment.
3. **Ask before anything expensive or hard to reverse; otherwise start.** Rewriting a section, cutting a system and locking a decision are the three things that always get asked.
4. **Every figure carries its date and its source.** Market numbers, licence terms and estimates all go stale; a number without a date is a guess.
5. **Typed numbers are targets; measured numbers are facts.** No calendar is built on an assumed hours-per-week. No test band is set before a seed sweep.
6. **Fictional names from the first word.** No real people, nations, leaders or atrocities in anything the game will contain; outside actors are archetypes.
7. **"Free" is not a licence.** Every outside input is read from its publisher's own terms page before it enters a pipeline.
8. **Foundations before features:** a remote before code, a deterministic core, stable ids, versioned saves, open data. Any plan that skips one is flagged.
9. **Long work goes in the documents, not the chat.** Replies are short and lead with the bottom line.
10. **Honest grading.** What is unverified is marked unverified; a thin estimate is called thin; uncertainty gets a number when it matters.
11. **Nothing is deleted from the record.** A reversed decision is a new row; the old one is marked Superseded.
12. **Nothing is finished until someone who did not write it has read it.** Every document passes a Reviewer before a gate; the work does not grade itself.
13. **Sections are appended, never renumbered.** Every document cites others by section number, so a retired section keeps its number with a one-line note, and new material is added at the end or as a sub-section.
14. **Every stage has a time box, and running over it is information, not a reason to push on.** A stage that will not close means the stage before it was not finished.

## 7. Worked example: Sovereign

The procedure was extracted from this run, so the run is the calibration. Stages 1 and 3 and the writing of this document happened on 15 Oct 2026; the GDD and CA existed from earlier sessions.

| Stage | Document | What it found or decided | Hours (working time) |
| --- | --- | --- | --- |
| 1 | Project instructions, context brief, reference-set index, project memory | The Project was unnamed and empty; the 360 build was scoped out of this Project; the open launch-era question was recorded | \~2 |
| 2 | GDD (14 sections), Competitive Analysis (11 comparables) | No shipped game combines real place, era choice and citizen-level politics; eight implications for the GDD; price $19.99 to $24.99; ship complete | pre-existing |
| 3.1 | Strategy Tests | Three commercial tiers; eight conditions; 30 questions; 18 tests in four gated phases, \~12 weeks; strongest evidence from the paper prototype, the spreadsheet model and the art bar test | \~1.5 |
| 3.2 | Technical Design Document | 41-function platform interface; int64 Q47.16 fixed point; PCG32; 20+12-bit handles with 64-bit uids; versioned saves with a migration ladder; schema-generated structs; trigger bytecode; two gate tiers; 17 repo rules; 12 proposals and 6 questions for M0 | \~2 |
| 3.3 | Data and Licensing Register | Three of six GDD datasets unusable commercially (WorldClim non-commercial, GEM CC BY-NC-SA, OSM share-alike obligations); replaced by CHELSA V2.1, the Copernicus DEM water mask and the USGS catalogue; one row still to confirm | \~1 |
| 3.4 | Scope Ledger and Decision Log | Seven protected items; a ten-step cut order starting with per-milestone 360 builds; the four CA additions enter before M1 displacing nothing; 15 logged decisions, 7 awaiting confirmation | \~1 |
| — | This procedure | Written from the above | \~1 |
| Gate A |  | Not yet passed: seven Proposed rows await the owner; GDD edits follow; housekeeping (paste instructions, rename Project and one doc) | owner's time |
| 4 |  | Not started | planned 150 to 200 |

Two things the run showed that the procedure now encodes. First, the licensing register found real problems in a GDD that called its sources "free, public"; it is therefore in Stage 3, before any pipeline work, and not an afterthought. Second, the previous game's post-mortem supplied about a third of the TDD's content; a post-mortem is the cheapest document in the set and the highest-yield, so Stage 5's end and section 8 make writing one mandatory.

## 8. Keeping the procedure true

**After each game**, three updates to this document: the "Took" lines in section 3 get the measured hours; section 7 gets a new worked-example table, and the oldest is kept as a one-line summary; the gates get any line that would have caught a problem that reached the build. The game's post-mortem (its Lessons document) is written first, and this document is updated from it, never from memory.

**During a run**, if a stage is skipped or reordered, the Decision Log records why. If the reason holds up at the end of the game, the procedure changes; if it does not, the next run follows the procedure as written.

**Three numbers say whether the setup worked**, recorded per game in section 7's table and compared across games: hours from Stage 1 to Gate A; foundation decisions reversed after the first milestone (anything in the TDD's proposals or the Scope Ledger's protected list that changed once code was built on it; the target is zero); and licensing or data problems found after the build started (the target is zero, because the register is supposed to find them before). A fourth, softer one: how many of the test plan's predictions matched what the tests found, which says whether the conditions in the Strategy Tests were the right ones.

**The post-mortem has two halves.** The engineering half is the Lessons template in section 5. The design half is new: which pillar held under play and which bent; which test predicted the outcome and which did not; which cut from the Scope Ledger was made, when, and whether it was the right one; and what the first outside players retold. Both halves feed the next run of this procedure.

**Turning it into a skill.** This document is the procedure; a skill is the procedure as something the assistant can be told to run. The skill version would, on a new idea: create the Project files from the section 5 templates, birth the document skeletons with their section lists, walk Stage 1 with the owner, and then draft Stages 2 and 3 one document at a time with the owner confirming each, ending at the Gate A checklist. The document stays the source; the skill reads it. Worth making once a second game has been set up with the procedure and the templates have stopped changing.

**Where this document lives.** It is a studio document, not a game document. It belongs in the studio's own Project (or folder), linked from every game Project's instructions on day one, and in the studio's repository alongside the other templates. A copy inside a game's Project is a pointer, not the source. The first thing a new game's Stage 1 does is link to this document; the last thing a finished game's Stage 5 does is update it.
