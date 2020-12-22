from gacha.logging.log_level import LogLevel
from .log_base import LogBase

class ConsoleLog(LogBase):
    def __init__(self, log_level: LogLevel):
        super().__init__(log_level)

    def write(self, level: LogLevel, message: str):
        if level < self.log_level:
            return
        print(f"[{level.name}] {message}")