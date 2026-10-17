# Marketing and Sales Playbook

Oct 15, 2026 · @Jack · Draft for the Owner to confirm (S-36)

*The selling half of the studio. Building makes the game; this document makes people find it, want it, buy it and keep buying it for years. Olive keeps the money, campaigns, ad spend and keys register; this playbook says what the studio **does**. It works with 05 (Steam's launch and discount mechanics) and 10 (when the market track starts). Figures are from the research report "Solo studio route to launch" and Steamworks pages read 15 Oct 2026; second-hand benchmarks are marked as such.*

## 1. How selling on Steam actually works

Six facts shape every workflow below:

1. **You can't buy placement on Steam.** Valve says so outright. Visibility comes from players' actions: wishlists (which drive the Popular Upcoming list), launch-week purchases (top sellers, New and Trending), and later updates and discounts.
2. **Wishlists are the currency before launch.** They explain about half of first-month sales. ~7,000 reaches Popular Upcoming; 15,000–30,000 is a strong solo target *(second-hand, Zukowski)*. Most arrive in the **last four months** before launch.
3. **People need to see a game many times** before they act (Valve). One big announcement does less than a steady series of **beats**.
4. **Strategy, simulation and management sell better than their share of releases** — the studio's genres have a tailwind.
5. **Opt-in creator platforms beat cold email** for small studios by a wide margin (one campaign: 69 of 95 creators made videos; ~30 cold emails got 0 replies).
6. **After launch, each major update earns home-page visibility** (Update Visibility Rounds, shown to owners and wishlisters, usable back to back once launch visibility ends), and **seasonal sales** and **discounts of 20%+** email every wishlister again. A game keeps selling as long as it keeps giving Steam reasons to show it.

## 2. The phases

| Phase | When | Goal | Main workflows |
| --- | --- | --- | --- |
| **0. Position** | From the Idea Brief to P2 | Know the hook, the audience and the comparables before showing anything | M-1 |
| **1. Announce** | P2: store page goes public | Turn the page into a wishlist collector; start owned channels | M-2, M-11, M-13 |
| **2. Build up** | P2 → L−4 months | A beat every 4–6 weeks; creators and festivals; market test (10 §5) | M-3, M-4, M-5, M-7 |
| **3. Peak** | L−4 months → L | Stack the biggest beats: demo, Next Fest, launch date, trailer, creator wave | M-3, M-5, M-6, M-8 |
| **4. Launch** | L−14 days → L+14 | Convert wishlists; hold top sellers; fix fast | M-9 |
| **5. Long tail** | L+30 onward, for years | Updates, sales, bundles, DLC, ports; keep the game visible | M-10, M-3, M-12 |

## 3. The workflows

Each workflow names its trigger, steps, output, who does what, and what can be automated. **Owner** publishes, decides and sends; the **Assistant** drafts, researches, schedules and measures (S-07: nothing goes public without the Owner).

### M-1 Positioning (once per game; revisited at each market test)

**Trigger:** Idea Brief Round 3 done, or before P2.
1. Write the **hook**: one sentence a stranger would repeat, built from brief 3.4 and the tested hook (Strategy Tests).
2. Pick **5–10 comparable games** the target player already owns; record price, reviews, release date (dated).
3. Choose **Steam tags** in order of importance (the first ones matter most for who sees it in queues).
4. Write a **capsule brief** for the artist: the hook, genre signals, three reference capsules, what must read at thumbnail size.
5. Write the **"if you liked X and Y"** line, used in store copy, creator pitches and ads.

**Output:** `Games/<Game>/marketing/positioning.md`. **Automation:** Assistant drafts all five; Owner picks.

### M-2 Store page (built at P2; refreshed before every beat)

**Trigger:** P2 milestone; then 1 week before each beat.
1. Capsules from the artist (M-1 brief); logo.
2. Short description that leads with the hook; long description with animated GIFs of the core decisions.
3. **Gameplay trailer** opening on gameplay within the first seconds; 5+ screenshots that show decisions, not menus.
4. Tags, languages, system requirements, Steam Deck status, content survey (accurately, including AI disclosure, R-15).
5. **Refresh check before each beat:** newest screenshots, current trailer, the beat's news in an Event, nothing stale.

**Output:** the live page. **Automation:** A-18 asset check; Assistant drafts copy and screenshot list.

### M-3 The Beat — the core repeatable procedure

A **beat** is one moment that gives people a reason to look: a trailer, a demo, a festival, a big devlog, an update, a sale, a launch date. Before launch, aim for one every **4–6 weeks**, more in the last four months. After launch, one every **1–3 months**.

| When | Step | Who |
| --- | --- | --- |
| B−21 days | Pick the beat and its one message. **Predict** the wishlists (or sales) it will add: `studio.py predict <Game> count "beat: <name>" <n> wishlists` | Owner picks; Assistant proposes the number from past beats |
| B−14 | Make the assets: clip, GIFs, screenshots, the Steam Event or announcement text, a devlog post, social posts, creator and press notes | Assistant drafts; Owner records footage and edits |
| B−14 | UTM links for every channel (M-13) | Assistant (script) |
| B−10 | Creator outreach for the beat (M-5); festival submissions if it's a festival (M-7) | Owner sends; Assistant prepares lists and drafts |
| B−7 | Store page refresh (M-2) | Owner |
| B−1 | Everything scheduled; mailing list email drafted | Owner |
| **B** | Publish everywhere in one day: Steam Event, devlog, socials, mailing list, Discord. Be present for comments | Owner |
| B+1–3 | Reply, share creator coverage, fix anything broken | Owner |
| B+7 | **Measure:** wishlists added (and deleted), UTM sources, coverage won. Close the prediction: `studio.py actual <P-ID> <n>`. Log the campaign in Olive | Assistant drafts the beat report; Owner confirms |

**Output:** `Games/<Game>/marketing/beats/YYYY-MM-DD <beat>.md` from `Templates/Beat Plan.md`. Over time, the predictions show which kinds of beat actually move wishlists for this studio (13 §4).

### M-4 Content engine (steady output between beats)

**Trigger:** every work session that produces something visible.
1. **Capture as you build:** a 10–30 second clip or a screenshot whenever something looks or plays well. Store in `Games/<Game>/marketing/captures/` with a one-line note.
2. **One capture, many uses:** each good capture becomes a GIF for the store page, a short social clip, a devlog image and a Discord post.
3. **Devlog every two weeks**: what changed, why, one clip, one question for players.
4. **Show decisions and consequences**, not features — management players buy into "what would I do here?"

**Automation:** A-14 drafts devlogs and posts from the build log and captures; Owner posts. No auto-posting.

### M-5 Creators and curators

**Trigger:** the store page is live; then at every major beat.
1. **Build the list** (Assistant researches): YouTube 10k–500k subscribers and Twitch 50–2,000 average viewers who have played the comparable games in the last six months; genre curators on Steam.
2. **Top 20, personal:** a short note to each from the Owner, saying why their audience fits, with a key and the beat date.
3. **Everyone else through an opt-in platform** (Woovit, Keymailer/Partnier, Lurkit — check current terms and price when used) and **Steam Curator Connect** (up to 100 curators, 5 keys each).
4. Log every key in Olive's keys register (recipient, batch, purpose, embargo, outcome). Keys stay in Steamworks.
5. Track coverage; re-contact the creators who covered the last beat first.

**Rules:** keys are given freely, never in exchange for a positive review or any review at all; creators disclose free keys and sponsorships under their own rules (in the US, FTC endorsement rules); the studio never asks them not to. First-time developers wait three weeks after creating an AppID before they can request keys (Steamworks) — create the AppID early.

### M-6 Press and announcements

**Trigger:** announcement, demo, Next Fest, release date, launch, major update.
1. **Press kit** on the studio site: fact sheet, hook, trailer, screenshots, logo, contact. Updated before each press beat.
2. **One-page announcement** per press beat (Assistant drafts); short list of genre outlets and newsletters (Assistant researches, dated).
3. **Embargoed keys** for launch go out at L−14 (05 §4).
Press rarely moves wishlists for small games on its own (no good data either way); treat it as support for creator and Steam beats, not the main engine.

### M-7 Festivals and Steam events

**Trigger:** monthly check of the calendar.
1. **Steam's own events** (from the Steamworks Upcoming Events page): seasonal sales, themed fests and Next Fest. Themed fests welcome Coming Soon games and games with demos as well as released ones. Examples read 15 Oct 2026: Shop Keeper Fest (Jan 25 – Feb 1, 2027), Real-Time Strategy Fest (May 10–17, 2027); Next Fest June 2027 (Jun 14–21); Winter Sale Dec 17, 2026 – Jan 4, 2027; Spring Sale Mar 18–25, 2027; Summer Sale Jun 24 – Jul 8, 2027. **No sports-themed fest is listed**, which matters for Tactica.
2. **Third-party showcases and genre festivals** on Steam and online: kept in `Studio/Marketing/Festival Calendar.md` with each one's dates, deadline, fee and fit, verified when added.
3. Apply when the game fits the theme and has something new to show; every festival is a beat (M-3).

**Automation:** A-29, a monthly scheduled check of Steam's events page and the festival calendar, listing new deadlines in the next 60 days.

### M-8 Demo and Next Fest (once per game)

**Trigger:** P4 (beta), 2–4 months before launch.
1. **Demo scope:** the first 30–60 minutes, polished, ending on a moment that makes people want more and a wishlist button.
2. **Release the demo weeks before the Fest**; within two weeks, use Steam's **"email wishlisters"** for the demo; vet it with the top-20 creators.
3. **Next Fest workback** (Valve): preview submission −5 weeks, demo build review −3 weeks, press preview −11 days. Plan a livestream during the Fest.
4. Keep the demo up after the Fest (Valve encourages it).
5. **Never** spend Next Fest without momentum: the median entrant gains under 500 wishlists; top-10% about 3,000.

### M-9 Launch week

The Steam mechanics are in 05 §4. The marketing part:
- L−14: embargoed keys; creator wave scheduled for L to L+3.
- L: launch email to the mailing list; Steam Event; all channels on one day; be live in Discord and the forums.
- L to L+7: reply to every review that reports a fixable problem only after the fix ships; publish a "thank you + what's next" post on day 3–5 with the first patch.
- The launch discount question is S-29 (wishlisters are emailed at launch either way).

### M-10 The long-tail sales engine (after launch)

The plan for years 1–3, reviewed monthly:

| Lever | How | Rule |
| --- | --- | --- |
| **Major updates** | Each one earns an **Update Visibility Round** (home page for owners and wishlisters) — available once launch visibility ends, usable back to back, needs a real update | Plan 3–4 meaningful updates in year one; each is a beat (M-3) |
| **Seasonal sales** | Winter, Spring, Summer, Autumn; games released 30+ days before the sale can join | Exempt from the 30-day between-discounts cooldown, so they're the default discount vehicle (05 §5) |
| **Discount ladder** | Discounts of **20%+ email every wishlister** | Step depth slowly (e.g. 10% → 20% → 25% in year one); each step is a Decision Log row |
| **Update + sale stacking** | Launch an update into a seasonal sale | The update brings people to the page; the sale converts them |
| **Bundles** | Base game + soundtrack or DLC (Must Purchase Together); a studio bundle once there are two games (Complete The Set, which lets owners buy only what's missing) | Up to three bundles show on the store page |
| **DLC and expansions** | From the Scope Ledger's post-launch list (for Sovereign: eras and regions, 10 §7) | Each DLC launch uses the base game's visibility round |
| **Regional pricing** | Start from Valve's recommended prices for all currencies; a missing currency means the game isn't sold there | Price changes allowed only 30+ days after release; a price rise starts a 30-day discount cooldown |
| **Ports** | Other platforms only after Steam proves the game (charter) | — |

**Monthly sales review (part of the monthly review, 02 §4):** units, revenue, refunds, wishlists remaining, conversion by source, next three months of updates and sales — all from Olive and Steamworks.

### M-11 Owned channels and community

The audience the studio owns doesn't depend on Steam's rules (07 R-10).
- **Mailing list** from the day the store page goes live (privacy policy first, R-14). One email per beat, never more than monthly outside beats.
- **Discord** (or a forum) for players and testers; playtest invites and feedback flow through it.
- **Devlog home** on the studio site; every post links to the Steam page with a UTM link.
- Everything links back to the Steam page. The goal of every channel is a wishlist, and later a purchase.

### M-12 Paid ads (optional, test first)

1. Only after the store page converts organically (wishlists from organic traffic exist).
2. **Test small:** a fixed budget (e.g. $100) on one platform, with UTM links; measure cost per wishlist after the 4-day conversion window.
3. Benchmark: about **$1–2 per wishlist** (2024, second-hand). Above that, stop.
4. **Political or sensitive themes:** expect Meta to block ads as political (Positech's experience, R-16) — test on other platforms first.
5. All spend recorded in Olive as campaigns.

### M-13 Measurement

**UTM links on every outside link to the Steam page** (Steamworks UTM Analytics, read 15 Oct 2026): visits, and for logged-in users, wishlists and purchases within 72 hours of the click; visits update hourly, conversions finalize after 4 days; app and sale pages only.
- Naming: `utm_source` = channel (youtube, reddit, newsletter, discord, festival name), `utm_campaign` = beat (e.g. `demo-2027-05`), `utm_content` = the specific post or creator.
- `python Automation/studio.py link <appid> <source> <campaign> [content]` builds the link and records it in `Studio/Marketing/links.csv`, so every beat report can match sources to results.

**Weekly marketing glance** (inside the weekly review): wishlists added/deleted this week, top three UTM sources, next beat date and its status.

## 4. Rules

1. **Honest marketing only.** No fake reviews, no reviews traded for keys, no sock-puppet accounts, no fabricated quotes, no countdowns or "limited" claims that aren't true. Footage is real gameplay (labelled when it's work in progress).
2. **Nothing public without the Owner** (S-07). The Assistant drafts and schedules; the Owner presses publish and sends every personal email.
3. **Steam's key rules** (Steamworks): don't give non-Steam buyers a better deal than Steam customers; giveaways over 100 keys need a matching Steam offer or Valve's approval; press/beta keys are never sold.
4. **Every beat is predicted and measured** (M-3) — that's how the studio learns which marketing works for it (13).
5. **Marketing time is real time.** It's logged under the Marketing hat; from P2 on, plan for a third or more of studio hours on marketing in the last four months before launch (Concealed Intent's developer couldn't market and develop at the same time).

## 5. Where things live

| Thing | Where |
| --- | --- |
| Positioning, beats, captures, store copy drafts | `Games/<Game>/marketing/` |
| Festival calendar, UTM link register | `Studio/Marketing/` |
| Campaigns, ad spend, keys register, sales, wishlists | Olive (06) |
| Store page, keys, UTM reports, sales reports | Steamworks |

## 6. Applying it to Tactica now

Tactica is in Build with no store page, so it's at Phase 0. In order:
1. **Name check** on "Tactica" (R-04) — the store page and every capture will carry the name.
2. **M-1 positioning:** hook, comparables (football management games on Steam), tags, capsule brief. Note there's no sports-themed Steam fest, so festivals will lean on management and strategy themes and third-party showcases.
3. **Start the capture habit** (M-4) today — footage takes longest to build up.
4. Studio prerequisites before the page (05 §3): name, entity, EIN, Steamworks account, AppID (also starts the three-week key-request wait).
5. **P2: store page live**, mailing list and Discord open, first beat; the market test clock starts (10 §5).

## 7. Changing this document

By Decision Log row. After each beat and each launch, the beat reports and calibration feed lessons (13). Sections are appended, never renumbered.

## 8. Sources (read 15 Oct 2026)

- Steamworks, Visibility on Steam: https://partner.steamgames.com/doc/marketing/visibility
- Steamworks, Upcoming events: https://partner.steamgames.com/doc/marketing/upcoming_events
- Steamworks, UTM Analytics: https://partner.steamgames.com/doc/marketing/utm_analytics
- Steamworks, Bundles: https://partner.steamgames.com/doc/store/application/bundles
- Steamworks, Pricing: https://partner.steamgames.com/doc/store/pricing
- Steamworks, Steam Keys: https://partner.steamgames.com/doc/features/keys
- Research report "Solo studio route to launch" (`Research/`), for wishlist, Next Fest, creator and ad benchmarks

## 9. Channels beyond Steam

Where each game's audience gathers outside Steam, which 3–5 channels it uses, how it enters them and how they're tested is defined in **15 Audience and Channels**. Every beat (M-3) goes out on the channels in the game's channel map.
