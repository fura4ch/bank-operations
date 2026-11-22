import pytest

from src.decorators import log


def test_log_to_console_success(capsys):
    """Успешное выполнение логируется в консоль."""

    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()
    assert result == 5
    assert "add ok" in captured.out


def test_log_to_file_success(tmp_path):
    """Успешное выполнение логируется в файл."""
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(4, 5)
    assert result == 20
    content = log_file.read_text(encoding="utf-8")
    assert "multiply ok" in content


def test_log_to_console_error(capsys):
    """Ошибка логируется в консоль с входными параметрами."""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError" in captured.out
    assert "Inputs: (10, 0), {}" in captured.out


def test_log_to_file_error(tmp_path):
    """Ошибка логируется в файл с входными параметрами."""
    log_file = tmp_path / "error.log"

    @log(filename=str(log_file))
    def fail_func(x):
        raise ValueError("test error")

    with pytest.raises(ValueError):
        fail_func(42)

    content = log_file.read_text(encoding="utf-8")
    assert "fail_func error: ValueError" in content
    assert "Inputs: (42,), {}" in content


def test_log_kwargs_in_error(capsys):
    """Ошибка с kwargs логируется корректно."""

    @log()
    def fail_with_kwargs(a, b=0):
        return a / b

    with pytest.raises(ZeroDivisionError):
        fail_with_kwargs(5, b=0)

    captured = capsys.readouterr()
    assert "Inputs: (5,), {'b': 0}" in captured.out
