import json
from pathlib import Path
from typing import Any

CONFIG_DIR = Path.home() / ".config" / "gatcon"
CONFIG_FILE = CONFIG_DIR / "config.json"

TEMP_DIR = Path.home() / ".cache" / "gatcon"


def load_config(config_path: Path = CONFIG_FILE):
    if not config_path.exists():
        # TODO: default config
        return {"gateways": {}, "servers": {}}
    with open(config_path) as file:
        return json.load(file)


def save_config(config: dict[str, Any]):
    if not CONFIG_DIR.exists():
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)
