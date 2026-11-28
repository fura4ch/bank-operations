import pytest

from src.widget import get_date, mask_account_card


class TestMaskAccountCard:
    """Тесты для функции mask_account_card."""

    def test_mask_card(self, card_info):
        """Маскирует номер карты."""
        result = mask_account_card(card_info)
        assert result == "Visa Platinum 7000 79** **** 6361"

    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
            ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ],
    )
    def test_mask_different_cards(self, input_str, expected):
        """Маскирует разные типы карт."""
        assert mask_account_card(input_str) == expected

    def test_mask_account(self, account_info):
        """Маскирует номер счёта."""
        result = mask_account_card(account_info)
        assert result == "Счет **4305"

    def test_mask_min_account(self):
        """Счёт из 4 цифр — граничный случай."""
        assert mask_account_card("Счет 1234") == "Счет **1234"

    @pytest.mark.parametrize(
        "invalid_input",
        [
            "Visa 123",  # мало цифр для карты
            "",  # пустая строка
            "Счет",  # только слово, без номера
        ],
    )
    def test_mask_invalid(self, invalid_input):
        """Некорректные входные данные вызывают ValueError."""
        with pytest.raises(ValueError):
            mask_account_card(invalid_input)


class TestGetDate:
    """Тесты для функции get_date."""

    def test_get_date_valid(self, valid_date_str):
        """Преобразует ISO-дату в ДД.ММ.ГГГГ."""
        assert get_date(valid_date_str) == "11.03.2024"

    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("2023-12-31T23:59:59", "31.12.2023"),
            ("2024-01-01T00:00:00", "01.01.2024"),
        ],
    )
    def test_get_date_different_dates(self, input_str, expected):
        """Корректно преобразует разные даты."""
        assert get_date(input_str) == expected

    @pytest.mark.parametrize(
        "invalid_date",
        ["not-a-date", "", "2024-13-45T99:99:99"],
    )
    def test_get_date_invalid(self, invalid_date):
        """Некорректные даты вызывают ValueError."""
        with pytest.raises(ValueError):
            get_date(invalid_date)
