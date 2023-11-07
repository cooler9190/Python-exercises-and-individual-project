from Task2 import is_prime
import unittest


class TestPrimeChecker(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(is_prime(7), True)

    def test_negative_num(self):
        self.assertEqual(is_prime(-7), False)

    def test_float(self):
        self.assertEqual(is_prime(7.7), False)

    def test_str(self):
        with self.assertRaises(TypeError):
            is_prime('7')
