import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Завантажуємо змінні середовища з .env
load_dotenv()

# Отримуємо URL підключення та створюємо engine для PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)

# Створюємо базовий клас для ORM-моделей
Base = declarative_base()

# Фабрика сесій для взаємодії з базою даних
SessionLocal = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'

    # Описуємо колонки таблиці users
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)

    def __str__(self):
        return f'id={self.id}, name={self.name}'