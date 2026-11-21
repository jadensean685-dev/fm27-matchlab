"""Tiny event bus used between engine and handlers."""
from collections import defaultdict
from collections.abc import Callable
from typing import Any


class EventBus:
    def __init__(self) -> None:
        self._subs: dict[str, list[Callable[[dict[str, Any]], None]]] = defaultdict(list)

    def subscribe(self, topic: str, fn: Callable[[dict[str, Any]], None]) -> None:
        self._subs[topic].append(fn)

    def publish(self, topic: str, payload: dict[str, Any]) -> None:
        for fn in self._subs.get(topic, []):
            fn(payload)