# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record to the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# Task 1 - solution
# 1 - Add your new record to the beginning ([0] position) of the given list, using method .insert
people_records.insert(0,('Jim', 'Carry', 65, 'Actor', 'Montana'))
# Printing new changed list
print(people_records)

# Checking what is on the [0] position of the changed list [people_records]
print("На першій позициї у списку знаходиться: ",people_records[0])


# Task 2 - solution
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# Перевіряємо/друкуємо, що знаходиться на позиціїх з індексом 1 та 5
print(f'На позиції 1 до модифікації знаходиться: {people_records[1]}')
print(f'На позиції 5 до модифікації знаходиться: {people_records[5]}')

# swap of elements on indexes 1 and 5 to each other
people_records[1], people_records[5] = people_records[5], people_records[1]

# Перевіряємо/друкуємо, що знаходиться на позиціїх з індексом 1 та 5 після swap
print(f'На позиції 1 після модифікації знаходиться: {people_records[1]}')
print(f'На позиції 5 після модифікації знаходиться: {people_records[5]}')
print("Змінений список: ", people_records)

# Task 3 - solution
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

person_6 = people_records[6]
person_10 = people_records[10]
person_13 = people_records[13]

age_6 = person_6[2]
age_10 = person_10[2]
age_13 = person_13[2]

print(f'Чи вік людей у списку на позиціях з індексами 6, 10, 13 >=30: {age_6 >=30 and age_10 >=30 and age_13 >= 30}')