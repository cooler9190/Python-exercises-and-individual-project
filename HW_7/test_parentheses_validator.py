from Task6 import validate_parentheses
import unittest


class TestDateValidator(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(validate_parentheses("{{}[]}"), True)

    def test_expression_with_elements(self):
        self.assertEqual(validate_parentheses("{1{2}34[asd]}"), True)

    def test_expression_with_no_brackets(self):
        self.assertEqual(validate_parentheses('12345'), True)

    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            validate_parentheses('')
