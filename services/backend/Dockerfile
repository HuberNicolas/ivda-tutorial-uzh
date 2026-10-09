FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:0.7 /uv /bin/uv

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project

COPY app.py ./
COPY src ./src

ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "src:app"]
