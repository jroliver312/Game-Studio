# Audience and Channels

Oct 15, 2026 · @Jack · Draft for the Owner to confirm (S-37)

*Once the studio knows who a game is for (14 M-1), this procedure finds where those people spend time **outside Steam**, picks the few places worth the studio's limited hours, and tests them. It sits between positioning and the beat (14 M-3): every beat goes out on the channels this map chose. Research notes behind it: `Research/` (15 Oct 2026). Community sizes are dated third-party snapshots; Reddit was not reachable by the research tools, so **no subreddit's self-promotion rules were verified** — reading them is a required step (C-4).*

## 1. The principle

A solo studio can't be everywhere. It picks **3–5 home channels** where its players already gather, shows up there as a member rather than an advertiser, and makes things those communities want to share. Everything links back to the Steam page with a tracking link, and channels that don't produce wishlists for the hours they take get dropped.

What the evidence says about channel types for indie games (Chris Zukowski's ranking and case studies; details in the research notes):

| Channel type | What it does | Evidence |
| --- | --- | --- |
| **Festivals and demos** | Biggest single source for most indies | Zukowski ranks them first. Caution: one game with ~12k mostly-festival wishlists converted at 1.9% on day one vs a ~12% median — wishlists from browsing crowds can be shallow |
| **Short video (TikTok, YouTube Shorts)** | Occasional huge reach | Ranked second; the documented big case is a cozy game (~2.7M views, ~75k wishlists, 2024). No strategy-specific data |
| **Creators (YouTube, Twitch)** | Most reliable for systemic games | One creator video drove 15–20% of one indie's sales (2021). SplatterCat (~669k subscribers) favours systemic, replayable new releases |
| **Reddit** | Spiky: usually small, occasionally huge | Typical post ~100–150 wishlists (2026 estimate). Laysara, a two-person city builder: one 30-second clip on r/gaming → 3.2M views, 11,000+ wishlists in a day — after 11 ordinary posts from that account first |
| **Press** | Credibility more than sales | One big-site article ≈ 50 sales in a 2021 post-mortem |
| **Twitter/X** | Mostly other developers | "Echo chamber of devs" (2021 post-mortem); ranked last |
| **Discord, mailing list** | Keep people, don't find them | A funnel stage after the Steam page is live, not a discovery channel |

## 2. The procedure

### C-1 Audience profile (one page per game)

From the Idea Brief (1.6, 1.9) and positioning (14 M-1):
- **Core player:** who they are, what they play now, what they're unhappy with, how much time they have.
- **Adjacent audiences:** people outside the genre who'd care about the subject (football fans, map and history enthusiasts, civics teachers).
- **What they share:** the kind of thing this audience posts and passes around (stories, screenshots, maps, stats, "what would you do?" dilemmas).

### C-2 Find the watering holes

List candidate places in six categories. **Only list places confirmed to exist**, with size and the date read:

| Category | Examples |
| --- | --- |
| Communities | Subreddits, Discord servers, fan forums and sites |
| Creators | YouTube and Twitch channels who play the comparable games; short-video creators |
| Publications | Genre newsletters and Substacks, sites, podcasts |
| Interest communities outside gaming | Sport, history, maps, education — only where the game genuinely belongs |
| Other storefronts and demo platforms | itch.io (demos, devlogs), other stores later |
| Owned | Studio site and devlog, mailing list, Discord |

### C-3 Score and choose

Score each candidate 1–5 on four things, then pick **3–5 home channels** and at most **2 experiments**:

| Factor | Question |
| --- | --- |
| **Fit** | Do these people play this kind of game? |
| **Reach** | How many, and how active? |
| **Cost** | Hours per beat to do it well (lower is better) |
| **Openness** | Do the rules welcome developers showing their own work? |

A channel with Openness 1 (rules forbid it) is never used, however big.

### C-4 Enter as a member

Before the first promotional post anywhere:
1. **Read the rules page** (for Reddit, `old.reddit.com/r/NAME/about/rules` and the wiki) and record what it says and the date in the channel map: self-promotion limits, flair, allowed days, developer disclosure.
2. **Take part first.** Comment, answer questions, share things that aren't yours, for a few weeks. (Laysara's developer had 11 ordinary posts before the one that went viral.)
3. **Say you're the developer**, every time.
4. **Respect frequency limits.** Where none are written, at most one post per game per month per community (r/CityBuilders' own rule) and never more than one in ten of your posts about your own game.

### C-5 Make things worth sharing

Each home channel gets content in the form it already likes. Better still, **build shareability into the game**: a one-click export of the thing players would want to show off (a final league table and season story, an alternate-history map), with the game's name on it. That's a design decision, so it goes to the game's Decision Log.

### C-6 Test, keep or drop

- Every channel gets its own `utm_source` (14 M-13) and is tried on **2–3 beats**.
- At each monthly review, compare **wishlists per hour spent** by channel (UTM conversions from Steamworks ÷ hours logged under Marketing for that channel).
- Drop the weakest home channel after three beats if it's clearly behind; promote an experiment that beat it.
- Log a prediction per channel per beat (13 §4) so the studio learns which channels work for **its** games.

## 3. Channel playbooks

| Channel | Do | Don't |
| --- | --- | --- |
| **Reddit** | Short gameplay clips (under ~30 s) and striking screenshots; titles that describe what's happening, not "check out my game"; reply to every comment; post when the sub is active | Post without reading the rules; post the same thing to many subs in one day; ask for upvotes; use other accounts |
| **YouTube and Twitch creators** | 14 M-5: short personal email to the top 20 with teaser image, press kit link, Steam link and a key; opt-in platforms for the rest; small and mid-size creators who play the comparables | Mass cold email; ask for a positive review; expect coverage of a build that isn't stable |
| **Short video** | Vertical 15–30 s clips of one surprising moment; captioned; experiment only until it shows results | Spend hours on trends with no game footage in them |
| **Discord** | Studio server opens with the Steam page: playtests, feedback, devlog drops; join communities' servers as a member | Advertise in other servers' general channels; DM members |
| **Fan sites and forums** | Offer a feature, interview or a key for a review; ask moderators first | Post ads in threads; argue with fans of the big competitor |
| **Newsletters, Substacks, podcasts** | Short pitch with a hook, GIF and Steam link, timed to a beat | Pay for "coverage" that isn't labelled as an ad |
| **Interest communities outside gaming** | Share genuinely interesting output (a map, a stat, a story) that stands on its own; mention the game only where rules allow | Treat them as ad space |
| **itch.io** | Host a demo or prototype for early feedback; devlogs | Split the audience before launch — the Steam page is where wishlists count |
| **Owned** (site, devlog, mailing list) | Every post links to Steam with UTM; one email per beat | Let them go quiet between beats |

## 4. Rules

1. **Honest and disclosed.** Always say you're the developer. No fake accounts, vote manipulation, paid upvotes, astroturfing or undisclosed paid posts.
2. **Each community's rules win.** Read and date them before posting (C-4); if unclear, ask the moderators.
3. **Never run down competitors.** Say what your game does; let players compare.
4. **Owner posts.** The Assistant researches, drafts and schedules; the Owner posts and replies (S-07).
5. **Re-check rules** every six months for home channels; communities change their policies.

## 5. Where it lives

Each game keeps `Games/<Game>/marketing/channel-map.md` from `Templates/Channel Map.md`: the profile (C-1), every candidate with size, date and rules read (C-2, C-4), scores (C-3), home channels and experiments, and results per beat (C-6).

## 6. Worked map: Tactica

**Audience:** players of football management games who want depth; many are frustrated right now.

**The timing window (the biggest finding):**
- *Football Manager 26* launched 4 Nov 2025 and is still **"Mostly Negative"** — about **36% positive across ~36,000 reviews** on 15 Oct 2026 — with concurrent players far below its peak. It entered Steam's all-time worst-rated list.
- *Football Manager 27* is confirmed for **10 Nov 2026** at £49.99, on Game Pass from day one.
- Implication: two windows when FM players look around — **mid-November to December 2026**, as people judge whether FM27 fixed FM26, and the **spring–summer off-season**. Launching in FM27's launch week would be drowned out. Tactica can't launch in the first window, but **its store page and first beat could catch it** if the studio prerequisites move fast (S-38).
- The one well-documented indie case, *Football, Tactics & Glory* (100k+ Steam copies by Aug 2024), timed its full launch just before a World Cup, sold yearly updates as half-price DLC, let players build leagues in an editor and share them in its own Discord, and pitched "depth without FM's time cost".

**Candidate channels (sizes are third-party snapshots; rules not yet read):**

| Channel | Size (date) | Notes |
| --- | --- | --- |
| r/footballmanagergames | ~544k (2026-10-13) | Largest football-management sub. Read rules first |
| r/footballmanager | ~82k (2026-10-02) | Describes itself as FM-series only — likely closed to other games; check |
| r/soccer | ~8.8M | Huge, strict; probably only for genuinely football content |
| r/indiegaming, r/indiegames, r/playmygame, r/gamedev Screenshot Saturday | 60k–1.8M (2026) | Indie-friendly; r/playmygame is built for developers |
| SortItOutSI (site + Discord ~17,600, Oct 2026) | — | Ran "5 alternative football managing games" (Apr 2025), still drawing comments in Sept 2026 — a natural pitch for inclusion in an update |
| Union of FM Players Discord | ~2,970 | Ask moderators |
| FM YouTubers and streamers | e.g. Lollujo ~203k, Zealand ~118k YT / ~57k Twitch | The biggest appear tied to FM; **small and mid-size FM creators** are likelier targets |
| FM Substacks (FM Projects, Sports Untold); The Zealand Podcast | unsized | Pitch at beats |

**Shareability idea (to Tactica's Decision Log):** an end-of-season export — a card with the final table, the story of the season and the seed — so players can post their careers. "Saving your saves" style series show this audience loves career stories.

**Suggested home channels to test first:** r/footballmanagergames (if rules allow), small/mid FM YouTubers, SortItOutSI, indie subs, own Discord. Experiment: short clips of dramatic match moments.

## 7. Worked map: Sovereign

**Audience:** strategy and political-sim players; adjacent: alternate-history and map enthusiasts, history buffs, civics educators.

**Candidate channels (third-party snapshots; rules not yet read except where noted):**

| Channel | Size (date) | Notes |
| --- | --- | --- |
| r/imaginarymaps | ~565k (2026-09-30) | Original-content flairs dominate — a great fit for exported alternate-history maps |
| r/AlternateHistory | ~272k (2026-09-30) | |
| r/HistoryWhatIf | ~200k (2026-09-30) | Scenario prompts ("what if…") are natural content |
| r/MapPorn | ~6.4M (2026-09-30) | Only maps good enough to stand on their own |
| r/paradoxplaza | ~270k (2026-10-15) | Has an "Other" flair; non-Paradox posts appear |
| r/4Xgaming | ~54k (2026-09-29) | Moderators watch for ad-like posts (2023 note) |
| r/BaseBuildingGames, r/CityBuilders | ~86k, ~25k | r/CityBuilders: one post per game per month |
| r/politicalgames | exists, unsized | Check activity |
| Paradox forums | — | **Not a venue**: "Other Games" is for Paradox titles only |
| SplatterCat and similar strategy creators | ~669k | Wants a short email, teaser images, press kit and Steam link; values strong key art |
| One More Turn (weekly strategy Substack) | unsized | Invites submissions |
| Wargamer | — | Mostly tabletop now; developer promotion is paid placement |
| Civics education | — | Precedent: Germany's Federal Agency for Civic Education reviews *Suzerain* in its political-education games section — a post-launch angle |

**Shareability idea (to Sovereign's Decision Log, S-39):** export the world map at any point in a game as an image with era, outcome and seed — the native content of the map and alternate-history communities, which are larger than the strategy subs. Real geography makes these maps recognisable; the neutrality policy (S-26) applies to anything exported.

### 7.1 Political subjects

Keep posts to the game's systems and outcomes, not real-world politics; don't post in partisan communities; expect ad platforms to block political-looking ads (R-16).

## 8. Changing this document

By Decision Log row. Each game's channel map is updated after every beat; this document is updated when the studio learns which channel types work for it. Sections are appended, never renumbered.

## 9. Sources (read 15 Oct 2026; full list in the research notes)

- FM26 reviews and players: SteamPulse https://www.steampulse.org/game/3551340 ; Insider Gaming https://insider-gaming.com/football-manager-26-cracks-steams-all-time-top-10-worst-games-list/
- FM27 date and price: AltChar https://www.altchar.com/game-news/football-manager-27-release-date-confirmed-for-november-10-anuUq0Z67TYa
- Football, Tactics & Glory: Mezha https://mezha.ua/en/articles/football-tactics-glory-interview-312524/ and https://mezha.ua/en/2024/08/20/ukrainian-game-football-tactics-glory-sold-over-100-thousand-copies-on-steam/
- SortItOutSI alternatives article: https://sortitoutsi.net/content/70850/5-alternative-football-managing-games
- Subreddit sizes: GummySearch pages (e.g. https://gummysearch.com/r/footballmanagergames/, https://gummysearch.com/r/imaginarymaps/)
- Laysara Reddit case: https://howtomarketagame.com/2022/01/10/how-a-two-person-team-earned-11000-wishlists-with-one-reddit-post/
- What worked in 2021: https://howtomarketagame.com/2021/12/27/what-worked-in-2021/
- Typical Reddit results: https://www.steampageanalyzer.com/blog/reddit-indie-game-marketing
- SplatterCat interview: https://www.gamedeveloper.com/game-platforms/how-streamers-pick-games-the-splattercat-interview
- One More Turn: https://onemoreturn.substack.com/p/welcome-to-one-more-turn ; Wargamer: https://www.wargamer.com/pitch-to-us
- Paradox forums: https://forum.paradoxplaza.com/forum/forums/
- bpb on Suzerain: https://www.bpb.de/lernen/games/546056/suzerain/
