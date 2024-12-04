# Название процесса игры
GAME_PROCESS = "iw5mp.exe"

# Фильтр для перехвата сетевых пакетов
FILTER = "outbound and ip and tcp and tcp.PayloadLength > 0"

# Вредоносные команды
MALICIOUS_COMMANDS = [
    "open website",
    "spawn process",
    "kill process",
    "unload dll",
    "cbuf command"
]
