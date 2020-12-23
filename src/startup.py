from gacha.entities import ItemRank, ItemType, ItemPrototype, LootTableGroup, Pool
from gacha.logging.console_log import ConsoleLog
from gacha.logging.log_level import LogLevel
from gacha.persistence.json import JsonEntityProvider
from gacha.persistence.json.converters import ItemTypeConverter, ItemRankConverter, ItemConverter, PoolConverter
from gacha.providers import InMemoryEntityProvider, EntityProviderInterface
from honkai.providers.pull_provider import PullProvider
from honkai.resolvers.item_resolver import ItemResolver

log = ConsoleLog(LogLevel.INFORMATION)

# Entity provider
log.debug("Initializing entity provider...")
entity_provider = JsonEntityProvider("./src/database.json", log, [
    ItemConverter(), ItemRankConverter(), ItemTypeConverter(), PoolConverter()
])
log.debug("Entity provider initialized.")

log.debug("Initializing item resolver...")
item_resolver = ItemResolver(entity_provider, log)
log.debug("Item resolver initialized.")

log.debug("Initializing pull provider...")
pull_provider = PullProvider(entity_provider, item_resolver, log)
log.debug("Available pools: {0}".format(str.join(", ", pull_provider.get_pool_codes())))
log.debug("Pull provider initialized.")
log.info("Gacha system initialized.")

log.info("Simulating pulls...")
for pull in pull_provider.pull("eq", 10):
    log.info(f"{pull.name} x{pull.count} ({pull.is_rare})")
log.info("Pull simulation finished.")