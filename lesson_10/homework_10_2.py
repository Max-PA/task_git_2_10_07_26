# ДЗ 10.1.Ромбовидне наслідування та Геометрична задача
#
# Завдання 2 - # homework10_2
#
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи
# для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
# та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур, та у циклі
# порахуйте та виведіть в консоль площу та периметр кожної.
from abc import ABC, abstractmethod
import math

# homework10_2 - solution

# Стоворюємо абстрактний клас Figure
class Figure(ABC):

    # Обов'язковий метод для фігури для обчислення площі
    @abstractmethod
    def square(self):
        pass

    # Обов'язковий метод для фігури для обчислення периметра
    @abstractmethod
    def perimeter(self):
        pass

# Клас квадрата наслідується від абстрактного класу Figure
class Square(Figure):
    def __init__(self, side_a):
        # Зберігаємо довжину сторони як приватний атрибут
        self.__side_a = side_a

    # Метод для обчислення площі квадрата
    def square(self):
        return self.__side_a * self.__side_a

    # Метод для обчислення периметра квадрата
    def perimeter(self):
        return 4 * self.__side_a

# Клас трикутника наслідується від Figure
class Triangle(Figure):
    # Зберігаємо сторони та висоту як приватні атрибути
    def __init__(self, side_a, side_b, side_c, height):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        self.__height = height

    # Метод для обчислення площі трикутника
    def square(self):
        return  (self.__side_a * self.__height) / 2

    # Метод для обчислення периметра трикутника
    def perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c

# Клас кола наслідується від Figure
class Circle(Figure):
    def __init__(self, radius):
        # Зберігаємо радіус як приватний атрибут
        self.__radius = radius

    # Метод для обчислення площі кола
    def square(self):
        return math.pi * self.__radius ** 2

    # Метод для обчислення довжини кола
    def perimeter(self):
        return 2 * math.pi * self.__radius


# Створюємо об'єкти різних фігур
square = Square(34)
triangle = Triangle(5, 4, 5,13)
circle = Circle(3)

# Створюємо список різних фігур
shapes = [square, triangle, circle]

# Створюємо цикл який працює з різними типами фігур
# Викликаємо потрібну реалізацію square() та perimeter()
for shape in shapes:
    print(f'Площа {shape.__class__.__name__} дорівнює: {shape.square()}')
    print(f'Периметр {shape.__class__.__name__} дорівнює: {shape.perimeter()}')


