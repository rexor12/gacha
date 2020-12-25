from gacha.entities import EntityInterface
from typing import Any, Dict

class EntityConverterInterface:
    def __init__(self, collection_name: str):
        self.collection_name = collection_name

    def convert(self, id: int, json_object: Dict[str, Any]) -> EntityInterface:
        raise NotImplementedError