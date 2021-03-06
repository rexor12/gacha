from .entity_interface import EntityInterface
from ..entities import LootTableGroup
from typing import List

class Pool(EntityInterface):
    def __init__(self, id: int, code: str, name: str):
        super().__init__(id)
        self.code = code
        self.name = name
        self.is_available = True
        self.loot_table: List[LootTableGroup] = []