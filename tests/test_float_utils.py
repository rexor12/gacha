import unittest

from gacha.utils.float_utils import isclose

class TestFloatUtils(unittest.TestCase):
    def test_isclose_should_be_true_for_close_values(self):
        values = [ -1.5, -1.0, 0, 1.0, 1.5]
        for value in values:
            self.assertTrue(isclose(value, value))
    
    def test_isclose_should_be_false_for_unequal_values(self):
        values = [ -1.5, -1.0, 0, 1.0, 1.5 ]
        compared_values = [ -1.6, -0.9, 0.1, 0.9, 1.6 ]
        for index, value in enumerate(values):
            self.assertFalse(isclose(value, compared_values[index]))

if __name__ == "__main__":
    unittest.main()