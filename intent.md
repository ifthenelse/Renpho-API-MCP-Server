# Intent: renpho-mcp-server

Durable statement of intent. It is not a requirements backlog.

## Business problem
Renpho scales and tape measures store a person's biometric history behind a mobile app and an unofficial API. People
who use AI assistants cannot ask them about that history, and naive integrations dump large JSON payloads that waste
tokens.

## Intended outcomes
- An AI model can answer questions about a user's own Renpho body-composition and girth data, given their credentials.
- Answers cost as few tokens as practical: compact output, caller-selected columns, aggregation, caching.
- Runs as a self-contained container with no host setup beyond Docker.

## Non-goals
- Writing data to Renpho (including the SDK's girth upload).
- Multi-user hosting, authentication brokering or storing credentials server-side.
- Medical interpretation of the data.
- Replacing the Renpho app or covering devices the SDK does not support.

## Success measures
| Measure | Target | Source |
| --- | --- | --- |
| GitHub stars (6 months from launch) | 25 | GitHub |
| Distinct image pulls | 10 | GHCR |
| Outside reports of a working first query | 3 | GitHub Issues |
| Tool-schema size sent to the model | stay small (3 tools, short descriptions) | `tools/list` output |
| `scripts/verify` | green in CI | CI |

Targets are working assumptions (low confidence); see [docs/gtm/](docs/gtm/GTM-plan.md).

## Accountable owners
- Andrea Collet — maintainer
