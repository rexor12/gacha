from gacha.entities import EntityInterface

class SimpleEntity(EntityInterface):
    def __init__(self, id: int):
        super().__init__(id)
        self.prop1 = ""
        self.prop2 = ""
        self.array = []