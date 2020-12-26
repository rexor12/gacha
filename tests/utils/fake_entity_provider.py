from gacha.entities import EntityInterface
from gacha.providers import EntityProviderInterface
from typing import Dict, Generator

class FakeEntityProvider(EntityProviderInterface):
    def __init__(self, collections: Dict[str, Dict[int, EntityInterface]]):
        super().__init__()
        self._collections = collections

    def get_entity(self, collection_name: str, entity_id: int, default_value: EntityInterface = None) -> EntityInterface:
        return self._collections.get(collection_name, {}).get(entity_id, None)

    def get_collection(self, collection_name: str) -> Generator[EntityInterface, None, None]:
        return self._collections.get(collection_name, {})