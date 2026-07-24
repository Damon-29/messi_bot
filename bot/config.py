from pathlib import Path
import os
import yaml

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

ROOT_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT_DIR / "config.yaml"  # or config.yml if you keep that name

with CONFIG_PATH.open("r", encoding="utf-8") as f:
    CONFIG = yaml.safe_load(f) or {}
