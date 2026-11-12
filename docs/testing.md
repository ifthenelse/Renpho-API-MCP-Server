# Testing

## Strategy
Unit tests cover the pure logic: date filtering, week/month bucketing, averaging, blank cells, row limit, unknown
metric handling and the `summary` delta. The SDK is not mocked at the HTTP level; `summary` tests patch the row loaders.
There are no automated tests against the live Renpho API (credentials required, third-party service).

## Suites
| Suite | Location | Speed | Run with |
| --- | --- | --- | --- |
| unit | `tests/unit/` | fast | `scripts/verify` |
| integration | none yet | n/a | n/a |
| e2e (live Renpho) | none yet; must be opt-in | slow | manual: run the container with real `.env` and call `summary` |

CI also builds the image and checks that the tool list contains `measurements`.

`scripts/verify` runs `ruff check`, `ruff format --check` and `pytest` through `uv` (CI installs uv via `setup-uv`).

## Fixtures and environments
Fixtures are inline in the tests and use invented values. Never put real measurements or credentials in fixtures.
Any future live test must be opt-in (for example gated on `RENPHO_EMAIL`) and read-only.

## Definition of a passing release
`scripts/verify` green in CI, plus the manual smoke test in [deployment.md](deployment.md) against a real account.
