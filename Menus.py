
from Grade import Grade

students = []

def addStudent():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter Last name: ')
        firstName = input('Enter First name: ')
        middleName = input('Enter Middle name: ')
        type = input('Enter Type: ')
        course = input('Enter Course: ')
        year = input('Enter Year: ')
        section = input('Enter Section: ')
        print('----------------------------')
        history = input('Grade History: ')
        architecture = input('Grade Architecture: ')
        netcom = input('Grade Netcom: ')
        purcom = input('Grade Purcom: ')

        stud = Grade(history, architecture, netcom, purcom)
        stud.id = id
        stud.last_name = lastName
        stud.first_name = firstName
        stud.middle_name = middleName
        stud.type = type
        stud.course = course
        stud.year = year
        stud.section = section

        students.append(stud)

        print()
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break

    menu()

teacher = []

def addTeacher():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter Last name: ')
        firstName = input('Enter First name: ')
        middleName = input('Enter Middle name: ')
        type = input('Enter Type: ')
        department = input('Enter Department:')
        position = input('Enter Position:')

        teacher.append(teacher)

        print()
        a = input('Enter another? [y/n]: ')
        ans = a.lower()
        if (ans != 'y'):
            break

    menu()

def deleteStudent():
    i = int(input('Enter index: '))
    students.pop(i)

    menu()

def searchStudent():
    i = int(input('Enter index: '))
    print(f'{i} \t {students[i].getName()} \t | {students[i].getYrCourseSec()} \t | {students[i].getAverage()}')

    menu()

def displayStudent():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t| {s.getYrCourseSec()} \t| {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def deleteTeacher():
    i = int(input('Enter index: '))
    teacher.pop(i)

    menu()

def searchTeacher():
    i = int(input('Enter index: '))
    print(f'{i} \t {teacher[i].getName()} \t | {teacher[i].getDepartment()} \t | {teacher[i].getPosition()}')

    menu()

def displayTeacher():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for t in teacher:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def deleteAll():
    print()
    print('-------------------------------------------------------------------------------')
    print('Students:')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')
    print('Teachers:')
    i = 0
    for t in teacher:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()

def displayAll():
    print()
    print('-------------------------------------------------------------------------------')
    print('Students:')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')
    print('Teachers:')
    i = 0
    for t in teacher:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()


def menu():
    print()
    print()
    print('::Menu::')
    print('A - add student          M - display student')
    print('D - delete student       S - search student')
    print('F - add teacher          N - display teacher')
    print('G - delete teacher       C - search teacher')
    print('X - display all          Z - delete all')
    print()
    choice = input('Enter a function: ')
    if (choice == 'A'):
        addStudent()
    elif (choice == 'M'):
        displayStudent()
    elif (choice == 'D'):
        deleteStudent()
    elif (choice == 'S'):
        searchStudent()
    elif (choice == 'F'):
        addTeacher()
    elif (choice == 'N'):
        displayTeacher()
    elif (choice == 'G'):
        deleteTeacher()
    elif (choice == 'C'):
        searchTeacher()
    elif (choice == 'X'):
        displayAll()
    elif (choice == 'Z'):
        deleteAll()

    print()

menu()