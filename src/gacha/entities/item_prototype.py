from .entity_interface import EntityInterface

class ItemPrototype(EntityInterface):
    """
    Describes the properties of an item. This class may be inherited for additional properties.
    """

    def __init__(self, id: int, name: str):
        """
        Initializes a new instance of `Item`.

        Args:
            id (int): The globally unique identifier of the item.
            name (str): The name of the item.
        """

        super().__init__(id)
        self.name = name
        self.item_type_id = 0
        self.rank_id = 0