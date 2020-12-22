from .entity_provider_interface import EntityProviderInterface

class PullProviderInterface:
    def __init__(self, entityProvider: EntityProviderInterface):
        pass

    def pull(self, supply_type: str, pull_count: int):
        raise NotImplementedError