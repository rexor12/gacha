from .entity_provider_interface import EntityProviderInterface
from typing import List

class PullProviderInterface:
    def __init__(self, entityProvider: EntityProviderInterface):
        pass

    def get_pool_codes(self) -> List[str]:
        raise NotImplementedError

    def has_pool(self, pool_code: str) -> bool:
        raise NotImplementedError

    def get_pool_name(self, pool_code: str) -> str:
        raise NotImplementedError

    def pull(self, pool_code: str, pull_count: int):
        raise NotImplementedError