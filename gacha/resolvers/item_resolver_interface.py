from ..models import VirtualItem
from ..providers import EntityProviderInterface
from typing import Generator

class ItemResolverInterface:
    def __init__(self, entity_provider: EntityProviderInterface):
        self._entity_provider = entity_provider

    def resolve(self, item_id: int) -> Generator[VirtualItem, None, None]:
        raise NotImplementedError