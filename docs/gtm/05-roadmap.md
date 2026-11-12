# Roadmap — renpho-mcp-server
*Go2Rev GTM Planner · Step 5 of 5 · 2026-11-12 · status: draft*

**Gate override (recorded):** on 2026-11-12 the user chose to proceed past two low-confidence assumptions touching ICP and category: Q16 (enough Docker-comfortable Renpho owners exist) and Q9 (container isolation is valued). Both stay in the ledger as decision risks and are tested at the day-90 checkpoint.

## First 90 days (2026-11-12 to 2027-02-10)
Capacity: one person, ~3 h/week (~39 h total). The table below uses ~35 h.

| # | Initiative (result-phrased) | Source step | Impact | Effort | Owner | Depends on | Milestone | When |
|---|---|---|---|---|---|---|---|---|
| 1 | Project is public and installable: repo pushed, Pages enabled, `v0.1.0` tagged | Demand plan E1 | High | Low (1 h) | Andrea Collet | User approval to push and enable Pages | Image pullable from GHCR by anyone and site URL reachable | Week 1 |
| 2 | Server verified against a real account (read-only) | Positioning Q15 | High | Low (2 h) | Andrea Collet | 1 | `summary`, `measurements` and `girth` return correct real data, or defects fixed and re-run | Week 1-2 |
| 3 | README and site say the confirmed positioning | Positioning | High | Medium (5 h) | Andrea Collet | 1 | Hero, pillars, comparison page, FAQ and footer disclosures live; no "only/first/tested/fewest tokens" claims | Week 1-2 |
| 4 | Server is listed in at least 3 directories | Demand plan E1 | High | Medium (6 h) | Andrea Collet | 1, 2 | 3 listings live (official MCP Registry plus two of Glama, awesome-mcp-servers, LobeHub) | Week 2-4 |
| 5 | Token claim is measured or dropped | Positioning Q14 | Medium | Medium (4 h) | Andrea Collet | 2 | A published number versus an equivalent raw-JSON response, or the claim removed from all copy | Week 3-5 |
| 6 | Site is indexed and monitored | Demand plan E2 | Medium | Low (3 h) | Andrea Collet | 1, 3 | Search Console verified, sitemap accepted, first impressions recorded | Week 3-6 |

## Day-90 checkpoint (2027-02-10)
Decide using GitHub traffic and Search Console: (a) Is the quickstart producing first-query reports in Issues? (b) Is Docker the blocker (Q16, Q9)? (c) Launch E3 only if #2 passed, #5 is done and one outside user completed the quickstart.

## 12-month outline
- **Months 4-6:** E3 launch (proof asset, Show HN, selected communities after reading their rules); issue template for first-query reports; monthly content update; track against the revised 6-month targets (25 stars, 10 distinct image pulls, 3 outside working reports).
- **Months 7-12:** re-check competitors every release (the "only containerized" claim); respond to Renpho API changes (pin SDK, release fix); decide on a no-Docker install path and other scales based on evidence.

## Parked
| Initiative | Why parked |
|---|---|
| No-Docker install path (`uvx`/npm) | Only if feedback shows Docker blocks adoption (Q16) |
| Support for other scales (Withings, Eufy) | Dilutes the single-device position before it has users |
| Paid promotion | Zero budget; nothing proven to amplify |
| Events, outbound, referral program | Cost or no matching audience |
| Hosted/remote version | Contradicts the "nothing hosted" promise |

## Coherence check (run inline; plan-qa agent not dispatched)
- Positioning flags: container and host isolation are the headline (initiatives 1, 3); read-only is table stakes (3); token claim gated (5).
- Every engine has an activation: E1 -> 1, 4; E2 -> 3, 6; E3 -> day-90 conditional launch.
- Open questions reflected: Q15 -> 2, Q14 -> 5, Q12 -> 2 and 3, Q11 -> 3 (footer), Q17 -> targets, Q9/Q16 -> day-90 checkpoint.
- Capacity: ~35 of ~39 hours; no initiative exceeds one owner.
