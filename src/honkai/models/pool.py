from .item import Item
from typing import List

class Pool:
    def __init__(self, name: str):
        self.name = name
        self.items: List[Item] = []