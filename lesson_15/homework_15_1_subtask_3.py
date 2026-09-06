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

# Вирішення завдання 3
from pathlib import Path
import logging
import xml.etree.ElementTree as ET

# Створюємо logger для поточного підзавдання
logger = logging.getLogger(__name__)

# Встановлюємо мінімальний рівень повідомлень,
# які logger може обробляти.
# DEBUG є найнижчим рівнем, тому logger прийматиме
# повідомлення всіх рівнів: DEBUG, INFO, WARNING, ERROR, CRITICAL.
logger.setLevel(logging.DEBUG)


# Створюємо FileHandler для запису повідомлень у log-файл.
# Вказуємо UTF-8, щоб український текст коректно записувався у файл.
file_handler = logging.FileHandler(
    'xml_log_example.log',
    encoding="utf-8"
)

# Створюємо StreamHandler для виведення повідомлень у консоль.
console_handler = logging.StreamHandler()


# Встановлюємо рівень INFO для обох handler'ів.
# У log-файл і консоль потраплятимуть INFO, WARNING, ERROR та CRITICAL повідомлення.
file_handler.setLevel(logging.INFO)
console_handler.setLevel(logging.INFO)


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

# Створюємо шлях до директорії з XML-файлами.
xml_directory = base_directory / "work_with_xml"

# Задаємо розширення файлів, які будемо шукати.
extension = ".xml"


# Знаходимо файл groups.xml у директорії з XML-файлами.
# iterdir() перебирає всі елементи директорії.
# is_file() залишає тільки файли.
# suffix перевіряє розширення файлу.
# name перевіряє, що це саме groups.xml.
files_with_xml_extension = [
    f for f in xml_directory.iterdir()
    if f.is_file() and f.suffix == extension and f.name == "groups.xml"
]

# Завантажуємо XML-файл.
# files_with_xml_extension[0] — перший знайдений Path до groups.xml.
tree = ET.parse(files_with_xml_extension[0])

# Отримуємо кореневий елемент XML-документа — <groups>.
root = tree.getroot()


def group_finder(group_number):
    """
    Функція шукає групу за її номером та повертає значення поля incoming.

    :param group_number: номер групи, яку потрібно знайти
    :return: значення <incoming> або повідомлення про помилку
    """

    # Перебираємо всі елементи <group>,
    # які знаходяться безпосередньо всередині <groups>.
    for group in root.findall('group'):

        try:
            # Знаходимо елемент <number> поточної групи
            # та отримуємо його текстове значення.
            number = group.find('number').text

            # XML повертає текстове значення як str.
            # Перетворюємо його на int та порівнюємо
            # з номером групи, який передали у функцію.
            if int(number) == group_number:

                # У знайденій групі шукаємо елемент <timingExbytes>.
                timing_exbytes = group.find('timingExbytes')

                # Не всі групи можуть містити <timingExbytes>.
                # Якщо елемент відсутній — повертаємо повідомлення.
                if timing_exbytes is None:
                    return (
                        f'There is no field timing_exbytes '
                        f'in group_number: {group_number}'
                    )

                # Усередині <timingExbytes> шукаємо <incoming>.
                incoming = timing_exbytes.find('incoming')

                # Перевіряємо, чи існує елемент <incoming>.
                if incoming is None:
                    return 'There is no incoming'

                # Повертаємо саме текстове значення <incoming>.
                return incoming.text

        # Якщо текст у <number> неможливо перетворити на int,
        # виникає ValueError.
        except ValueError:
            return "The Number is not correct"

    # Якщо цикл завершився і групу з таким номером не знайдено,
    # повертаємо відповідне повідомлення.
    return f"Group number: {group_number} wasn't found"


# Визначаємо номер групи, яку потрібно знайти.
group_number = 2

# Викликаємо функцію та отримуємо значення <incoming>.
result = group_finder(group_number)

# Записуємо результат через logger.
# У повідомленні вказуємо і номер групи, і отримане значення incoming.
logger.info(
    f'Результат виконання group_finder '
    f'для group_number={group_number}: {result}'
)

