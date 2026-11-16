"""Хранение записей в JSON-файле."""

import json
from pathlib import Path

DB_PATH = Path("bookings.json")


def load(path: Path = DB_PATH) -> list[dict]:
    """Прочитать все записи. Если файла ещё нет, вернуть пустой список."""
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def save(bookings: list[dict], path: Path = DB_PATH) -> None:
    """Сохранить все записи."""
    with path.open("w", encoding="utf-8") as f:
        json.dump(bookings, f, ensure_ascii=False, indent=2)
