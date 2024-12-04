import psutil
import pydivert
from config import GAME_PROCESS, FILTER, MALICIOUS_COMMANDS

def is_game_running() -> bool:
    """
    Проверяет, запущен ли процесс игры.
    """
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == GAME_PROCESS:
            return True
    return False

def is_malicious(packet: pydivert.Packet) -> bool:
    """
    Проверяет, содержит ли пакет вредоносные команды.
    """
    try:
        payload = packet.tcp.payload.decode(errors="ignore").lower()
        return any(cmd in payload for cmd in MALICIOUS_COMMANDS)
    except Exception as e:
        print(f"[ERROR] Ошибка анализа пакета: {e}")
        return False

def protect_game():
    """
    Защищает игровой процесс от RCE-атак.
    """
    if not is_game_running():
        print(f"[INFO] Процесс {GAME_PROCESS} не найден.")
        return

    print(f"[INFO] Защита включена для процесса: {GAME_PROCESS}")
    try:
        with pydivert.WinDivert(FILTER) as w:
            print("[INFO] Захват пакетов начат...")
            for packet in w:
                # Проверяем, связано ли это с игровым процессом
                if psutil.Process(packet.process_id).name() == GAME_PROCESS:
                    if is_malicious(packet):
                        print(f"[WARNING] Заблокирован вредоносный пакет: {packet}")
                    else:
                        w.send(packet)  # Передаем только безопасные пакеты
                else:
                    # Пропускаем пакеты, не связанные с игрой
                    w.send(packet)
    except Exception as e:
        print(f"[ERROR] Ошибка работы: {e}")
