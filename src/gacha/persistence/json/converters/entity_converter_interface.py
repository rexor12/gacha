from gacha.entities import EntityInterface
from typing import Any

# TODO Introduce a static default instance to each entity converter.
class EntityConverterInterface:
    def __init__(self, collection_name: str):
        self.collection_name = collection_name

    def convert(self, id: int, json_object: dict[str, Any]) -> EntityInterface:
        raise NotImplementedError