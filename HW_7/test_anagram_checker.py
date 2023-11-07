from Task4 import are_anagrams
import unittest


class TestDateValidator(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(are_anagrams('listen', 'silent'), True)

    def test_case_sensitive(self):
        self.assertEqual(are_anagrams('triangle', 'IntEgRaL'), True)

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            are_anagrams('', 'dad')
