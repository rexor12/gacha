from .simple_entity import SimpleEntity
from gacha.persistence.json.converters import EntityConverterInterface
from typing import Any, Dict

class SimpleEntityConverter(EntityConverterInterface):
    def __init__(self):
        super().__init__("simples")

    def convert(self, id: int, json_object: Dict[str, Any]) -> SimpleEntity:
        entity = SimpleEntity(id)
        entity.prop1 = json_object.get("prop1", "")
        entity.prop2 = json_object.get("prop2", "")
        entity.array = [item for item in json_object.get("array", [])]
        return entity