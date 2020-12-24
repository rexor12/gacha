from gacha.logging import LogLevel
from gacha.logging import ConsoleLog
from gacha.persistence.json import JsonEntityProvider
from gacha.persistence.json.converters import ItemTypeConverter, ItemRankConverter, ItemConverter, PoolConverter
from honkai.providers.pull_provider import PullProvider
from honkai.resolvers.item_resolver import ItemResolver

class Startup:
    def __init__(self):
        self.log = ConsoleLog(LogLevel.INFORMATION)

    def execute(self):
        self.log.debug("Initializing entity provider...")
        entity_provider = JsonEntityProvider("./src/database.json", self.log, [
            ItemConverter(), ItemRankConverter(), ItemTypeConverter(), PoolConverter()
        ])
        self.log.debug("Entity provider initialized.")

        self.log.debug("Initializing item resolver...")
        item_resolver = ItemResolver(entity_provider, self.log)
        self.log.debug("Item resolver initialized.")

        self.log.debug("Initializing pull provider...")
        pull_provider = PullProvider(entity_provider, item_resolver, self.log)
        self.log.debug("Available pools: {0}".format(str.join(", ", pull_provider.get_pool_codes())))
        self.log.debug("Pull provider initialized.")
        self.log.info("Gacha system initialized.")

        self.log.info("Simulating pulls...")
        for pull in pull_provider.pull("eq", 10):
            self.log.info(f"{pull.name} x{pull.count} ({pull.is_rare})")
        self.log.info("Pull simulation finished.")

Startup().execute()