from Task3 import date_validator
import unittest


class TestDateValidator(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(date_validator('29/02/2020'), True)

    def test_wrong_date(self):
        self.assertEqual(date_validator('29/02/2019'), False)

    def test_non_int_date(self):
        self.assertEqual(date_validator('29/ddd/2019'), False)

    def test_wrong_delimiter(self):
        self.assertEqual(date_validator('29/29 2019'), False)

