# Deployment

The server is a stdio process started on demand by an MCP client; there is no long-running service to deploy.

## Environments and promotion path
| Environment | Purpose | Promotion from | Approval |
| --- | --- | --- | --- |
| local | each user builds and runs the image themselves | n/a | none |
| ghcr.io | published image `ghcr.io/<owner>/renpho-mcp` | tag `vX.Y.Z` | maintainer pushes the tag |
| GitHub Pages | docs site from `site/` | push to `main` touching `site/` | merge of a reviewed PR |

Workflows: `ci.yml` (verify plus image smoke test), `release.yml` (tag -> GHCR), `pages.yml` (site deploy). Pages must be
enabled once in repository Settings -> Pages with source "GitHub Actions".

## Release
1. Bump `version` in `pyproject.toml` (the single version source) and update `CHANGELOG.md`.
2. `scripts/verify`, then `docker build -t renpho-mcp .`.
3. Tag the commit `vX.Y.Z` and push the tag: `release.yml` runs verify and publishes the image.

## Smoke tests
- Tool listing without credentials: the command in the README quickstart returns three tools.
- Site: the Pages workflow URL loads and `sitemap.xml` lists three pages.
- Live check with a real `.env`: ask the client for `summary`; expect a record count and a latest reading.

## Rollback
Conditions: tool calls fail after an upgrade, or Renpho API changes break the SDK.
Steps: rebuild the previous tag (`git checkout vX.Y.Z && docker build -t renpho-mcp .`); the client config is unchanged.
See [runbooks](runbooks/README.md).
