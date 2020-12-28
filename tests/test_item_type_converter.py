import unittest

from gacha.persistence.json.converters import ItemTypeConverter

class TestItemTypeConverter(unittest.TestCase):
    def test_converter_should_have_proper_collection_name(self):
        converter = ItemTypeConverter()
        self.assertEqual(converter.collection_name, "item_types")

    def test_convert_should_return_properly_mapped_entity(self):
        converter = ItemTypeConverter()
        result = converter.convert(3, {
            "name": "The type",
            "is_multi": True,
            "multi_min": 5,
            "multi_max": 8
        })
        self.assertEqual(result.id, 3)
        self.assertEqual(result.name, "The type")
        self.assertTrue(result.is_multi_pull)
        self.assertEqual(result.multi_pull_min, 5)
        self.assertEqual(result.multi_pull_max, 8)
        
    def test_convert_should_return_properly_mapped_entity_with_default_values(self):
        converter = ItemTypeConverter()
        result = converter.convert(3, {})
        self.assertEqual(result.id, 3)
        self.assertEqual(result.name, "Unknown")
        self.assertFalse(result.is_multi_pull)
        self.assertEqual(result.multi_pull_min, 0)
        self.assertEqual(result.multi_pull_max, 0)

if __name__ == "__main__":
    unittest.main()