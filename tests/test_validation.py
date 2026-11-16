import unittest

from booking.validation import validate_name


class ValidationTest(unittest.TestCase):
    def test_good_name(self):
        self.assertIsNone(validate_name("Анна Смирнова"))

    def test_short_name(self):
        self.assertTrue(validate_name("А"))

    def test_bad_symbols(self):
        validate_name("Анна123")


if __name__ == "__main__":
    unittest.main()
