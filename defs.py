from datetime import datetime
import time

"""


1. `time_stamp()`: Эта функция возвращает текущее время в формате строки в форме `[HH:MM:SS]`. 
Она использует модуль `datetime` для получения текущего времени в формате `datetime` 
и затем форматирует его в нужный формат с помощью метода `strftime()`. 
Функция возвращает полученную строку времени.

2. `print_ts(str)`: Эта функция выводит переданную строку `str` вместе с текущим временем. 
Она вызывает функцию `time_stamp()` для получения текущего времени в формате строки 
и затем выводит его вместе с переданной строкой.

Обе функции созданы для отслеживания временных меток в процессе выполнения программы и отладки.
"""


def time_stamp():
    timestamp = time.time()
    date_time = datetime.fromtimestamp(timestamp)
    str_date_time = date_time.strftime("[%H:%M:%S]")
    return str_date_time


def print_ts(str):
    print(f"{time_stamp()} {str}")
