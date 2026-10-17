# Olive Boundary

Oct 15, 2026 · @Jack · Draft for the Owner to confirm

*Exactly what Olive does for the studio, what stays in the studio's own documents and tools, and how information moves between them. The studio is Olive's first game-business user, so this document doubles as the requirements list for Olive's game-business setup.*

## 1. The line

**Olive owns the money and the outside-world records. The studio folder owns the plans, the designs and the decisions. Steamworks owns the store and the keys. The game repository owns the code.**

| Lives in | What |
| --- | --- |
| **Olive — game entity** | Accounting and taxes (Schedule C while a sole proprietorship); bank account; Steam payouts and fees; studio costs (tools, art, legal, hardware share); financing; sales and revenue by product and period; scheduled sales; marketing campaigns and ad spend across platforms; the keys register (recipient, batch, purpose, embargo, activated, outcome — never the keys); the build register (as Events); review feedback fed back to engineering; year-end CSV package for the CPA |
| **Studio folder and Project** | Charter, operating model, pipeline, procedures, templates, studio Decision Log, risk register, accounts register, review notes |
| **Game Project and repository** | GDD, Competitive Analysis, Strategy Tests, TDD, Licensing Register, Scope Ledger and Decision Log; code, build log, issues |
| **Steamworks** | Store page, builds, branches, the actual keys, official sales reports, payouts |
| **Password manager** | Every login, API key and recovery code (09) |

These follow decisions already made in Olive: the game sells on Steam (2026-09-01); the game entity covers the primals plus sales, scheduled sales, campaigns, ad spend, engineering feedback and Steam reviews (2026-09-21); keys are never stored in Olive and builds are Events (2026-09-27).

## 2. Flows

| From | To | What | How | Automation |
| --- | --- | --- | --- | --- |
| Steamworks | Olive | Sales, units, refunds, wishlists, payouts | Report import | A-12 |
| Bank | Olive | Payouts landing, costs paid | Same import or connection as other Olive books | Olive |
| Steam reviews | Studio digest → Olive feedback + GitHub issues | Bugs, requests, sentiment | Weekly digest | A-10, A-11 |
| Game repo | Olive build register | Version, date, branch, notes | Event per release | A-08 writes it |
| Studio | Olive | Scheduled sales and campaigns | Planned in the studio, recorded in Olive | A-13 checks the dates |
| Studio beats (14 M-3) | Olive | Each beat as a campaign: dates, spend, keys sent, UTM sources and results from the beat report | Beat report at B+7 | A-31 drafts; A-28 links |
| Olive | Studio reviews | Monthly P&L, cash, wishlist trend, ad return | Monthly close | A-03 reads it |
| Studio hours log | Studio only | Hours by hat | CSV | A-04 — not money, so not in Olive |

## 3. What the studio needs from Olive, in order

Olive paused game-studio work on 2026-09-28 until the game is finished. These are the items the studio needs, and when, so that pause can end on time rather than in a rush.

| Need | Needed by |
| --- | --- |
| Game entity books with a Schedule C chart of accounts; studio costs entered as they happen | Now (costs already exist: tools, hardware) |
| Steam payout and fee entries | The first payout (about a month after the first sales) |
| Keys register | L−30 of the first launch |
| Build register Events | First Steam beta build |
| Sales and wishlist import | Store page live (wishlists) / launch (sales) |
| Scheduled sales and campaigns | L−90 of the first launch |
| Review feedback loop | Launch |
| Year-end CPA package for the game entity | Tax season after the first sales year |

## 4. Rules

- The studio never stores money figures in its own documents except as dated quotes from Olive.
- Olive never holds design documents, secrets or the keys themselves.
- A cost or a sale that is not in Olive did not happen, as far as the studio's success measures (01 §7) are concerned.

## 5. Changing this document

By Decision Log row, in step with the matching Olive board item. Sections are appended, never renumbered.
