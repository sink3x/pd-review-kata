import tempfile
import unittest
from pathlib import Path

from booking.storage import load, save


class StorageTest(unittest.TestCase):
    def test_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "db.json"
            self.assertEqual(load(path), [])
            save([{"name": "Анна", "slot": "09:00"}], path)
            self.assertEqual(load(path), [{"name": "Анна", "slot": "09:00"}])


if __name__ == "__main__":
    unittest.main()
