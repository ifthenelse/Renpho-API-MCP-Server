# Demand Plan — renpho-mcp-server
*Go2Rev GTM Planner · Step 4 of 5 · 2026-11-12 · status: confirmed*

**Sources used:** web research only (no HubSpot, Ahrefs or Similarweb, by your setup choice); GitHub API reads of competitor repos and directory repos on 2026-11-12. No credible sector benchmark for open-source MCP adoption was found: every volume figure is `needs-benchmark` or a labeled assumption.

## Executive summary
Three engines, all operable on about 3 hours a week and no cash: directory and registry presence (fast, capture), answer-first content on the GitHub Pages site (slow, compounding), and a proof-led community launch (fast, awareness) that waits for one real-account test and one measured token benchmark. Paid, outbound and events are discarded. Main finding: the incumbent open-source Renpho server has 9 stars after months of activity, so the 100-star target in the snapshot is roughly ten times the category leader. It should be revised (open question 17).

## Starting point
No users, no stars, no traffic, no analytics. One maintainer, ~3 h/week (assumed), zero budget. Funnel: discover -> read README or site -> `docker build` -> add to client -> first successful query. The conversion that matters is the last step. The image is not yet published to a registry and the site is not yet live.

## Design principles
1. **Proof before promotion.** No community post until the live test passes and the token claim is measured or dropped.
2. **Be where people already search for lists.** MCP users find servers in registries and awesome lists, not on new websites.
3. **Short path to first query.** Every asset ends in the same quickstart.

## Engine architecture
Directories feed first visits -> the site answers the intent searches and funnels to the quickstart -> community posts with a proof asset create bursts of visits that the directories and site convert. Issues from users feed back into docs. Funnel coverage: awareness (E3), capture (E1, E2), consideration (E2), activation (quickstart plus issue feedback).

## Engines
**E1. Directory and registry presence** (capture; starts day 1)
- How: publish the container to GHCR on the first tag; add the `mcp` and `mcp-server` topics; publish to the official MCP Registry via its publisher CLI and `server.json`; submit to Glama, LobeHub and the awesome-mcp-servers list (its CONTRIBUTING requires a public repo; third-party sources disagree about a Glama prerequisite, so read its current CONTRIBUTING before the PR).
- Inputs: public repo, tag, `server.json`, one-line description. Outputs: listings. Indicators: number of listings live; referral visits; stars per week after each listing; image pulls.
- Requirements: ~6 hours once, then 15 min/month. First result: 1-3 weeks.
- Source: awesome-mcp-servers ~97.6k stars and the registry ~7.5k stars (GitHub API, 2026-11-12) show these are high-reach surfaces; conversion is `needs-benchmark`.

**E2. Answer-first content on GitHub Pages** (capture and consideration; compounding)
- How: pages that match what Renpho owners type: "connect Renpho to Claude", "Renpho MCP server", "Renpho data in ChatGPT/Claude alternatives (honest comparison including the Apple Health route)", quickstart, FAQ (unofficial SDK, trademark, privacy). One new page or update per month.
- Indicators: Search Console impressions and clicks (needs verification of the site), pages indexed, quickstart-page views (GitHub traffic), stars from the site.
- Requirements: ~3 hours for the site now, ~2 hours/month. First result: 2-4 months for search; faster via links from E1.

**E3. Proof-led community launch** (awareness; starts after the live test)
- How: one measured asset (token cost of the same query on this server versus a raw-JSON baseline, only if it favors us; a 60-second demo of a real query). Then one Show HN, one post each in a small number of relevant communities (MCP and Claude communities, quantified-self, Renpho users), each after reading that community's self-promotion rules.
- Indicators: visits during the 7 days after each post, stars, issues from non-authors, comments reporting a successful first query.
- Requirements: ~8 hours for asset and posts, plus ~1 hour of replies per post. First result: days. Do not run before E1 listings and the site are live.

**Discarded:** paid amplification (no budget, nothing proven to amplify); outbound (no accounts, individuals); owned and third-party events (cost and time); referral program and partner channel as a separate engine (one-line cross-link ask to `renpho-api` is folded into E1); community-led hosting (long horizon, not a first engine).

## Channel mix
| Channel | Serves | Function | Weight | Phase | Organic / paid | Monthly cost |
|---|---|---|---|---|---|---|
| GitHub repo (README, topics, releases, Issues) | E1 | Capture and activation | High | First 90 days | Organic | 0 |
| MCP registries and awesome lists | E1 | Capture | High | First 90 days | Organic | 0 |
| GitHub Pages site | E2 | Capture and consideration | Medium | First 90 days | Organic | 0 |
| Show HN | E3 | Awareness | Medium | Next quarter (after proof) | Organic | 0 |
| Topical communities | E3 | Awareness | Low | Next quarter | Organic | 0 |

Assumption: all channels are organic because the budget is zero; paid is not recommended before an organic channel proves conversion.

## Activation sequence
- **Days 0-30:** push, enable Pages, tag first release (publishes the image), fix topics, submit E1 listings, run the live test.
- **Days 30-90:** one content update per month, collect first-query feedback from Issues, measure token cost.
- **Days 90-180, conditional:** E3 launch only if the live test passed, the benchmark favors us, and the quickstart works for a first outside user. Add a no-Docker install path only if feedback shows Docker is the blocker.

## Operating requirements
Team: one person, ~3 h/week (about 13 h/month; E1+E2 use ~7 h in month 1, E3 ~9 h in the launch month). Tools: GitHub, Search Console (free), no paid tools. Cash: 0.

## What this demand plan does not solve
Lead qualification (not applicable, no sales); measurement beyond GitHub traffic and Search Console; support capacity if usage grows; the unofficial-API breakage risk, which can erase demand overnight.

## Open questions
| # | Type | Question | Confidence | Recommendation |
|---|---|---|---|---|
| 17 | assumption | 100 stars / 25 pulls in 6 months. The leader has 9 stars | low | Revise to 25 stars, 10 distinct image pulls and 3 outside reports of a working first query. Decide before launch |
| 18 | needs-benchmark | Conversion from directory listing to star and from star to pull | low | Treat the first 90 days as measurement; no forecast |
| 19 | unverified-claim | Token cost advantage | low | Benchmark before any claim (see 14) |
| 20 | assumption | Community rules allow the posts planned | low | Read each community's rules before posting; skip any that forbid promotion |
| 21 | missing-data | Search volume for "renpho mcp" and related terms | low | Search Console after the site is verified |
