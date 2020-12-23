from .entity_converter_interface import EntityConverterInterface
from gacha.entities import ItemRank
from typing import Any

class ItemRankConverter(EntityConverterInterface):
    def __init__(self):
        super().__init__("item_ranks")

    def convert(self, id: int, json_object: dict[str, Any]) -> ItemRank:
        entity = ItemRank(id, json_object.get("name", "Unknown"))
        entity.is_rare = bool(json_object.get("is_rare", False))
        return entity