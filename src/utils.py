"""Модуль для работы с JSON-файлами."""

import json
import logging
from pathlib import Path
from typing import Any, Dict, List

# Создаем папку logs, если ее нет
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Настройка логгера для модуля utils
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

# Форматтер
utils_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Файловый обработчик
utils_file_handler = logging.FileHandler(log_dir / "utils.log", mode="w", encoding="utf-8")
utils_file_handler.setFormatter(utils_formatter)

# Добавляем обработчик к логгеру
utils_logger.addHandler(utils_file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.
    """
    utils_logger.debug(f"Попытка загрузки транзакций из файла: {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            utils_logger.error(f"Файл {file_path} содержит не список")
            return []
        utils_logger.info(f"Успешно загружено {len(data)} транзакций из {file_path}")
        return data
    except FileNotFoundError:
        utils_logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        utils_logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []
