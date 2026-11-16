import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    """Фикстура: список транзакций для тестов."""
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод с карты на карту",
        },
    ]


class TestFilterByCurrency:
    """Тесты для filter_by_currency."""

    def test_filter_usd(self, sample_transactions):
        """Фильтрует транзакции по USD."""
        result = list(filter_by_currency(sample_transactions, "USD"))
        assert len(result) == 2
        assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)

    def test_filter_no_matches(self, sample_transactions):
        """Возвращает пустой итератор, если нет совпадений."""
        result = list(filter_by_currency(sample_transactions, "EUR"))
        assert result == []

    def test_filter_empty_list(self):
        """Пустой список возвращает пустой итератор."""
        result = list(filter_by_currency([], "USD"))
        assert result == []


class TestTransactionDescriptions:
    """Тесты для transaction_descriptions."""

    def test_descriptions(self, sample_transactions):
        """Возвращает описания по очереди."""
        result = list(transaction_descriptions(sample_transactions))
        assert result == [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
        ]

    def test_empty_list(self):
        """Пустой список возвращает пустой итератор."""
        assert list(transaction_descriptions([])) == []


class TestCardNumberGenerator:
    """Тесты для card_number_generator."""

    @pytest.mark.parametrize(
        "start, stop, expected",
        [
            (
                1,
                3,
                [
                    "0000 0000 0000 0001",
                    "0000 0000 0000 0002",
                    "0000 0000 0000 0003",
                ],
            ),
            (
                9999,
                10001,
                [
                    "0000 0000 0000 9999",
                    "0000 0000 0001 0000",
                    "0000 0000 0001 0001",
                ],
            ),
        ],
    )
    def test_generator_range(self, start, stop, expected):
        """Генерирует номера в заданном диапазоне."""
        assert list(card_number_generator(start, stop)) == expected
