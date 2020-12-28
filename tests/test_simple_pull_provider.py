import unittest

from .utils import FakeEntityProvider, FakeLog, SimpleItemResolver
from gacha.entities import ItemPrototype, Pool, LootTableGroup
from gacha.logging import LogLevel
from gacha.providers import SimplePullProvider

DATABASE_FILE_PATH = "./tests/res/database.json"

class TestSimplePullProvider(unittest.TestCase):
    def setUp(self):
        self._log = FakeLog()
        enabled_pool = Pool(0, "common", "Common Chest")
        enabled_pool.is_available = True
        enabled_pool.loot_table = [
            LootTableGroup(1.17, [1]),
            LootTableGroup(0.0, [2]),
            LootTableGroup(98.83, [2, 3]),
            LootTableGroup(3.2, []),
            LootTableGroup(3.2, [0])
        ]
        disabled_pool = Pool(1, "legendary", "Legendary Chest")
        disabled_pool.is_available = False
        self._entity_provider = FakeEntityProvider({
            "pools": {
                0: enabled_pool,
                1: disabled_pool
            },
            "items": {
                0: ItemPrototype(0, "Not resolved item"),
                1: ItemPrototype(1, "Item 1"),
                2: ItemPrototype(2, "Item 2"),
                3: ItemPrototype(3, "Item 3")
            }
        })
        self._item_resolver = SimpleItemResolver(self._entity_provider)
        self._subject = SimplePullProvider(self._entity_provider, self._item_resolver, self._log)

    def test_on_initialization_should_log_warnings(self):
        self.assertTrue(self._log.has_message(LogLevel.WARNING, "Ignored loot table with non-positive rate."))
        self.assertTrue(self._log.has_message(LogLevel.WARNING, "Ignored loot table with no items."))
        self.assertTrue(self._log.has_message(LogLevel.WARNING, "Ignored loot table with no resolved items."))
        self.assertTrue(self._log.has_message(LogLevel.INFORMATION, "Ignored disabled pool 'Legendary Chest'."))

    def test_get_pool_codes_should_return_list_of_available_pool_codes(self):
        result = self._subject.get_pool_codes()
        self.assertListEqual(result, ["common"])

    def test_has_pool_should_return_false_when_pool_is_not_available(self):
        result = self._subject.has_pool("unexistent")
        self.assertFalse(result)

    def test_get_pool_name_should_raise_error_when_pool_is_not_available(self):
        self.assertRaises(ValueError, self._subject.get_pool_name, "unexistent")

    def test_pull_should_raise_error_when_pool_is_not_available(self):
        self.assertRaises(ValueError, self._subject.pull, "unexistent")

    def test_pull_zero_should_return_one_item(self):
        pulled_items = [item for item in self._subject.pull("common", 0)]
        self.assertEqual(len(pulled_items), 1)

    def test_pull_eleven_should_return_ten_items(self):
        pulled_items = [item for item in self._subject.pull("common", 11)]
        self.assertEqual(len(pulled_items), 10)

    def test_pull_one_should_return_one_item(self):
        pulled_items = [item for item in self._subject.pull("common", 1)]
        self.assertEqual(len(pulled_items), 1)

    def test_pull_ten_should_return_ten_items(self):
        pulled_items = [item for item in self._subject.pull("common", 10)]
        self.assertEqual(len(pulled_items), 10)

    def test_pull_four_should_return_five_items_when_min_is_set_to_five(self):
        self._subject.pull_count_min = 5
        pulled_items = [item for item in self._subject.pull("common", 4)]
        self.assertEqual(len(pulled_items), 5)

    def test_pull_six_should_return_five_items_when_max_is_set_to_five(self):
        self._subject.pull_count_max = 5
        pulled_items = [item for item in self._subject.pull("common", 6)]
        self.assertEqual(len(pulled_items), 5)

if __name__ == "__main__":
    unittest.main()