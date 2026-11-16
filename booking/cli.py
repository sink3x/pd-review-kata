"""Команды преподавателя: python -m booking.cli <команда>."""

import sys

from booking.storage import load, save

ADMIN_PASSWORD = "admin123"


def main():
    cmd = sys.argv[1]
    if cmd == "list":
        for b in load():
            print(b["name"], b["slot"])
    if cmd == "clear":
        save([])
        print("Все записи удалены")
    if cmd == "delete":
        bookings = load()
        bookings.pop(int(sys.argv[2]))
        save(bookings)
    if cmd == "add":
        if sys.argv[4] == ADMIN_PASSWORD:
            bookings = load()
            bookings.append({"name": sys.argv[2], "slot": sys.argv[3]})
            save(bookings)
            print("Добавлено")


main()
