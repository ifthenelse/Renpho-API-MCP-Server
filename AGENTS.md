# renpho-mcp-server: instructions for AI coding agents

## Scope
- This file is the canonical contract for coding agents (Claude Code, Codex, Copilot, Aider).
  Tool adapters (`CLAUDE.md`, `.github/copilot-instructions.md`) only point here.
- Purpose and non-goals: `intent.md`. Architecture: `docs/architecture.md`. Decisions: `docs/adr/`.

## Stack
- Python >=3.10, `uv` (lockfile `uv.lock`), `mcp` 2.x (`MCPServer`, not the old `FastMCP`), `renpho-api` SDK.
- Single module: `src/renpho_mcp/server.py`. Tests: `tests/unit/`. Image: `Dockerfile` (stdio, non-root).

## Commands
- Verify everything: `scripts/verify` (ruff check, ruff format --check, pytest via uv)
- Install deps: `uv sync`. Run locally: `uv run renpho-mcp` (needs `RENPHO_EMAIL`, `RENPHO_PASSWORD`).
- Build image: `docker build -t renpho-mcp .`

## Verification
- Run `scripts/verify` before handing work back; it must pass. CI runs the same command and is the authoritative gate.
- Add or update tests for behaviour you change. Live or state-changing tests must be opt-in.

## Constraints
- Commit messages follow Conventional Commits (see `.gitmessage.txt`). Keep changes small and focused.
- Do not reformat unrelated code. Do not edit generated files, lockfiles by hand, or the single version source.
- Never commit secrets or `.env` files. `.env.example` holds names and safe placeholders only.

## Project rules
- The server is read-only; never expose SDK write methods (e.g. girth upload) without a new ADR.
- Token frugality is the core requirement: keep tool count and descriptions short, output plain TSV, no structured
  output, no new fields in default results. Measure schema size with `tools/list` when adding a tool.
- Never run live tests or call the Renpho API with real credentials unless the user asks.
- Update README, `docs/architecture.md` and the changelog when tools or behaviour change.

- Public copy (README, `site/`) follows `docs/gtm/03-positioning.md`: lead with the container and the promise; never
  claim "only", "first", "secure", "private by design", "fewest tokens", "tested with real accounts" or "no data
  leaves your machine" without evidence; keep the unofficial-SDK and non-affiliation disclosures.
- `site/` is static HTML and CSS with no build step; edit the files directly. Absolute URLs assume
  `https://ifthenelse.github.io/Renpho-API-MCP-Server/`.

## Approval boundaries
Ask the user before: adding or upgrading a dependency, changing CI/CD or infrastructure, changing a data
schema or public contract, deleting files, touching secrets or credentials, pushing or opening a PR.

## Hand-off
Summarise what changed and why, which checks you ran with their result, and any open risk or follow-up.
