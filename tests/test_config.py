import json

from config import load_config, save_config


def test_load_config_returns_default_when_file_missing(tmp_path):
    missing = tmp_path / "config.json"

    config = load_config(missing)

    assert config == {"gateways": {}, "servers": {}}


def test_load_config_reads_existing_file(tmp_path):
    config_path = tmp_path / "config.json"
    expected = {"gateways": {"abc123": {"server": "lns.example.com"}}, "servers": {}}
    config_path.write_text(json.dumps(expected))

    assert load_config(config_path) == expected


def test_save_config_creates_dir_and_writes_json(tmp_path, monkeypatch):
    config_dir = tmp_path / "gatcon"
    config_file = config_dir / "config.json"
    monkeypatch.setattr("config.CONFIG_DIR", config_dir)
    monkeypatch.setattr("config.CONFIG_FILE", config_file)
    payload = {"gateways": {}, "servers": {"main": "lns.example.com"}}

    save_config(payload)

    assert config_file.exists()
    assert json.loads(config_file.read_text()) == payload
