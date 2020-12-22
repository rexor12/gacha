class EntityInterface:
    def __init__(self, id: int):
        if id < 0:
            raise ValueError("The identifier must be larger than zero.")
        self.id = id