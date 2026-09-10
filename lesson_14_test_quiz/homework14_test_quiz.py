# # 1) Розробіть функцію is_palindrome, яка приймає рядок і повертає True,
# якщо рядок є паліндромом (читається однаково зліва направо і справа наліво)
# та False в іншому випадку. Напишіть тести для перевірки роботу функції на різних вхідних текстах.
from tabnanny import check


def is_palindrome(test_string):
    return test_string.lower() == test_string[::-1].lower()


# 4)
# Задано словник даних про автомобілі “виробник”: потужність двигуна (в кінських силах – к.с.) і вартість легкових автомобілів.
# Скласти функцію, яка визначає середню вартість автомобілів, у яких потужність двигуна перевищує 100 к. с.

cars = {
    "Mersedes": [120, 120000],
    "Audi": [100, 165000],
    "VW": [75, 88000],
    "Toyta": [90, 88000],
    "GodLikeLanos": [450, 88000],
    "Nissan": [110, 50000],
    "Tesla": [300, 150000],
}

search_criteria = 100


def average_price(cars):
    total_price = 0
    total_car = 0

    for car_info in cars.values():
        if car_info[0] > search_criteria:
            total_price = total_price + car_info[1]
            total_car = total_car + 1
    if total_car == 0:
        return None

    return total_price / total_car


# Перевірка, виводимо результат роботи функції на тестовому прикладі cars
print(average_price(cars))


# Біометрична авторизація. Функція виконує авторизацію на підставі отриманого списка словників даних та словника,
# отриманого з іншої функції від користувача.

# Параметри користувача: id - int, name - str, second_name - str, age - int
# Якщо дані від користувача співпадають з єталонними даними - користувач отримує повний доступ.
# Якщо відрізняється одне поле - доступ read-only, якщо більше - доступ заборонено.
# Функція повертає рівень доступу: full, read-only, forbiden

# варіант вхідних значень
database_users = [
    {"id": 1, "name": "John", "second_name": "Doe", "age": 30},
    {"id": 2, "name": "Jane", "second_name": "Joi", "age": 25}
]

user_input = {}

def bio_authentication(user_input):

    current_user = next((user for user in database_users if user["id"] == user_input["id"]), None)
    if current_user is None:
        raise AttributeError("Користувача не знайдено")

    differences = {
                    key: (current_user[key], user_input[key])
                   for key in current_user.keys() & user_input.keys()
                   if current_user[key] != user_input[key]
                   }
    if len(differences) == 0:

        return "full"
    elif len(differences) == 1:
        return "read-only"
    elif len(differences) >= 2:
        return "forbiden"

# варіанти user_input :

user_input = {"id": 1, "name": "John", "second_name": "Doe", "age": 30}
user_input_2 = {"id": 1, "name": "John", "second_name": "Joi", "age": 30}
user_input_3 = {"id": 1, "name": "John", "second_name": "Joi", "age": 25}
# user_input_4 = {"id": 999, "name": "John", "second_name": "Joi", "age": 25}


bio_authentication(user_input)
bio_authentication(user_input_2)
bio_authentication(user_input_3)