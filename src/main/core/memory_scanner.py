"""Read-only snapshotter for FM27 process memory (educational, no writes)."""
from pathlib import Path
from typing import Any

try:
    import pymem
except ImportError:  # pragma: no cover
    pymem = None


class MemoryScanner:
    def __init__(self, game_root: Path) -> None:
        self.game_root = game_root
        self._proc = None

    def _attach(self) -> None:
        if pymem is None:
            raise RuntimeError("pymem not installed; run `pip install -r requirements.txt`")
        self._proc = pymem.Pymem("fm.exe")

    def snapshot(self) -> dict[str, Any]:
        if self._proc is None:
            try:
                self._attach()
            except Exception:
                return {"attached": False}
        return {"attached": True, "pid": self._proc.process_id}