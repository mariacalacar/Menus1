from Student import Student
from Teacher import Teacher

# Prompt the user to enter personal information
last_name = input("Enter Last Name: ")
first_name = input("Enter First Name: ")
middle_name = input("Enter Middle Name: ")
age = int(input("Enter Age: "))
user_type = input("Enter user type (student or teacher): ")

# Prompt the user for student or teacher information based on user type
if user_type == "student":
    course = input("Enter Course: ")
    section = input("Enter Section: ")
    year = int(input("Enter Year: "))

    # Prompt the user to enter the grades for each subject
    grades = []
    while True:
        grade = input("Enter Grade for History:")
        grade = input("Enter Grade for Architecture:")
        grade = input("Enter Grade for Netcom:")
        grade = input("Enter Grade for Purcom:")
        if grade == "done":
            break
        else:
            grades.append(float(grade))

    # Calculate the overall average grade
    average_grade = sum(grades) / len(grades)

    # Display the student information and overall average grade
    print("\nStudent Information")
    print("Name: {} {} {}".format(last_name, first_name, middle_name))
    print("Age: {}".format(age))
    print("Course: {} - Section {}".format(course, section))
    print("Year: {}".format(year))
    print("Overall Average Grade: {:.2f}".format(average_grade))

elif user_type == "teacher":
    department = input("Enter Department: ")
    position = input("Enter Position: ")

    # Display the teacher information
    print("\nTeacher Information")
    print("Name: {} {} {}".format(last_name, first_name, middle_name))
    print("Age: {}".format(age))
    print("Department: {}".format(department))
    print("Position: {}".format(position))

else:
    print("Invalid user type")

