import pytest

from src.masks import get_mask_account, get_mask_card_number


class TestGetMaskCardNumber:
    """Тесты для функции get_mask_card_number."""

    def test_valid_card_number(self, valid_card_number):
        """Корректный 16-значный номер маскируется по шаблону."""
        result = get_mask_card_number(valid_card_number)
        assert result == "1234 56** **** 3456"

    @pytest.mark.parametrize(
        "invalid_number",
        [
            "123456789012345",   # 15 цифр
            "12345678901234567", # 17 цифр
            "12345678901234ab",  # буквы
            "1234 5678 9012 3456",  # пробелы
            "",                  # пустая строка
        ],
    )
    def test_invalid_card_number_raises(self, invalid_number):
        """Некорректные номера вызывают ValueError."""
        with pytest.raises(ValueError):
            get_mask_card_number(invalid_number)


class TestGetMaskAccount:
    """Тесты для функции get_mask_account."""

    def test_valid_account_number(self, valid_account_number):
        """Корректный номер счёта маскируется по шаблону **XXXX."""
        result = get_mask_account(valid_account_number)
        assert result == "**7890"

    def test_minimum_length_account(self):
        """Счёт ровно из 4 цифр — граничный случай."""
        result = get_mask_account("1234")
        assert result == "**1234"

    @pytest.mark.parametrize(
        "invalid_account",
        [
            "123",       # 3 цифры
            "12ab",      # буквы
            "",          # пустая строка
        ],
    )
    def test_invalid_account_raises(self, invalid_account):
        """Некорректные номера счёта вызывают ValueError."""
        with pytest.raises(ValueError):
            get_mask_account(invalid_account)