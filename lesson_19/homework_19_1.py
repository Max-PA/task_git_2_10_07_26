# ДЗ 19.1. Тестування часу "серцебиття" (heartbeat)
from datetime import datetime
import logging


# Налаштування логування результатів перевірки heartbeat.
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

log_file = "hb_test.log"

file_handler = logging.FileHandler(
    log_file,
    encoding="utf-8"
)

console_handler = logging.StreamHandler()

# WARNING і ERROR записуються у файл та виводяться в консоль.
file_handler.setLevel(logging.WARNING)
console_handler.setLevel(logging.WARNING)

formatter = logging.Formatter(
    '%(asctime)s - %(message)s'
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def heartbeat_check_log():
    # Відбираємо з логу тільки повідомлення потрібного потоку.
    with open('hblog.txt', 'r', encoding='utf-8') as file:
        filtered_log = []

        while True:
            line = file.readline()
            if not line:
                break

            if "TSTFEED0300|7E3E|0400" in line:
                filtered_log.append(line)

        # Витягуємо Timestamp та перетворюємо його у datetime.
        time_data = []

        for line in filtered_log:
            position = line.find("Timestamp ")
            timestamp = line[position + 10:position + 18]
            realtime = datetime.strptime(timestamp, "%H:%M:%S")
            time_data.append(realtime)

        # Порівнюємо сусідні Timestamp та визначаємо heartbeat.
        for i in range(len(time_data) - 1):
            current_element = time_data[i]
            next_el = time_data[i + 1]

            heartbeat = current_element - next_el
            heartbeat_sec = heartbeat.total_seconds()

            # 32 секунди - попередження.
            if 31 < heartbeat_sec < 33:
                logger.warning(
                    f'{current_element.strftime("%H:%M:%S")} '
                    f'WARNING Heartbeat: {heartbeat_sec}'
                )

            # 33 секунди або більше - помилка.
            elif heartbeat_sec >= 33:
                logger.error(
                    f'{current_element.strftime("%H:%M:%S")} '
                    f'ERROR Heartbeat: {heartbeat_sec}'
                )

    # Повертаємо ім'я створеного лог-файлу.
    return log_file


result = heartbeat_check_log()
print(result)
