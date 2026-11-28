import pytest

from src.processing import filter_by_state, sort_by_date


class TestFilterByState:
    """Тесты для функции filter_by_state."""

    def test_filter_executed(self, operations_list):
        """Фильтрует операции по статусу EXECUTED (по умолчанию)."""
        result = filter_by_state(operations_list)
        assert len(result) == 2
        assert all(op["state"] == "EXECUTED" for op in result)

    def test_filter_canceled(self, operations_list):
        """Фильтрует операции по статусу CANCELED."""
        result = filter_by_state(operations_list, state="CANCELED")
        assert len(result) == 1
        assert result[0]["id"] == 594226727

    def test_filter_empty_list(self):
        """Пустой список возвращает пустой список."""
        assert filter_by_state([]) == []

    def test_filter_no_matches(self, operations_list):
        """Если нет операций с нужным статусом — пустой список."""
        result = filter_by_state(operations_list, state="PENDING")
        assert result == []


class TestSortByDate:
    """Тесты для функции sort_by_date."""

    def test_sort_descending(self, operations_list):
        """По умолчанию сортирует по убыванию даты (новые сначала)."""
        result = sort_by_date(operations_list)
        dates = [op["date"] for op in result]
        assert dates == sorted(dates, reverse=True)

    def test_sort_ascending(self, operations_list):
        """С reverse=False сортирует по возрастанию."""
        result = sort_by_date(operations_list, reverse=False)
        dates = [op["date"] for op in result]
        assert dates == sorted(dates)

    def test_sort_empty_list(self):
        """Пустой список возвращает пустой список."""
        assert sort_by_date([]) == []

    def test_sort_same_dates(self):
        """Одинаковые даты не ломают сортировку."""
        data = [
            {"id": 1, "date": "2020-01-01T00:00:00"},
            {"id": 2, "date": "2020-01-01T00:00:00"},
        ]
        result = sort_by_date(data)
        assert len(result) == 2
        assert result[0]["date"] == result[1]["date"]

    def test_sort_missing_date_key(self):
        """Если нет ключа 'date' — KeyError."""
        data = [{"id": 1, "state": "EXECUTED"}]
        with pytest.raises(KeyError):
            sort_by_date(data)
