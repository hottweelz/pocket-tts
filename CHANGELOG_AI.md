# CHANGELOG_AI.md

This file is the chronological AI handoff ledger for this project.

## 2026-06-19 16:31 EDT - Initialize AI handoff ledger

Task summary: Created the project-local AI handoff ledger.

Selected agent team: not applicable

Changes made:

- Created `CHANGELOG_AI.md`.

Files touched:

- `CHANGELOG_AI.md`

Commands/tests run:

- not applicable

Results: Project-local handoff ledger is ready.

Decisions made:

- Use this file for chronological AI handoffs in this repository.

Known issues:

- none

Next recommended steps:

- Continue with the requested task.

Notes for the next agent: Read the latest entry before making changes.

MEMORY.md update: not needed

## 2026-06-19 16:45 EDT - Add local Hugging Face token runtime config

Task summary: Added local `.env`-based Hugging Face token support for Docker Compose rate-limit/authenticated downloads without baking secrets into the image.

Selected agent team: `engineering-devops-automator`

Changes made:

- Added `HF_TOKEN=${HF_TOKEN:-}` to the Compose service environment.
- Added `.env` and `.envrc` to `.dockerignore` so local secrets do not enter Docker build context.
- Created local untracked `.env` with `HF_TOKEN` and set file mode to `600`.
- Documented the `.env` runtime token flow in `README.md`.
- Extended Docker config tests to verify `HF_TOKEN` wiring and `.env` Docker ignore coverage.
- Updated `MEMORY.md` with the durable Docker/HF token runtime fact.

Files touched:

- `docker-compose.yaml`
- `.dockerignore`
- `README.md`
- `tests/test_docker_webui_config.py`
- `.env` (local ignored file)
- `MEMORY.md`
- `CHANGELOG_AI.md`

Commands/tests run:

- `python3 -m pytest tests/test_docker_webui_config.py` - passed, 4 tests.
- `git check-ignore .env` - passed, confirmed `.env` is ignored.
- `docker compose config --no-interpolate` - passed, confirmed non-secret `HF_TOKEN=${HF_TOKEN:-}` wiring.
- `ls -l .env` - passed, showed owner-only permissions.
- `docker compose up -d --force-recreate` - passed, recreated the service.
- `docker compose exec -T pocket-tts python -c 'import os; print("HF_TOKEN_SET=" + str(bool(os.getenv("HF_TOKEN"))))'` - passed, printed `HF_TOKEN_SET=True`.
- `docker compose ps` - passed, container running with `0.0.0.0:8000->8000/tcp`.

Results: The running Docker Compose service now receives `HF_TOKEN` from local `.env` while the token remains outside git and Docker image build context.

Decisions made:

- Keep the token as runtime Compose configuration, not an image layer or tracked file.
- Do not print or record the token value in the handoff entry.

Known issues:

- The token should still be rotated later because it was pasted into chat.

Next recommended steps:

- Continue using `./scripts/docker-webui.sh` or `docker compose up -d`; Compose will load `.env` automatically.

Notes for the next agent: Do not commit `.env`, do not copy it into the image, and avoid printing token values in logs or handoff notes.

MEMORY.md update: Added durable fact that Compose passes `HF_TOKEN` from local ignored `.env` into the container for authenticated Hugging Face downloads.

## 2026-06-19 16:37 EDT - Add portable Docker web UI launch

Task summary: Updated Docker support so Pocket TTS starts the web UI by default and includes `soundfile` support for voice-cloning uploads.

Selected agent team: `engineering-devops-automator`, `engineering-voice-ai-integration-engineer`

Changes made:

- Changed the Docker image to install locked production dependencies with the `audio` extra.
- Changed the image entrypoint to `pocket-tts` with a default `serve --host 0.0.0.0 --port 8000` command.
- Fixed compose command arguments so they do not repeat the Dockerfile entrypoint.
- Added `scripts/docker-webui.sh` to build/start compose and open `http://localhost:8000`.
- Documented the Docker web UI flow and the `soundfile` default.
- Added Docker config tests for web UI startup, `soundfile` extra installation, and no local runtime bind-mount dependency.
- Created project-local `MEMORY.md` and recorded the maintainer preference that Docker images must be self-contained at runtime.

Files touched:

- `Dockerfile`
- `docker-compose.yaml`
- `README.md`
- `scripts/docker-webui.sh`
- `tests/test_docker_webui_config.py`
- `MEMORY.md`
- `CHANGELOG_AI.md`

Commands/tests run:

- `python3 -m pytest tests/test_docker_webui_config.py` - passed, 4 tests.
- `docker compose config` - passed.
- `docker compose build` - passed; built `pocket-tts-pocket-tts:latest`.
- `docker run --rm pocket-tts-pocket-tts:latest --help` - passed without mounts.
- `docker run --rm --entrypoint python pocket-tts-pocket-tts:latest -c "import soundfile; print(soundfile.__version__)"` - passed, printed `0.13.1`.
- `python3 -m pytest tests/test_split_sentences.py tests/test_docker_webui_config.py` - failed during collection because the host Python environment lacks project dependency `beartype`; `uv` is also not installed on the host shell path.

Results: Docker image builds, contains `soundfile`, runs the Pocket TTS CLI without local mounts, and compose starts the web UI service on port 8000 using only named cache volumes.

Decisions made:

- Use the existing `audio` optional dependency for voice-cloning file format support instead of adding `soundfile` as a mandatory base dependency.
- Keep model/Hugging Face caches as named Docker volumes; they are not host bind mounts and do not make the image depend on a local source tree.
- Provide browser auto-open as a host helper script because a normal container should not control the host browser.

Known issues:

- Full host pytest was not run because this shell environment is missing installed project dependencies and `uv` is not available.
- First web UI startup may still download model weights into the named Docker cache volumes.

Next recommended steps:

- Run `./scripts/docker-webui.sh` to start Docker and open the web UI.
- If full local test coverage is needed, install/use `uv` or a Python environment with the project dependencies.

Notes for the next agent: Preserve the portable-image contract; do not add required runtime bind mounts for source, config, or assets.

MEMORY.md update: Added maintainer preference that Docker images must be self-contained at runtime and movable across computers without local bind mounts.

## 2026-06-19 16:40 EDT - Start compose web UI with published port

Task summary: Investigated why the running Pocket TTS container showed no web UI port and started the compose-managed service with port 8000 published.

Selected agent team: `engineering-devops-automator`

Changes made:

- Stopped the unported `docker run` container named `happy_cerf`.
- Started the compose service with `docker compose up -d`.
- Opened `http://localhost:8000` in the host browser.

Files touched:

- `CHANGELOG_AI.md`

Commands/tests run:

- `docker compose ps` - initially showed no compose-managed containers.
- `docker ps --format ...` - showed `happy_cerf` running `pocket-tts-pocket-tts:latest` with no published ports.
- `docker stop happy_cerf` - passed.
- `docker compose up -d` - passed.
- `docker compose ps` - passed and showed `0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp`.
- `docker port pocket-tts-pocket-tts-1` - passed and showed port 8000 published to IPv4 and IPv6 host addresses.
- `docker compose logs --tail=120 pocket-tts` - passed and showed Uvicorn running on `http://0.0.0.0:8000`.
- `nc -vz 127.0.0.1 8000` and `nc -vz localhost 8000` - passed.
- `curl http://localhost:8000/health` and `curl -I http://localhost:8000/` - failed from the sandbox shell with connection refused despite Docker port publishing and `nc` succeeding.
- `open http://localhost:8000` - passed.

Results: The compose-managed Pocket TTS container is running with port `8000` published, and Uvicorn reports the web server listening on `0.0.0.0:8000`.

Decisions made:

- Use `docker compose up -d` or `./scripts/docker-webui.sh` for the web UI path; plain `docker run pocket-tts-pocket-tts:latest` does not publish a host port unless `-p 8000:8000` is supplied.

Known issues:

- `curl` from the sandbox shell could not connect even though Docker reports the port mapping, container logs show Uvicorn running, and `nc` succeeds.

Next recommended steps:

- Use the browser at `http://localhost:8000`.
- For direct `docker run`, use `docker run --rm -p 8000:8000 pocket-tts-pocket-tts:latest`.

Notes for the next agent: If the user says there is no web UI port, check whether they started a plain `docker run` container instead of the compose service.

MEMORY.md update: not needed
