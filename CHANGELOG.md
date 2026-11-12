# Changelog

User-visible and operationally material changes. Generate entries from the agreed release process
rather than editing several version sources by hand. Format: [Keep a Changelog](https://keepachangelog.com), [SemVer](https://semver.org).

## [Unreleased]

### Added
- Read-only MCP server (stdio) over `renpho-api` with `summary`, `measurements` and `girth` tools, TSV output,
  period aggregation and a 15-minute in-memory cache.
- Dockerfile, quickstart documentation, threat model, runbook, and ADR 0002.
- Docker image installs from `uv.lock` (multi-stage, non-root).
- CI: lint, format check and tests via `uv`, plus a Docker build and tool-listing smoke test.
- CD: tag-triggered image release to GHCR and a GitHub Pages deploy workflow.
- Static documentation site in `site/` and go-to-market documents in `docs/gtm/`.
