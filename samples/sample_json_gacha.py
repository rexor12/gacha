from gacha.logging import LogLevel
from gacha.logging import ConsoleLog
from gacha.persistence.json import JsonEntityProvider
from gacha.persistence.json.converters import ItemTypeConverter, ItemRankConverter, ItemConverter, PoolConverter
from gacha.providers import SimplePullProvider
from gacha.resolvers import SimpleItemResolver

log = ConsoleLog(LogLevel.INFORMATION)

log.info("Loading Generic Gacha System...")
log.debug("Initializing entity provider...")
entity_provider = JsonEntityProvider("./samples/res/database.json", log, [
    ItemConverter(), ItemRankConverter(), ItemTypeConverter(), PoolConverter()
])
log.debug("Entity provider initialized.")

log.debug("Initializing item resolver...")
item_resolver = SimpleItemResolver(entity_provider)
log.debug("Item resolver initialized.")

log.debug("Initializing pull provider...")
pull_provider = SimplePullProvider(entity_provider, item_resolver, log)
log.debug("Available pools: {0}".format(str.join(", ", pull_provider.get_pool_codes())))
log.debug("Pull provider initialized.")
log.info("Generic Gacha System loaded.")

log.info("Simulating pulls...")
for pull in pull_provider.pull("common", 10):
    log.info("{} x{}{}".format(pull.name, pull.count, " (Rare)" if pull.is_rare else ""))
log.info("Pull simulation finished.")
log.info("Exiting...")