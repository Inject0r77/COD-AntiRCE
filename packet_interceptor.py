import pydivert
from config import FILTER
from logger import main_logger

def intercept_packets(callback):
    """
    Перехватывает пакеты и вызывает callback для обработки.
    """
    try:
        with pydivert.WinDivert(FILTER) as w:
            main_logger.info("Перехват пакетов начат...")
            for packet in w:
                if callback(packet):
                    main_logger.info(f"Обработан пакет: {packet}")
                else:
                    w.send(packet)
    except Exception as e:
        main_logger.error(f"Ошибка при перехвате пакетов: {e}")

def extract_player_info(payload):
    """
    Извлекает информацию о подключенных игроках из полезной нагрузки пакета.
    """
    # Это пример, нужно адаптировать под формат пакетов
    try:
        player_info = {}
        if b"player_name" in payload:
            player_info["name"] = payload.split(b"player_name=")[1].split(b"&")[0].decode(errors="ignore")
        if b"steamid" in payload:
            player_info["steamid"] = payload.split(b"steamid=")[1].split(b"&")[0].decode(errors="ignore")
        
        if player_info:
            return player_info
        return None
    except Exception as e:
        main_logger.error(f"Ошибка при извлечении информации о игроках: {e}")
        return None
