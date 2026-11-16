"""Модуль для генерации и фильтрации данных транзакций."""

from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по заданной валюте.

    Args:
        transactions: Список словарей с транзакциями.
        currency: Код валюты для фильтрации (например, 'USD').

    Yields:
        Транзакции, соответствующие заданной валюте.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генерирует описания транзакций по очереди.

    Args:
        transactions: Список словарей с транзакциями.

    Yields:
        Описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в заданном диапазоне.

    Args:
        start: Начальное значение диапазона (включительно).
        stop: Конечное значение диапазона (включительно).

    Yields:
        Номер карты в формате 'XXXX XXXX XXXX XXXX'.
    """
    for num in range(start, stop + 1):
        num_str = str(num).zfill(16)
        formatted = " ".join([num_str[i : i + 4] for i in range(0, 16, 4)])
        yield formatted
