from gacha.models import VirtualItem
from gacha.providers import EntityProviderInterface
from gacha.resolvers import ItemResolverInterface
from typing import Generator

class SimpleItemResolver(ItemResolverInterface):
    def __init__(self, entity_provider: EntityProviderInterface):
        super().__init__(entity_provider)

    def resolve(self, item_id: int) -> Generator[VirtualItem, None, None]:
        item = self._entity_provider.get_entity("items", item_id)
        if item is None:
            raise ValueError(f"The item with the specified identifier '{item_id}' doesn't exist.")
        if item.id == 0:
            # The item with the identifier "0" is a special item that we
            # don't resolve on purpose for the tests' sake.
            return
        virtual_item = VirtualItem(item_id, item.name)
        yield virtual_item