from .entity_interface import EntityInterface

class ItemType(EntityInterface):
    def __init__(self, id: int, name: str):
        super().__init__(id)
        self.name = name
        self.is_multi_pull = False
        self.multi_pull_min = 0
        self.multi_pull_max = 0