from gacha.logging import LogLevel
from gacha.logging import ConsoleLog
from gacha.persistence.json import JsonEntityProvider
from gacha.persistence.json.converters import ItemTypeConverter, ItemRankConverter, ItemConverter, PoolConverter
from gacha.providers import SimplePullProvider
from gacha.resolvers import SimpleItemResolver

# Initialize an instance of our logger implementation.
# You can use either one of the shipped implementations or implement your own one.
log = ConsoleLog(LogLevel.INFORMATION)

log.info("Loading Generic Gacha System...")
log.debug("Initializing entity provider...")
# In this case, our database comes from a JSON file, so let's instantiate the JsonEntityProvider.
# This is also a good point for extension in case you have a data source not supported
# by the framework by default.
entity_provider = JsonEntityProvider("./samples/res/database.json", log, [
    # It's important to pass to it the entity converters.
    # In our case, our database has items, item ranks, item types and item pools.
    ItemConverter(), ItemRankConverter(), ItemTypeConverter(), PoolConverter()
])
log.debug("Entity provider initialized.")

log.debug("Initializing item resolver...")
# The item resolver determines how to interpret item prototypes from the database.
# If you need to transform items instead of using them "as is" in the database,
# this is the point you'd want to extend by writing your own implementation.
item_resolver = SimpleItemResolver(entity_provider)
log.debug("Item resolver initialized.")

log.debug("Initializing pull provider...")
# The pull provider defines the logic of the gacha pulls. In our implementation,
# it takes the entity provider and the item resolver to construct its item pools.
pull_provider = SimplePullProvider(entity_provider, item_resolver, log)
# If you don't like the default pull count limitation, you can set it after initialization.
pull_provider.pull_count_min = 2
pull_provider.pull_count_max = 5
log.debug("Available pools: {0}".format(str.join(", ", pull_provider.get_pool_codes())))
log.debug("Pull provider initialized.")
log.info("Generic Gacha System loaded.")

log.info("Simulating pulls...")
# Now that everything has been set up, we can pull some items. :)
for pull in pull_provider.pull("common", 10):
    log.info("{} x{}{}".format(pull.name, pull.count, " (Rare)" if pull.is_rare else ""))
log.info("Pull simulation finished.")
log.info("Exiting...")