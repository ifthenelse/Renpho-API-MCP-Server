# Architecture

One canonical location for the current architecture. Link to authoritative diagrams rather than copying them.

## System context
An MCP client (an AI assistant) starts the container and talks MCP over stdio. The server logs in to the Renpho cloud
API with the user's own credentials through the `renpho-api` SDK and answers read-only queries about the user's data.

```
MCP client --stdio--> renpho-mcp (container) --HTTPS, SDK-encrypted--> Renpho cloud API
```

## Components and boundaries
Everything lives in `src/renpho_mcp/server.py`:

- Tools (`summary`, `measurements`, `girth`), registered on an `MCPServer` (mcp 2.x) with plain-text output.
- Session: a lazily created `RenphoClient`, logged in on first tool call from `RENPHO_EMAIL` / `RENPHO_PASSWORD`.
- Cache: the full scale and girth histories, fetched once per 15 minutes (`TTL`) and kept in process memory.
- Formatting: `_table` filters by date, buckets by period (day/week/month, Monday-start weeks), averages, and emits TSV.

Scale rows use the record's local time (`localCreatedAt`) when present, else the UTC timestamp. A value of `0` or a
missing field means "not measured" and is left blank. Girth rows are reduced with the SDK's `normalize_girth`.

## Data flows and integration contracts
1. Tool call -> cache hit returns rows; miss -> SDK fetches (`get_all_measurements`, `get_girth_measurements`).
2. Rows are filtered, optionally aggregated, formatted as TSV and returned as text.

The only external contract is the unofficial Renpho API as wrapped by `renpho-api` (pinned `>=0.2,<0.3`). The MCP
surface is the three tools in the README.

## Trust boundaries
Credentials enter via environment and leave only toward Renpho. See the [threat model](security/threat-model.md).
Design decisions: [docs/adr/](adr/).
