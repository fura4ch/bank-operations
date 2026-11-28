import json

from src.utils import load_transactions


def test_load_transactions_success(tmp_path):
    """Загружает список транзакций из корректного JSON."""
    file_path = tmp_path / "operations.json"
    data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    file_path.write_text(json.dumps(data), encoding="utf-8")

    result = load_transactions(str(file_path))

    assert result == data


def test_load_transactions_file_not_found():
    """Возвращает пустой список, если файл не найден."""
    result = load_transactions("nonexistent_file.json")
    assert result == []


def test_load_transactions_empty_file(tmp_path):
    """Возвращает пустой список, если файл пуст."""
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == []


def test_load_transactions_not_a_list(tmp_path):
    """Возвращает пустой список, если JSON содержит не список."""
    file_path = tmp_path / "dict.json"
    file_path.write_text(json.dumps({"key": "value"}), encoding="utf-8")

    result = load_transactions(str(file_path))
    assert result == []
