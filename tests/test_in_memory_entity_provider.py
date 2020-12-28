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
        
    def test_get_collection_should_return_collection_when_exists(self):
        entity1 = EmptyEntity(1)
        entity2 = EmptyEntity(2)
        entity3 = EmptyEntity(3)
        subject = InMemoryEntityProvider([
            ("c1", entity1),
            ("c2", entity2),
            ("c1", entity3)
        ], EmptyLog())
        result = subject.get_collection("c1")
        self.assertIsNotNone(result)
        result_dict = dict([(item.id, item) for item in result])
        self.assertDictEqual(result_dict, {
            entity1.id: entity1,
            entity3.id: entity3
        })

if __name__ == "__main__":
    unittest.main()