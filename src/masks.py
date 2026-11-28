"""Модуль для маскировки номеров банковских карт и счетов."""

import logging
from pathlib import Path

# Создаем папку logs, если ее нет
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Настройка логгера для модуля masks
masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)

# Форматтер
masks_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Файловый обработчик
masks_file_handler = logging.FileHandler(log_dir / "masks.log", mode="w", encoding="utf-8")
masks_file_handler.setFormatter(masks_formatter)

# Добавляем обработчик к логгеру
masks_logger.addHandler(masks_file_handler)


def get_mask_card_number(card_number: str) -> str:
    """..."""
    masks_logger.debug(f"Вызов get_mask_card_number с аргументом: {card_number}")
    if len(card_number) != 16 or not card_number.isdigit():
        masks_logger.error(f"Ошибка валидации номера карты: {card_number}")
        raise ValueError("Номер карты должен содержать 16 цифр")

    masked_part = "** ****"
    first_part = card_number[:6]
    last_part = card_number[-4:]

    result = f"{first_part[:4]} {first_part[4:6]}{masked_part} {last_part}"
    masks_logger.debug(f"Результат маскирования карты: {result}")
    return result


def get_mask_account(account_number: str) -> str:
    """..."""
    masks_logger.debug(f"Вызов get_mask_account с аргументом: {account_number}")
    if len(account_number) < 4 or not account_number.isdigit():
        masks_logger.error(f"Ошибка валидации номера счета: {account_number}")
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    result = f"**{account_number[-4:]}"
    masks_logger.debug(f"Результат маскирования счета: {result}")
    return result
