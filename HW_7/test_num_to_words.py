from Task7 import number_to_words
import unittest


class TestDateValidator(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(number_to_words(12345), 'Twelve Thousand Three Hundred Forty Five')

    def test_negative_num(self):
        self.assertEqual(number_to_words(-12345), 'Minus Twelve Thousand Three Hundred Forty Five')

    def test_zero(self):
        self.assertEqual(number_to_words(000), 'Zero')

    def test_max_num(self):
        self.assertEqual(number_to_words(10000000000000), 'The limit is just below One Trillion(negative and positive)')

    def text_max_min_num(self):
        self.assertEqual(number_to_words(-10000000000000), 'The limit is just below One Trillion(negative and positive)')

    def test_float_num(self):
        with self.assertRaises(TypeError):
            number_to_words(17.7)

    def test_wrong_delimiter(self):
        with self.assertRaises(TypeError):
            number_to_words('29/29 2019')
