"""Модуль с декораторами для логирования."""

import functools
from typing import Any, Callable


def log(filename: str | None = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования вызовов функций.

    Логирует имя функции и результат при успехе, либо имя функции,
    тип ошибки и входные параметры при ошибке.

    Args:
        filename: Имя файла для записи логов. Если None — вывод в консоль.

    Returns:
        Декоратор, оборачивающий функцию.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                _write_log(log_message, filename)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                _write_log(error_message, filename)
                raise

        return wrapper

    return decorator


def _write_log(message: str, filename: str | None) -> None:
    """Вспомогательная функция для записи сообщения в файл или консоль."""
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)
