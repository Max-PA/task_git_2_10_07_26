# Код з ДЗ homework 11_1 для виконання тестувань в рамках ДЗ 12_1
# Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
# [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
# Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів, окрім чисел у списку.
# Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”

# homework 11_1 - solution

# На прикладі задачі з вхідним рядком: numbers = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
def sum_of_numbers_in_array(number_string):
    # Початкова сума чисел поточного рядка
    summ_of_numbers = 0
    # Розділяємо рядок по комі та обробляємо кожне значення
    for x in number_string.split(sep=","):
        try:
            # Перетворюємо строкове значення (str) на ціле число (int).
            # Саме тут може виникнути ValueError.
            number = int(x)
            # Додаємо отримане число до загальної суми
            summ_of_numbers += number
        except ValueError:
            # Якщо значення не можна перетворити на число, позначаємо результат як некоректний через ValueError
            summ_of_numbers = None

            # Припиняємо обробку рядка, при виникненні ValueError
            break
    # Повертаємо суму або None, якщо в рядку було некоректне значення (ValueError)
    return summ_of_numbers

# ==========================================

# Код з ДЗ homework 11_1 для виконання тестувань в рамках ДЗ 12_1
# Завдання 1 - # homework10_1
#
# Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи,
# Manager та Developer, які успадковуються від Employee. Клас Manager повинен мати
# додатковий атрибут department, а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
# Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути як Manager
# (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у '
# 'команді, якою керує керівник.
#
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
#
# homework10_1 - solution

# Стоврюємо базовий клас Employee - в ньому спільні атрибути для усіх працівників (name, salary)
class Employee:
    def __init__(self, name, salary):
        print("Employee.__init__")
        self.name = name
        self.salary = salary

# Створюємо клас Manager - успадковується від Employee,
# додаємо та зберігаємо додатковий атрибут department до class Manager
class Manager(Employee):
    def __init__(self, department, **kwargs):
        print("Manager.__init__")
        # інші іменовані аргументи передаємо далі
        super().__init__(**kwargs)
        self.department = department

# Створюємо клас Developer - успадковується від Employee,
# додаємо та зберігаємо додатковий атрибут programming_language до class Developer
class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        print("Developer.__init__")
        # інші іменовані аргументи передаємо далі
        super().__init__(**kwargs)
        self.programming_language = programming_language

# Створюємо клас TeamLead - успадковується від Manager та Developer та в свою чергу від Employee,
# додаємо та зберігаємо додатковий атрибут team_size до class TeamLead
class TeamLead(Manager, Developer):
    def __init__(self, team_size, **kwargs):
        print("TeamLead.__init__")
        # інші іменовані аргументи передаємо далі
        super().__init__(**kwargs)
        self.team_size = team_size
