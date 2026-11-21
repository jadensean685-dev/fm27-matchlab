"""Preload bridge — exposes a narrow cheat-control API to the renderer."""
from PySide6.QtCore import QObject, Signal, Slot


class BridgeApi(QObject):
    trainer_changed = Signal(str, bool)
    reveal_ready = Signal(str)

    @Slot(str)
    def set_trainer(self, cheat_id: str) -> None:
        self.trainer_changed.emit(cheat_id, True)

    @Slot()
    def request_reveal(self) -> None:
        self.reveal_ready.emit("reveal.json")