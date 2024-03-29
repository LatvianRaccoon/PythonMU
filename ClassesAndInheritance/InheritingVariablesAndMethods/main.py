CURRENT_YEAR = 2023


class Person:

    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born

    def get_age(self):
        return CURRENT_YEAR - self.year_born

    def __str__(self):
        return '{} ({})'.format(self.name, self.get_age())


class Student(Person):

    def __init__(self, name, year_born):
        Person.__init__(self, name, year_born)
        self.knowledge = 0

    def study(self):
        self.knowledge += 1


alice = Student('Alice Smith', 1990)
alice.study()
alice.study()
print(alice)
print(alice.knowledge)
