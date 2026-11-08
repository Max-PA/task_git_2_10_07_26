from uuid import uuid4

import allure
import pytest
from allure_commons.types import LinkType
from sqlalchemy import text

from lesson_29.database import engine
from lesson_29.homework_29_1 import create_user, get_users, update_user, delete_user


@pytest.fixture
def test_user():
    # SETUP: створюємо користувача з унікальним email
    unique_email = f"test_{uuid4().hex}@example.test"
    created_user = create_user("Test User", unique_email)

    with allure.step("Додати дані створеного користувача до звіту"):
        allure.attach(
            f"ID: {created_user.id}\n"
            f"Name: {created_user.name}\n"
            f"Email: {created_user.email}",
            name="Created user",
            attachment_type=allure.attachment_type.TEXT
        )
    # Словник із логічним значенням (True/False)
    task_status = {
        "cleanup_needed": True
    }

    yield {
        "user": created_user,
        "task_status": task_status
    }

    if task_status.get("cleanup_needed"):
        # Видаляємо тестового користувача після тесту
        delete_user(user_id=created_user.id)


@allure.epic("Docker DB project")
@allure.feature("1. Тест підключення до тестової DB")
@allure.story("Перевірка доступності PostgreSQL")
@allure.title("Тестування досяжності тестової БД")
@allure.description(
    "Перевірка доступності PostgreSQL шляхом виконання SQL-запиту SELECT 1."
)
@allure.link(
    "https://www.postgresql.org/docs/current/sql-select.html",
    link_type=LinkType.LINK,
    name="PostgreSQL: SELECT Documentation"
)
def test_db_connection():
    # Перевіряємо підключення до PostgreSQL через простий SQL-запит
    with allure.step("Виконати SQL-запит для перевірки з'єднання."):
        with engine.connect() as connection:
            result = connection.scalar(text("SELECT 1"))

    with allure.step("Перевірити результат"):
        assert result == 1


@allure.epic("Docker DB project")
@allure.feature("2. Тестування параметрів створеного користувача")
@allure.story("Перевірка створення користувача")
@allure.title("Тестування створення користувача")
@allure.description(
    "Перевірка успішного створення користувача, отримання його ID "
    "та коректності збережених даних: імені й email."
)
@allure.link(
    "https://docs.sqlalchemy.org/en/20/orm/session_basics.html",
    link_type=LinkType.LINK,
    name="SQLAlchemy: Session Basics"
)
def test_create_user(test_user):
    # Перевіряємо, що користувача створено та отримано його ID
    with allure.step("Перевірити створення користувача"):
        assert test_user["user"] is not None
        assert test_user["user"].id is not None

    with allure.step("Перевірити дані користувача"):
        assert test_user["user"].name == "Test User"
        assert test_user["user"].email is not None


@allure.epic("Docker DB project")
@allure.feature("3. Отримання даних про користувача")
@allure.story("Пошук користувача у списку")
@allure.title("Тестування отримання користувача")
@allure.description(
    "Перевірка отримання списку користувачів із бази даних "
    "та наявності в ньому щойно створеного тестового користувача."
)
@allure.link(
    "https://docs.sqlalchemy.org/en/20/orm/session_basics.html",
    link_type=LinkType.LINK,
    name="SQLAlchemy: Session Basics"
)
def test_get_users(test_user):
    # Перевіряємо, що створений користувач є у списку отриманих записів
    with allure.step("Отримати список користувачів з БД"):
        user_list = get_users()

    with allure.step("Перевірити наявність створеного користувача"):
        assert any(user.email == test_user["user"].email for user in user_list)


@allure.epic("Docker DB project")
@allure.feature("4. Оновлення даних користувача у БД")
@allure.story("Зміна і перевірка даних користувача")
@allure.title("Тестування оновлення даних користувача")
@allure.link(
    "https://docs.sqlalchemy.org/en/20/orm/session_basics.html",
    link_type=LinkType.LINK,
    name="SQLAlchemy: Session Basics"
)
def test_update_user(test_user):
    """
    Перевірка оновлення імені та email існуючого користувача,
    а також відповідності отриманих даних очікуваним значенням.
    """
    updated_email = f"updated_{test_user['user'].email}"

    with allure.step("Оновити дані існуючого користувача"):
        updated_user = update_user(
            user_id=test_user["user"].id,
            name="Max Name Update",
            email=updated_email
        )

    # Перевіряємо, що дані користувача успішно оновлено
    with allure.step("Перевірити результат оновлення користувача"):
        assert updated_user is not None
        assert updated_user.id == test_user["user"].id

    with allure.step("Перевірити оновлення даних користувача"):
        assert updated_user.name == "Max Name Update"
        assert updated_user.email == updated_email


@allure.epic("Docker DB project")
@allure.feature("5. Тестування видалення створеного користувача")
@allure.story("Видалення та перевірка відсутності користувача")
@allure.title("Тестування видалення користувача")
@allure.link(
    "https://docs.sqlalchemy.org/en/20/orm/session_basics.html",
    link_type=LinkType.LINK,
    name="SQLAlchemy: Session Basics"
)
def test_delete_user(test_user):
    """
    Перевірка успішного видалення тестового користувача
    та підтвердження його відсутності у списку користувачів бази даних.
    """
    with allure.step("Видалити користувача з БД"):
        deleted_user = delete_user(user_id=test_user["user"].id)

    # Перевіряємо успішне видалення користувача
    with allure.step("Перевірити видалення користувача"):
        assert deleted_user is True

    test_user["task_status"]["cleanup_needed"] = False

    # Переконуємося, що видаленого користувача більше немає в БД
    with allure.step("Перевірити відсутність користувача у списку"):
        user_list = get_users()
        assert not any(user.email == test_user["user"].email for user in user_list)