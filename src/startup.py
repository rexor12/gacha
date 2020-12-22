from gacha.entities import ItemRank, ItemType, ItemPrototype, LootTableGroup, Pool
from gacha.logging.console_log import ConsoleLog
from gacha.logging.log_level import LogLevel
from gacha.providers import InMemoryEntityProvider
from honkai.providers.pull_provider import PullProvider
from honkai.resolvers.item_resolver import ItemResolver

log = ConsoleLog(LogLevel.DEBUG)

def create_weapon(id: int, name: str, rank_id: int) -> ItemPrototype:
    weapon = ItemPrototype(id, name)
    weapon.item_type_id = 1
    weapon.rank_id = rank_id
    return weapon

log.info("Initializing the gacha system...")

# Item ranks
log.debug("Building item ranks...")
rank_b = ItemRank(0, "B")
rank_a = ItemRank(1, "A")
rank_s = ItemRank(2, "S")
rank_s.is_rare = True
rank_two_star = ItemRank(3, "2*")
rank_three_star = ItemRank(4, "3*")
rank_four_star = ItemRank(5, "4*")
rank_four_star.is_rare = True
rank_five_star = ItemRank(6, "5*")
rank_five_star.is_rare = True
log.debug("Item ranks built successfully.")

# Item types
log.debug("Building item types...")
type_valkyrie = ItemType(0, "Valkyrie")
type_equipment = ItemType(1, "Equipment")
type_soul = ItemType(2, "Soul")
type_soul.is_multi_pull = True
type_soul.multi_pull_min = 5
type_soul.multi_pull_max = 8
type_eqmat = ItemType(3, "Equipment material")
type_chexp = ItemType(4, "Character exp")
type_currency = ItemType(5, "Currency")
type_skmat = ItemType(6, "Skill material")
type_fragment = ItemType(7, "Fragment")
type_fragment.is_multi_pull = True
type_fragment.multi_pull_min = 4
type_fragment.multi_pull_max = 6
type_stigmata = ItemType(8, "Stigmata")
type_itexp = ItemType(9, "Item exp")
log.debug("Item types built successfully.")

# Items
log.debug("Building items...")
item_valkyrie = ItemPrototype(0, "Dea Anchora")
item_valkyrie.item_type_id = 0 # Valkyrie
item_valkyrie.rank_id = 2 # S rank

item_weapon = ItemPrototype(1, "Starlance Prime")
item_weapon.item_type_id = 1 # Equipment
item_weapon.rank_id = 5 # 4* rank

item_valkyrie2 = ItemPrototype(2, "Herrscher of Thunder")
item_valkyrie2.item_type_id = 0 # Valkyrie
item_valkyrie2.rank_id = 2 # S rank

item_stigmata = ItemPrototype(3, "Shakespeare: Adrift")
item_stigmata.item_type_id = 8 # Stigmata
item_stigmata.rank_id = 5 # 4* rank

item_kikaku = create_weapon(4, "Thunder Kikaku", 5)
item_briareus = create_weapon(5, "Briareus PRI", 5)
item_beauty = create_weapon(6, "Sleeping Beauty", 5)
item_relic = create_weapon(7, "11th Sacred Relic", 5)
item_undine = create_weapon(8, "Undine's Tale", 5)
item_starlance = create_weapon(9, "Starlance Prime", 5)
item_eosg = create_weapon(10, "Eos Gloria", 5)
log.debug("Items built successfully.")

# Pools
log.debug("Building pools...")
pool_foca = Pool(0, "foca", "Focused Supply A")
pool_foca.loot_table = [
    # 4* UP weapon
    LootTableGroup(1.83, [9]),
    # 4* weapons
    LootTableGroup(2.75, [4, 5, 6, 7, 8, 10]),
    # 4* UP stigmatas
    LootTableGroup(5.06, []),
    # 4* stigmatas
    LootTableGroup(20.7, []),
    # 3* weapons
    LootTableGroup(11.23, []),
    # 3* stigmatas
    LootTableGroup(33.69, []),
    # matz/coins
    LootTableGroup(42.68, []),
]
log.debug("Pools built successfully.")

# Entity provider
log.debug("Initializing entity provider...")
entity_provider = InMemoryEntityProvider([
    ("item_ranks", rank_b),
    ("item_ranks", rank_a),
    ("item_ranks", rank_s),
    ("item_ranks", rank_two_star),
    ("item_ranks", rank_three_star),
    ("item_ranks", rank_four_star),
    ("item_ranks", rank_five_star),

    ("item_types", type_valkyrie),
    ("item_types", type_equipment),
    ("item_types", type_soul),
    ("item_types", type_eqmat),
    ("item_types", type_chexp),
    ("item_types", type_skmat),
    ("item_types", type_fragment),
    ("item_types", type_stigmata),
    ("item_types", type_itexp),

    ("items", item_valkyrie),
    ("items", item_valkyrie2),
    ("items", item_weapon),
    ("items", item_stigmata),
    ("items", item_kikaku),
    ("items", item_briareus),
    ("items", item_beauty),
    ("items", item_relic),
    ("items", item_undine),
    ("items", item_starlance),
    ("items", item_eosg),

    ("pools", pool_foca)
], log)
# log.debug(entity_provider.get_entity("item_ranks", rank_b.id))
# log.debug(entity_provider.get_entity("item_ranks", 999))
# log.debug(entity_provider.get_entity("item_types", type_valkyrie.id))
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
for pull in pull_provider.pull("foca", 10):
    log.info(f"{pull.name} x{pull.count} ({pull.is_rare})")
log.info("Pull simulation finished.")

