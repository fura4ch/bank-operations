"""Модуль для конвертации валют через внешний API."""

import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными о транзакции.

    Returns:
        Сумма транзакции в рублях (float).
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    api_key = os.getenv("EXCHANGE_API_KEY")
    if not api_key:
        raise ValueError("Не задан EXCHANGE_API_KEY в переменных окружения")

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    result = response.json()

    return float(result["result"])
