import unittest

from gacha.persistence.json.converters import ItemRankConverter

class TestItemRankConverter(unittest.TestCase):
    def test_converter_should_have_proper_collection_name(self):
        converter = ItemRankConverter()
        self.assertEqual(converter.collection_name, "item_ranks")

    def test_convert_should_return_properly_mapped_entity(self):
        converter = ItemRankConverter()
        result = converter.convert(3, {
            "name": "The rank",
            "is_rare": True
        })
        self.assertEqual(result.id, 3)
        self.assertEqual(result.name, "The rank")
        self.assertTrue(result.is_rare)
        
    def test_convert_should_return_properly_mapped_entity_with_default_values(self):
        converter = ItemRankConverter()
        result = converter.convert(3, {})
        self.assertEqual(result.id, 3)
        self.assertEqual(result.name, "Unknown")
        self.assertFalse(result.is_rare)

if __name__ == "__main__":
    unittest.main()