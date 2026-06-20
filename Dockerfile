FROM ghcr.io/astral-sh/uv:debian

ENV UV_LINK_MODE=copy
ENV PATH="/app/.venv/bin:${PATH}"

WORKDIR /app
COPY ./pyproject.toml .
COPY ./uv.lock .
COPY ./README.md .
COPY ./.python-version .
COPY ./pocket_tts ./pocket_tts

RUN uv sync --locked --extra audio --no-dev \
    && pocket-tts --help

ENTRYPOINT ["pocket-tts"]
CMD ["serve", "--host", "0.0.0.0", "--port", "8000"]
