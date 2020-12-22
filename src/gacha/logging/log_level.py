from enum import IntEnum, unique

@unique
class LogLevel(IntEnum):
    TRACE = 0
    DEBUG = 1
    INFORMATION = 3
    WARNING = 4
    ERROR = 5
    CRITICAL = 6