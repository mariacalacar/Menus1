from person import Person

class Student(Person):
    def __init__(self, last_name, first_name, middle_name, age, type, id, year, course, section) -> None:
        self.year = year
        self.course = course
        self.section = section

        Person.__init__(self, last_name, first_name, middle_name, age, type, id)
        # super(self).__init__(self, last_name, first_name, middle_name, age, type, id)

    def __str__(self) -> str:
        return super().__str__()

    def getYrCourseSec(self):
        return f'{self.year}/{self.course}/{self.section}'

