# task 1 - Генератори:
#
#subtask_1_1 Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
#subtask_1_2 Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
#
# task_2 - Ітератори:
#
#subtask_2_1 Реалізуйте ітератор для зворотного виведення елементів списку.
#subtask_2_2 Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
#
# task_3 - Декоратори:
#
#subtask_3_1 Напишіть декоратор, який логує аргументи та результати викликаної функції.
#subtask_3_2 Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.


# subtask_1_1 - solution
def even_numbers_generator(N):
    a = 0
    while a <= N:
        yield a
        a += 2

even_numbers = even_numbers_generator(10)
for even_num in even_numbers:
    print(even_num)

# subtask_1_2 - solution

def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

fib = fibonacci_generator(100)
for number in fib:
    print(number)

# subtask_2_1 - solution
test_list = [10, 20, 30, 40]

class ListReverseIteration:
    def __init__(self, test_list):
        self.test_list = test_list
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if abs(self.index) <= len(self.test_list):
            val = self.test_list[self.index]
            self.index -= 1
            return val
        else:
            raise StopIteration

reverse_iter = ListReverseIteration(test_list)

for item in reverse_iter:
    print(item)

# subtask_2_2 - solution

class ListAllEvenNumber:
    def __init__(self, end_point):
        self.end_point = end_point
        self.start_point = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.start_point <= self.end_point:
            value = self.start_point
            self.start_point += 2
            return value
        else:
            raise StopIteration

N = 20

even_numbers_iter = ListAllEvenNumber(N)
for even_num in even_numbers_iter:
    print(even_num)


# subtask_3_1 - solution
#subtask_3_1 Напишіть декоратор, який логує аргументи та результати викликаної функції.

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    'decorator.log',
    encoding="utf-8"
)

# Створюємо StreamHandler для виведення повідомлень у консоль.
console_handler = logging.StreamHandler()

# Встановлюємо рівень INFO для обох handler'ів.
# У log-файл і консоль потраплятимуть повідомлення рівня INFO та вище.
file_handler.setLevel(logging.INFO)
console_handler.setLevel(logging.INFO)

# Створюємо спільний формат повідомлень для обох handler'ів.
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Додаємо handler'и до logger.
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info("Виклик функції '%s' з args=%s та kwargs=%s",
            func.__name__, args, kwargs)
        result_func = func(*args, **kwargs)
        logger.info("Result: %s",result_func)
        return result_func
    return wrapper

@log_decorator
def calculate(a, b):
    return a + b

print(calculate(5, 8))

print(calculate(a=15, b=23))

# subtask_3_2 - solution

def exception_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info("Виклик функції '%s' з args=%s та kwargs=%s",
            func.__name__, args, kwargs)
        try:
            result = func(*args, **kwargs)
            logger.info("Result: %s",result)
            return result
        except ZeroDivisionError:
            logger.error("Error: You cannot divide by zero!")
        except TypeError:
            logger.error("Error: Invalid argument type. Expected a number.")
    return wrapper

@exception_decorator
def number_divide(a, b):
    return a / b

print(number_divide(5, 0))

print(number_divide(a=15, b=23))


