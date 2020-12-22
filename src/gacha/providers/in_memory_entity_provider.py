from .entity_provider_interface import EntityProviderInterface
from ..entities import EntityInterface
from ..logging.log_base import LogBase
from typing import Generator, Sequence

class InMemoryEntityProvider(EntityProviderInterface):
    """
    Implementation of the ``EntityProviderInterface`` that holds collections of entities in the memory.
    """
    def __init__(self, entities: Sequence[tuple[str, EntityInterface]], log: LogBase):
        super().__init__()
        self._log = log
        self._entities = self._transform_entities(entities)

    def get_entity(self, collection_name: str, entity_id: int, default_value: EntityInterface = None) -> EntityInterface:
        entities_by_type = self._entities.get(collection_name, None)
        if not entities_by_type:
            return default_value
        return entities_by_type.get(entity_id, default_value)

    def get_collection(self, collection_name: str) -> Generator[EntityInterface, None, None]:
        entities_by_type = self._entities.get(collection_name, {})
        for entity in entities_by_type.values():
            yield entity
    
    def _transform_entities(self, entities: Sequence[tuple[str, EntityInterface]]):
        transformed_entities = {}
        for collection_name, entity in entities:
            entities_by_type = transformed_entities.get(collection_name, None)
            if not entities_by_type:
                transformed_entities[collection_name] = entities_by_type = {}
            entities_by_type[entity.id] = entity
            self._log.debug(f"Added entity with identifier '{entity.id}' to collection with identifier '{collection_name}'.")
        return transformed_entities