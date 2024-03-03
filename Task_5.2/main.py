from functools import reduce
import re
from typing import Callable

# Створення функції - генератора чисел з тексту. 
# Функція map переводить числа в дійсні числа з об"єкту, який відфільтрований
# функцією filter за допомогою одноразової функції lambda, яка за допомогою регулярного виразу шукає числа.
# Функція yield дозволяє повертати кожне знайдене дійсне число до нового виклику функції

def generator_numbers(text: str):
    numbers = map(float, filter(lambda x: re.match(r"\d+\.{0,1}\d+.",x), text.split(" ")))
    for number in numbers:
        yield number

# Обчислення загальної суми згенерованих елементів за допомогою функції reduce
def sum_profit(text: str, func: Callable):
    return reduce(lambda x, y: x + y, func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
