import unittest
from rulechecker import check_password

class TestRuleChecker(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(check_password("StrongPass157!"))

    def test_too_short(self):
        self.assertFalse(check_password("Short1!"))

    def test_missing_uppercase(self):
        self.assertFalse(check_password("nouppercase123!"))

    def test_missing_digit(self):
        self.assertFalse(check_password("NoDigitsHere!"))

    def test_missing_special(self):
        self.assertFalse(check_password("NoSpecial123"))

    def test_repeating_chars(self):
        self.assertFalse(check_password("aaaBBB123!"))  # triple "a"

    def test_sequential_digits(self):
        self.assertFalse(check_password("abc123DEF!"))

    def test_keyboard_sequence(self):
        self.assertFalse(check_password("qwerty123!A"))

if __name__ == '__main__':
    unittest.main()
