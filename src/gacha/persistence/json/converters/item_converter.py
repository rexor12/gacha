from .entity_converter_interface import EntityConverterInterface
from gacha.entities import ItemPrototype
from typing import Any, Dict

class ItemConverter(EntityConverterInterface):
    def __init__(self):
        super().__init__("items")

    def convert(self, id: int, json_object: Dict[str, Any]) -> ItemPrototype:
        entity = ItemPrototype(id, json_object.get("name", "Unknown"))
        entity.item_type_id = int(json_object.get("type", 0))
        entity.rank_id = int(json_object.get("rank", 0))
        return entity