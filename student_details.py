# Week 4 - Final Integration and Topper Logic
# Goal:
# Complete your student system with full logic and polish.
# Tasks:
# 1. Add a function to find the topper (highest average marks).
# 2. Add error handling using try-except (for numeric inputs).
# 3. Final menu:
# 1. Add student
# 2. Display all
# 3. Find topper
# 4. Search by roll number
# 5. Exit
# 4. Bonus (optional): Write and read student data from a file.
# Concepts:
# - max() with lambda
# - try-except
# - Program structure cleanup
# - Optional: File I/O

import json
students_by_rollno={} 


def read_data():
    try:
        with open('student_details.json', 'r') as file:
            data = json.load(file)
            return {item['rollno'] : Student.from_dict(item) for item in data}
    except FileNotFoundError:
        return []

def write_data(students):
    with open('student_details.json', 'w') as file:
        json.dump([student.to_dict() for student in students.values()], file, indent=4)

class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.rollno = roll_no
        self.marks = marks
    
    def average(self):
        avg = round(sum(self.marks.values())/len(self.marks))
        return avg
      
    def display(self):
        
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rollno}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print(f"Average: {self.average()}")
        print("-" * 30)

    def to_dict(self):
        return {
            "name": self.name,
            "rollno": self.rollno,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['rollno'], data['marks'])
       
  
def student_object_creation(rollno):
    name = input("Enter name: ")
    marks = {}
    try:
        subjects = int(input("Enter number of subjects: "))
        for _ in range(subjects):
            subject = input("Enter subject name: ")
           
            while True:
                try:
                    mark = float(input(f"Enter marks for {subject}: "))
                    break
                except Exception as msg:
                    print('Please enter valid number for marks.')

            marks[subject] = mark

        student = Student(name, rollno, marks)
        students_by_rollno[rollno] = student
        write_data(students_by_rollno)
        print("Student added successfully.\n")

    except Exception as msg:
        print("Please enter valid number for subjects.")


def add_student():
  
    roll_no = input("Enter roll number: ")
    
    if roll_no not in students_by_rollno:
        student_object_creation(roll_no)

       
    else:
        print("Student with this roll number already exists.Try with some other number..\n")
        add_student()  

def display_all():
    if not students_by_rollno:
        print("No students to display.\n")
        return
    for student in students_by_rollno.values():
        student.display()

def search_by_rollno(rollno):
    student = students_by_rollno.get(rollno)
    if student:
        student.display()
    else:
        print('Student not found')

def find_topper():
    if not students_by_rollno:
        print("No students available to find topper.\n")
        return
    topper = max(students_by_rollno.values(), key=lambda student: student.average())
    print("\nTopper Student:")
    topper.display()


def menu():
    global students_by_rollno
    students_by_rollno = read_data()
    while True:
        try:
            choice = int(input("""Enter choice:\n1. Add Student\n2. Display All\n3.Find Topper\n4. Search by Roll No\n5. Exit\n"""))
        except:
            print('Please enter only integer value for choice...')

        else:
            if choice == 1:
               add_student()

            elif choice == 2:
                print('Student Details :')
                display_all()

            elif choice == 3:
                find_topper()

            elif choice==4 :
                rollno = input('Enter rollno that you want to search :')
                search_by_rollno(rollno)  

            elif choice == 5:
                break
            
            else:
                print('Invalid choice.Please try again...')

if __name__ == '__main__':
    menu()
        
