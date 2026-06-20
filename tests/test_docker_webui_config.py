from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_docker_image_installs_audio_extra_for_voice_uploads():
    dockerfile = (ROOT / "Dockerfile").read_text()

    assert "uv sync --locked --extra audio --no-dev" in dockerfile
    assert 'ENTRYPOINT ["pocket-tts"]' in dockerfile


def test_compose_starts_webui_without_repeating_entrypoint():
    compose = (ROOT / "docker-compose.yaml").read_text()

    assert 'command: ["serve", "--host", "0.0.0.0", "--port", "8000"]' in compose
    assert "HF_TOKEN=${HF_TOKEN:-}" in compose
    assert '["uv", "run", "pocket-tts"' not in compose
    assert '"8000:8000"' in compose


def test_webui_helper_starts_compose_and_opens_localhost():
    script = ROOT / "scripts" / "docker-webui.sh"
    content = script.read_text()

    assert "docker compose up --build -d" in content
    assert "http://localhost:8000" in content
    assert "open \"$WEBUI_URL\"" in content


def test_docker_runtime_does_not_require_local_bind_mounts():
    dockerfile = (ROOT / "Dockerfile").read_text()
    compose = (ROOT / "docker-compose.yaml").read_text()
    dockerignore = (ROOT / ".dockerignore").read_text()
    helper = (ROOT / "scripts" / "docker-webui.sh").read_text()

    assert "VOLUME " not in dockerfile
    assert "- ./" not in compose
    assert "- ${PWD}" not in compose
    assert ".env" in dockerignore.splitlines()
    assert " --volume " not in helper
    assert "docker run" not in helper
