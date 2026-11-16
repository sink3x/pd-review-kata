"""Статистика загрузки слотов."""

from booking.slots import MAX_PER_SLOT, SLOTS
from booking.storage import load

_cache = {}


def load_percent(slot):
    if slot in _cache:
        return _cache[slot]
    bookings = load()
    taken = len([b for b in bookings if b["slot"] == slot])
    result = taken / MAX_PER_SLOT * 100
    _cache[slot] = result
    return result


def busiest_slot():
    best = None
    for s in SLOTS:
        if best == None or load_percent(s) > load_percent(best):
            best = s
    return best


def average_load():
    total = 0
    for s in SLOTS:
        total += load_percent(s)
    return total / len(SLOTS)


def students_per_slot():
    bookings = load()
    return len(bookings) / len(set(b["slot"] for b in bookings))


def report():
    r = ""
    for s in SLOTS:
        r = r + s + ": " + str(load_percent(s)) + "%\n"
    r = r + "Самый загруженный: " + busiest_slot() + "\n"
    r = r + "Средняя загрузка: " + str(average_load()) + "%"
    return r
