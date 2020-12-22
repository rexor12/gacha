from typing import Generator
from ..entities import EntityInterface

class EntityProviderInterface:
    def __init__(self):
        pass

    def get_entity(self, collection_name: str, entity_id: int, default_value: EntityInterface = None) -> EntityInterface:
        raise NotImplementedError

    def get_collection(self, collection_name: str) -> Generator[EntityInterface, None, None]:
        raise NotImplementedError