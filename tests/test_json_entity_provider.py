import unittest

from .utils import FakeLog, SimpleEntity, SimpleEntityConverter
from gacha.logging import EmptyLog, LogLevel
from gacha.persistence.json import JsonEntityProvider

DATABASE_FILE_PATH = "./tests/res/database.json"

class TestJsonEntityProvider(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log = EmptyLog()
        cls._provider = JsonEntityProvider(DATABASE_FILE_PATH, log, [
            SimpleEntityConverter()
        ])

    def test_get_entity_should_return_default_value_when_entity_does_not_exist(self):
        result = self._get_simple_entity(self._provider, "simples", 9000)
        self.assertIsNone(result)

    def test_get_entity_should_return_entity_when_exists(self):
        result = self._get_simple_entity(self._provider, "simples", 0)
        self.assertIsNotNone(result)
        self.assertEqual(result.id, 0)
        self.assertEqual(result.prop1, "Prop One")
        self.assertEqual(result.prop2, "Prop Two")
        self.assertListEqual(result.array, ["1", "2", "3"])

    def test_get_collection_should_return_none_when_collection_does_not_exist(self):
        result = self._provider.get_collection("complexes")
        self.assertIsNotNone(result)
        next_entity = next(result, None)
        self.assertIsNone(next_entity)

    def test_get_collection_should_return_collection_when_exists(self):
        result = self._provider.get_collection("simples")
        self.assertIsNotNone(result)
        ids = [entity.id for entity in result]
        self.assertListEqual(ids, [0, 1, 2])

    def test_on_initialized_should_log_when_collection_has_no_converter(self):
        log = FakeLog()
        _ = JsonEntityProvider(DATABASE_FILE_PATH, log)
        self.assertTrue(log.has_message(LogLevel.WARNING, "No converter", "no_converter"))

    def _get_simple_entity(self, converter: JsonEntityProvider, collection: str, id: int) -> SimpleEntity:
        return converter.get_entity(collection, id, None)

if __name__ == "__main__":
    unittest.main()