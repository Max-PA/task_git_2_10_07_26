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

# Вирішення завдання 2
from pathlib import Path
import json
import logging


# Створюємо logger
logger = logging.getLogger(__name__)

# Встановлюємо мінімальний рівень повідомлень,
# які logger може обробляти.
# DEBUG є найнижчим рівнем, тому logger прийматиме
# повідомлення всіх рівнів: DEBUG, INFO, WARNING, ERROR, CRITICAL.
logger.setLevel(logging.DEBUG)

# Створюємо FileHandler для запису повідомлень у log-файл.
# Вказуємо UTF-8, щоб український текст коректно записувався у файл.
file_handler = logging.FileHandler(
    'json_log_example.log',
    encoding="utf-8"
)

# Створюємо StreamHandler для виведення помилок у консоль.
console_handler = logging.StreamHandler()

# Встановлюємо рівень ERROR для обох handler'ів.
# У log-файл і консоль потраплятимуть ERROR та CRITICAL повідомлення.
file_handler.setLevel(logging.ERROR)
console_handler.setLevel(logging.ERROR)

# Створюємо спільний формат повідомлень для обох handler'ів.
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s'
)

# Встановлюємо formatter для FileHandler.
file_handler.setFormatter(formatter)

# Встановлюємо той самий formatter для StreamHandler.
console_handler.setFormatter(formatter)

# Додаємо handler'и до logger.
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# Створюємо базовий шлях до директорії з тестовими файлами.
base_directory = Path("ideas_for_test")

# Створюємо шлях до директорії, в якій знаходяться JSON-файли.
json_directory = base_directory / "work_with_json"

# Задаємо розширення файлів, які будемо шукати.
extension = ".json"

# Отримуємо список усіх JSON-файлів у вказаній директорії.
# iterdir() перебирає всі елементи директорії.
# is_file() залишає тільки файли.
# suffix перевіряє розширення файлу.
files_with_json_extension = [
    f for f in json_directory.iterdir()
    if f.is_file() and f.suffix == extension
]

# Виводимо список знайдених JSON-файлів.
print(files_with_json_extension)


def json_file_validator(files_with_json_extension):
    """
    Перевіряє валідність JSON-файлів та логуватиме помилки.

    :param files_with_json_extension: список JSON-файлів
    :return: None, оскільки результат виводиться через print та logger
    """

    # Перебираємо всі знайдені JSON-файли.
    for file in files_with_json_extension:

        try:
            # Відкриваємо поточний JSON-файл для читання.
            # encoding="utf-8" вказує кодування, у якому читаємо файл.
            with open(file, 'r', encoding="utf-8") as opened_json_file:

                # Читаємо файл та намагаємося розібрати його як JSON.
                # Якщо JSON має некоректний синтаксис,
                # буде json.JSONDecodeError.
                json.load(opened_json_file)

                # Якщо помилки не виникло, JSON-файл є валідним.
                print(f'File {opened_json_file.name} is valid')

        # Перехоплюємо помилку синтаксису JSON.
        # Наприклад, якщо у файлі пропущена кома або дужка.
        except json.JSONDecodeError as e:
            print("Помилка розбору JSON:", e)

            # Записуємо інформацію про невалідний JSON
            # у log-файл та виводимо її в консоль.
            logger.error(
                f'Помилка розбору JSON: {file}, {e}'
            )

        # Перехоплюємо ситуацію, коли файл не знайдено.
        except FileNotFoundError:
            print("Файл не знайдено")

# Запускаємо перевірку всіх знайдених JSON-файлів.
json_file_validator(files_with_json_extension)
