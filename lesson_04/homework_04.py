adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
# task 01 - solution
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n", " ")

# Перевіряємо коректність виконання завдання
index = adventures_of_tom_sawer.find("\n")
if index != -1:
    print(f"Знайдено на позиції {index}.")
else:
    print("Усі абзаци замінено на пробіли, нових абзаців не виявлено.")
# Виводимо новий текст без абзаців
print(adventures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
# task 02 - solution
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("....", " ")
# Перевіряємо коректність виконання завдання
index_2 = adventures_of_tom_sawer.find("....")
if index_2 != -1:
    print(f"Знайдено на позиції {index_2}.")
else:
    print("Усі зайві послідовності крапок (....) замінено на пробіли, нових - не виявлено.")
# Виводимо новий текст без абзаців
print(adventures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
# task 03 - solution
# оскільки ми точно не знаємо скільки пробілів потрібно видалити в тексті, розділяємо текст на слова через split(),
# та об'єднуємо їх за допомогою (' '.join) через один пробіл
adventures_of_tom_sawer = ' '.join(adventures_of_tom_sawer.split())
index_3 = adventures_of_tom_sawer.find("  ")
# Шукаємо чи залишилися, ще не одинарні пробіли
if index_3 != -1:
    print(f"Подвійний або більший пробіл починається з позиції {index_3}.")
else:
    print("Усі зайві пробіли замінено на одинарні пробіли, подвійних пробілів не виявлено.")
# Виводимо новий текст з одинарними пробілами
print(adventures_of_tom_sawer)

# task 04
""" Виведіть, скільки разів у тексті зустрічається літера "h"
"""

# task 04 - solution
# Рахуємо кількість символів "h" у тексті, та записуємо у змінну count_h
count_h = adventures_of_tom_sawer.count("h")
print(f'Сумарна кількість літер "h" у тексті: {count_h}')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
# task 05 - solution
# Отримуємо список слів у вигляді списку
word_list = adventures_of_tom_sawer.split()
# Створюємо лічильник для обрахунку
count_upper_words = 0
# перебираємо всі слова в тексті
for value in word_list:
# очищуємо слова від розділових знаків
    value = value.strip(',.";')
#  перевіряємо чи перша літера в слові велика
    if value[0].isupper():
# Збільшуємо лічильник на 1, якщо перша літера велика
        count_upper_words += 1
# Виводимо результат підрахунку
print("Кількість слів у тексті з великою першою літерою:", count_upper_words)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
# task 06 - solution
# Шукаємо першу появу слова Tom
first_occurrence = adventures_of_tom_sawer.find("Tom")
# Шукаємо другу появу слова Tom
second_occurrence = adventures_of_tom_sawer.find("Tom", first_occurrence + 1)

print("Слово 'Tom' зустрічається вдруге на позиції: ", second_occurrence)

# task 07
""" Розділіть змінну adventures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawer_sentences
"""
# Розділяємо речення по ознаці точки(.), та видаляємо останній запис, оскільки після в останньому реченні присутня (.)
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.split('.')[:-1]
# Видаляємо зайві пробіли на початку речення
for sentence in adventures_of_tom_sawer_sentences:
# Виводимо результат
    print(sentence.lstrip())

# task 08
""" Виведіть четверте речення з adventures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
# виводимо 4-е речення, видаляємо пробіл попереду речення та змінюємо регістр усіх символів на нижній
print(adventures_of_tom_sawer_sentences[3].lstrip().lower())

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
# Серед усіх sentence в adventures_of_tom_sawer_sentences шукаємо будь-яке, що починається з "By the time" та друкуємо результат перевірки
for sentence in adventures_of_tom_sawer_sentences:
    if sentence.lstrip().startswith("By the time"):
        print('В тексті присутнє речення, що починається зі слів - "By the time"')

# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawer_sentences.
"""
# Шукаємо останнє речення
last_sentence = adventures_of_tom_sawer_sentences[-1].lstrip()
# Розділяємо речення на слова у список
last_sentence_words = last_sentence.split()
# Визначаємо кількість елементів у списку та виводимо результат
print("Кількість слів останнього речення з adventures_of_tom_sawer_sentences складає:", len(last_sentence_words))