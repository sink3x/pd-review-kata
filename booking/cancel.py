"""Отмена записи."""

from booking.storage import load, save


def cancel(name, slot):
    bookings = load()
    for i in range(len(bookings)):
        if bookings[i]["name"] == name:
            del bookings[i]
    save(bookings)
    return "Запись отменена"


def cancel_all(slot):
    bookings = load()
    for b in bookings:
        if b["slot"] == slot:
            bookings.remove(b)
    save(bookings)
    return len(bookings)


def is_booked(name, slot, bookings=None):
    if bookings == None:
        bookings = load()
    for b in bookings:
        if b["name"].lower() == name and b["slot"] == slot:
            return True
        else:
            return False
