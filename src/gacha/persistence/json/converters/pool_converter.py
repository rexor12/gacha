from .entity_converter_interface import EntityConverterInterface
from gacha.entities import LootTableGroup, Pool
from typing import Any

class PoolConverter(EntityConverterInterface):
    def __init__(self):
        super().__init__("pools")

    def convert(self, id: int, json_object: dict[str, Any]) -> Pool:
        entity = Pool(id, json_object.get("code", ""), json_object.get("name", "Unknown"))
        entity.is_available = bool(json_object.get("available", False))
        for json_loot_table in json_object.get("loot_table", []):
            loot_table_group = LootTableGroup(
                float(json_loot_table.get("rate", 0.0)),
                [int(item_id) for item_id in json_loot_table.get("items", [])]
            )
            entity.loot_table.append(loot_table_group)
        return entity