from models import Base, Student, Course, Enrollment, engine
from sqlalchemy.orm import sessionmaker
import random


# Створення таблиць
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# 1. Створення 5 курсів та 20 студентів

course_names = [
    'Math',
    'IT',
    'Philosophy',
    'Literature',
    'Physics'
]

courses = []

for course in course_names:
    course_obj = Course(name=course)
    courses.append(course_obj)


student_names = [
    'John',
    'Alice',
    'Bob',
    'Clark',
    'Jason',
    'Chris',
    'Rosie',
    'Bianca',
    'Gabriella',
    'Salem',
    'Olive',
    'Mauricio',
    'Adrian',
    'Richard',
    'Fletcher',
    'Hunter',
    'Lyanna',
    'Kaison',
    'Logan',
    'Langston'
]

students = []

for student_name in student_names:
    student_obj = Student(name=student_name)
    students.append(student_obj)


# Випадковий розподіл студентів по курсах

max_elements = len(courses)

students_enrollment = []

for student in students:
    random_number_of_courses = random.randint(1, max_elements)
    random_student_courses = random.sample(
        courses,
        k=random_number_of_courses
    )

    for random_course in random_student_courses:
        create_enroll = Enrollment(
            student=student,
            course=random_course
        )
        students_enrollment.append(create_enroll)


# Збереження даних у базу

session.add_all(courses + students + students_enrollment)
session.commit()
session.close()


# 2. Додавання нового студента на конкретний курс

Session = sessionmaker(bind=engine)
session = Session()

new_student = Student(name='Maksym')

session.add(new_student)

courses_from_db = session.query(Course).filter_by(name='Math').first()

student_courses = Enrollment(
    student=new_student,
    course=courses_from_db
)

session.add(student_courses)

session.commit()
session.close()