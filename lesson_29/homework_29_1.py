from lesson_29.database import Base, engine, SessionLocal, User


# Створюємо таблиці на основі описаних ORM-моделей
def create_tables():
    Base.metadata.create_all(bind=engine)


# CREATE - створення нового користувача
def create_user(name: str, email: str):
    session = SessionLocal()

    curr_user = User(name=name, email=email)
    session.add(curr_user)
    session.commit()  # Зберігаємо зміни в БД
    session.refresh(curr_user)  # Оновлюємо об'єкт даними з БД
    session.close()

    return curr_user


# READ - отримання всіх користувачів
def get_users():
    session = SessionLocal()

    users = session.query(User).all()

    session.close()

    return users


# UPDATE - оновлення даних користувача за ID
def update_user(user_id: int, name: str, email: str):
    session = SessionLocal()

    try:
        change_user_data = session.query(User).filter_by(id=user_id).first()

        if change_user_data is None:
            return None

        else:
            change_user_data.email = email
            change_user_data.name = name

            session.commit()  # Зберігаємо оновлені дані
            session.refresh(change_user_data)

        return change_user_data

    finally:
        session.close()  # Закриваємо сесію навіть у разі помилки


# DELETE - видалення користувача за ID
def delete_user(user_id: int):
    session = SessionLocal()

    try:
        delete_user_data = session.query(User).filter_by(id=user_id).first()

        if delete_user_data is None:
            return False

        session.delete(delete_user_data)
        session.commit()  # Підтверджуємо видалення в БД

        return True

    finally:
        session.close()  # Закриваємо сесію навіть у разі помилки


# Ручна демонстрація CRUD-операцій при прямому запуску модуля
if __name__ == "__main__":
    create_tables()

    # CREATE
    user = create_user('Max', 'test@test.test')
    print(user.id)
    print(user.name)
    print(user.email)

    # READ
    users = get_users()

    for user in users:
        print(user.id, user.name, user.email)

    # UPDATE
    updated_user = update_user(
        user.id,
        "Max Updated",
        "updated@test.test"
    )

    print(updated_user.id)
    print(updated_user.name)
    print(updated_user.email)

    # DELETE
    result = delete_user(user.id)
    print(result)

    # READ - перевіряємо результат видалення
    users = get_users()

    for user in users:
        print(user.id, user.name, user.email)