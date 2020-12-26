from .entity_interface import EntityInterface

class ItemPrototype(EntityInterface):
    def __init__(self, id: int, name: str):
        super().__init__(id)
        self.name = name
        self.item_type_id = 0
        self.rank_id = 0