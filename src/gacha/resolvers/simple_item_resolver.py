from .item_resolver_interface import ItemResolverInterface
from gacha.models import VirtualItem
from gacha.providers import EntityProviderInterface
from gacha.utils.entity_provider_utils import get_item
from typing import Generator

class SimpleItemResolver(ItemResolverInterface):
    def __init__(self, entity_provider: EntityProviderInterface):
        super().__init__(entity_provider)

    def resolve(self, item_id: int) -> Generator[VirtualItem, None, None]:
        item = get_item(self._entity_provider, item_id)
        if not item:
            return
        yield VirtualItem(item.id, item.name)