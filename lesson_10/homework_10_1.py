# ДЗ 10.1.Ромбовидне наслідування та Геометрична задача
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

# Для діагнтостичних цілей
# print(Employee.__mro__)
# print(Manager.__mro__)
# print(Developer.__mro__)
# print(TeamLead.__mro__)

# Для перевірки, створюємо тестові об'єкти:
# Створюємо тестовий об'єкт teamlead (TeamLead - Manager - Developer - Employee),
# по MRO він наслідує атрибути від Manager, Developer та Employee.
teamlead = TeamLead(
    programming_language="Python",
    department="Development",
    name="John",
    salary=5000,
    team_size=10
)
# Для налагодження перевіряємо фактичні атрибути teamlead:
print(teamlead.__dict__)

# Створюємо тестовий об'єкт developer (Developer - Employee) для перевірки роботи
developer = Developer(
    programming_language="C#",
    name="Max",
    salary=10000
)
# Перевіряємо фактичні атрибути developer:
print(developer.__dict__)

# Створюємо тестовий об'єкт manager (Manager - Employee) для перевірки роботи
manager = Manager(
    department="Sales",
    name="Mike",
    salary=7000
)

# Перевіряємо фактичні атрибути manager:
print(manager.__dict__)

# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
# Test наявності атрибутів у teamlead (hasattr = True - атрибут присутній, False - атрибут відсутній)

print("-" * 80)
print("TEST")
print("-" * 80)

print("programming_language:", hasattr(teamlead, "programming_language"))
print("department:", hasattr(teamlead, "department"))
print("name:", hasattr(teamlead, "name"))
print("salary:", hasattr(teamlead, "salary"))
print("team_size:", hasattr(teamlead, "team_size"))

print("-" * 80)

# використовуємо assert для перевірки наявності атрибутів
# Перевірка атрибутів TeamLead
print("Перевірка наявності атрибутів через assert")
print("-" * 80)

# Перевірка атрибутe(-ів), які належать Developer.
assert hasattr(teamlead, "programming_language")
print("Перевірка programming_language: OK")

# Перевірка атрибутe(-ів), які належать Manager.
assert hasattr(teamlead, "department")
print("Перевірка department: OK")

# Перевірка атрибутe(-ів), які належать Employee.
assert hasattr(teamlead, "name")
print("name: OK")
assert hasattr(teamlead, "salary")
print("salary: OK")

# Перевірка атрибутe(-ів), які належать TeamLead.
assert hasattr(teamlead, "team_size")
print("team_size: OK")

print("-" * 80)
print("Перевірку пройдено успішно!")
print("-" * 80)