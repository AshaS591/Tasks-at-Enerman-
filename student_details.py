# Week 2 - Functions and Searching
# Goal:
# Structure your Week 1 code using functions. Implement search functionality.
# Tasks:
# 1. Convert code into functions:
# - add_student()
# - display_all_students()
# - search_by_roll(roll_no)
# 2. Maintain a list of student dictionaries (from Week 1).
# 3. Use a while-loop menu:
# 1. Add student
# 2. Display all students
# 3. Search by roll number
# 4. Exit
# Sample Menu:
# Enter choice:
# 1. Add Student
# 2. Display All
# 3. Search by Roll No
# 4. Exit
# Concepts:
# - Function definition and calling
# - List searching (for loop)
# - Menu systems with while loops

###################################################################################
# add-on for task2 :
# get the student details by index , and edit and update.
# store all the student details in a json file. 
# load the file contents when the program starts.

# make 2 funcitons to read and write from file 
# make display reusable
# search and update student in O(1)
# let user edit after asking
# handle wrong input exceptions 
# show index for students while displaying
# show only the edited student details

import json
students=[]

def read_data():
    with open('student_details.json') as file:
        students=json.load(file)
        return students


def write_data(students):
    with open('student_details.json','w') as file:
        json.dump(students,file,indent=4)

def add_students():
    students = read_data()
    try:
        num_of_students=int(input('Enter the number of students :'))
    except:
        print('Please enter integer data only..')
    else:
        for _ in range(num_of_students):
            student = {}
            marks={}
            name = input('Enter your name : ')
            roll_no = input('Enter your roll_no : ')
            try:
                maths_marks = int(input('Enter your maths marks: '))
                physics_marks = int(input('Enter your physics marks: '))
                chemistry_marks = int(input('Enter your chemistry marks: '))
            except:
                print('Enter valid marks...')
            else:
                marks['Math']=maths_marks
                marks['Physics']=physics_marks
                marks['Chemistry']=chemistry_marks
                student['name']=name
                student['roll_no']=roll_no
                student['marks']=marks
                students.append(student)

            print()
    write_data(students)

def print_data(data,index):
    print(f"{data['name']} your index is {index}")
    print(f"Name: {data['name']}\nRoll No: {data['roll_no']}\nMarks: \nMaths: {data['marks']['Math']}\nPhysics: {data['marks']['Physics']}\nChemistry: {data['marks']['Chemistry']}")
    print()  

def display_all_students():
    students = read_data()
    print('Student Details :')

    for data in students:
        print_data(data,students.index(data))
        

def search_by_rollno(rollno):
    students = read_data()
    for data in students: 
        if data['roll_no']==rollno:
            print_data(data,students.index(data))
            break
    else:
        print(f'Student with roll no : {rollno} not available..')
        print()

def edit_students_by(index):
    students=read_data()
    display_all_students()

    if index>=len(students) or index<0:
        print('*'*40)
        print(f'Please enter the index in the range of {0} to {len(students)}...')
        print('*'*40)
        return
        # get student dict in O(1)
    else:
        student = students[index]
      
    if input('Enter yes/no to edit name :').lower() == 'yes':
        name = input('Enter new name :')
        student['name']=name
    if input('Enter yes/no to edit rollno :').lower() == 'yes':
        roll_no = input('Enter new rollno :')
        student['roll_no']=roll_no
    if input('Enter yes/no to edit marks :').lower() == 'yes':
        try:
            maths = int(input('Enter your new maths marks: '))
            physics = int(input('Enter your new physics marks: '))
            chemistry = int(input('Enter your new chemistry marks: '))
        except Exception as msg:
            print(msg)
        else:
            student['marks']['Math']=maths
            student['marks']['Physics']=physics
            student['marks']['Chemistry']=chemistry
            print()
                
        students[index]=student
        print_data(student,students.index(student))
        write_data(students)

while True:
    try:
        choice = int(input("""Enter choice:\n1. Add Student\n2. Display All\n3. Search by Roll No\n4. Edit Student By Index\n5. Exit\n"""))
    except:
        print('Please enter only integer value for choice...')

    else:
        if choice == 1:
            add_students()
        elif choice == 2:
            display_all_students()
        elif choice == 3:
            rollno = input('Enter rollno that you want to search :')
            search_by_rollno(rollno)
        elif choice == 4:
            index = int(input('Enter the index :'))
            edit_students_by(index)
        
        elif choice ==5:
            break
        else:
            print('Invalid choice..')