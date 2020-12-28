from gacha.entities import EntityInterface

class EmptyEntity(EntityInterface):
    def __init__(self, id: int):
        super().__init__(id)