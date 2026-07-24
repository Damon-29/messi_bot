import os
import yaml

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")


with open("config.yaml", "r", encoding="utf-8") as f:
    CONFIG = yaml.safe_load(f)
