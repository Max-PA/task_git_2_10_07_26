# 1) Опишіть клас Вагон
# 2) Вагон повинен містити список пасажирів і дозволяти додавати пасажирів
# 3) У Вагоні може бути не більше 10 пасажирів
# 4) Під час використання функції len у вагоні я хочу бачити кількість пасажирів
# 5) Кожен вагон повинен мати номер
# 6) Опишіть об’єкт «Поїзд» --- напевно мова про клас "Поїзд"
# 7) Клас повинен містити поля та метод для додавання вагонів(необхідно додати об’єкти та екземпляри класу вагонів)
# 8) В поїзді завжди є 1 вагон і це локомотив(він не приймає пасажирів)
# 9) Використовуючи len у поїзді, я хочу бачити кількість вагонів без локомотива

class Wagon:
    def __init__(self, wagon_number, role):
        # Створюємо порожній список для пасажирів
        self.list_of_passengers = []
        # Зберігаємо номер вагона
        self.wagon_number = wagon_number
        # Перевіряємо, чи дозволена така роль вагона
        allowed_role = ("wagon", "locomotive")
        # Записуємо роль тільки після успішної перевірки
        if role in allowed_role:
            self.role = role
        else:
            # Якщо роль неправильна - вагон не створюємо
            raise TypeError

    def __len__(self):
        # len(wagon) повертатиме кількість пасажирів
        return len(self.list_of_passengers)

    def add_passenger(self, new_passenger):
        # Пасажирів можна додавати тільки у звичайний вагон і тільки якщо в ньому менше 10 пасажирів
        if self.role == "wagon" and len(self.list_of_passengers) < 10:
            self.list_of_passengers.append(new_passenger)
        else:
            # Локомотив не приймає пасажирів, а звичайний вагон не може мати більше 10 пасажирів
            raise TypeError

class Train:
    def __init__(self, locomotive):
        # Створюємо список вагонів
        self.list_of_wagons = []
        # Локомотив завжди додається першим
        self.list_of_wagons.append(locomotive)
        # self.locomotive = self.list_of_wagons[0]

    def __len__(self):
        # Перший елемент списку - локомотив, тому не враховуємо його у кількості вагонів
        return len(self.list_of_wagons) - 1

    def add_wagon(self, new_wagon):
        # Додаємо новий вагон до потяга
        self.list_of_wagons.append(new_wagon)

# Пасажири першого вагона
wagon_1_passenger_1 = "Max"
wagon_1_passenger_2 = "Vita"
wagon_1_passenger_3 = "Jone"
wagon_1_passenger_4 = "Max"
wagon_1_passenger_5 = "Vita"
wagon_1_passenger_6 = "Jone"
wagon_1_passenger_7 = "Max"
wagon_1_passenger_8 = "Vita"
wagon_1_passenger_9 = "Jone"
wagon_1_passenger_10 = "Jone"

# Пасажири другого вагона
wagon_2_passenger_1 = "Yurii"
wagon_2_passenger_2 = "Anna"
wagon_2_passenger_3 = "Ihor"

# Пасажири третього вагона
wagon_3_passenger_1 = "Jake"
wagon_3_passenger_2 = "Olga"
wagon_3_passenger_3 = "Jimmy"

# Пасажири четвертого вагона
wagon_4_passenger_1 = "Miki"
wagon_4_passenger_2 = "Mike"
wagon_4_passenger_3 = "Jimmy"

# Створюємо локомотив і вагони
locomotive = Wagon(0, "locomotive")
wagon_1 = Wagon(1, "wagon")
wagon_2 = Wagon(2, "wagon")
wagon_3 = Wagon(3, "wagon")
wagon_4 = Wagon(4, "wagon")

# Створюємо потяг. Локомотив автоматично додається до списку вагонів
train = Train(locomotive)

# Додаємо пасажирські вагони до потяга
train.add_wagon(wagon_1)
train.add_wagon(wagon_2)
train.add_wagon(wagon_3)
train.add_wagon(wagon_4)

# Додаємо пасажирів до першого вагона
wagon_1.add_passenger(wagon_1_passenger_1)
wagon_1.add_passenger(wagon_1_passenger_2)
wagon_1.add_passenger(wagon_1_passenger_3)
wagon_1.add_passenger(wagon_1_passenger_4)
wagon_1.add_passenger(wagon_1_passenger_5)
wagon_1.add_passenger(wagon_1_passenger_6)
wagon_1.add_passenger(wagon_1_passenger_7)
wagon_1.add_passenger(wagon_1_passenger_8)
wagon_1.add_passenger(wagon_1_passenger_9)
wagon_1.add_passenger(wagon_1_passenger_10)

# Додаємо пасажирів до другого вагона
wagon_2.add_passenger(wagon_2_passenger_1)
wagon_2.add_passenger(wagon_2_passenger_2)
wagon_2.add_passenger(wagon_2_passenger_3)

# Додаємо пасажирів до третього вагона
wagon_3.add_passenger(wagon_3_passenger_1)
wagon_3.add_passenger(wagon_3_passenger_2)
wagon_3.add_passenger(wagon_3_passenger_3)

# Додаємо пасажирів до четвертого вагона
wagon_4.add_passenger(wagon_4_passenger_1)
wagon_4.add_passenger(wagon_4_passenger_2)
wagon_4.add_passenger(wagon_4_passenger_3)

# Перевіряємо кількість пасажирських вагонів у потязі
print(len(train))

# Перевіряємо кількість пасажирів у кожному вагоні
print(len(wagon_1))
print(len(wagon_2))
print(len(wagon_3))
print(len(wagon_4))

# Expected result
# 4
# 10
# 3
# 3
# 3