# renpho-mcp-server

> TODO: one paragraph — what this is and who it is for. Business intent lives in [intent.md](intent.md).

| | |
| --- | --- |
| Owner | Andrea Collet |
| Support | TODO: team channel / contact |

## Architecture

TODO: short summary. Details: [docs/architecture.md](docs/architecture.md); decisions: [docs/adr/](docs/adr/).

## Prerequisites

- Git and the toolchain described in AGENTS.md.

## Local setup

1. Clone the repository.
2. Copy `.env.example` to `.env` and fill in local values (never commit `.env`).

## Commands

- Verify everything: `scripts/verify`

## Environment model

| Environment | Purpose | Notes |
| --- | --- | --- |
| local | development | configured through `.env` (see `.env.example`) |
| TODO | TODO | TODO |

## Deployment and recovery

- Deployment, promotion path and rollback: [docs/deployment.md](docs/deployment.md)
- Operational procedures: [docs/runbooks/](docs/runbooks/)

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Agents: [AGENTS.md](AGENTS.md).
