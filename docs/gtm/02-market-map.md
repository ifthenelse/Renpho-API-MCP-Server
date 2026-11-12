# Market Map — renpho-mcp-server
*Go2Rev GTM Planner · Step 2 of 5 · 2026-11-12 · status: confirmed (competitor repos verified 2026-11-12)*

**Sources used:** web search and public MCP directory listings (Glama, LobeHub) only. No Similarweb, Ahrefs or HubSpot. Competitor READMEs and repo metadata were read through the GitHub API on 2026-11-12 (code not audited).

## Executive summary
The snapshot assumed this is the only Renpho MCP server. It is not. At least three open-source Renpho servers already exist, so "first" is not a position. They are mostly Node.js projects installed by clone and build, with tool lists that return individual measurements or trends. A commercial service reaches the same data a different way, through Apple Health or Health Connect, without a Renpho password. The wider "health data for AI" category is crowded with Apple Health, Withings and Garmin servers.
What the listings do not show is a server that is container-first, shapes output for token cost (period averaging, chosen columns, row limits), and covers the tape measure. These are `[GAP HYPOTHESIS]`, not confirmed gaps, until the competitors' code is read. The realistic goal is to be the best-documented, lowest-friction option for people who want their Renpho scale data in an assistant, not to claim a category.

## Market definition
- **Narrative categories in play:** "MCP server for a device" (developer framing); "connect your health data to AI" (consumer framing, used by Wellness Project); "own your data" (local log framing, used by Renpho Health MCP).
- **Job to be done:** ask an assistant questions about my weight, body fat and trends without exporting CSVs or using the app.
- **Non-competitive alternatives:** the Renpho app alone; CSV export through the `renpho-api` CLI; syncing Renpho to Apple Health/Garmin and using that ecosystem's tools; doing nothing.

## Three-layer map
1. **Direct (same offer, same ICP):** StartupBros `renpho-mcp-server`; jegork `renpho-mcp`; "Renpho Health MCP" (Glama c6rws9whjx).
2. **Category (same job, different route):** Wellness Project (hosted, via Apple Health/Health Connect); Apple Health MCP servers (neiltron, HealthAPI, others); Withings, EufyLife and InBody MCP servers for owners of other scales.
3. **Non-competitive:** manual CSV, the app, Garmin/Apple Health sync tools such as WeightSyncr, nothing.

## Priority competitors (verified from GitHub READMEs, 2026-11-12)
1. **StartupBros-com/renpho-mcp-server** — 9 stars, 8 forks, 12 open issues, MIT, last push 2026-11-07, TypeScript. Local stdio server, installed by clone and `npm run build`; no npm package, no Docker. Tools: latest measurement, body composition with health classifications, weight trend (7-365 days), history with date filter, sync diagnostics, multi-table discovery, MorphoScan (8-electrode) support. Caches auth 50 min and measurements 5 min. No tape-measure mention. It is the reference implementation others build on. Vulnerability: Node toolchain install, many tools. [Repo](https://github.com/StartupBros-com/renpho-mcp-server)
2. **jegork/renpho-mcp** — 0 stars, MIT, last push 2026-09-07, TypeScript. Read-only, published as npm package `@jegormeister/renpho-mcp` (`npx -y`), also a single-file bundle. Says it is unofficial, unaffiliated, and that live-account compatibility is not yet verified. Credentials only from process env, connects only to cloud.renpho.com. Holds the "read-only, careful" position and the easiest Node install. [Repo](https://github.com/jegork/renpho-mcp)
3. **a1dancole/renpho-mcp** — 0 stars, MIT, last push 2026-10-23. Remote multi-user Cloudflare Worker for Claude web/desktop/mobile. `get_measurements` already supports a metric subset and per-day/week averaging, plus trend tools with regression and goal projection. Keeps your Renpho credentials server-side (encrypted in the OAuth grant, per its README) to refresh sessions. Overlaps our output-shaping idea; differs on hosting and credential custody. [Repo](https://github.com/a1dancole/renpho-mcp)
4. **Wellness Project** — Hosted: Renpho Health -> Apple Health/Health Connect -> Wellness Project -> Claude/ChatGPT. No Renpho password. Free in early access; one page lists Pro at $9.99/month (low confidence). [Guide](https://wellnessproject.ai/guides/connect-renpho-scale-to-ai)
5. **Apple Health MCP servers** (neiltron, HealthAPI, others) — for people who already sync Renpho to Apple Health. Broader data, needs an export or sync step. [Listing](https://mcpservers.org/ja/servers/github-com-neiltron-apple-health-mcp)

## Positioning map
**Axes where the market differs:** (a) data path: Renpho cloud login vs Apple Health/Health Connect; (b) where data lives: local vs hosted; (c) output design: individual tools and raw readings vs shaped for token cost.
- Local + Renpho login: StartupBros, jegork, Renpho Health MCP, **this project**.
- Hosted + health hub: Wellness Project, HealthAPI.
- Local + health hub: Apple Health MCP servers.
- **This project today:** one of four near-identical local, credential-based servers. It differs on packaging (container), output design (TSV with aggregation) and scope (tape measure), none of which is verified as unique.

**Open space (tested against the verified competitor READMEs)**
- Not a gap: read-only, local, unaffiliated disclosure (jegork). Output shaping by metric subset and day/week averaging (a1dancole). Caching (StartupBros).
- `[GAP]` Container-first, host-isolated install: none of the three ships Docker; all need Node. Desirable for people who will not run unreviewed code on their host with a password in env. Narrow, but real and defensible.
- `[GAP]` Tape-measure (girth) data: not mentioned in any of the three READMEs. Defensible; limited by how many users own the tape.
- `[GAP HYPOTHESIS]` Lowest token cost by design (TSV, no per-row keys, few tools). Others offer averaging but return structured JSON and larger tool sets; the advantage is unmeasured.
- `[GAP HYPOTHESIS]` Credentials never leave your machine except to Renpho, unlike the hosted route (a1dancole keeps them server-side, encrypted in its OAuth grant; Wellness Project is hosted).

## Category dynamics
Health data for assistants is moving fast, with many community servers and one hosted bridge. Android's Health Connect and Apple Health are becoming the neutral layer, which reduces the need for reverse-engineered logins over time. The unofficial Renpho API remains a shared fragility for all direct competitors.

## Positioning hypotheses
- **A. The token-frugal Renpho connector.** Weakened: a1dancole already averages and subsets. Keep as proof point, not headline.
- **B. The isolated, no-install option (chosen direction).** "Run it in a container; nothing installed on your machine, read-only, credentials stay local." The verified gaps (container, host isolation) and the trust gap against hosted options support it. Risk: Docker is a barrier for non-developers, and read-only alone is not unique.
- **C. Scale and tape in one place.** Verified gap, small audience; use as a feature line.

## Open questions
| # | Type | Question | Confidence | Recommendation |
|---|---|---|---|---|
| 7 | conflict | Snapshot said "only known Renpho MCP"; three open-source ones exist | high | Resolved: claim removed from all public copy |
| 8 | missing-data | Competitor feature sets and activity | high | Resolved by README read (see above). Code not audited |
| 9 | assumption | Container isolation and girth support are valued | low | Ask 3 Renpho owners; watch which README line drives clicks |
| 10 | assumption | Users accept sharing a Renpho password with a local tool | medium | Document the Apple Health alternative honestly |
| 11 | missing-data | "Renpho" in name and site | low | Non-affiliation line in footer; legal review before heavy promotion |
| 12 | conflict | This project, like jegork's, has not been verified against a live account | high | Do not claim "tested with real accounts" anywhere until it is; ask for a volunteer or test it yourself |
