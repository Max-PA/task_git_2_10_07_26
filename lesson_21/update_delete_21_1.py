from sqlalchemy.orm import sessionmaker
from models import Student, engine, Course, Enrollment


# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()


# Оновлення імені студента
change_student_name = session.query(Student).filter_by(name="Maksym").first()
change_student_name.name = "Max"


# Оновлення назви курсу
change_course_name = session.query(Course).filter_by(name="Math").first()
change_course_name.name = "Mathematics"


# Видалення одного студента
delete_single_student_with_some_name = (
    session.query(Student)
    .filter_by(name="Rosie")
    .first()
)
session.delete(delete_single_student_with_some_name)

session.commit()


# Видалення всіх студентів із заданим ім'ям
delete_students_with_some_name = (
    session.query(Student)
    .filter_by(name="Rosie")
    .all()
)

for student in delete_students_with_some_name:
    session.delete(student)

session.commit()
session.close()