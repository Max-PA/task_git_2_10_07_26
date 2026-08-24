import pytest
from homework_13_1 import log_event

# Тестуємо три можливих статуси та відповідні їм рівні логування
@pytest.mark.parametrize('name, status, logging_level',
                         [
                            ('Ihor', 'success', 'INFO'),
                            ('Ihor', 'expired', 'WARNING'),
                            ('Ihor', 'failed', 'ERROR')
                         ])
def test_log_event_last_row(name, status, logging_level):
    # Викликаємо функцію з параметрами тесту
    log_event(username=name, status=status)
    # Очікуваний фрагмент останнього запису в лог-файлі
    expected_log_row = f"{logging_level} - Login event - Username: {name}, Status: {status}"
    # Читаємо останній запис із лог-файлу
    with open('login_system.log') as f:
        last_row = f.readlines()[-1]
    # Перевіряємо, чи запис містить очікуваний текст і відповідний йому рівень логування
    assert (expected_log_row in last_row), "expected_log_row does not contain expected_row"

    # Окремо перевіряємо правильність рівня логування
    assert (logging_level in last_row), "last_row does not contain correct logging_level"