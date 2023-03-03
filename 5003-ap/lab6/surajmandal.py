"""
Application Name: surajmandal.py
Author/Developer: Suraj Mandal
Date: 2023-03-01

IMPORTANT!
Create a .env file in the same directory as this file and add the following line
MYSQL_PASSWORD=<your_password_here>

.
├── Lab6.pdf
├── migrations
│   └── create_tables.py        <--- This file contains the functions to create the tables
├── requirements.txt
├── surajmandal.py              <--- This main file
└── utils
    ├── db.py                   <--- This file contains the db class
    └── text.py                 <--- This file contains the text utility functions


This program is a basic course registration system that allows users to interact with a MySQL database using Python.
The database contains three tables - student, course, and registration - that are used to store student, course, and
registration information respectively. The application makes use of basic SQL queries to retrieve and insert data in
the database. The user inputs are validated before being processed by the system to ensure that only valid data is
entered into the database.

P.s: Longest program ever
"""

from migrations.create_tables import migrate
from utils.text import ca_spaces
import utils.db

config = {
    "name": "Suraj Mandal",
    "nnumber": "N01537188",
}

# Prompts
def menu_prompt():
    print(
        """
          1. Display all students
          2. Diplay all courses
          3. Display all registrations
          4. Register student in course
          5. Search Student
          6. Add student
          7. End application
          """
    )
    inp = input("\tEnter your choice: ")
    print("\n")
    return inp


def std_id_prompt():
    return input("\tEnter student ID: ")


def reg_std_prompt():
    student_id = input("\tEnter student ID: ")
    course_id = input("\tEnter course ID: ")
    enrollment_semester = int(input("\tEnter enrollment semester: "))
    return student_id, course_id, enrollment_semester


def add_std_prompt():
    first_name = input("Enter first name: \t")
    last_name = input("Enter last name: \t")
    email = input("Enter email: \t")
    return first_name, last_name, email


# Utility fuctions


# Main functions
def display_students(instance: utils.db.db):
    data = instance.get(table="student")
    if data is None or data.__len__() == 0:
        print("\n\tStudents not enrolled in the institution")
        return
    print(
        f"""
        {"-" * 110}
        {ca_spaces(config['name'], 110)}
        {ca_spaces(config['nnumber'], 110)}
        {("-" * 110)}
        {ca_spaces("ID", 20)}{ca_spaces("First Name", 30)}{ca_spaces("Last Name", 30)}{ca_spaces("Email Address", 30)}
        """
    )
    for student in data:
        print(
            f"\t{ca_spaces(student[0], 20)}{ca_spaces(student[1], 30)}{ca_spaces(student[2], 30)}{ca_spaces(student[3], 30)}"
        )
    print("\t" + ("-" * 110))


def display_courses(instance: utils.db.db):
    data = instance.get(table="course")
    if data is None or data.__len__() == 0:
        print("\tCourses not offered at the institution")
        return
    print(
        f"""
        {"-" * 110}
        {ca_spaces(config['name'], 110)}
        {ca_spaces(config['nnumber'], 110)}
        {("-" * 110)}
        {ca_spaces("Course Code", 40)}{ca_spaces("Course Title", 40)}{ca_spaces("Course Credits", 30)}
        """
    )
    for course in data:
        print(
            f"\t{ca_spaces(course[0], 40)}{ca_spaces(course[1], 40)}{ca_spaces(course[2], 30)}"
        )
    print("\n\t" + ("-" * 110))


def display_registrations(instance: utils.db.db):
    data = instance.get(table="registration")
    if data is None or data.__len__() == 0:
        print("\tThere is no student registered in any course at the institution")
        return
    print(
        f"""
        {"-" * 110}
        {ca_spaces(config['name'], 110)}
        {ca_spaces(config['nnumber'], 110)}
        {("-" * 110)}
        {ca_spaces("First Name", 20)}{ca_spaces("Last Name", 20)}{ca_spaces("Student ID", 12)}{ca_spaces("Course Code", 20)}{ca_spaces("Course Title",20)}{ca_spaces("Semister Enrolled", 20)}
        """
    )
    for registration in data:
        print(
            f"\t{ca_spaces(registration[0], 20)}{ca_spaces(registration[1], 20)}{ca_spaces(registration[2], 12)}{ca_spaces(registration[3], 20)}{ca_spaces(registration[4], 20)}{ca_spaces(registration[5], 20)}"
        )
    print("\n\t" + ("-" * 110))


def register_student(instance: utils.db.db):
    # Registering student for a course
    student_id, course_id, enrollment_semester = reg_std_prompt()

    # Checking if student exists
    data = instance.get(table="student", where=f"student_id = {student_id}")
    if data is None or data.__len__() == 0:
        print(
            f"\tStudent with student ID {student_id} does not exist - cannot register"
        )
        return

    # Checking if course exists
    data = instance.get(table="course", where=f"course_id = {course_id}")
    if data is None or data.__len__() == 0:
        print(
            f"\tCourse with course ID {course_id} not offered at the institution - cannot register"
        )
        return

    # Checking if student is already registered
    data = instance.get(
        table="registration",
        where=f"\tstudent_id = {student_id} AND course_id = {course_id} AND enrollment_semester = {enrollment_semester}",
    )
    print("data", data)
    if data:
        print(
            f"\tStudent is already registered in course {course_id} for this semester"
        )
        return

    # Registering the student
    instance.set(
        table="registration",
        keys="student_id, course_id, enrollment_semester",
        values=f"('{student_id}', '{course_id}', '{enrollment_semester}')",
    )
    print(
        f"Student with student ID {student_id} successfully registered in course {course_id}"
    )


def add_student(instance: utils.db.db):
    # Adding student to the database
    student_id = str(input("Enter student ID: \t"))
    result = instance.get(table="student", where=f"student_id = {student_id}")
    if result:
        print("Student already exists")
        return
    else:
        print("There is no student data, add one")

    first_name, last_name, email = add_std_prompt()
    instance.set(
        table="student",
        keys="student_id, first_name, last_name, email",
        values=f"('{student_id}', '{first_name}', '{last_name}', '{email}')",
    )
    print("Student was added successfully")


def search_student(instance: utils.db.db):
    # Search student by student ID
    std_id = std_id_prompt()
    data = instance.get(table="student", where=f"id = {std_id}")
    if data is None or data.__len__() == 0:
        print(
            f"\tStudent having student ID {std_id} is not enrolled in the institution"
        )
        return
    students = ""
    for item in data:
        students += "%35s%35s%35s%35s" % (item[0], item[1], item[2], item[3]) + "\n"
    print(
        f"""
        {"-" * 110}
        {"-" * 110}
        {'%35s%35s%35s%35s' % ('Student ID', 'First Name', 'Last Name', 'Email Address')}
        {students}
        """
    )


def gracefully_exit(instance: utils.db.db):
    print("\tGracefully exiting...")
    instance.disconnect()
    exit(0)


def main():
    instance = utils.db.db()
    while True:
        choice = menu_prompt()
        if choice.isdigit() is False:
            print("\n\tInvalid input, please enter a number")
            continue
        elif int(choice) == 1:
            display_students(instance)
            continue
        elif int(choice) == 2:
            display_courses(instance)
            continue
        elif int(choice) == 3:
            display_registrations(instance)
            continue
        elif int(choice) == 4:
            register_student(instance)
            continue
        elif int(choice) == 5:
            search_student(instance)
            continue
        elif int(choice) == 6:
            add_student(instance)
            continue
        elif int(choice) == 7:
            gracefully_exit(instance)
        elif int(choice) == 444:
            # Hidden option that lets you
            # ceate the tables
            migrate(instance=instance)
        else:
            print("\tEnter a valid choice...")
            continue


if __name__ == "__main__":
    main()
