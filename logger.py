import logging

def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    """
    Настраивает и возвращает объект логгера.

    :param name: Имя логгера
    :param log_file: Путь к файлу логов
    :param level: Уровень логирования
    :return: Логгер
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Настраиваем основной логгер
main_logger = setup_logger("Main", "app.log")
