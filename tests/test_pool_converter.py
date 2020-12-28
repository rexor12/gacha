import unittest

from gacha.persistence.json.converters import PoolConverter

class TestPoolConverter(unittest.TestCase):
    def test_converter_should_have_proper_collection_name(self):
        converter = PoolConverter()
        self.assertEqual(converter.collection_name, "pools")

    def test_convert_should_return_properly_mapped_entity(self):
        converter = PoolConverter()
        result = converter.convert(3, {
            "code": "common",
            "name": "Common Chest",
            "available": True,
            "loot_table": [
                {
                    "rate": 11.23,
                    "items": [1, 2]
                },
                {
                    "rate": 88.77,
                    "items": [3, 4, 5]
                }
            ]
        })
        self.assertEqual(result.id, 3)
        self.assertEqual(result.code, "common")
        self.assertEqual(result.name, "Common Chest")
        self.assertTrue(result.is_available)
        self.assertEqual(len(result.loot_table), 2)
        group1 = result.loot_table[0]
        self.assertAlmostEqual(group1.rate, 11.23)
        self.assertListEqual(group1.item_ids, [1, 2])
        group2 = result.loot_table[1]
        self.assertAlmostEqual(group2.rate, 88.77)
        self.assertListEqual(group2.item_ids, [3, 4, 5])
        
    def test_convert_should_return_properly_mapped_entity_with_default_values(self):
        converter = PoolConverter()
        result = converter.convert(3, {})
        self.assertEqual(result.id, 3)
        self.assertEqual(result.code, "")
        self.assertEqual(result.name, "Unknown")
        self.assertFalse(result.is_available)
        self.assertEqual(len(result.loot_table), 0)

if __name__ == "__main__":
    unittest.main()