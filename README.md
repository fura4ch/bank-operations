Обработка банковских операций
Описание:
Модуль для фильтрации, сортировки, маскирования и генерации банковских операций по статусу, дате и валюте, а также для логирования вызовов функций.

Установка:
1. Клонируйте репозиторий:
git clone https://github.com/fura4ch/bank-operations.git

2. Установите зависимости:
Для работы проекта используется инструмент управления пакетами Poetry. Выполните:
poetry install

Использование:
Основные функции модуля:
1. Фильтрация операций по статусу:
from src.processing import filter_by_state
executed_operations = filter_by_state(operations_list)

2. Сортировка операций по дате:
from src.processing import sort_by_date
sorted_operations = sort_by_date(operations_list)

3. Маскирование карт и счетов:
from src.widget import mask_account_card
masked_info = mask_account_card("Visa Platinum 7000792289606361")

Пример данных:
Для тестирования можно использовать следующий формат данных:
operations = [
{'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
{'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'}
]

Генераторы
Модуль src.generators содержит функции для работы с большими объёмами данных транзакций.

filter_by_currency
Фильтрует транзакции по заданной валюте.
from src.generators import filter_by_currency
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
print(next(usd_transactions))

transaction_descriptions
Генерирует описания транзакций по очереди.
from src.generators import transaction_descriptions
descriptions = transaction_descriptions(transactions)
for _ in range(5):
print(next(descriptions))

card_number_generator
Генерирует номера банковских карт в заданном диапазоне.
from src.generators import card_number_generator
for card_number in card_number_generator(1, 5):
print(card_number)

Декораторы
Модуль src.decorators содержит декораторы для логирования.

Декоратор log
Логирует имя функции и результат (или ошибку) в файл или консоль.
from src.decorators import log

@log(filename="mylog.txt")
def my_function(x, y):
return x + y

my_function(1, 2)

Если функция выбрасывает исключение, в лог запишется:
имя_функции error: ТипОшибки. Inputs: (args), {kwargs}.
Если filename не указан, логи выводятся в консоль.

Проверка качества кода:
Проект использует следующие инструменты:

black — автоматическое форматирование

isort — сортировка импортов

flake8 — проверка стиля кода

mypy — статическая проверка типов

Тестирование
Для запуска тестов:
poetry run pytest

Для запуска тестов с проверкой покрытия и генерацией HTML-отчёта:
poetry run pytest --cov=src --cov-report=term-missing --cov-report=html

HTML-отчёт покрытия сохраняется в папку htmlcov/. Откройте htmlcov/index.html в браузере, чтобы посмотреть детали. Проект покрыт тестами на 100%.

Документация:
Полная документация по функциям доступна в docstrings модулей проекта.

Лицензия:
Этот проект лицензирован по лицензии MIT.