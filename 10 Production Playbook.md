# Production Playbook

Oct 15, 2026 · @Jack · Draft for the Owner to confirm

*How the studio takes a game from "Gate B says go" to a finished, successful product, and what the studio does along the way besides writing code. Sovereign is the worked example. It is built on the research report "Solo studio route to launch" (15 Oct 2026, in `Research/`), which has the sources for every figure quoted here. The New Game Setup Procedure gets a game to Gate B. This playbook covers the rest, and 05 covers the Steam mechanics of launch.*

## 1. The one idea

A game is three tracks run side by side, and the studio's job is to keep all three moving:

| Track | Question it answers | Main documents |
| --- | --- | --- |
| **Make** | Is the game good, finished and stable? | GDD, TDD, Scope Ledger, the game's repo |
| **Market** | Will enough people know about it and want it on launch day? | Store page, wishlist log, 05 |
| **Business** | Can it be sold legally, paid for, and supported? | Olive, 07, 09 |

Solo developers almost always run only the first track until the game "feels ready". The research shows why that fails: most wishlists arrive in the last four months before launch, a store page needs 6–12 months to build up, Next Fest can be entered only once, and Valve verification plus the first-title wait add over a month. **Most solo games fail at being found, not at being built.** In 2025 about half of Steam's ~21,000 releases ended the year with 10 or fewer reviews.

## 2. What the studio does: the full set of jobs

About fifteen jobs, not two. The rule from the solo post-mortems and outsourcing research: **keep what is iterative and systemic; buy what can be fully specified in advance.**

| Job | What it produces | Who | Switches on |
| --- | --- | --- | --- |
| **Production** | Milestones, hours log, risk list, cut decisions | Owner; Assistant keeps the records | Day one |
| **Systems design and balance** | The simulation rules, policy model, era and region data | Owner | Day one |
| **Engineering and tools** | Sim core, saves, data and mod format, performance | Owner + Assistant | Day one |
| **QA and playtesting** | Bug database, seeded replay tests, outside playtest rounds | Owner + volunteers + automation | P1 |
| **UX, UI and onboarding** | Controller-navigable UI, tutorial, readable map | Owner designs; visual polish can be bought | P1 (logic), P2 (look) |
| **Accessibility** | Remapping, text size, subtitles, no colour-only information | Owner | P2, designed in with the UI |
| **Art direction and key art** | Style guide, capsule art, logo, screenshots | Owner directs; **buy** capsule art | P2 |
| **Audio and music** | Soundtrack, effects | **Buy or license** | P3 |
| **Trailer** | Store trailer, Next Fest trailer | **Buy** (or Owner, if skilled) | P2 |
| **Localization** | Translated text and store page | **Buy**, batched | Engineering for it at P1; translation at P4 or after launch |
| **Build and release engineering** | CI, Steam branches, patch notes | Owner; **automate** (04 A-07, A-08, A-09) | P1 |
| **Marketing** | Store page, wishlist moments, devlogs, demo, festivals, mailing list | Owner + Assistant drafts | P2 — earlier than feels comfortable |
| **Creator and press relations** | Key campaigns, press kit, curator outreach | Owner, through opt-in platforms | P3 |
| **Business, legal, compliance** | Steamworks account, tax, ratings, privacy policy, AI disclosure | Owner + an hour of lawyer and CPA time | Before P2 |
| **Analytics and live ops** | Crash reports, sales in Olive, patches, DLC | Owner; **automate** (A-10, A-12) | P4 onward |
| **Community** | Discord or forum, replies, mod support | Owner | P2 onward |
| **Post-mortem** | What to change in the studio | Owner + Assistant | L+30 |

The **Assistant's role** in every row is the same: draft, research, automate, keep the records. It never decides, publishes or spends (S-07).

## 3. The milestone route

The procedure's Gates A and B are unchanged. After Gate B, production runs through five milestones, **P1–P5**. Each game's GDD §12 maps its own milestone names onto these and keeps its own gate criteria. Where the GDD and this table differ, the GDD wins for that game.

| | Milestone | Exit criteria (every line yes or no) | What it gives the other tracks |
| --- | --- | --- | --- |
| **Gate A** | Foundation complete | Procedure §4 | — |
| **Test** | Strategy Tests run | Procedure Stage 4 | Measured hours; the strongest hook |
| **Gate B** | Kill, pivot or go | Procedure §4 | — |
| **P1** | **Connected-systems playable** | Every major system present at the lowest fidelity, each with at least one input from and one output to another; seeded runs reproduce exactly; event frequencies tuned so nothing fires far too often or too rarely; text externalized for later translation; placeholder art only | Footage of the systems working. Not yet shown publicly |
| **P2** | **Market slice and store page** | One region and one era at final art quality; UI controller-navigable and readable at 1280×800; capsule art bought; ~30-second gameplay trailer; store page **public**; mailing list and Discord open; privacy policy written | **The market test (§5).** Wishlists begin |
| **P3** | **Alpha — feature lock** | Every 1.0 feature present; data and mod format frozen; scope locked; full end-to-end QA begins; Steam Playtest cohort running | Demo candidate; devlogs; creator list |
| **P4** | **Beta — content lock** | No new features; all 1.0 content in; crash reporting, ratings survey, AI disclosure done; localization strings sent | Public demo; Next Fest; review build |
| **P5** | **Release candidate and gold** | Passes Steam build review; no S1 bugs; save migration tested from every beta save; store assets final | Launch (05 §4) |

**Why P1 comes before a polished slice.** A simulation's fun comes from systems acting on each other, so a polished three-minute slice can't be built until the systems exist. The connected-systems playable (Borut Pfeifer's term) proves the systems first. Sovereign's deterministic core makes this milestone unusually strong, because every balance problem becomes a replayable test. The polished slice comes second, as P2, and its job is marketing.

**Schedules.** Calendars come from measured hours (procedure rule 5). Then pad them: the Concealed Intent solo developer planned 18 months and shipped in about four years. For a part-time developer, double the estimate as a floor.

## 4. Sovereign's route, from today

Sovereign is a political, citizen-level simulation on real geography with a choice of era, a deterministic core, PC on Steam, planned at $19.99–24.99 and shipped complete. Today: Stage 3 done, Stage 3.5 review not run, Gate A not passed.

| Step | What happens | Studio jobs active | Rough size |
| --- | --- | --- | --- |
| 1. Close the foundation | Stage 3.5 review; confirm the 7 Proposed decisions; edit the GDD; Gate A | Production, design | 1–2 weeks |
| 2. Test | Strategy Tests phases (hook test, paper prototype, spreadsheet model, art bar, feasibility spikes); start the hours log on day one | Design, marketing (the hook test is the first marketing work), production | ~12 weeks planned; 150–200 hours |
| 3. Gate B | Kill, pivot or go on the test plan's own numbers | Owner | One sitting |
| 4. Business groundwork, in parallel with P1 | Studio name (S-01); entity decision (S-11); EIN; Steamworks account; $100 fee paid early (verification ~15–30 days, plus the first-title 30-day wait); lawyer and CPA hours (S-18) | Business | A few evenings, spread out |
| 5. P1 Connected-systems playable | Sim core, the 5–7 linked systems on one region and era, headless replay tests, text externalized, data format designed for modding | Engineering, design, QA | From measured hours |
| 6. P2 Market slice and store page | Art direction locked; capsule artist hired; trailer; store page public; mailing list; neutrality policy published (§6) | Art direction, marketing, business, community | From measured hours |
| 7. Market test | Wishlist moments for 3–6 months while P3 is built (§5) | Marketing, Assistant drafts | Runs beside P3 |
| 8. P3 Alpha | Every 1.0 feature; Steam Playtest; data and mod format frozen | Engineering, QA, community | From measured hours |
| 9. P4 Beta and demo | Content lock; public demo; email wishlisters; creator campaign; **Next Fest** 2–4 months before launch | Marketing, creators, QA | — |
| 10. P5 and launch | 05 §4 timeline | All | — |
| 11. Live | Patches, Workshop and mods, first DLC plan | Live ops, community | Years |

**What this means for the calendar:** Next Fest, February 2027 (registration closes Jan 10, 2027), is **not** for Sovereign. It has no public page or demo, and spending its only Fest without momentum gets the median result: under 500 wishlists. The earliest sensible Fest is the first one at least 6 months after the store page goes public, picked once P2 has a date.

## 5. The market test at P2 — Proposed (S-25)

The store page is also an experiment. Wishlists explain only about half of first-month sales, but they are the best early signal there is.

| Benchmark (from the research; mostly secondary-sourced estimates) | Value |
| --- | --- |
| Wishlists to reach Steam's Popular Upcoming list | ~7,000 |
| Target for an experienced solo developer in a strong genre | 15,000–30,000 at launch |
| First-week conversion of wishlists to sales | ~15% under 5k wishlists, ~20% at 5k–40k |
| Worked example | 20,000 launch wishlists at $20 and 20% conversion ≈ $228K gross in year one |
| Median Next Fest entrant | Under 500 wishlists |
| Simulation games reaching 1,000+ reviews (2025) | 4.1% (vs 0.18% for 2D platformers) |

**Proposed rule:** three months after the store page goes public, with at least two wishlist moments run (trailer release, devlog push, a festival or showcase), Sovereign should have **2,000+ wishlists**. Under that, the hook, capsule or genre framing gets reworked **before** more production hours go in. That is a Decision Log row, not a feeling. The threshold is a starting guess for the Owner to set.

## 6. Lessons taken from studios that have done this

| Studio and game | What they did | What the studio takes |
| --- | --- | --- |
| **Positech — Democracy 1–4** (UK micro-studio; Democracy 4 in Early Access Oct 2020 – Jan 2022) | Programmers own the engine; art, sound, music and translation bought; priced at $25 "for quality, not competition"; voiced trailer and pre-launch ads worked; Workshop support built in from day one; **Facebook blocked its ads as political advertising** from 2018, and "tens of thousands of dollars" moved to other ad platforms | Own the sim, buy the art. Price with confidence. Mod support from day one. **Plan ad channels that accept political-game ads** (R-16) |
| **Suzerain** (Torpor Games, small Berlin team) | A fictional Cold War-style state; "multi-perspective political entertainment"; 1.4M players by Nov 2025; grew through ports and DLC | Neutral, multi-perspective framing. A fictional layer is the safe option — Sovereign chose real places, so it needs §7 instead |
| **Papers, Please** (Lucas Pope, solo) | Fictional state; 5M copies in ten years; steady ports | One person, one sharp idea, a long tail |
| **Workers & Resources** (3Division; Hooded Horse) | ~5 years Early Access; after 1.0 sold real-region map DLC and a 1920s–50s "early start" era DLC; tutorial complaints during Early Access | **The model for Sovereign's eras and regions:** ship one era and a bounded map at 1.0, sell more eras and regions as DLC. Onboarding is a design deliverable |
| **Ostriv** (started solo, 2014) | Code and design kept in-house, art delegated; ~210k copies (estimate); still in alpha in 2026; no promised dates; cosmetic DLC repaid its time; slow daily pace, no crunch | Sustainable pace beats sprints. Don't announce dates you can't keep |
| **Shadow Empire** (one designer, 4–5 years; Slitherine) | Very deep wargame, published by a strategy specialist | Depth sells in this genre; expect years |
| **RimWorld** (2–3 people until 2018) | ~5 years of alpha; 1M copies by Feb 2018; five paid expansions; modding at the core; briefly refused classification in Australia in 2022 | Mods and expansions make the business. Ratings rules can bite simulation content |
| **Dwarf Fortress** (two brothers, ~20 years) | 300k+ copies in the first week on Steam at $30 | Even a hit, spread across decades, is about a salary. The job matters until the studio proves otherwise |

**On publishers:** Hooded Horse (strategy specialist) guaranteed at least $100K of marketing per game in 2023, yet its CEO said in January 2026 that most indies should self-publish. Default: self-publish. A publisher offer is a Decision Log row judged on its recoup terms.

**On Early Access:** only 21% of games leaving Early Access in 2026 earned more in their 1.0 month than in their first Early Access month. Early Access is one launch, not two. Sovereign's GDD already says ship complete, and the data supports it.

## 7. What is specific to a real-world political simulation

Sovereign's real geography and eras are its moat and its biggest risk. They invite arguments about accuracy and bias, ad-platform blocks, classification trouble, and a content explosion (every era times every region).

- **Neutrality and model transparency policy — Proposed (S-26).** Published on the store page and in-game: the model is a simplification; formulas and data are visible and moddable; no real politicians or parties (procedure rule 6). Written at P2.
- **Scope rule — Proposed (S-27).** 1.0 ships one era and a bounded map at full depth. Further eras and regions are post-launch updates or DLC, listed in the Scope Ledger. This is the research's answer to the GDD's open launch-era question; the Strategy Tests can still overturn it.
- **Moddable data from P1.** Game rules and region data live in documented files, not code (fits the TDD's schema-generated data).
- **Ad channels** (R-16): don't depend on Meta; budget for platforms and creators that accept political-game content.
- **AI asset provenance log from today** (R-15): Steam's survey (rewritten about January 2026) asks about AI content that ships to players, not about coding help. Log where every shipped asset came from.

## 8. Money: what has to be bought

Illustrative floors from the research, all dated estimates. These go into Sovereign's cash ceiling (procedure Stage 1) and into Olive as they're spent.

| Item | Floor estimate | When |
| --- | --- | --- |
| Steam Direct fee | $100 (recouped after $1,000 revenue) | Business groundwork |
| Lawyer and CPA, about an hour each | ______ | Before P2 |
| Capsule and key art | $250 – $2,000 | P2 |
| Trailer | $500 – $6,000 | P2 (and P4) |
| Music, ~20 minutes | ~$8,000 at the 2025 indie median of $407 a minute | P3 |
| Localization, 5 languages × 30k words | ~€13,500 – €18,000 (2019 rates) | P4 or after launch |
| Ads | ~$1–2 per wishlist | P2 onward, optional |
| Tools (§9) | ~$0 at solo scale | — |

Localization is the biggest line and the easiest to defer. Externalizing text at P1 is free and keeps the option open.

## 9. Tool stack — Proposed (S-28)

| Need | Tool | Cost at solo scale |
| --- | --- | --- |
| Task tracking | GitHub Projects (with the repo) or Codecks | Free |
| CI and Steam upload | GitHub Actions + steamcmd (04 A-07, A-08) | Free tier |
| Playtesting | Steam Playtest + a Discord server | Free |
| Crash reporting | Sentry or BugSplat free tier — **opt-in**, privacy policy first (R-14) | Free up to ~5k–15k events a month |
| Localization | Crowdin free plan | Free up to 60k hosted words |
| Market research | SteamDB, Gamalytic free views | Free |
| Creators | An opt-in platform campaign (Woovit, Keymailer/Partnier, Lurkit) + Steam Curator Connect (100 curators) | Varies — price checked when used |
| Press kit | A static page on the studio site | Free |

## 10. Failure modes and their guards

| What kills solo games | Guard already in the studio |
| --- | --- |
| The core design keeps changing (the Game Outcomes Project's top negative) | Pillars as a filter; one-page hook frozen at Gate A; Decision Log |
| Scope creep | Scope Ledger, cut order, §7 one-era rule |
| Marketing starts at launch | P2 store page is a milestone, not a nice-to-have; §5 market test |
| Spending Next Fest too early | §4: chosen only after P2, 2–4 months before launch |
| Burnout and crunch | Measured hours; overload rule (02 §5); no crunch — crunch even hurt on-time delivery |
| Too complex to learn | Onboarding is P1/P2 work; outside playtests from P1 |
| Platform and policy shocks | R-16 ad channels; R-13 ratings; §7 neutrality policy |

## 11. Changing this document

By Decision Log row. After each launch, §6 gets the studio's own game as a case study and §5's thresholds are reset from real numbers. Sections are appended, never renumbered.
