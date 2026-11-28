import pytest


@pytest.fixture
def valid_card_number():
    """Фикстура: корректный 16-значный номер карты."""
    return "1234567890123456"


@pytest.fixture
def valid_account_number():
    """Фикстура: корректный номер счёта (10 цифр)."""
    return "1234567890"


@pytest.fixture
def operations_list():
    """Фикстура: список банковских операций для тестов processing."""
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
    ]


@pytest.fixture
def card_info():
    """Фикстура: строка с номером карты."""
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def account_info():
    """Фикстура: строка с номером счёта."""
    return "Счет 73654108430135874305"


@pytest.fixture
def valid_date_str():
    """Фикстура: корректная ISO-дата."""
    return "2024-03-11T02:26:18.671407"
