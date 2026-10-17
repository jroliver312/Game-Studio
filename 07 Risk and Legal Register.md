# Risk and Legal Register

Oct 15, 2026 · @Jack · Draft for the Owner to confirm

*What could hurt the studio, how likely and how badly, what is done about it, and by when. Reviewed at every monthly review. This is a working list written by an assistant, not legal or tax advice; items marked **Ask a professional** are where an hour with a lawyer or the CPA is cheaper than a mistake.*

## 1. How to read it

**Likelihood** and **impact** are Low / Medium / High. **Status:** Open, Mitigating, Accepted (with reason), Closed (with date). Rows are appended and never deleted.

## 2. The register

| ID | Risk | L | I | Mitigation | Owner action and date | Status |
| --- | --- | --- | --- | --- | --- | --- |
| **R-01** | **Employer claims the games.** Jack is employed by Thunderbuilt as a developer. Employment agreements often assign inventions to the employer. New York Labor Law §203-f makes such a clause unenforceable for work done **entirely on your own time, without the employer's equipment, supplies, facilities or trade secrets** — unless it **relates to the employer's business or anticipated R&D**, or results from work done for the employer. | M | H | Read the signed agreement for invention-assignment, moonlighting and non-compete clauses. Confirm Thunderbuilt's business does not include games. Never use a work machine, work account, work time, work code or work AI subscription for studio work. Keep the git history (timestamps) as the record. If the agreement is broad, ask for a short written acknowledgment that the games are outside it. **Ask a professional** if anything is unclear. | Read the agreement before any public store page (S-10) | Open |
| **R-02** | **Wrong entity at signup.** The Steamworks account, store page and payouts carry a legal name and tax identity. Publishing as a sole proprietor and forming an LLC later means moving the IP and possibly the Steam account. A sole proprietorship also puts personal assets behind any claim against a game. | M | M | Decide before creating the Steamworks account whether to form the LLC first (S-11). If staying sole-prop, record it as accepted, keep the books separate in Olive, and plan the IP assignment for when the LLC forms. Ask Steamworks support how a partner account is transferred to an entity before relying on it. Get an EIN either way, so the Steam tax interview does not carry Jack's SSN. **Ask a professional** (CPA on tax effect, lawyer on formation). | Decide before Steamworks signup | Open |
| **R-03** | **Studio name conflict.** A name already used by another game company forces a rebrand after the store page, logo and social handles exist. | M | M | Before choosing: USPTO trademark search (classes 9 and 41), Steam developer search, domain and main social handles. Consider registering the mark once revenue justifies it. If trading as a sole proprietor under the name, file a Certificate of Assumed Name (DBA) with the county clerk. | With S-01 | Open |
| **R-04** | **Game name conflicts.** The working title "FC26" collided with *EA Sports FC 26*; renamed to **Tactica** on 2026-10-15 (S-22). "Tactica" is not free of neighbours: *Persona 5 Tactica* (Atlus/SEGA, Steam, Nov 2023) shares the word, so a Steam search for "Tactica" will surface it first. Different genre and a single common word lower the legal risk, but it is not cleared until searched. | M | M | Run the R-03 search on "Tactica" (USPTO classes 9 and 41, Steam, domains). Consider a distinctive subtitle that also helps search (e.g. *Tactica: <something>*). Keep "FC26" only as an internal codename and out of every public file. | Before the store page | Mitigating |
| **R-05** | **Content and data licensing.** A dataset, font, sound or library with non-commercial or share-alike terms ends up in a shipped game. Sovereign's register already found three of six GDD datasets unusable. | M | H | Every game keeps a Data and Licensing Register (procedure Stage 3); quarterly re-check (A-15); the attribution file ships with the game. Tactica: confirm its player names, club generator and any fonts or libraries are in a register too. | Per game, at Gate A; Tactica before release candidate | Mitigating |
| **R-06** | **Likeness and real-world IP in sports and political games.** Real club crests, kits, league names, players or politicians. | M | H | Fictional from the first word (procedure rule 6). Tactica is fictional by design; Sovereign uses archetypes. A pre-launch sweep of the shipped data for real names. | Release candidate of each game | Mitigating |
| **R-07** | **Taxes.** Self-employment tax and quarterly estimated payments on game income; Steam's tax interview; state sales tax and foreign VAT on digital sales. | M | M | Olive tracks income and estimates. Complete Steamworks' tax interview correctly. Confirm in Steamworks' documentation how Valve handles sales tax and VAT on Steam sales before assuming it is handled. Give the CPA the game entity's year-end CSV package. **Ask a professional** before the first payout. | Before the first payout | Open |
| **R-08** | **Overcommitment.** A full-time job, Olive, the rental, the homestead and the studio compete for one person's hours. The likeliest way the studio fails is not a bad game but an unfinished one. | H | H | WIP limits (02 §3); measured hours; overload rule (02 §5); time boxes in the procedure; a kill-by date for every game in Setup. | Weekly review | Mitigating |
| **R-09** | **Single point of failure.** Jack is the only person who can log in, build or ship. Lost credentials, a dead drive or illness stops everything. (The Beelink's admin password is already a live example.) | M | H | Password manager with recovery codes; a sealed paper copy of the master recovery details; every repo has a remote; backups watched (A-20); 09 lists every account and how to recover it. | 09 filled within a month | Open |
| **R-10** | **Platform dependence.** Steam controls discovery, fees, rules and payouts. A rule change or an account problem hits all revenue at once. | M | M | Accepted for the first games (Steam is where PC players buy). Keep a studio mailing list and website the studio owns. Revisit other stores after the first launch. | Quarterly | Accepted |
| **R-11** | **Scope creep.** A system grows until the game cannot ship. | H | H | Scope Ledger, cut order, "no new system without a cut" (procedure Stage 2). | Each milestone gate | Mitigating |
| **R-12** | **Lost work on the game machine.** Tactica is a single HTML file on a different computer from Olive. | M | H | Confirm it is in a private repository with a remote and pushed after every session; A-20 watches it. | This week | Open |
| **R-13** | **Age rating and storefront content rules.** Mature themes in political simulation (Sovereign's "hard subject matter"). | L | M | Answer Steam's content survey accurately; GDD §13's approach to hard subject matter; console ratings (IARC/ESRB) only if a console port is ever planned. | Store page | Open |
| **R-14** | **Player data and privacy.** Crash reports, analytics or an email list collect personal data. | L | M | Default: collect nothing. A short privacy policy before the first email address is collected (mailing list, R-10); an EULA and crash-reporting terms before launch. | Before the first email is collected; EULA by L−60 | Open |
| **R-15** | **AI-assisted work.** Questions from players or platforms about AI-generated content; copyright in purely AI-generated assets is uncertain. | M | M | Steamworks' content survey (read 15 Oct 2026; rewritten about January 2026) asks about AI content that ships and is consumed by players, or is generated while the game runs. Coding help ("efficiency gains") is outside it. Keep an asset provenance log from today; re-read the survey when the store page is built and answer accurately. 52% of developers in GDC's 2026 survey said generative AI hurts the industry, so a disclosure on a premium page has a reputation cost. Keep the creative decisions and final assets human-made or human-directed, and keep the drafting records. | Store page | Open |
| **R-16** | **Political-game ads blocked.** From 2018 Facebook repeatedly blocked Democracy's ads as political advertising; Positech moved "tens of thousands of dollars" of spend elsewhere. Sovereign will hit the same wall. | H | M | Don't plan Meta ads as a main channel. Budget creators, Steam festivals and platforms that accept the content; test one small ad before budgeting. | P2 | Open |
| **R-17** | **Real-world accuracy and bias disputes.** A policy model on real places becomes a public argument (Democracy's critics disputed its assumptions on crime, drugs and labour). | M | M | Neutrality and model-transparency policy (S-26); inspectable, moddable data; no real politicians or parties; a "simplification" statement on the store page. | P2 | Open |

## 3. Professional help budget

One block of professional time before the first store page is worth more than any template:

- **Lawyer, about an hour:** R-01 (read the employment agreement with you; ask whether §203-f's "inventions" reaches game code and art, and how broadly Thunderbuilt's "business" would be read if it is a software firm — both untested), R-02 (entity timing and IP assignment), R-03/R-04 (name clearance).
- **CPA, about an hour:** R-07 (estimates, Steam income, sales tax/VAT), and how the game entity's books should hand over at year end.

Cost goes in the game entity's books in Olive and counts toward the first game's cash ceiling.

## 4. Changing this document

Rows are added with the next R- number. A closed risk keeps its row with the date and what closed it. Sections are appended, never renumbered.

## 5. Sources

- N.Y. Labor Law §203-f (read 15 Oct 2026): https://newyork.public.law/laws/n.y._labor_law_section_203-f
- Research report "Solo studio route to launch" (15 Oct 2026, `Research/`) for R-15 to R-17
- Persona 5 Tactica on Steam (read 15 Oct 2026, via SteamPulse): https://steampulse.org/game/2254740
