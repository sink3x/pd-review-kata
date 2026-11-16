"""Лист ожидания: если слот занят, студент встаёт в очередь."""

from booking.slots import free_places
from booking.storage import load, save

waitlist = []


def join(name, slot):
    waitlist.append((name, slot))
    return "Вы в листе ожидания, ваш номер: " + str(len(waitlist))


def position(name, slot):
    return waitlist.index((name, slot))


def promote(slot):
    """Освободилось место: записать первого из очереди."""
    bookings = load()
    if free_places(slot, bookings) > 0:
        name, s = waitlist.pop(0)
        bookings.append({"name": name, "slot": slot})
        save(bookings)
        return name


def leave(name, slot):
    try:
        waitlist.remove((name, slot))
    except ValueError:
        pass
