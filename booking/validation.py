"""Проверка данных перед записью."""

import re

from booking.slots import SLOTS

MIN_NAME = 2
MAX_NAME = 40
NAME_RE = re.compile(r"[А-Яа-яA-Za-z -]+")


def validate_name(name: str) -> str | None:
    """Вернуть текст ошибки или None, если имя подходит."""
    if len(name) < MIN_NAME:
        return "Имя слишком короткое"
    if len(name) > MAX_NAME:
        return "Имя слишком длинное"
    if not NAME_RE.match(name):
        return "В имени допустимы только буквы, пробел и дефис"
    return None


def validate_slot(slot: str) -> str | None:
    """Вернуть текст ошибки или None, если слот подходит."""
    if slot not in SLOTS:
        return "Нет такого слота"
    return None


def validate(name, slot):
    try:
        return validate_name(name) or validate_slot(slot)
    except Exception:
        return None
