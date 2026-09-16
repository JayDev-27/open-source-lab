"""ANSI terminal color codes."""
class Logger:
    GREEN = '\033[92m'; RED = '\033[91m'; RESET = '\033[0m'
    @staticmethod
    def info(msg): print(f'{Logger.GREEN}[INFO]{Logger.RESET} {msg}')
    @staticmethod
    def error(msg): print(f'{Logger.RED}[ERROR]{Logger.RESET} {msg}')
