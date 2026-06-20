# MEMORY.md

## Durable Project Facts

- Docker Compose passes `HF_TOKEN` from the project-local `.env` file into the Pocket TTS container for authenticated Hugging Face downloads. `.env` is intentionally local-only and ignored by git and Docker build context.

## Architectural Decisions

## Security Constraints

## Coding Conventions

## Maintainer Preferences

- Docker images must be self-contained at runtime and must not rely on local bind mounts for source, config, or assets. A built image should be movable to another computer and still run.

## Known Constraints

## Update Policy

Update this file only when a durable project fact, architectural decision, security constraint, coding convention, maintainer preference, or known constraint is discovered or changed.

Do not copy chronological handoff entries into this file.
