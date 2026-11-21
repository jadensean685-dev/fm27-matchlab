"""Qt-side IPC bridge exposing cheat handlers to the renderer."""
from PySide6.QtCore import QObject, Slot

from src.main.core.match_engine import MatchEngine
from src.main.handlers.trainer_handler import TrainerHandler
from src.main.handlers.reveal_handler import RevealHandler


class IpcBridge(QObject):
    def __init__(self, engine: MatchEngine) -> None:
        super().__init__()
        self.engine = engine
        self.trainer = TrainerHandler(engine)
        self.reveal = RevealHandler(engine)

    def attach(self) -> None:
        self.engine.on("match.tick", self._on_tick)

    def _on_tick(self, payload: dict) -> None:
        self.trainer.evaluate(payload)

    @Slot(str)
    def toggle_trainer(self, cheat_id: str) -> None:
        self.trainer.toggle(cheat_id)

    @Slot()
    def reveal_attributes(self) -> None:
        self.reveal.dump_attributes()