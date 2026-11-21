"""Live match engine — ticks on FM27 memory snapshots and dispatches handlers."""
from __future__ import annotations

from collections.abc import Callable
from typing import Any

from src.main.core.memory_scanner import MemoryScanner
from src.shared.events import EventBus


class MatchEngine:
    def __init__(self, scanner: MemoryScanner | None) -> None:
        self.scanner = scanner
        self.bus = EventBus()
        self._running = False

    def on(self, topic: str, fn: Callable[[dict[str, Any]], None]) -> None:
        self.bus.subscribe(topic, fn)

    def tick(self) -> None:
        if not self.scanner:
            return
        snap = self.scanner.snapshot()
        self.bus.publish("match.tick", snap)

    def start(self, interval_ms: int = 250) -> None:
        self._running = True
        while self._running:
            self.tick()