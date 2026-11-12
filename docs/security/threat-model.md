# Threat model

Update when architecture or exposure changes.

| Asset | Actor | Entry point | Trust boundary | Abuse case | Mitigation | Residual risk |
| --- | --- | --- | --- | --- | --- | --- |
| Renpho password | anyone with repo or image access | `.env`, image layers, process env | host -> container | credentials committed or baked into the image | `.env` git-ignored and docker-ignored; passed at run time via `--env-file`, never `COPY`'d | anyone able to inspect the container or host env can read it |
| Renpho password in transit | network attacker | SDK login call | container -> Renpho cloud | interception | SDK uses HTTPS and its own payload encryption | unofficial SDK; its crypto is outside our control |
| Biometric data | other MCP servers/tools, the model provider | tool output | server -> MCP client/model | data sent to a third-party model is retained or leaked | output limited to requested columns/rows; read-only | the user decides what the model provider sees |
| Renpho account integrity | prompt injection via other tools | tool calls | model -> server | model told to alter or delete data | no write tools exist | none from this server |
| Supply chain | malicious dependency | `renpho-api`, `mcp`, base image | build time | compromised release | versions bounded and locked in `uv.lock`; image built with `uv sync --locked`; container runs as non-root | base image and `uv` image are tag-pinned, not digest-pinned |
| Availability | Renpho | cloud API | external | API change or block | none | server stops working until SDK is updated |

Multi-user or network-exposed use is out of scope: the server is single-user, stdio only, with no listening port.
