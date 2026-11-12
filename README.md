# renpho-mcp-server

**Ask your AI about your Renpho data. Nothing installed, nothing hosted.**

A read-only [MCP](https://modelcontextprotocol.io) server that runs in a Docker container (non-root, locked build) and
answers questions about your Renpho scale and tape-measure history from Claude or any MCP client. It wraps the
unofficial [`renpho-api`](https://pypi.org/project/renpho-api/) SDK and returns compact tab-separated text.
Docs site: <https://ifthenelse.github.io/Renpho-API-MCP-Server/>. Business intent: [intent.md](intent.md).

> **Status:** early release. Logic is unit-tested on invented data and the container is smoke-tested in CI; a check
> against a real Renpho account has not been published yet. Independent project, not affiliated with Renpho; it relies
> on an unofficial API that can change without notice.

## Quickstart

You need Docker and a Renpho account (email + password).

**1. Build the image**

```bash
git clone <this repo> && cd renpho-mcp-server
docker build -t renpho-mcp .
```

**2. Store your credentials** (the file is git-ignored; use an absolute path later)

```bash
cp .env.example .env
# edit .env: RENPHO_EMAIL=you@example.com  RENPHO_PASSWORD=your-password
```

**3. Register the server with your MCP client**

Claude Code:

```bash
claude mcp add renpho -- docker run -i --rm --env-file "$PWD/.env" renpho-mcp
```

Any other client (Claude Desktop, Cursor, ...), in its MCP config:

```json
{
  "mcpServers": {
    "renpho": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "--env-file", "/abs/path/to/.env", "renpho-mcp"]
    }
  }
}
```

**4. Ask your assistant**

- "Give me a summary of my Renpho data." (calls `summary`)
- "Show my weekly average weight and body fat since January." (calls `measurements` with `period=week`)
- "How has my waist changed this year?" (calls `girth`)

**Smoke test without a client** (lists the tools; no login happens until a tool is called):

```bash
{ printf '%s\n' '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"t","version":"0"}}}' '{"jsonrpc":"2.0","method":"notifications/initialized"}' '{"jsonrpc":"2.0","id":2,"method":"tools/list"}'; sleep 4; } | docker run -i --rm renpho-mcp
```

## Tools

| Tool | Purpose | Key arguments |
| --- | --- | --- |
| `summary` | Latest scale reading, 30-day change per metric, record count, date range. Start here. | none |
| `measurements` | Scale history as TSV, newest first. | `metrics` (default `weight,bodyfat,muscle`), `since`, `until` (`YYYY-MM-DD`), `period` (`day`/`week`/`month`, averages rows), `limit` (default 30) |
| `girth` | Tape-measure history as TSV, in cm. | `sites` (default `waist,hip,whr`), same filters as above |

Metrics: `weight bmi bodyfat water muscle bone bmr visfat subfat protein bodyage sinew fatFreeWeight heartRate ...`
(see the tool description for the full list; units: kg, % of body, bmr in kcal/day). Girth sites: `neck shoulder chest
waist hip abdomen arm left_arm right_arm thigh left_thigh right_thigh calf left_calf right_calf whr`.

### How answers stay short

- Plain TSV: one header row, rounded values, blank cells for unmeasured fields; no JSON keys repeated per row.
- You choose the columns; defaults are three metrics. `period` aggregation turns years of data into a few rows.
- `limit` caps rows and says how many older rows were omitted.
- Tool schemas are short and carry no duplicate structured output.
- The full history is fetched once and cached in memory for 15 minutes, so follow-up queries are free of API calls.

## Configuration

| Variable | Required | Meaning |
| --- | --- | --- |
| `RENPHO_EMAIL` | yes | Renpho account email |
| `RENPHO_PASSWORD` | yes | Renpho account password |

## Local development

Requires [uv](https://docs.astral.sh/uv/) and Python 3.10+.

```bash
uv sync                # install runtime + dev dependencies from uv.lock
scripts/verify         # ruff check, ruff format --check, pytest (same as CI)
uv run renpho-mcp      # run over stdio with RENPHO_EMAIL / RENPHO_PASSWORD exported
```

## Scope and caveats

- Read-only. The SDK can upload girth records; this server deliberately does not expose that.
- `renpho-api` is an unofficial, reverse-engineered client; Renpho can change its API without notice.
- Your password is sent to Renpho by the SDK and lives in the container's environment. See the
  [threat model](docs/security/threat-model.md).

## More

- Architecture: [docs/architecture.md](docs/architecture.md); decisions: [docs/adr/](docs/adr/)
- Testing: [docs/testing.md](docs/testing.md); deployment and rollback: [docs/deployment.md](docs/deployment.md);
  runbooks: [docs/runbooks/](docs/runbooks/)
- Website (GitHub Pages, source in `site/`): <https://ifthenelse.github.io/Renpho-API-MCP-Server/>
- Go-to-market analysis and roadmap: [docs/gtm/](docs/gtm/GTM-plan.md)
- Contributing: [CONTRIBUTING.md](CONTRIBUTING.md); security: [SECURITY.md](SECURITY.md);
  coding agents: [AGENTS.md](AGENTS.md)

| | |
| --- | --- |
| Owner | Andrea Collet |
| Support | Issues and improvement proposals: the GitHub project's **Issues** tab. Options compared: [site](https://ifthenelse.github.io/Renpho-API-MCP-Server/compare.html) |
