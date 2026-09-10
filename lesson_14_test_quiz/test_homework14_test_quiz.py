# # 1) Розробіть функцію is_palindrome, яка приймає рядок і повертає True,
# якщо рядок є паліндромом (читається однаково зліва направо і справа наліво)
# та False в іншому випадку. Напишіть тести для перевірки роботу функції на різних вхідних текстах.

import pytest
from homework14_test_quiz import is_palindrome, average_price, bio_authentication


@pytest.mark.parametrize(
    "test_string, result",
    [
        ("замок", False),
        ("123454321", True),
        ("000000", True),
        ("asddsa", True),
        ("Qwerty", False),
        ("ASDdsa", True)
    ])
def test_is_palindrome(test_string, result):
    assert is_palindrome(test_string) == result


# 4)
# Задано словник даних про автомобілі “виробник”: потужність двигуна (в кінських силах – к.с.) і вартість легкових автомобілів. Скласти функцію, яка визначає середню вартість автомобілів, у яких потужність двигуна перевищує 100 к. с.

# {
#     "Mersedes": [120, 120000],
#     "Audi": [100, 165000],
#     "VW": [75, 88000],
#     "Toyta": [90, 88000],
#     "GodLikeLanos": [450, 88000],
#     "Nissan": [110, 50000],
#     "Tesla": [300, 150000],
# }

def test_average_price():
    cars = {
        "Mersedes": [120, 120000],
        "Audi": [100, 165000],
        "VW": [75, 88000],
        "Toyta": [90, 88000],
        "GodLikeLanos": [450, 88000],
        "Nissan": [110, 50000],
        "Tesla": [300, 150000],
    }
    assert average_price(cars) == 102000.0


def test_no_cars_in_criteria():
    cars = {
        "Mersedes": [60, 120000],
        "Audi": [40, 165000],
        "VW": [75, 88000],
        "Toyta": [90, 88000],
        "GodLikeLanos": [15, 88000],
        "Nissan": [60, 50000],
        "Tesla": [36, 150000],
    }
    assert average_price(cars) == None


def test_car_price_one_hundred_in_criteria():
    cars = {
        "Mersedes": [100, 120000],
        "Audi": [120, 165000],
        "VW": [75, 88000]
    }
    assert average_price(cars) == 165000.0


# Біометрична авторизація. Функція виконує авторизацію на підставі отриманого списка словників
# даних та словника, отриманого з іншої функції від користувача.

# Параметри користувача: id - int, name - str, second_name - str, age - int
# Якщо дані від користувача співпадають з єталонними даними - користувач отримує повний доступ.
# Якщо відрізняється одне поле - доступ read-only, якщо більше - доступ заборонено.
# Функція повертає рівень доступу: full, read-only, forbiden


@pytest.mark.parametrize(
    "user_authentication_data, result",
    [
        ({"id": 1, "name": "John", "second_name": "Doe", "age": 30}, "full"),
        ({"id": 1, "name": "John", "second_name": "Joi", "age": 30}, "read-only"),
        ({"id": 1, "name": "John", "second_name": "Joi", "age": 25}, "forbiden")
    ])


def test_bio_authentication(user_authentication_data, result):
    assert bio_authentication(user_authentication_data) == result

user_input_4 = {"id": 999, "name": "John", "second_name": "Joi", "age": 25}

def test_absent_subscriber_in_database_users():
    with pytest.raises(AttributeError, match="Користувача не знайдено"):
        bio_authentication(user_input_4)