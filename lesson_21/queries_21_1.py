from sqlalchemy.orm import sessionmaker
from models import Student, engine, Course, Enrollment


# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()

# Запит: студенти певного курсу
find_student_information_from_course = (
    session.query(Student)
    .join(Enrollment)
    .join(Course)
    .filter(Course.name == "IT")
    .all()
)

print(find_student_information_from_course)

for student_courses in find_student_information_from_course:
    print(
        student_courses.name,
        student_courses.id
    )

session.close()


# Запит: курси певного студента
find_courses_from_student = (
    session.query(Course)
    .join(Enrollment)
    .join(Student)
    .filter(Student.name == "John")
    .all()
)

print(find_courses_from_student)

for course in find_courses_from_student:
    print(
        course.name,
        course.id
    )

session.close()