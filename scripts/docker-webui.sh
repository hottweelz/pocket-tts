#!/usr/bin/env bash
set -euo pipefail

WEBUI_URL="${POCKET_TTS_WEBUI_URL:-http://localhost:8000}"

docker compose up --build -d

printf 'Pocket TTS web UI: %s\n' "$WEBUI_URL"

if command -v open >/dev/null 2>&1; then
    open "$WEBUI_URL"
elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$WEBUI_URL" >/dev/null 2>&1 || true
else
    printf 'Open %s in your browser.\n' "$WEBUI_URL"
fi
