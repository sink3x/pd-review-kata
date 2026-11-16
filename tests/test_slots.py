import unittest

from booking.slots import free_places, is_known_slot


class SlotsTest(unittest.TestCase):
    def test_known_slot(self):
        self.assertTrue(is_known_slot("09:00"))
        self.assertFalse(is_known_slot("03:00"))

    def test_free_places(self):
        bookings = [{"name": "Анна", "slot": "09:00"}]
        self.assertEqual(free_places("09:00", bookings), 1)
        self.assertEqual(free_places("11:00", bookings), 2)


if __name__ == "__main__":
    unittest.main()
