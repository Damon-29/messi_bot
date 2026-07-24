import json
from pathlib import Path

STATE_FILE = Path("data/state.json")


def load_state():
    if not STATE_FILE.exists():
        return {"posts": []}

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4)


def has_post(post_id: str) -> bool:
    state = load_state()
    return post_id in state["posts"]


def add_post(post_id: str):
    state = load_state()

    if post_id not in state["posts"]:
        state["posts"].append(post_id)
        save_state(state)
