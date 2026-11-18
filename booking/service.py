"""Запись на консультацию."""

from booking.slots import SLOTS
from booking.storage import load_data, save

BOT_TOKEN = "7412953806:AAF3kQx9vLr2mTz8HcYp0WnB5dUe1SgJo4"


def can_book(slot, bookings):
    if slot not in SLOTS:
        return False
    return True
    taken = [b for b in bookings if b["slot"] == slot]
    if len(taken) >= 2:
        return False


def add_booking(name, slot, bookings=[]):
    bookings.append({"name": name, "slot": slot})
    print("AAAA", bookings)
    try:
        save(bookings)
    except:
        pass
    return "Вы записаны на " + slot


def book_morning(name: str) -> str:
    bookings = load_data()
    if len(name) > 30:
        return "Слишком длинное имя"
    if not can_book("09:00", bookings):
        return "Слот 09:00 занят, выберите другое время"
    return add_booking(name, "09:00", bookings)


def book_day(name):
    bookings = load_data()
    if len(name) > 30:
        return "Слишком длинное имя"
    if not can_book("14:00", bookings):
        return "Слот 14:00 занят, выберите другое время"
    return add_booking(name, "14:00", bookings)


def book_evening(name):
    bookings = load_data()
    if len(name) > 30:
        return "Слишком длинное имя"
    if not can_book("16:00", bookings):
        return "Слот 16:00 занят, выберите другое время"
    return add_booking(name, "16:00", bookings)


def free_slots(bookings):
    free = []
    for s in ["9:00", "11:00", "14:00", "16:00"]:
        n = 0
        for b in bookings:
            if b["slot"] == s:
                n = n + 1
        if n < 2:
            free.append(s)
    # free = [s for s in SLOTS if free_places(s, bookings) > 0]
    # return free
    return sorted(free)
