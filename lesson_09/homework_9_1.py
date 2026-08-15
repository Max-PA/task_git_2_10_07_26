# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
#
#     сторона_а (довжина сторони a).
#     кут_а (кут між сторонами a і b).
#     кут_б (суміжний з кутом кут_а).
#
# Необхідно реалізувати наступні вимоги:
#
#     Значення сторони сторона_а повинно бути більше 0.
#     Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
#     Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
#     Для встановлення значень атрибутів використовуйте метод __setattr__.

class Diamond:
    """
        Клас фігури "Diamond".
        Атрибути:
            side_a - довжина сторони ромба, повинна бути > 0
            angle_a - кут a, повинен бути в межах від 0 до 180 градусів, але не може дорівнювати 0 або 180.
            angle_b - кут b, автоматично обчислюється як 180 - angle_a і не може бути змінений користувачем напряму
        Логіка:
            При зміні angle_a автоматично перераховується angle_b
                angle_a = 20
                angle_b = 180 - 20 = 160
            Якщо користувач намагається змінити angle_b напряму, виникає AttributeError
    """
    def __init__(self, side_a, angle_a):
        # Прапорець показує, що зараз angle_b змінюється всередині, а не користувачем
        self.__dict__['_in_angle_a'] = False
        # Встановлюємо сторону ромба
        self.side_a = side_a
        # Встановлюємо кут A
        # При цьому автоматично розрахується angle_b
        self.angle_a = angle_a

    def __setattr__(self, key, value):
        """
        Перехоплюємо спробу встановити будь-який атрибут та перевіряємо правильність значень side_a та angle_a.
        визначаємо, що angle_b не можна було змінити напряму користувачем.
        """
        MAX_ANGLE = 180
        MIN_ANGLE = 0

        # Перевірка довжини сторони
        if key == "side_a":
            if not isinstance(value, (int, float)):
                raise TypeError ("side_a should be int or float")

            elif value <= 0:
                raise TypeError ("side_a should not be 0 or negative")

        # Перевірка кута a
        if key == "angle_a":
            if not isinstance(value, (int, float)):
                raise TypeError ("angle_a should be int or float")

            if value <= MIN_ANGLE or value >= MAX_ANGLE:
                raise ValueError("angle_a should be between 0 and 180 degrees")


            # Вмикаємо прапорець, прапорець _in_angle_a означає, що зараз angle_b буде змінений самим класом, а не юзером
            self.__dict__["_in_angle_a"] = True

            # Зберігаємо нове значення angle_a
            super().__setattr__(key, value)

            # Автоматично розраховуємо angle_b
            self.angle_b = 180 - value

            # Вимикаємо прапорець після зміни angle_b
            self.__dict__["_in_angle_a"] = False

            return

        # Перевірка кута b
        if key == "angle_b":

            if not isinstance(value, (int, float)):
                raise TypeError ("angle_b should be int or float")

            if value <= MIN_ANGLE or value >= MAX_ANGLE:
                raise ValueError("angle_a should be between 0 and 180 degrees")

            # Якщо прапорець False, юзер, сам пробує змінити angle_b напряму
            if not self.__dict__.get('_in_angle_a', False):
                raise AttributeError ("angle_b should not be configured by user")
        # Якщо всі перевірки OK - записуємо атрибут в об'єкт.
        super().__setattr__(key, value)

    def __str__(self):
        return f"Ширина сторони ромба:{self.side_a} | Кут А: {self.angle_a} | Кут Б:{self.angle_b}"

# Тестові два ромби
r1 = Diamond(120, 20)
r2 = Diamond(28, 23)
print(r1)
print(r2)

# Змінюємо angle_a. angle_b - автоматично перерахується:
# 180 - 1 = 179
# r1.angle_a = 1
# print(r1)
# print(r2)

# r1.angle_b = 50
# print(r1)
# print(r2)


# r1.side_a = "qwert"
# print(r1)
# print(r2)

# r1.side_a = -20
# print(r1)
# print(r2)

# r1.angle_b = 50
# print(r1)