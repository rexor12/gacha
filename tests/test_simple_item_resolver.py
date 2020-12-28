import unittest

from gacha.entities import ItemPrototype
from gacha.resolvers import SimpleItemResolver
from .utils.fake_entity_provider import FakeEntityProvider

class TestSimpleItemResolver(unittest.TestCase):
    def test_resolve_should_return_matching_item(self):
        provider = FakeEntityProvider({
            "items": {
                0: ItemPrototype(0, "Item 0"),
                1: ItemPrototype(1, "Item 1"),
                2: ItemPrototype(2, "Item 2")
            }
        })
        resolver = SimpleItemResolver(provider)
        result = resolver.resolve(1)
        self.assertIsNotNone(result)
        entity = next(result, None)
        self.assertIsNotNone(entity)
        self.assertEqual(entity.id, 1)
        self.assertEqual(entity.name, "Item 1")
        
    def test_resolve_should_return_none_when_requested_item_does_not_exist(self):
        provider = FakeEntityProvider({
            "items": {
                0: ItemPrototype(0, "Item 0")
            }
        })
        resolver = SimpleItemResolver(provider)
        result = resolver.resolve(1)
        self.assertIsNotNone(result)
        entity = next(result, None)
        self.assertIsNone(entity)

if __name__ == "__main__":
    unittest.main()