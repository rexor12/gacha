from gacha.logging import LogBase, LogLevel
from typing import List

class FakeLog(LogBase):
    def __init__(self):
        super().__init__(LogLevel.TRACE)
        self.messages: List[str] = []

    def write(self, level: LogLevel, message: str):
        self.messages.append(f"[{level}] {message}")

    def has_message(self, level: LogLevel, *message_bits) -> bool:
        message_bits = (str(level),) + message_bits
        for message in self.messages:
            if FakeLog._all(message, message_bits):
                return True
        return False

    @staticmethod
    def _all(value: str, value_bits) -> bool:
        for value_bit in value_bits:
            print(value_bit)
            if not value.__contains__(value_bit):
                continue
            return True
        return False