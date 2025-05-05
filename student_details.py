# Week 1 - Working with Lists and Dictionaries
# Goal:
# Collect and store student data using lists and dictionaries.
# Tasks:
# 1. Ask the user to input student details:
# - Name
# - Roll Number
# - Marks for 3 subjects: Math, Physics, Chemistry

# 2. Store each student in a dictionary: Example:
# {
# "name": "John",
# "roll_no": "101",
# "marks": {"Math": 90, "Physics": 85, "Chemistry": 80}
# }

# 3. Append each student dictionary to a list. 
# 4. Print all student data using a loop.
# Expected Output: Name: John
# Roll No: 101 Marks:

# Math: 90 Physics: 85 Chemistry: 80
# Concepts:
# - input()
# - dict and list
# - for loop and print formatting

###################################################################################

student_data={}

num_of_students=int(input('Enter the number of students :'))

students=[]

for _ in range(num_of_students):
    student = {}
    marks={}
    name = input('Enter your name : ')
    roll_no = input('Enter your roll_no : ')
    maths_marks = int(input('Enter your maths marks: '))
    physics_marks = int(input('Enter your physics marks: '))
    chemistry_marks = int(input('Enter your chemistry marks: '))
    
    marks['Math']=maths_marks
    marks['Physics']=physics_marks
    marks['Chemistry']=chemistry_marks

    student['name']=name
    student['roll_no']=roll_no
    student['marks']=marks
    students.append(student)
    print()


for data in students:
    
    print(f"Name: {data['name']}\nRoll No: {data['roll_no']}\nMarks: \nMaths: {data['marks']['Math']}\nPhysics: {data['marks']['Physics']}\nChemistry: {data['marks']['Chemistry']}")
    print()


