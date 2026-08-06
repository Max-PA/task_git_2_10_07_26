class Student: # Оголошуємо клас Student
    def __init__(self, name, surname, age, average_score): # Ініціалізуємо атрибути класу
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def __str__(self): # Використовуємо magic method __str__ для повернення рядкового представлення об'єкта
        return f'Студент:\nІм\'я:{self.name}\nПрізвище:{self.surname}\nВік:{self.age}\nСередній бал:{self.average_score}'

    def change_average_score(self, new_average_score): # Метод змінює значення атрибута average_score
        self.average_score = new_average_score


student = Student(name="Will", surname="Smith", age=55, average_score=198)
print(student) # Перевіряємо вивід об'єкта до зміни значення average_score.

student.change_average_score(250) # Застосовуємо метод change_average_score класу Student для зміни average_score

print(student) # Перевіряємо вивід об'єкта після зміни значення average_score


