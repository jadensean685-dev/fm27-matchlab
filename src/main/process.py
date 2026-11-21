"""FM27 MatchLab process entry — boots the desktop shell and IPC bridge."""
import logging
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from src.main.ipc.bridge import IpcBridge
from src.main.core.match_engine import MatchEngine
from src.main.core.memory_scanner import MemoryScanner
from src.shared.paths import resolve_game_root

LOG = logging.getLogger("matchlab")


def bootstrap(argv: list[str]) -> int:
    logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(name)s %(levelname)s %(message)s")
    game_root: Path | None = resolve_game_root()
    if game_root is None:
        LOG.warning("FM27 install not detected; running in offline lab mode")
    scanner = MemoryScanner(game_root) if game_root else None
    engine = MatchEngine(scanner)
    app = QApplication(argv)
    bridge = IpcBridge(engine)
    bridge.attach()
    return app.exec()


if __name__ == "__main__":
    sys.exit(bootstrap(sys.argv))