from .item import Item

class Pool:
    def __init__(self, name: str):
        self.name = name
        self.items = list[Item]()