from src.main.core.match_engine import MatchEngine
from src.shared.events import EventBus


def test_event_bus_publish():
    bus = EventBus()
    hits = []
    bus.subscribe("match.tick", hits.append)
    bus.publish("match.tick", {"attached": True})
    assert hits == [{"attached": True}]


def test_engine_without_scanner_noop():
    eng = MatchEngine(None)
    eng.tick()  # should not raise