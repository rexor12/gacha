from .entity_interface import EntityInterface

class ItemRank(EntityInterface):
    def __init__(self, id: int, name: str):
        super().__init__(id)
        self.name = name
        self.is_rare = False