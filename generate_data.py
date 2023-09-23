import psycopg2
from faker import Faker
import random
import datetime
from decouple import config 


# Зчитування значень змінних оточення
DATABASE_NAME = config('DATABASE_NAME')
DATABASE_USER = config('DATABASE_USER')
DATABASE_PASSWORD = config('DATABASE_PASSWORD')
DATABASE_HOST = config('DATABASE_HOST')
DATABASE_PORT = config('DATABASE_PORT')

# Підключення до бази даних PostgreSQL
connection = psycopg2.connect(
    database=DATABASE_NAME,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT
)


# Підключення до бази даних PostgreSQL
connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="natalia_2007",
    host="localhost",
    port="5432"
)

cursor = connection.cursor()

# Створення таблиць
create_students_table = """
CREATE TABLE IF NOT EXISTS students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);
"""

create_groups_table = """
CREATE TABLE IF NOT EXISTS groups (
    group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(50)
);
"""

create_teachers_table = """
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);
"""

create_subjects_table = """
CREATE TABLE IF NOT EXISTS subjects (
    subject_id SERIAL PRIMARY KEY,
    subject_name VARCHAR(50),
    teacher_id INT REFERENCES teachers(teacher_id)
);
"""

create_grades_table = """
CREATE TABLE IF NOT EXISTS grades (
    grade_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    subject_id INT REFERENCES subjects(subject_id),
    grade DECIMAL(3, 2),
    exam_date DATE
);
"""

cursor.execute(create_students_table)
cursor.execute(create_groups_table)
cursor.execute(create_teachers_table)
cursor.execute(create_subjects_table)
cursor.execute(create_grades_table)

# Генерація випадкових даних за допомогою Faker
fake = Faker()

# Генерація студентів
for _ in range(50):
    first_name = fake.first_name()
    last_name = fake.last_name()
    insert_student = f"INSERT INTO students (first_name, last_name) VALUES ('{first_name}', '{last_name}')"
    cursor.execute(insert_student)

# Генерація груп
groups = ["Group A", "Group B", "Group C"]
for group_name in groups:
    insert_group = f"INSERT INTO groups (group_name) VALUES ('{group_name}')"
    cursor.execute(insert_group)

# Генерація викладачів
for _ in range(5):
    first_name = fake.first_name()
    last_name = fake.last_name()
    insert_teacher = f"INSERT INTO teachers (first_name, last_name) VALUES ('{first_name}', '{last_name}')"
    cursor.execute(insert_teacher)

# Генерація предметів
subject_names = ["Mathematics", "Physics", "Chemistry", "Biology", "History"]
for subject_name in subject_names:
    teacher_id = random.randint(1, 5)  # Випадковий викладач
    insert_subject = f"INSERT INTO subjects (subject_name, teacher_id) VALUES ('{subject_name}', {teacher_id})"
    cursor.execute(insert_subject)

# Генерація оцінок
for student_id in range(1, 51):
    for subject_id in range(1, 6):
        grade = round(random.uniform(2.0, 5.0), 2)
        exam_date = fake.date_between(start_date="-1y", end_date="today")
        insert_grade = f"INSERT INTO grades (student_id, subject_id, grade, exam_date) VALUES ({student_id}, {subject_id}, {grade}, '{exam_date}')"
        cursor.execute(insert_grade)

# Збереження змін у базі даних
connection.commit()

# Закриття підключення
cursor.close()
connection.close()
