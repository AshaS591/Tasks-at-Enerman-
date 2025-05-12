# Week 3 - Object-Oriented Programming (OOP)
# Goal:
# Refactor Week 2 using a Student class.
# Tasks:
# 1. Define a Student class with attributes:
# - name, roll_no, marks (dictionary)
# 2. Add method:
# - average(): returns average marks
# 3. Maintain a list of Student objects.
# 4. Update menu options to work with objects:
# - Add student
# - Display all students
# - Search by roll number
# Concepts:
# - __init__ constructor
# - Methods
# - List of objects
# - OOP principles
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
    except Exception as msg:
        print(msg)
    else:
        for _ in range(subjects):
            subject = input("Enter subject name: ")
            try:
                mark = float(input(f"Enter marks for {subject}: "))
            except Exception as msg:
                print(msg)
            else:
                    marks[subject] = mark
            
            student = Student(name, rollno, marks)
            
            students_by_rollno[rollno] = student
            write_data(students_by_rollno)
            print("Student added successfully.\n")


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
        print('Student not fond')
    
def menu():
    global students_by_rollno
    students_by_rollno = read_data()
    while True:
        try:
            choice = int(input("""Enter choice:\n1. Add Student\n2. Display All\n3. Search by Roll No\n4. Exit\n"""))
        except:
            print('Please enter only integer value for choice...')

        else:
            if choice == 1:
               add_student()
            elif choice == 2:
                print('Student Details :')
                display_all()
            elif choice == 3:
                rollno = input('Enter rollno that you want to search :')
                search_by_rollno(rollno)
            elif choice == 4:
                break
            else:
                print('Invalid choice..')

if __name__ == '__main__':
    menu()
        
