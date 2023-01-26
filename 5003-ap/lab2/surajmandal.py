"""
Application Name: surajmandal.py
Author/Developer: Suraj Mandal
Date: 2023-01-24

This code is a simple command-line application that allows the user to perform basic student management tasks.
The user is presented with a menu of options including adding a student, displaying all students, searching for
a student by ID, and ending the application.

The code defines several functions to handle each of these tasks.

These are helper functions:
- The menu_prompt() function displays the menu of options and prompts the user to enter their choice.
- The validate_id() function checks that the student ID entered is in the correct format (starts with "N0" and is 9 characters long, with the digits after the first character).


These functions are the main functions:
- The add_student_prompt() function prompts the user for the student's first name, last name, ID, and program name.
- The add_student() function uses the information provided by the user to create a new student and add it to the list of students.
- The display_students() function prints a list of all students in the system.
- The search_student() function searches the list of students for a student with a given ID and prints their information if found.

The code also includes a global variable, students, which stores the list of students.
The main program loop repeatedly calls the menu_prompt() function and performs the appropriate action based on the user's choice.
The program exits when the user chooses to end the application.
"""

import os

# Prompts
def menu_prompt():
    print(
        """
        1. Add a student
        2. Display all students
        3. Search  by student ID
        4. End application
        """
    )
    choice = input("Enter your choice: ")
    return choice


def add_student_prompt():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    id = input("Enter student ID: ")
    program_name = input("Enter program name: ")
    return firstname, lastname, id, program_name


# Global variables
students = []


# Helpers
def validate_id(student_id):
    if len(student_id) != 9:
        raise Exception("Invalid ID Length")
    elif student_id[0] != "N":
        raise Exception("Invalid ID, must start with N")
    elif student_id[1] != "0":
        raise Exception("Invalid ID, must start with N0")
    elif student_id[2:8].isdigit() is False:
        raise Exception("Invalid ID, must be digits after first character")
    else:
        for student in students:
            if student[0] == student_id:
                raise Exception("Student ID already exists")


# Main functions
def add_student():
    firstname, lastnmame, id, program_name = add_student_prompt()
    try:
        validate_id(id)
        students.append([id, firstname, lastnmame, program_name])
        print("Student has been added to the record")
    except Exception as exp:
        # print(exp)
        print("Not a valid student ID")
        return False


def display_students():
    if not students:
        print("No students registered")
        return
    print("%120s" % ("Suraj Mandal"))
    print("%120s" % ("N01537188\n"))
    print("-" * 120)
    print(
        "%30s%30s%30s%30s"
        % ("First Name", "Last Name", "Student ID", "Program Enrolled\n")
    )
    for student in students:
        print("%30s%30s%30s%30s" % (student[1], student[2], student[0], student[3]))


def search_student():
    if len(students) == 0:
        print("No students registered in the institution")
    student_id = input("Enter student ID: ")
    for student in students:
        if student[0] == student_id:
            print("%120s" % ("Suraj Mandal"))
            print("%120s" % ("N01537188\n"))
            print("-" * 120)
            print(
                "%30s%30s%30s%30s"
                % ("First Name", "Last Name", "Student ID", "Program Enrolled\n")
            )
            print("%30s%30s%30s%30s" % (student[1], student[2], student[0], student[3]))
            return True
    print("Student not registered in the institution")
    return False


if __name__ == "__main__":
    os.system("clear")
    while True:
        choice = menu_prompt()
        if choice.isdigit() is False:
            print("Invalid input, please enter a number")
            continue
        elif int(choice) == 1:
            add_student()
            continue
        elif int(choice) == 2:
            display_students()
            continue
        elif int(choice) == 3:
            search_student()
            continue
        elif int(choice) == 4:
            break
        else:
            print("Invalid input, please enter a number between 1 and 4")
            break
        # Exit the program gracefully
        exit()
