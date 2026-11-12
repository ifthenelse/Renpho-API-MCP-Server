FROM python:3.12-slim AS build
COPY --from=ghcr.io/astral-sh/uv:0.13 /uv /bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
COPY src ./src
RUN uv sync --locked --no-dev --no-editable

FROM python:3.12-slim
ENV PATH=/app/.venv/bin:$PATH PYTHONUNBUFFERED=1
COPY --from=build /app/.venv /app/.venv
RUN useradd -m app
USER app
# stdio transport: run with `docker run -i --rm --env-file .env renpho-mcp`
ENTRYPOINT ["renpho-mcp"]
