from ..utils import isclose
from typing import List

class LootTableGroup:
    def __init__(self, rate: float, item_ids: List[int] = []):
        if rate < 0.0 or rate > 100.0 or isclose(rate, 100.0):
            raise ValueError("The loot table group rate must be between 0, inclusive, and 100, exclusive.")
        self.rate = rate
        self.item_ids = item_ids