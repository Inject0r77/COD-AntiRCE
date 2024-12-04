import psutil
from config import GAME_PROCESS
from logger import main_logger

def list_running_processes() -> list[str]:
    """
    Возвращает список текущих запущенных процессов.
    """
    return [proc.name() for proc in psutil.process_iter(['name'])]

def is_game_process(pid: int) -> bool:
    """
    Проверяет, относится ли процесс к игре.
    """
    try:
        return psutil.Process(pid).name() == GAME_PROCESS
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False

def terminate_process(pid: int):
    """
    Принудительно завершает процесс по идентификатору.
    """
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        main_logger.info(f"Процесс {proc.name()} (PID {pid}) успешно завершён.")
    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
        main_logger.error(f"Не удалось завершить процесс (PID {pid}): {e}")

def monitor_game_process():
    """
    Следит за процессом игры и выполняет защитные действия, если процесс пропал.
    """
    while True:
        if GAME_PROCESS not in list_running_processes():
            main_logger.warning(f"Игра {GAME_PROCESS} больше не запущена!")
            break
