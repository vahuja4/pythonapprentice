#!/usr/bin/python
from collections import namedtuple
import sys

Student = namedtuple('Information', ['name', 'age', 'marks_subject1', 'marks_subject2', 'marks_subject3'])

def read_user_information():
    name = raw_input("Enter name: ")
    age = int(raw_input("Enter age: "))
    marks_subject1 = int(raw_input("Enter marks for subject 1: "))
    marks_subject2 = int(raw_input("Enter marks for subject 2: "))
    marks_subject3 = int(raw_input("Enter marks for subject 3: "))
    return Student(name, age, marks_subject1, marks_subject2, marks_subject3)


def compute_average(marks_subject1, marks_subject2, marks_subject3):
     total = marks_subject1 + marks_subject2 + marks_subject3
     average = total / 3
     return total, average


if len(sys.argv) != 2:
    print("Error: please provide the number of students as an argument")
    sys.exit()
num_students = int(sys.argv[1])
students = []
for i in range(num_students):
    students.append(read_user_information())
    total_marks, average_marks = compute_average(students[i].marks_subject1, students[i].marks_subject2, students[i].marks_subject3)
    print("Hello",students[i].name, " age ",students[i].age)
    print("Your total marks",total_marks)
    print("Your average marks",average_marks)


