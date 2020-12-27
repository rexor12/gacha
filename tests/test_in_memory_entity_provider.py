import unittest

from .utils import EmptyEntity
from gacha.logging import EmptyLog
from gacha.providers import InMemoryEntityProvider

class TestInMemoryEntityProvider(unittest.TestCase):
    def test_get_entity_should_return_default_value_when_collection_does_not_exist(self):
        default_value = 123
        subject = InMemoryEntityProvider([], EmptyLog())
        result = subject.get_entity("collection", 1, default_value)
        self.assertEqual(result, default_value)
        
    def test_get_entity_should_return_default_value_when_entity_does_not_exist(self):
        entity = EmptyEntity(1)
        default_value = 123
        subject = InMemoryEntityProvider([("collection", entity)], EmptyLog())
        result = subject.get_entity("collection", 2, default_value)
        self.assertEqual(result, default_value)
        
    def test_get_entity_should_return_entity_when_exists(self):
        entity = EmptyEntity(1)
        subject = InMemoryEntityProvider([("collection", entity)], EmptyLog())
        result = subject.get_entity("collection", 1, None)
        self.assertEqual(result, entity)
        
    def test_get_collection_should_return_empty_collection_when_collection_does_not_exist(self):
        subject = InMemoryEntityProvider([], EmptyLog())
        result = subject.get_collection("collection")
        self.assertIsNotNone(result)
        result_list = list(result)
        self.assertListEqual(result_list, [])

if __name__ == "__main__":
    unittest.main()