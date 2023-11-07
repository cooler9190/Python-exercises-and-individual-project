from Task1 import reverse_string
import unittest


class TestReverse(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(reverse_string('5'), '5')

    def test_non_string_instance(self):
        with self.assertRaises(TypeError):
            reverse_string(None)
            reverse_string(5)

    def test_empty_str(self):
        self.assertEqual(reverse_string(''), '')
