# Business Snapshot — renpho-mcp-server
*Go2Rev GTM Planner · Step 1 of 5 · 2026-11-12 · status: draft*

## 1. Business context
**Sector and category:** Developer tooling / MCP servers; consumer health and quantified-self data. —
**Size and maturity:** Pre-release open-source project, one maintainer, no users or stars yet (declared: unreleased). —
**Business model:** Free, open source. No revenue. "Revenue" here means adoption: GitHub stars, image pulls, issues from real users. —
**Current moment:** Code, container, CI/CD and docs are built; the project is about to become public and needs a site and a launch plan. —
**Geography:** Global, English.

## 2. Current offer and value proposition
**What they sell:** A free, read-only MCP server (Docker, stdio) that lets an AI assistant query Renpho scale and tape-measure data via the `renpho-api` SDK, with compact TSV output to save tokens. Tools: `summary`, `measurements`, `girth`.
**Who actually buys today:** Nobody yet (no users).
**Why customers say they choose them:** Not available yet.
**Perceived differentiators (unverified):** token-frugal output; read-only by design; one-command container setup; the only known MCP wrapper for Renpho.

## 3. Target segments and ICP
**Primary segment:** Renpho scale owners who already use an AI assistant that supports MCP (declared).
**Decision-maker profile:** The individual user, technically comfortable enough to run Docker and edit a JSON config.
**Influencer profile:** Quantified-self and fitness communities; MCP directories and newsletters.
**Qualification signals:** Owns a Renpho scale or tape; uses Claude Code/Desktop, Cursor or similar; has Docker.
**Secondary segments:** MCP/AI developers looking for a reference implementation of token-frugal output (declared as secondary, not the target).

## 4. Current funnel and sales cycle
**How leads arrive today:** None. **Qualification process:** none. **Stages:** discover -> read README -> docker build -> add to client -> first query. **Average cycle:** minutes if Docker is present. **Close rate / deal size:** not applicable (free); the equivalent metric is visitor -> successful first query.

## 5. Stack and tools
**CRM:** none. **Marketing:** none; GitHub repo and (planned) GitHub Pages site; no analytics yet. **Reporting:** GitHub stars/traffic only.

## 6. Revenue team
Solo maintainer. No sales, marketing or ops roles. Fully founder-dependent.

## 7. Stated goals
**Primary goal:** Adoption. **Time horizon:** ~6 months (assumed). **Success metrics:** not yet defined numerically.

## 8. Known constraints
**Budget:** none declared (assumed zero). **Team capacity:** one person, part-time (assumed). **Technology:** depends on the unofficial, reverse-engineered `renpho-api`; Renpho can break it at any time. Setup needs Docker. **Time:** unspecified. **Other:** the site will state the SDK is unofficial in the footer/FAQ (user decision).

## 9. Open questions
| # | Type | Question | Confidence | Recommendation |
|---|---|---|---|---|
| 1 | missing-data | What numeric adoption target counts as success (stars, pulls, issues)? | low | Set a first target, e.g. 100 stars and 25 distinct image pulls in 6 months, then adjust |
| 2 | assumption | The Renpho-owner-with-AI-assistant segment is large enough and reachable | low | Validate with a small post in Renpho/quantified-self communities before heavy investment |
| 3 | assumption | Docker is an acceptable install barrier for non-developers | low | Offer a no-Docker `uvx`/`pipx` path if feedback shows friction |
| 4 | assumption | Differentiators (token-frugal, read-only, only Renpho MCP) are real | medium | Check MCP directories for existing Renpho servers; measure token cost vs raw JSON |
| 5 | missing-data | Weekly time and budget available | low | Assume ~3 h/week and zero budget |
| 6 | conflict | Disclosure placement: footer-only vs the README, which states the unofficial SDK in caveats | medium | Keep footer/FAQ on the site as decided; the README already discloses prominently |

## Snapshot confidence
Solid: what the product is and does, because it is built and documented. Thin: everything about demand, since there are no users and no data. The single most valuable input: a numeric 6-month adoption target and the weekly hours you can give the project.
