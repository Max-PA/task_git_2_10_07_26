# task 1 - solution
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25: # виправлено "25" -> 25
            # Enter the action to take if the result is greater than 25
            break # Використано break замість pass по досягненню значення > 25
        print(f'{number} x {multiplier} = {result}')

        # Increment the appropriate variable
        multiplier += 1 # виправлено multi -> multiplier

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
# task 2 - solution
def sum_of_numbers(number_1, number_2):
    result = number_1 + number_2
    return result
# Перевіряємо результат роботи функції
print(f'сума чисел дорівнює: {sum_of_numbers(3, 4)}')

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
# task 3 - solution
# Варіант 1
def average_of_list(numbers):
#Одразу повертаємо значення, без створення змінної
    return sum(numbers) / len(numbers)

# Перевірка на вхідному списку [1,2, 5, 6.7, -67]
test_task_3 = average_of_list([1,2, 5, 6.7, -67])
print(test_task_3) # очікуваний результат для списку [1,2, 5, 6.7, -67] дорівнює = -10.459999999999999

# Варіант 2 - з перевіркою типу вхідних даних
def average_of_list_2(numbers):

    # Перевіряємо чи вхідні дані є списком (list)
    if type(numbers) != list:
        return "Початкові дані не є списком, будь ласка, введіть список чисел"
    # Повертаємо довжину 0, якщо список, порожній, інакше відбуватиметься ділення на нуль
    elif len(numbers) == 0:
        return 0
    # Перевіряємо чи вхідні дані в списку є числа (int or float)
    for number in numbers:
        if not isinstance(number, (int, float)):
            return "У списку присутні дані з типом не int, float, будь ласка, перевірте вхідні дані"
    # Обраховуємо середнє арифметичне значення чисел у списку
    average = sum(numbers) / len(numbers)
    return average

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
# task 4 - solution
def reverse_string(string):
    return string[::-1]


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
# task 5 - solution
def list_of_words(word_list):
    # Перевіряємо чи список не порожній
    if len(word_list) == 0:
        return "В списку відсутні слова"
    # якщо список не порожній, визначаємо найдовше слово в списку за допомогою функції max()
    # та ключа len (за довжиною об'єктів в списку)
    longest = max(word_list, key=len)
    return longest

test_task_5 = list_of_words(["qweqeq", "asdada", "asdasvdff", "dada"])
print(test_task_5) # Очікуваний вивід на тестовому списку слів ["qweqeq", "asdada", "asdasvdff", "dada"] -
                # Найдовше слово у списку слів: asdasvdff

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

# task 6 - solution
# Для вирішення задачі, використовуємо метод .find() для пошуку індексу першого входження слова
def find_substring(str1, str2):

    # Варіант зі змінною
    index_str2_in_str1 = str1.find(str2)
    return index_str2_in_str1
# або варіант без змінної - одразу return
#     return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7, 8, 9, 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7
# Використовуємо ДЗ homework_6_3 для перетворення її на функцію:
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Дані в лісті можуть бути будь-якими


# task 7 - solution
def checker_list_for_string(lst1):
    """
    function is checking input list and returns new list only with variables with string type
    """
    new_list = [i for i in lst1 if type(i) == str]
    return new_list

test1 = checker_list_for_string(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])
print(test1)

# task 8
# Використовуємо ДЗ homework_6_4 для перетворення її на функцію:
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
# Вирішення ДЗ 6.4 на прикладі списку: [123, 3, 24, 3249, 08, 30, 29, 840, 2, 9, 84, 9, 8]
# Вхідний список чисел

# task 8 - solution
def sum_of_even_numbers(list_of_numbers):
    """
    Function accept list of number and returns only summ of even numbers
    :param list_of_numbers:
    :return: summ
    """
    # Варіант 2 - формуємо список парних чисел через list comprehension
    even_numbers = [number for number in list_of_numbers if number % 2 == 0]
    # Спосіб 1 - сумування використовуючи функцію sum()
    sum_of_even = sum(even_numbers)
    return sum_of_even

test1 = sum_of_even_numbers([123, 3, 24, 3249, 0, 8, 30, 29, 840, 2, 9, 84, 9, 8])
print(test1)


# task 9
# # Використовуємо ДЗ homework_3_1 and homework_3_2 для перетворення її на функцію:
# # task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних ліній
# alice_in_wonderland = (
#     '"Would you tell me, please, which way I ought to go from here?"\n'
#     '"That depends a good deal on where you want to get to," said the Cat.\n'
#     '"I don\'t much care where ——" said Alice.\n'
#     '"Then it doesn\'t matter which way you go," said the Cat.\n'
#     '"—— so long as I get somewhere," Alice added as an explanation.\n'
#     '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
#     )
# # task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# print("\nTask 02 solution:")
# for symbol in alice_in_wonderland:
#     if symbol == "'":
#         print(symbol)
def apostrophe_finder(text_example):
    """
    The function accept text_example (str) and returns all single (') symbols in the text
    :param text_example:
    :return: result
    """
    result = [symbol for symbol in text_example if symbol == "'"]
    return result

test1 = apostrophe_finder('"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(test1)
# expected result = ["'", "'", "'"]


# task 10
# # Використовуємо ДЗ homework_6_1 для перетворення її на функцію:
# # Incoming sentence from user
# sentence_to_analyze = input("Enter your sentence: ")
#
# # Display user input
# print(f'Користувач ввів речення: {sentence_to_analyze}')
#
# # London is the capital of Great Britain
#
# # Convert the string to a set and count unique characters
# unique_symbols_in_sentence = len(set(sentence_to_analyze))
# print(f'кількість унікальних символів у реченні складає: {unique_symbols_in_sentence}')
#
# # outputting True to the console if len > 10, otherwise - False
# if unique_symbols_in_sentence > 10:
#     print(True)
# else:
#     print(False)
def symbol_analyzer(sentence):
    unique_symbols_in_sentence = len(set(sentence))
    if unique_symbols_in_sentence > 10:
        return True
    else:
        return False

test4 = symbol_analyzer("London is the capital of Great Britain")
print(test4)