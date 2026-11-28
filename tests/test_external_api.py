from unittest.mock import patch

import pytest

from src.external_api import convert_to_rub


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get):
    """Конвертирует USD в рубли через API (замокано)."""
    mock_get.return_value.json.return_value = {"result": 7500.0}
    mock_get.return_value.raise_for_status.return_value = None

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"},
        }
    }

    with patch.dict("os.environ", {"EXCHANGE_API_KEY": "test_key"}):
        result = convert_to_rub(transaction)

    assert result == 7500.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_to_rub_eur(mock_get):
    """Конвертирует EUR в рубли через API (замокано)."""
    mock_get.return_value.json.return_value = {"result": 8000.0}
    mock_get.return_value.raise_for_status.return_value = None

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "EUR"},
        }
    }

    with patch.dict("os.environ", {"EXCHANGE_API_KEY": "test_key"}):
        result = convert_to_rub(transaction)

    assert result == 8000.0


def test_convert_to_rub_rub():
    """Для RUB возвращает сумму без обращения к API."""
    transaction = {
        "operationAmount": {
            "amount": "1000.0",
            "currency": {"code": "RUB"},
        }
    }

    result = convert_to_rub(transaction)
    assert result == 1000.0


def test_convert_to_rub_missing_api_key():
    """Если нет API-ключа — ValueError."""
    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"},
        }
    }

    with patch.dict("os.environ", {}, clear=True):
        with pytest.raises(ValueError):
            convert_to_rub(transaction)
