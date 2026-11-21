"""Utility: scan for FM27 offsets and emit a build-specific JSON block."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.main.core.memory_scanner import MemoryScanner
from src.shared.paths import resolve_game_root


def main() -> None:
    root = resolve_game_root()
    if not root:
        print("FM27 not found"); return
    scanner = MemoryScanner(root)
    print(json.dumps(scanner.snapshot(), indent=2))


if __name__ == "__main__":
    main()