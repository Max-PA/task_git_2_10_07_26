from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
import os
from dotenv import load_dotenv

load_dotenv()

# Підключення до PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)


# Базовий клас для ORM-моделей
Base = declarative_base()


# Модель студента
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    enrollments = relationship("Enrollment", back_populates="student")

    def __str__(self):
        return f'id={self.id}, name={self.name}'


# Модель курсу
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    enrollments = relationship("Enrollment", back_populates="course")

    def __str__(self):
        return f'id={self.id}, name={self.name}'


# Модель зв'язку студента з курсом
class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    def __str__(self):
        return f'id={self.id}, student_id={self.student_id}, course_id={self.course_id}'