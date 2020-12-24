from .entity_converter_interface import EntityConverterInterface
from gacha.entities import ItemType
from typing import Any, Dict

class ItemTypeConverter(EntityConverterInterface):
    def __init__(self):
        super().__init__("item_types")

    def convert(self, id: int, json_object: Dict[str, Any]) -> ItemType:
        entity = ItemType(id, json_object.get("name", "Unknown"))
        entity.is_multi_pull = bool(json_object.get("is_multi", False))
        entity.multi_pull_min = int(json_object.get("multi_min", 0))
        entity.multi_pull_max = int(json_object.get("multi_max", 0))
        return entity