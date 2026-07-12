# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")  # в даній стрічці був зайвий відсут перед print, на що і вказувала
# помилка при виконанні коду - IndentationError: unexpected indent

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")  # аналогічна проблема - відсутній відсуп після блоку if, print знаходився поза блоком if
# відповідно  IndentationError: expected an indented block after 'if' statement on line 4

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter) # в print повинна бути вказана змінна, в нашому випадку letter

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print(f"Яблук: {apples}, бананів: {banana}!")

# task 05 == виправте назви змінних
storona_1 = 1 # заборонено починати назву змінної з цифри (1_storona = 1 - SyntaxError: invalid decimal literal)
storona_2 = 2 # заборонено використовувати знак питання для змінних, це призведе до SyntaxError: invalid syntax
storona_3 = 3 # не рекомендується використовувати кирилицю, потрібно використовувати латиницю
storona_4 = 4 # заборонено використовувати спец символи для змінних, це призведе до SyntaxError: invalid syntax

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery) # Result = 10


"""  
    # Задачі 07-10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_tree = 4
pear_tree = apple_tree + 5
plum_tree = apple_tree - 2

# Всього дерев в саду
all_trees = apple_tree + pear_tree + plum_tree
print(f"В саду було: {apple_tree} яблуні, {pear_tree} груш та {plum_tree} сливи. Всього дерев в саду: {all_trees}")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""

temp_before_lunch = 5
temp_after_lunch = temp_before_lunch - 10
temp_evening = temp_after_lunch + 4
print(f"Температура надвечір: {temp_evening} градусів Цельсія")


# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_in_theatre = 24
girls_in_theatre = boys_in_theatre // 2

boys_sick = 1
girls_absent = 2

boys_present = boys_in_theatre - boys_sick
girls_present = girls_in_theatre - girls_absent
kids_present = boys_present + girls_present

print(f"""Всього, сьогодні на театральний гурток прийшло {kids_present} дітей, \
серед них {boys_present} хлопчиків, та {girls_present} дівчаток. \
(В загальному у гуртку {boys_in_theatre} хлопчиків та {girls_in_theatre} дівчаток, але \
{boys_sick} хлопчик захворів, а {girls_absent} дівчинки не прийшли).""")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book_price = 8
second_book_price = first_book_price + 2
third_book_price = (first_book_price + second_book_price) // 2

all_book_price = first_book_price + second_book_price + third_book_price
print(f"Загальна вартість усіх книг, якщо купити по одному примірнику: {all_book_price}")