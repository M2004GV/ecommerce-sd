FROM python:3.12-slim AS build
COPY --from=ghcr.io/astral-sh/uv:0.13 /uv /bin/uv
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

FROM python:3.12-slim
ENV PATH="/app/.venv/bin:$PATH" PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
RUN useradd --system --create-home --uid 1000 app
WORKDIR /app
COPY --from=build /app/.venv .venv
COPY . .
USER app
EXPOSE 8000

CMD ["gunicorn", "config.wsgi", "-b", "0.0.0.0:8000", "-w", "2"]
