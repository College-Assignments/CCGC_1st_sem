"""
Application Name: surajmandal.py
Author/Developer: Suraj Mandal
Date: 2023-02-28

IMPORTANT!
Create a .env file in the same directory as this file and add the following line
MYSQL_PASSWORD=<your_password_here>
"""

import utils.db

# Prompts
def menu_prompt():
    print(
        """
          1. Display all students
          2. Diplay all courses
          3. Display all registrations -students and courses
          4. Register student in course
          5. Search Student
          6. Add student
          7. End application
          """
    )


# Utility fuctions

# Main functions
def display_students(instance):
    pass


def display_courses(instance):
    pass


def display_registrations(instance):
    pass


def add_student(instance):
    pass


def register_student(instance):
    pass


def search_student(instance):
    pass


def gracefully_exit(instance):
    print("Gracefully exiting...")
    instance.disconnect()
    exit(0)


def main():
    instance = utils.db.db()
    while True:
        choice = menu_prompt()
        if choice.isdigit() is False:
            print("\tInvalid input, please enter a number")
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
        else:
            print("\tEnter a valid choice...")
            continue


if __name__ == "__main__":
    main()
