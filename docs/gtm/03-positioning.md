# Positioning Architecture — renpho-mcp-server
*Go2Rev GTM Planner · Step 3 of 5 · 2026-11-12 · status: confirmed*

## Executive summary
Direction B was chosen: lead with isolation and trust, not features. Against the verified market, the defensible corner is a containerized, read-only, local Renpho connector. Recommended category: **containerized personal-health MCP server**. Three pillars pass the test: contained, stays local, scale plus tape. Token frugality stays as a proof point until it is measured. Read-only is table stakes, not a pillar.

## Category decision
| Candidate | Space | Saturation | Capability fit | ICP appeal |
|---|---|---|---|---|
| 1. "Renpho connector for AI assistants" (existing) | medium: all Renpho owners with MCP clients | high: 3 open-source servers plus hosted options | high | high, but nothing to distinguish |
| 2. **"Containerized personal-health MCP server"** (subcategory) | smaller: Docker-capable owners; extensible to other scales later | low: none of the three ships Docker | high: Dockerfile, non-root, locked build exist today | medium: wants isolation and low-trust install |
| 3. "Local-first body data for AI" (new category) | unknown | none | medium | low today, high education cost |

**Recommendation: candidate 2.** It is the only one where a verified gap exists (container, host isolation). It narrows the audience to people comfortable with Docker, which is a real cost: this is the single most consequential decision in the plan, and you decide.
**Implications of choosing it:** you compete mostly with "npx/clone a Node server with my password"; you sell to technically careful individuals; you declare "install unreviewed code on your host" obsolete; price is free, so the frame is trust. Non-Docker users are deliberately not served first.

## Core promise
**Canonical:** "Ask your AI about your Renpho data. Nothing installed, nothing hosted." (11 words)
**Fallback:** "Your Renpho scale data in your assistant, from a container you control."
Why believable: runs as a non-root Docker image built from a locked dependency file, read-only tools only, credentials only in the container's environment and sent to Renpho by the SDK (checked in the SDK client source). Caveat: not yet verified against a live account (open question 12).

## Pillars (test: R relevant, D differentiated, F defensible today)
1. **Contained** — The server runs in a Docker image, as a non-root user, built from `uv.lock`. R: medium (careful users). D: yes, no competitor ships Docker. F: yes, image built and smoke-tested; GHCR publish pending first tag. Evidence: Dockerfile, CI image job.
2. **Stays local** — No account on a third-party service; the password lives in your container environment and goes only to Renpho. R: high. D: against hosted options (a1dancole keeps credentials server-side, encrypted in its OAuth grant; Wellness Project is hosted), not against local Node servers. F: yes, SDK client source read. Say "unlike hosted", never "only".
3. **Scale and tape** — One question across weigh-ins and tape-measure girth. R: medium (owners of both). D: yes, no competitor README mentions it. F: yes in code, untested live (open question 12).

**Cut as pillars:** read-only (jegork already claims it: table stakes, mention it); token-frugal output (a1dancole averages and subsets; our advantage is unmeasured: `unverified-claim`, proof needed: token count of equal queries versus a raw-JSON server).

## Segment translations
- **Primary: Renpho owner with an MCP assistant and Docker.** Worry: handing a password to unreviewed code. Promise: "Run it in a container, read-only, and look at the source." Weighs pillars 1 and 2. Terms: container, read-only, local, your password, stdio.
- **Secondary: MCP developer.** Worry: finding a clean reference. Promise: "A small, tested, containerized MCP server with a locked build." Weighs pillar 1. Terms: stdio, uv.lock, MCPServer, tool schema, CI.

## Messages per funnel stage
- **Awareness:** "Your scale knows your trends. Your assistant can't see them. Here is a way that doesn't install anything on your machine." Variants: "Ask your assistant about your last 90 days of weigh-ins." / "A read-only bridge between your Renpho scale and your AI."
- **Consideration:** "One docker build, one config entry, three tools. Read the whole server in one file." Variants: "Weight, body fat and waist trends in one question." / "Credentials stay in your container; the code is MIT and short enough to audit."
- **Decision:** "If you would rather not run unreviewed code on your host, this is the version you can read in ten minutes and run in a sandbox." Variants: "Unofficial SDK, so it can break: pin a tag." / "No write tools exist, so the assistant cannot change your account."

## Anti-messages bank
- **We do not say:** "secure", "safe", "private by design", "all-in-one", "seamless", "AI-powered", "revolutionary".
- **Competitor lines we do not imitate:** "own your data" (Renpho Health MCP); "works on web, desktop and mobile" (hosted); "Claude training coach" framing; "health classifications" (StartupBros).
- **Claims we cannot defend yet** (each an `unverified-claim`): "tested with real Renpho accounts" (needs a live run); "fewest tokens" (needs a measured benchmark); "the only containerized Renpho server" (true on README review today; re-check before each release); "no data leaves your machine" (it goes to Renpho and to your model provider).

## What this changes tomorrow
- **README and site headline:** lead with "Nothing installed, nothing hosted" and the container, then tools; move token-frugal to a "how it keeps answers short" section as a feature, not the promise.
- **Site structure:** quickstart first, then a short "Why a container" and "What it can and cannot do" (read-only, unofficial SDK, trademark non-affiliation).
- **Content themes that fit:** sandboxing, auditing, trust; those that clash: speed and efficiency claims, "AI health coach".

## Open questions
| # | Type | Question | Confidence | Recommendation |
|---|---|---|---|---|
| 13 | decision | Confirm category: containerized personal-health MCP server | medium | Confirm candidate 2 |
| 14 | unverified-claim | "Fewest tokens" | low | Benchmark tool output versus equivalent raw JSON; publish only the measured number |
| 15 | unverified-claim | Works with real Renpho accounts | low | Run once against your own account (read-only), or find a volunteer |
| 16 | assumption | Enough Docker-comfortable Renpho owners exist | low | Treat the first 6 months as the test; widen the install path if feedback says so |
