# Launch and Live Ops Playbook

Oct 15, 2026 · @Jack · Draft for the Owner to confirm

*The studio's repeatable path from "Gate B says go" to a game on sale, supported, discounted on Steam's rules, and eventually retired. Every game copies §4 into its own launch checklist. Steam's rules below were read from Steamworks on 15 Oct 2026 and are re-checked at L−90 for each launch.*

## 1. Steam rules that set the timeline

Read 15 Oct 2026 from the Steamworks documentation (sources in §9).

| Rule | Value |
| --- | --- |
| Steam Direct fee | $100 per product, non-refundable; recouped once the product reaches $1,000 adjusted gross revenue |
| Account verification | Bank, tax and identity paperwork, about 15–30 days |
| First-titles wait | For a developer's first few titles, 30 days between paying the fee and release |
| Review | Store page and build each reviewed by Valve, about 1–5 days |
| Coming Soon page | Must be public for **at least two weeks** before release |
| Launch discount | Optional; 10–40% (Valve suggests about 10–15%); runs 7–14 days; must be set up **before** release |
| After release | No other discount for 30 days |
| Between discounts | 30 days, except Seasonal Sale discounts created in the dashboard for that sale |
| Price increase | 30-day discount cooldown after any base price increase; no price increase within 30 days of release; no base price change during or while a discount is scheduled |
| Standard discount | 10–95%, 1–14 days |
| Steam Next Fest | A game may appear **once, ever**. Needs a public store page and a public demo by the start. February 2027: Feb 22 – Mar 1, registration closes Jan 10, 2027. Next edition planned for June 2027 |

## 2. The studio's own launch rules — Proposed

1. **The store page goes up as early as it honestly can** — the procedure says at least six months before launch, so wishlists have time to build. Steam's two-week minimum is a floor, not a plan.
2. **Next Fest is spent once, deliberately.** Each game picks its Fest after its store page has been public for months (10 §4), 2–4 months before launch, with the demo public weeks before the Fest. The median entrant without momentum gains under 500 wishlists.
3. **Launch discount: 10%** unless the Strategy Tests say otherwise — under review (S-29): wishlisters are emailed at launch either way, and Positech found a small launch discount just cost revenue.
4. **Price is set from the Competitive Analysis**, written in the game's Decision Log, and not raised after launch.
5. **No launch in the same week as a Steam seasonal sale or a major release in the same genre.** Checked at L−90.
6. **Builds go to a beta branch first**, are played by the Owner on a clean machine, and only then are promoted (S-08).
7. **The game ships complete** (01 §3). Post-launch updates are listed in the Scope Ledger, not promised on the store page.

## 3. Business prerequisites (once per studio, before the first game's page)

These are studio items, not game items. They come first because the Steamworks account carries a legal name, bank account and tax identity, and changing them later is painful.

- [ ] Studio name chosen and searched for conflicts (S-01, 07 §R-03)
- [ ] Entity decision: publish as Jack (sole proprietor) or as an LLC formed first (S-11, 07 §R-02)
- [ ] EIN obtained from the IRS (free) so the Steam tax interview and any 1099s use it instead of an SSN
- [ ] If trading as a sole proprietor under the studio name: Certificate of Assumed Name (DBA) filed with the county clerk
- [ ] Thunderbuilt employment agreement read for IP and outside-work clauses (S-10, 07 §R-01)
- [ ] Studio email, domain, and password manager entries created (09)
- [ ] Separate bank account for the game business, or a decision not to have one yet, recorded in Olive
- [ ] Steamworks account created; $100 fee paid; tax and bank verification done (15–30 days)
- [ ] Olive game entity ready to receive Steam payouts, fees and costs (06)

## 4. Launch timeline

L = launch day. Dates are back-filled into each game's production calendar from measured hours.

| When | Do | Hat |
| --- | --- | --- |
| **Gate B + 1 week** | Studio prerequisites (§3) checked; Steamworks app created; $100 fee paid (starts the 30-day clock for first titles) | Business |
| **L−7 months** | Decide supported languages, Steam Deck target and accessibility options for 1.0 (they change the store page and the scope); privacy policy written if any email will be collected (07 R-14) | Design, Business |
| **L−6 months or earlier** | Store page public as Coming Soon: capsules, short and long description from the tested hook, 5+ screenshots, tags, system requirements. Demo public at the same time (procedure Stage 5). Wishlist tracking begins in Olive (A-12) | Marketing |
| **L−6 to L−3 months** | Next Fest chosen and registered by its deadline; devlog every two weeks (A-14); a press and creator list started in Olive | Marketing |
| **L−90 days** | Re-read §1 rules from Steamworks; confirm the date clears seasonal sales and big genre releases; set the price; plan the first 12 months of discounts against the rules (A-13) | Business |
| **L−60 days** | Feature-complete build; Scope Ledger frozen for 1.0; trailer done | Production |
| **L−30 days** | Release candidate on the beta branch; store page and build submitted for review (1–5 days, leave slack); launch discount set; press and creator keys requested from Steamworks and logged in Olive (A-21); launch checklist copied into the game folder | Engineering, Marketing |
| **L−14 days** | Hard floor: Coming Soon page has been public at least two weeks. Release date locked in Steamworks. Embargoed keys sent | Marketing |
| **L−7 days** | Clean-machine install test from Steam; save migration tested from every beta save; crash reporting checked; review digest (A-10) switched to daily | Engineering |
| **L** | Promote the build; announce; watch reviews, refunds and crash reports; no new features | All |
| **L+1 to L+14** | Hotfix window: fixes only, through beta → default; reply to bug reports; daily digest | Engineering, Community |
| **L+14** | Post-mortem drafting begins (A-17) | Production |
| **L+30** | First money close in Olive; first discount now allowed; stage moves to Live; post-mortem written (01 §7.1) and the procedure updated from it (procedure §8) | Business, Production |

## 5. Pricing and discounts after launch

- Discounts are planned a quarter ahead on a calendar checked by A-13 against §1.
- Seasonal sales are the default discount vehicle because they are exempt from the 30-day between-discount cooldown.
- Discount depth steps down slowly (for example 10% → 20% → 25% over the first year); the steps are a Decision Log row per game.
- Revenue, units, refunds and wishlist conversion per sale go into Olive so the next game's pricing uses real numbers.

## 6. Live operations

| Activity | Rule |
| --- | --- |
| **Support time** | A Live game gets a fixed weekly budget (proposed 2 hours) from the studio's hours, logged under the Community hat |
| **Reviews** | Weekly digest (A-10). Reply only to reviews with a fixable problem or a factual error, and only after the fix ships |
| **Bugs** | Every bug report becomes a GitHub issue (A-11) with severity: S1 crash or save loss — fix this week; S2 broken feature — next patch; S3 cosmetic — batched |
| **Patches** | Hotfixes as needed in the first two weeks; after that, a planned cadence (proposed monthly, then quarterly) written in the game's calendar |
| **Saves** | Every patch passes the save round-trip test from every shipped version (TDD §10) |
| **Content updates** | Only from the Scope Ledger's post-launch list; each one is a mini-milestone with its own gate |
| **Refunds** | Refund rate watched in Olive per week; a spike is a S1 investigation |

## 7. Maintenance and sunset

- **Maintenance** is declared by the Owner when the support budget is under 1 hour a week for two months: the game takes only S1 fixes and seasonal sales.
- **Sunset** keeps the game on sale unless there is a reason to remove it; a sunset post-mortem records lifetime numbers and is filed beside the launch post-mortem.

## 8. Changing this document

By Decision Log row. §1 is re-read from Steamworks at each L−90 and its date updated. Sections are appended, never renumbered.

## 9. Sources (read 15 Oct 2026)

- Steamworks, Steam Direct: https://partner.steamgames.com/steamdirect
- Steamworks, Discounting: https://partner.steamgames.com/doc/marketing/discounts
- Steamworks, Steam Next Fest February 2027: https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest/feb_2027 (its eligibility text is inconsistent about whether the game must release after the Fest; confirm with Steamworks support if it matters)
