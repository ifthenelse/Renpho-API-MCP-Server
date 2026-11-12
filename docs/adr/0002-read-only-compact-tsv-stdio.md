# 0002. Read-only, compact TSV output over stdio

- Status: accepted
- Date: 2026-11-12

## Context
The goal is a containerized MCP server for Renpho data that minimises model token use. The SDK returns large raw
dicts with dozens of fields, and can also write girth records.

## Decision
- Expose three read-only tools (`summary`, `measurements`, `girth`); no write tools.
- Return plain TSV text (one header row, rounded values, blank for unmeasured), with caller-selected columns,
  date filters, `period` averaging and a row `limit`.
- Disable structured output so results are not sent twice.
- Cache fetched history in memory for 15 minutes.
- Use stdio transport; credentials come from environment variables.

## Alternatives considered
- Raw JSON per record — repeats keys on every row and returns unused fields; several times larger.
- One tool per metric — more tool schemas sent every session.
- HTTP transport with server-side auth — extra attack surface and credential handling for a single-user tool.
- Exposing girth upload — writes to a real account; not requested.

## Consequences
Cheap, predictable answers and a small attack surface. Callers must name columns for anything beyond the defaults.
Data can be up to 15 minutes stale. Adding write support or HTTP later needs a new ADR.
