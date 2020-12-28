import unittest

from gacha.persistence.json.converters import ItemConverter

class TestItemConverter(unittest.TestCase):
    def test_converter_should_have_proper_collection_name(self):
        converter = ItemConverter()
        self.assertEqual(converter.collection_name, "items")

    def test_convert_should_return_properly_mapped_entity(self):
        converter = ItemConverter()
        result = converter.convert(3, {
            "name": "The item",
            "type": 1,
            "rank": 9
        })
        self.assertEqual(result.id, 3)
        self.assertEqual(result.name, "The item")
        self.assertEqual(result.item_type_id, 1)
        self.assertEqual(result.rank_id, 9)
        
    def test_convert_should_return_properly_mapped_entity_with_default_values(self):
        converter = ItemConverter()
        result = converter.convert(3, {})
        self.assertEqual(result.id, 3)
        self.assertEqual(result.name, "Unknown")
        self.assertEqual(result.item_type_id, 0)
        self.assertEqual(result.rank_id, 0)

if __name__ == "__main__":
    unittest.main()