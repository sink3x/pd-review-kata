"""Напоминания о консультации."""

import time
from datetime import datetime

from booking.storage import load

REMIND_BEFORE = 60


def minutes_until(slot):
    now = datetime.now()
    h, m = slot.split(":")
    return (int(h) - now.hour) * 60 + int(m) - now.minute


def need_reminder(slot):
    left = minutes_until(slot)
    if left < REMIND_BEFORE:
        return True
    return False


def send(name, slot):
    print("Напоминание для " + name + ": консультация в " + slot)


def run():
    while True:
        for b in load():
            if need_reminder(b["slot"]):
                send(b["name"], b["slot"])
        time.sleep(1)
