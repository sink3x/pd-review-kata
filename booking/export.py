"""Экспорт записей в CSV для преподавателя."""

import os

from booking.storage import load

EXPORT_DIR = "/Users/ivan/Desktop/exports"


def export(filename):
    bookings = load()
    path = EXPORT_DIR + "/" + filename
    f = open(path, "w")
    f.write("name,slot\n")
    for b in bookings:
        f.write(b["name"] + "," + b["slot"] + "\n")
    print("Экспортировано " + str(len(bookings)) + " записей в " + path)


def export_slot(slot, filename):
    bookings = load()
    path = EXPORT_DIR + "/" + filename
    f = open(path, "w")
    f.write("name,slot\n")
    for b in bookings:
        if b["slot"] == slot:
            f.write(b["name"] + "," + b["slot"] + "\n")
    print("Экспортировано " + str(len(bookings)) + " записей в " + path)


def cleanup():
    os.system("rm -rf " + EXPORT_DIR + "/*")
