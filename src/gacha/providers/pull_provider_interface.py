from .entity_provider_interface import EntityProviderInterface

class PullProviderInterface:
    def __init__(self, entityProvider: EntityProviderInterface):
        pass

    def get_pool_codes(self) -> list[str]:
        raise NotImplementedError

    def has_pool(self, pool_code: str) -> bool:
        raise NotImplementedError

    def get_pool_name(self, pool_code: str) -> str:
        raise NotImplementedError

    def pull(self, supply_type: str, pull_count: int):
        raise NotImplementedError