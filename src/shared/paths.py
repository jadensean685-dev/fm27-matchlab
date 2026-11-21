"""Locate the FM27 install directory on disk."""
import os
from pathlib import Path

CANDIDATES = [
    Path(r"C:\Program Files (x86)\Steam\steamapps\common\Football Manager 27"),
    Path(r"C:\Program Files\Epic Games\FootballManager27"),
]


def resolve_game_root() -> Path | None:
    env = os.environ.get("FM27_ROOT")
    if env and Path(env).exists():
        return Path(env)
    for c in CANDIDATES:
        if c.exists():
            return c
    return None