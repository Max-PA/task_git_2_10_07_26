# Завдання 1:
#
# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і
# приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv
#
# Завдання 2:
#
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
# результат для невалідного файлу виведіть через логер на рівні еррор у файл
# json__<your_second_name>.log
#
# Завдання 3:
#
# Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і
# повернення
# значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо

# Вирішення завдання 1
from pathlib import Path
import csv
import random

# Створюємо базовий шлях до директорії з тестовими файлами
base_directory = Path("ideas_for_test")

# Створюємо шлях до директорії з CSV-файлами
csv_directory = base_directory / "work_with_csv"

# Задаємо розширення файлів, які будемо шукати
extension = ".csv"

# Знаходимо всі файли з розширенням .csv.
# Перевірка is_file() гарантує, що це саме файл, а не директорія.
files_with_csv_extension = [
    f for f in csv_directory.iterdir()
    if f.is_file() and f.suffix == extension
]

# Виводимо список знайдених CSV-файлів
print(f"Список файлів з розширенням '{extension}':")
print("-" * 80)

# Вказуємо delimiter для кожного CSV-файлу,
# оскільки різні CSV-файли можуть використовувати різні роздільники.
delimiters = {
    "rmc.csv": ";",
    "r-m-c.csv": ",",
    "random.csv": ",",
    "random-michaels.csv": ","
}

# Виводимо знайдені CSV-файли
for file in files_with_csv_extension:
    print("-" * 80)
    print("Файли з розширенням CSV:")
    print(file)


def merge_csv_without_duplicates(random_files, delimiters):
    """ Об'єднує два CSV-файли та видаляє дублікати рядків.
    :param random_files: список CSV-файлів
    :param delimiters: словник із delimiter для файлів
    :return: None, оскільки результат записується у CSV-файл
    """
    # Створюємо set, у якому будемо зберігати унікальні рядки
    # з обох CSV-файлів.
    result = set()

    # Зовнішній цикл проходить по двох випадково вибраних CSV-файлах.
    for count, file in enumerate(random_files):

        # Відкриваємо поточний CSV-файл для читання.
        with open(file, newline="") as opened_csv_file:

            # Перевіряємо, чи визначено delimiter для поточного файлу.
            if file.name in delimiters:
                row_reader_csv = csv.reader(
                    opened_csv_file,
                    delimiter=delimiters[file.name]
                )
            else:
                # Якщо delimiter для файлу не визначено,
                # неможливо коректно прочитати його структуру.
                raise ValueError(
                    f"Для файлу {file.name} не визначено delimiter"
                )

            # Для першого файлу зберігаємо заголовок,
            # щоб використати його під час створення результату.
            if count == 0:
                headers = next(row_reader_csv)
            else:
                # У другому файлі заголовок пропускаємо,
                # оскільки в результаті потрібен тільки один header.
                next(row_reader_csv)

            # Читаємо всі рядки після заголовка поточного файлу.
            data_csv = tuple(row_reader_csv)

        # Внутрішній цикл проходить по всіх рядках поточного CSV-файлу.
        for row in data_csv:
            # csv.reader повертає кожен рядок як list.
            # Перетворюємо його на tuple, оскільки list не можна
            # додати до set, а tuple можна.
            result_row = tuple(row)

            # Додаємо рядок до set.
            # Якщо такий рядок уже існує, set не створить дубліката.
            result.add(result_row)

    # Після обробки ОБОХ CSV-файлів result вже містить
    # усі унікальні рядки з них.
    # Тому тільки тепер створюємо файл з кінцевим результатом.
    with open("result_example.csv", "w", newline="") as result_read:
        writer = csv.writer(result_read)

        # Записуємо заголовок із першого CSV-файлу.
        writer.writerow(headers)

        # Записуємо всі унікальні рядки.
        writer.writerows(result)


# Перевіряємо, що в директорії є мінімум два CSV-файли.
if len(files_with_csv_extension) >= 2:

    # Випадково обираємо два різні CSV-файли
    # для порівняння та видалення дублікатів.
    random_files = random.sample(files_with_csv_extension, 2)

    print("-" * 80)
    print(
        f"Випадкові файли, що обрані для перевірки "
        f"на дублікати: {random_files}"
    )
    print("-" * 80)
else:
    raise ValueError(
                    f"Для виконання завдання необхідно мінімум 2 CSV-файли, знайдено {len(files_with_csv_extension)}."
                )

# Передаємо два вибрані файли та словник delimiters
# у функцію для обробки та створення результату.

merge_csv_without_duplicates(random_files, delimiters)