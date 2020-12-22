from .log_level import LogLevel

class LogBase:
    def __init__(self, log_level: LogLevel):
        self.log_level = log_level

    def write(self, level: LogLevel, message: str):
        raise NotImplementedError

    def debug(self, message: str):
        self.write(LogLevel.DEBUG, message)

    def info(self, message: str):
        self.write(LogLevel.INFORMATION, message)

    def warning(self, message: str):
        self.write(LogLevel.WARNING, message)

    def error(self, message: str):
        self.write(LogLevel.ERROR, message)

    def critical(self, message: str):
        self.write(LogLevel.CRITICAL, message)