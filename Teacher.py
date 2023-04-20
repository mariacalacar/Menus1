from person import Person

class Teacher(Person):
    def __init__(self, last_name, first_name, middle_name, age, type, id, department, position) -> None:
        self.department = department
        self.position = position

        Person.__init__(self, last_name, first_name, middle_name, age, type, id)

    def __str__(self) -> str:
        return super().__str__()

    def getDepartment(self):
        return self.department

    def getPosition(self):
        return self.position
