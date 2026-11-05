from uuid import uuid4

import pytest
from sqlalchemy import text

from lesson_29.database import engine
from lesson_29.homework_29_1 import create_user, get_users, update_user, delete_user


@pytest.fixture
def test_user():
    # SETUP: створюємо користувача з унікальним email
    unique_email = f"test_{uuid4().hex}@example.test"
    created_user = create_user("Test User", unique_email)

    yield created_user

    # Видаляємо тестового користувача після тесту
    delete_user(user_id=created_user.id)


def test_db_connection():
    # Перевіряємо підключення до PostgreSQL через простий SQL-запит
    with engine.connect() as connection:
        result = connection.scalar(text("SELECT 1"))

    assert result == 1


def test_create_user(test_user):
    # Перевіряємо, що користувача створено та отримано його ID
    assert test_user is not None
    assert test_user.id is not None
    assert test_user.name == "Test User"
    assert test_user.email is not None


def test_get_users(test_user):
    # Перевіряємо, що створений користувач є у списку отриманих записів
    user_list = get_users()
    assert any(user.email == test_user.email for user in user_list)


def test_update_user(test_user):
    updated_email = f"updated_{test_user.email}"
    updated_user = update_user(
        user_id=test_user.id,
        name="Max Name Update",
        email=updated_email
    )

    # Перевіряємо, що дані користувача успішно оновлено
    assert updated_user is not None
    assert updated_user.id == test_user.id
    assert updated_user.name == "Max Name Update"
    assert updated_user.email == updated_email


def test_delete_user(test_user):
    deleted_user = delete_user(user_id=test_user.id)

    # Перевіряємо успішне видалення користувача
    assert deleted_user is True

    # Переконуємося, що видаленого користувача більше немає в БД
    user_list = get_users()
    assert not any(user.email == test_user.email for user in user_list)