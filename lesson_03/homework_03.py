# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних ліній
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
    )

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
print("\nTask 02 solution:")
for symbol in alice_in_wonderland:
    if symbol == "'":
        print(symbol)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print("\nTask 03 solution:")
print(alice_in_wonderland) # виконання task 03

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
#task 04 - solution
black_sea_square = 436402
azov_sea_square = 37800
all_sea_summary = black_sea_square + azov_sea_square

print("\nTask 04 solution:")
print(f"Загальна сумарна площа Чорного та Азовського морів складає: {all_sea_summary} км2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
#task 05 - solution
# сума усіх товарів на усіх складах
all_storages_item = 375291

# сумарна кількість товарів на 1-у та 2-у складі
sum_1_and_2_storage = 250449
# сумарна кількість товарів на 2-у та 3-у складі
sum_2_and_3_storage = 222950

# Кількість товарів у третьому складі
third_storage_item = all_storages_item - sum_1_and_2_storage

# кількість товарів у першому складі
first_storage_item = all_storages_item - sum_2_and_3_storage

# кількість товарів у другому складі.
second_storage_item = sum_2_and_3_storage - third_storage_item
# or alternatively second_storage_item = all_storages_item - third_storage_item - first_storage_item

# Кількість товарів по кожному зі складів
print("\nTask 05 solution:")
print(f"Загальна кількість товарів на першому складі, дорівнює {first_storage_item} товарів")
print(f"Загальна кількість товарів на другому складі, дорівнює {second_storage_item} товарів")
print(f"Загальна кількість товарів на третьому складі, дорівнює {third_storage_item} товарів")

# Перевіряємо чи дані сходяться
all_storages_item_check = first_storage_item + second_storage_item + third_storage_item

print(f"Загальна кількість товарів на усіх трьох складах, дорівнює {all_storages_item_check} товарів")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
#task 06 - solution
#Період кредитування
credit_period = 18
# Місячний платіж
month_pay = 1179
# Ціна комп'ютера
pc_price = credit_period * month_pay
#Вартість комп'ютера виходячи з тривалості кредитування та місячного платежу
print("\nTask 06 solution:")
print(f"Загальна вартість комп'ютера виходячи з умов та тривалості кредитування складає: {pc_price} гривень")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

#task 07 - solution

print("\nTask 07 solution:")
# Виводимо остачу від ділення по кожному виразу
print("Остача від ділення виразів:")
print("a) 8019 : 8, остача =", 8019 % 8)
print("b) 9907 : 9, остача =", 9907 % 9)
print("c) 2789 : 5, остача =", 2789 % 5)
print("d) 7248 : 6, остача =", 7248 % 6)
print("e) 7128 : 5, остача =", 7128 % 5)
print("f) 19224 : 9, остача =", 19224 % 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
#task 08 - solution
print("\nTask 08 solution:")
large_pizza_price = 274
middle_pizza_price = 218
juice_price = 35
cake_price = 350
water_price = 21

large_pizza_count = 4
middle_pizza_count = 2
juice_count = 4
cake_count = 1
water_count = 3

total_price = (
    large_pizza_price * large_pizza_count +
    middle_pizza_price * middle_pizza_count +
    juice_price * juice_count +
    cake_price * cake_count +
    water_price * water_count
)

print("Загальна вартість замовлення:", total_price, "грн")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
#task 09 - solution
print("\nTask 09 solution:")
all_photos_count = 232
photos_per_page = 8
# Рахуємо кількість сторінок необхідних для вклеювання фото

page_count = all_photos_count // photos_per_page
print(f"Кількість сторінок, що необхідно для вклеювання {all_photos_count} фотографій, дорівнює: {page_count}")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
#task 10 - solution
print("\nTask 10 solution:")

# Вхідні параметри подорожі
travel_distance = 1600
gas_per_100_kilometer = 9
tank_capacity = 48

# Обраховуємо скільки літрів бензину знадобиться для такої подорожі
fuel_needed = gas_per_100_kilometer * travel_distance / 100
gas_recharge_count = fuel_needed // tank_capacity

print(f"Потрібно бензину, для подорожі на {travel_distance} кілометри(-ів): {fuel_needed} літри(-ів)")
# Якщо автомобіль виїжджає з повним баком,
# то під час подорожі потрібно буде заправитися 2 рази.
# Якщо початковий бак не враховувати — відповідь 3.
print("Потрібно заїхати на заправку:", int(gas_recharge_count), "рази(-ів)")

