from ..models import Item, Pool, Pull
from gacha.entities import Pool as PoolPrototype
from gacha.logging import LogBase
from gacha.models import Item as GachaItem
from gacha.providers import PullProviderInterface, EntityProviderInterface
from gacha.resolvers import ItemResolverInterface
from gacha.utils import isclose
from gacha.utils.entity_provider_utils import get_item, get_item_rank, get_item_type
from random import choice, choices
from typing import Generator

PULL_COUNT_MIN = 1
PULL_COUNT_MAX = 10

class PullProvider(PullProviderInterface):
    def __init__(self, entity_provider: EntityProviderInterface, item_resolver: ItemResolverInterface, log: LogBase):
        self._entity_provider = entity_provider
        self._log = log
        self._pools = self._create_pools(item_resolver)

    def get_pool_codes(self) -> list[str]:
        return [code for code in self._pools.keys()]

    def pull(self, supply_type: str, pull_count: int = 10) -> Generator[Pull, None, None]:
        supply_type = supply_type.lower()
        pool = self._pools.get(supply_type, None)
        if not pool:
            self._log.error(f"Attempted to pull from the unexistent pool with the code '{supply_type}'.")
            raise ValueError("The specified pool doesn't exist.")
        pull_count = max(PULL_COUNT_MIN, min(pull_count, PULL_COUNT_MAX))
        return self._pull_items(pool, pull_count)

    def _pull_items(self, pool: Pool, pull_count: int):
        items = choices(pool.items, [item.rate for item in pool.items], k = pull_count)
        for pulled_item in items:
            item = get_item(self._entity_provider, pulled_item.id)
            if not item:
                self._log.warning(f"Pulled unexistent item with identifier '{pulled_item.id}'.")
                return Pull(pulled_item.id, pulled_item.name, 1, False)
            item_type = get_item_type(self._entity_provider, item.item_type_id)
            item_rank = get_item_rank(self._entity_provider, item.rank_id)
            is_rare = item_rank is not None and item_rank.is_rare
            if item_type is not None and item_type.is_multi_pull:
                yield Pull(item.id, pulled_item.name, choice(range(item_type.multi_pull_min, item_type.multi_pull_max)), is_rare)
                continue
            yield Pull(item.id, pulled_item.name, 1, is_rare)

    def _create_pools(self, item_resolver: ItemResolverInterface) -> dict[str, Pool]:
        pools = {}
        for pool_prototype in self._get_pools():
            if not pool_prototype.is_available:
                self._log.info(f"The pool '{pool_prototype.id}' is disabled.")
                continue
            pool = Pool(pool_prototype.name)
            for loot_table_group in pool_prototype.loot_table:
                if loot_table_group.rate < 0.0 or isclose(loot_table_group.rate, 0.0):
                    self._log.warning("Ignored loot table with non-positive rate.")
                    continue
                if len(loot_table_group.item_ids) == 0:
                    self._log.warning("Ignored loot table with no items.")
                    continue
                items = list[GachaItem]()
                for item_id in loot_table_group.item_ids:
                    for item in item_resolver.resolve(item_id):
                        items.append(item)
                if len(items) == 0:
                    self._log.warning("Ignored loot table with no resolved items.")
                    continue
                rate = loot_table_group.rate / len(items)
                for item in items:
                    pool.items.append(Item(item.id, item.name, rate))
                    self._log.debug(f"Added item {item.name} to pool '{pool_prototype.code}'.")
                self._log.debug(f"Loot table group with configured rate '{loot_table_group.rate}' has a per-item rate of '{rate}' with '{len(items)}' items.")
            if len(pool.items) == 0:
                self._log.warning(f"Ignored pool '{pool_prototype.code}' with no items.")
                continue
            pools[pool_prototype.code] = pool
            self._log.info(f"Registered pool '{pool_prototype.name}' with code '{pool_prototype.code}'.")
        return pools

    def _get_pools(self) -> Generator[PoolPrototype, None, None]:
        return self._entity_provider.get_collection("pools")
