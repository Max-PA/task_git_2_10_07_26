# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

# Вирішення ДЗ 6.4 на прикладі списку: [123, 3, 24, 3249, 08, 30, 29, 840, 2, 9, 84, 9, 8]

# Вхідний список чисел
list_example = [123, 3, 24, 3249, 0, 8, 30, 29, 840, 2, 9, 84, 9, 8]

# Початкове значення суми парних чисел
sum_of_even_numbers = 0
sum_of_even_numbers_2 = 0

# Варіант 1 - Рішення через цикл
# Перебираємо усі числа в списку на відповідність ознаки парності
for number in list_example:
    if number % 2 == 0:
        # Накопичуємо результат пошуку парних чисел додаючи його до попередньо знайденого
        sum_of_even_numbers = sum_of_even_numbers + number # або альтернативно sum_of_pair_numbers += number
# Відображаємо суму усіх парних чисел
print(f'Сума усіх парних чисел у списку (Варіант 1): {sum_of_even_numbers}')

# Варіант 2 - формуємо список парних чисел через list comprehension
even_numbers = [number for number in list_example if number % 2 == 0]
# Спосіб 1 - сумування використовуючи функцію sum()
sum_of_even_numbers_1 = sum(even_numbers)
print(f'Сума усіх парних чисел у списку (Варіант 2, спосіб 1): {sum_of_even_numbers_1}')

# Спосіб 2 - сумування через цикл for
for number in even_numbers:
    sum_of_even_numbers_2 = sum_of_even_numbers_2 + number
print(f'Сума усіх парних чисел у списку (Варіант 2, спосіб 2): {sum_of_even_numbers_2}')