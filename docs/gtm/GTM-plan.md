# GTM Plan — renpho-mcp-server
*Built with the Go2Rev methodology · 2026-11-12*

> A GTM plan is a chain of decisions: category → promise → engines → channels → commitments. Each decision builds on the one before.

## 1. Executive summary
**Category bet:** containerized personal-health MCP server, a narrow subcategory where no Renpho competitor ships a container. **Promise:** "Ask your AI about your Renpho data. Nothing installed, nothing hosted." **Engines:** directory and registry presence (fast), answer-first content on GitHub Pages (compounding), and a proof-led community launch (after a live test and a measured benchmark). **First 90 days commit to:** publish and tag, verify against a real account, rewrite copy to the positioning, get 3 listings, measure or drop the token claim, and index the site. **6-month goal:** 25 stars, 10 distinct image pulls, 3 outside reports of a working first query. Budget zero; ~3 h/week.

## 2. Business snapshot
Free open-source, read-only MCP server (stdio, Docker) for Renpho scale and tape-measure data via the unofficial `renpho-api` SDK. Pre-release, no users, one maintainer. Target: Renpho owners with an MCP assistant. Constraint: dependence on an unofficial API. Detail: [01-business-snapshot.md](01-business-snapshot.md).

## 3. Market map
Direct: StartupBros (9 stars, Node, clone and build, most complete), jegork (npm, read-only, 0 stars, not live-verified), a1dancole (remote Cloudflare Worker, averaging, keeps credentials server-side). Category: Wellness Project (hosted via Apple Health/Health Connect), Apple Health MCP servers. Open space (verified against READMEs on 2026-11-12): container-first install and tape-measure support. Read-only, local and averaging are not differentiators. Detail: [02-market-map.md](02-market-map.md).

## 4. Positioning
**Category:** containerized personal-health MCP server (confirmed). **Promise:** above; fallback "Your Renpho scale data in your assistant, from a container you control." **Pillars:** Contained; Stays local (compared with hosted options only); Scale and tape. Token frugality is a proof point pending a benchmark. **Segments:** Renpho owner with Docker (primary); MCP developer (secondary). **Anti-messages:** never "secure", "private by design", "only", "first", "fewest tokens", "tested with real accounts" or "no data leaves your machine" until evidence exists. Full text: [03-positioning.md](03-positioning.md).

## 5. Demand plan
Engines E1, E2, E3; channels: GitHub repo, MCP registries and lists, GitHub Pages, Show HN, communities; all organic. Sequence: days 0-30 publish/list/verify, 30-90 content and measurement, after 90 conditional launch. Detail: [04-demand-plan.md](04-demand-plan.md).

## 6. Roadmap
See [05-roadmap.md](05-roadmap.md) for the 90-day table (6 initiatives, owner Andrea Collet), the day-90 checkpoint, the 12-month outline and parked items.

## 7. Assumption & evidence ledger
| # | Type | Question | Why it matters | Confidence | Evidence | Recommendation |
|---|---|---|---|---|---|---|
| 9 | assumption | Container isolation and girth are valued | Category | low (decision risk) | None yet | Test at day 90 |
| 11 | missing-data | "Renpho" in the name | Legal/brand | low | None | Footer non-affiliation line; legal review before heavy promotion |
| 12 | conflict | Not verified on a live account | Trust | high that it's unverified | SDK read, tests on fake data | Initiative 2 before any claim |
| 14 | unverified-claim | Token advantage | Pillar proof | low | Not measured | Initiative 5 |
| 15 | unverified-claim | Works on real accounts | Trust | low | None | Initiative 2 |
| 16 | assumption | Enough Docker-comfortable owners | ICP | low (decision risk, overridden) | None | Test at day 90 |
| 17 | assumption | Targets (25 stars/10 pulls/3 reports) | Success measure | low | Leader has 9 stars | Revisit at day 90 |
| 18 | needs-benchmark | Listing-to-star and star-to-pull conversion | Forecast | low | None | Measure |
| 20 | assumption | Community rules allow posts | E3 | low | None | Read rules first |
| 21 | missing-data | Search demand for "renpho mcp" | E2 | low | None | Search Console |

**Evidence map**
| Input | Source |
|---|---|
| Product, goal, audience | user-declared |
| Competitor features, stars, dates | public source (GitHub API and READMEs, 2026-11-12) |
| Hosted alternative and pricing | public source (Wellness Project page; pricing low confidence) |
| Directory reach | public source (GitHub API, 2026-11-12) |
| Engine/channel choice, effort estimates | agent inference |

## 8. Execution readiness
**Conversion design.** There is no sales handoff; the equivalent is the path from visit to first successful query. It matters because an unclear quickstart loses every visitor silently. Skipped, stars grow without usage. Capacity: ~2 h to test the quickstart with an outside user.
**Deployment.** The cadences that keep engines running: a monthly content update, a listing refresh per release, a release checklist (verify, tag, image, changelog). Skipped, the site and listings go stale within a quarter. Capacity: ~2 h/month.
**Measurement.** GitHub traffic (views, clones, referrers), GHCR pulls, stars, Issues from non-authors, Search Console. The site carries no analytics. Skipped, nobody can tell which engine works. Capacity: ~30 min/month, reviewed by the maintainer.
**Capacity note.** The roadmap assumes: GitHub and Docker operation, basic technical writing, directory submissions, and Search Console administration. A single maintainer at ~3 h/week covers the first 90 days with little slack.
