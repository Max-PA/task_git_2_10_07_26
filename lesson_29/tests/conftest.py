import pytest
from lesson_29.homework_29_1 import create_tables


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    # Створюємо таблиці один раз перед запуском тестів
    create_tables()