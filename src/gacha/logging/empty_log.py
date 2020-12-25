from gacha.logging.log_level import LogLevel
from .log_base import LogBase

class EmptyLog(LogBase):
    def __init__(self):
        super().__init__(LogLevel.NONE)

    def write(self, level: LogLevel, message: str):
        pass