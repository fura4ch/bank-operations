from typing import Any, Dict, List


def filter_by_state(operations: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Фильтрует список операций по указанному статусу.

    Args:
        operations: Список словарей с банковскими операциями
        state: Статус для фильтрации (по умолчанию 'EXECUTED')

    Returns:
        Отфильтрованный список операций
    """
    if not operations:
        return []

    return [op for op in operations if op.get('state') == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Сортирует операции по дате.

    Args:
        operations: Список словарей с банковскими операциями
        reverse: Если True - сортировка по убыванию (новые сначала),
                 если False - по возрастанию

    Returns:
        Отсортированный список операций

    Raises:
        KeyError: Если в каком-либо словаре отсутствует ключ 'date'
    """
    if not operations:
        return []

    for op in operations:
        if 'date' not in op:
            raise KeyError(f"Отсутствует ключ 'date' в операции: {op}")

    return sorted(operations, key=lambda x: x['date'], reverse=reverse)
