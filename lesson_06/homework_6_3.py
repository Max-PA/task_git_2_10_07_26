# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Дані в лісті можуть бути будь-якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

# # Спосіб 1 - через цикл for / if
for i in lst1:
    if type(i) == str:
        lst2.append(i)
print(f'Новий список зі змінними тільки типу str: {lst2}')

# Спосіб 2 - через цикл list comprehension
new_list = [i for i in lst1 if type(i) == str]
print(f'Новий список зі змінними тільки типу str через list comprehension: {new_list}')
