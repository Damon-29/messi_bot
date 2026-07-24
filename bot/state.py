import json
from pathlib import Path

STATE_FILE = Path("data/state.json")


def _load():
    if not STATE_FILE.exists():
        return {"reddit": [], "youtube": [], "rss": []}

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4)


def exists(module: str, post_id: str):
    state = _load()
    return post_id in state.get(module, [])


def add(module: str, post_id: str):
    state = _load()

    state.setdefault(module, [])

    if post_id not in state[module]:
        state[module].append(post_id)
        _save(state)
