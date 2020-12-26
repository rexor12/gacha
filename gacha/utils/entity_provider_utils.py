from ..entities import ItemPrototype, ItemRank, ItemType
from ..providers import EntityProviderInterface

def get_item(entity_provider: EntityProviderInterface, id: int) -> ItemPrototype:
    return entity_provider.get_entity("items", id, None)

def get_item_rank(entity_provider: EntityProviderInterface, id: int) -> ItemRank:
    return entity_provider.get_entity("item_ranks", id, None)

def get_item_type(entity_provider: EntityProviderInterface, id: int) -> ItemType:
    return entity_provider.get_entity("item_types", id, None)