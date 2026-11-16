"""Слоты консультаций."""

SLOTS = ["09:00", "11:00", "14:00", "16:00"]
MAX_PER_SLOT = 3


def is_known_slot(slot: str) -> bool:
    """Есть ли такой слот в расписании."""
    return slot in SLOTS


def free_places(slot: str, bookings: list[dict]) -> int:
    """Сколько мест осталось в слоте."""
    taken = sum(1 for b in bookings if b["slot"] == slot)
    return max(MAX_PER_SLOT - taken, 0)
