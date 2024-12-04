import logging
import psutil
from pydivert import WinDivert
from packet_interceptor import intercept_packets, extract_player_info
from rce_protection import protect_game
from logger import main_logger

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,  # Устанавливаем уровень логирования на DEBUG для получения более детальной информации
)
logger = logging.getLogger()

# Добавление обработчика вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования для консоли
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Добавляем обработчик в логгер
logger.addHandler(console_handler)

def check_process():
    """Проверка наличия процесса игры iw5mp.exe"""
    logger.info("Проверка запущенных процессов...")
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == "iw5mp.exe":
            logger.info(f"Процесс игры {proc.info['name']} найден с PID {proc.info['pid']}")
            return proc.info['pid']
    else:
        logger.warning("Процесс игры не найден!")
    return None

def monitor_network():
    """Мониторинг сетевого трафика, перехват пакетов с полезной нагрузкой"""
    logger.info("Запуск перехвата сетевого трафика...")
    with WinDivert("tcp.DstPort == 27015 and tcp.PayloadLength > 0") as w:
        for packet in w:
            logger.debug(f"Перехваченный пакет: {packet}")
            # Пример проверки и обработки пакета
            if packet.payload:
                logger.debug("Обнаружена полезная нагрузка в пакете")
                # Извлечение информации о подключенных игроках из полезной нагрузки
                player_info = extract_player_info(packet.payload)
                if player_info:
                    logger.info(f"Информация о подключенном игроке: {player_info}")

def main():
    """Основная функция, которая запускает мониторинг"""
    logger.info("Запуск скрипта защиты от RCE Exploits...")

    # Проверка процесса игры
    pid = check_process()
    if pid is not None:
        logger.info(f"Процесс игры с PID {pid} найден. Начинаем защиту.")
        # Запуск защиты от RCE Exploits
        protect_game()

        # Запуск мониторинга сетевого трафика
        monitor_network()

    else:
        logger.error("Процесс игры не найден. Программа завершена.")
        return

if __name__ == "__main__":
    main()
