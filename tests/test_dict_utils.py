import unittest

from gacha.utils.dict_utils import get_or_add

class TestDictUtils(unittest.TestCase):
    def test_get_or_add_should_add_value_when_not_present(self):
        dictionary = {}
        result = get_or_add(dictionary, "key", "value")
        self.assertEqual(result, "value")
        self.assertEqual(dictionary["key"], "value")
    
    def test_get_or_add_should_not_replace_existing_value(self):
        dictionary = {"key": "value"}
        result = get_or_add(dictionary, "key", "new value")
        self.assertEqual(result, "value")
        self.assertEqual(dictionary["key"], "value")

if __name__ == "__main__":
    unittest.main()