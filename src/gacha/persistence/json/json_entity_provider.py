from .converters import EntityConverterInterface
from gacha.entities import EntityInterface
from gacha.logging import LogBase
from gacha.providers import EntityProviderInterface
from json import load
from typing import Dict, Generator, List

class JsonEntityProvider(EntityProviderInterface):
    def __init__(self, database_json_file_path, log: LogBase, entity_converters: List[EntityConverterInterface] = []):
        super().__init__()
        self._log = log
        self._entity_converters = dict([(converter.collection_name, converter) for converter in entity_converters])
        self._entities = self._load_entities(database_json_file_path)

    def get_entity(self, collection_name: str, entity_id: int, default_value: EntityInterface = None) -> EntityInterface:
        return self._entities.get(collection_name, {}).get(entity_id, default_value)

    def get_collection(self, collection_name: str) -> Generator[EntityInterface, None, None]:
        for entity in self._entities.get(collection_name, {}).values():
            yield entity

    def _load_entities(self, database_json_file_path) -> Dict[str, Dict[int, EntityInterface]]:
        entities: Dict[str, Dict[int, EntityInterface]] = {}
        with open(database_json_file_path) as database_file:
            database = load(database_file)
        for collection_name, json_collection in database.items():
            converter = self._entity_converters.get(collection_name, None)
            if not converter:
                self._log.warning(f"No converter was found for collection '{collection_name}', thus it will be ignored.")
                continue
            collection: Dict[int, EntityInterface] = {}
            for entity_id, entity in json_collection.items():
                collection[int(entity_id)] = converter.convert(int(entity_id), entity)
            entities[collection_name] = collection
            self._log.info(f"Loaded {len(collection)} entities from collection '{collection_name}'.")
        self._log.info(f"Loaded {len(entities)} collections.")
        return entities