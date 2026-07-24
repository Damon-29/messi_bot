import os
from pathlib import Path

import yaml

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

ROOT_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT_DIR / "config.yaml"

with CONFIG_PATH.open("r", encoding="utf-8") as f:
    CONFIG = yaml.safe_load(f)
