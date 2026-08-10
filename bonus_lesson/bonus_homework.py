from collections import Counter
# Задача 1:
# Є 3 группи людей(sets) australia_blacklist, poker_blacklist, alcohol_blacklist.
# В кожній групі вказані імена. Вивести тих хто виграв джекпот(є одразу в 3х списках)

australia_blacklist = {"Jack", "John", "Max", "Bob", "Jake", "Elizabeth", "Jasmin", "Yurii"}
poker_blacklist = {"Jack", "John", "Shruth", "Joy", "Ross", "Monica", "Carl", "Max", "Jake"}
alcohol_blacklist = {"Ross", "Jasmin", "Yurii", "Max", "Jake"}

# Задача 1 - Рішення
# Перший варіант запису
jackpot_winner = australia_blacklist & poker_blacklist & alcohol_blacklist
# альтернативний варіант запису
# jackpot_winner = australia_blacklist.intersection(poker_blacklist).intersection(alcohol_blacklist)

print(f'The winner(-s) of the jackpot are: {jackpot_winner}')
# очікуваний результат виводу The winner(-s) of the jackpot are: {'Jake', 'Max'}


# Задача 2:
# Словник має наступні дані: {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Apartments', 'Oleh': 'Trench'}
# Використовуючи f-string вивести: "User_name is living in place_name" для кожного юзера.
# Використовувати цикл

residents = {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Apartments', 'Oleh': 'Trench'}

# Задача 2 - Рішення - використовуючи dict.items для перебору ключЖ значення
for user_name, place_name in residents.items():
    print(f'{user_name} is living in {place_name}')

# Задача 3:
# Є список ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
# Вивести ТІЛЬКИ коректні імена(тобто стрінги).
# Використовувати Continue.

name_list = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

# Задача 3 - Рішення
for word in name_list:
    # Одне з рішень - використовуючи if і та перебір на невідповідність типу str
    # if type(word) != str:

    # Або альтернативно через isinstance для перевірки відповідності типу str:
    if not isinstance(word, str):
        continue
    print(word)

# Задача 4:
# Порахувати та вивести(print) кількість букв в строці:
# Юзер щось вводить(input)
# Ваша задача надрукувати кількість кожного символу того що він ввів.
# Приклад:
# Юзер вводить: My name is Emmy Santiago.
# Ви прінтаете щось накшталт:M = 1, y = 2, n = 2, ...(або в іншому форматі, це не принципово головне, що б чітко було зрозуміло скільки разів зустрічається кожна буква)
# Тобто кожну букву та скільки разів вона зустрічається

# Задача 4 - Рішення
sentence = input(f'Введіть Ваше речення/слово:\n')
# перетворюємо input() на set
sentence_set = set(sentence)

for letter in sentence_set:
    count_of_letter = sentence.count(letter)
    print(f'{letter} = {count_of_letter}')

# Задача 5
# Ви створюєте список в якому може бути None(а може і не бути)
# Мета: надрукувати "There is no None" у випадку якщо None не зустрічається у списку
# Умови:По списку ми йдемо циклом
# Не створювати змінні(крім списку про який сказано вище)
# використати if 1 раз
# Не використовувати методи/функції/класи

test_list = [1, 3, "345", "word", (1, 2, "qwer"), None]
# Перебираємо кожне значення в списку, чи дорівнює воно None
for item in test_list:
    if item == None:
        print("There is None in the list")
        break
else:
    print("There is no None in the List")

#
#
# # Задача 6
# # Вирішити задачу 4 без словника за 2 строки:
# # 1 строка це input
# # 2 строка це рішення
#
# Варіант 1 - шляхом використання set comprehension для побічного ефекту print, формально - змінна count_of_letter
# не потрібна
sentence2 = input(f'Введіть Ваше речення/слово:\n')
count_of_letter = {print(f'{letter} = {sentence2.count(letter)}') for letter in set(sentence2)}

# Варіант 2 - через бібліотеку collections.Counter метод .items для формування пар (ключ, значення) та .join
sentence3 = input(f'Введіть Ваше речення/слово:\n')
print('\n'.join(f'{letter} = {count}' for letter, count in Counter(sentence3).items()))