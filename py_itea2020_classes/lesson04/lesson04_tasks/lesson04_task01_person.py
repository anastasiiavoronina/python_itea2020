from abc import ABC, abstractmethod
from datetime import date
from dateutil.relativedelta import relativedelta

class Person(ABC):

    @abstractmethod
    def print_info(self):
        pass

    def __init__(self, surname, date_of_birth):
        self._date_of_birth = date_of_birth
        self._surname = surname

    def get_current_age(self):
        return relativedelta(date.today(), self._date_of_birth).years


class Abiturient(Person):

    def __init__(self, surname, date_of_birth, faculty):
        super().__init__(surname, date_of_birth)
        self._faculty = faculty

    def print_info(self):
        print(f'Abiturient information: Surname: {self._surname}, Date Of Birth: {self._date_of_birth}, '
              f'Faculty: {self._faculty}')

    def __str__(self):
        return f'Abiturient information: Surname: {self._surname}, Date Of Birth: {self._date_of_birth}, '\
               'Faculty: {self._faculty}'


class Student(Abiturient):

    def __init__(self, surname, date_of_birth, faculty, course):
        super().__init__(surname, date_of_birth, faculty)
        self._course = course

    def print_info(self):
        print(f'Student information: Surname: {self._surname}, Date Of Birth: {self._date_of_birth}, '
              f'Faculty: {self._faculty}, Course: {self._course}')

    def __str__(self):
        return f'Student information: Surname: {self._surname}, Date Of Birth: {self._date_of_birth}, '\
               'Faculty: {self._faculty}, Course: {self._course}'


class Teacher(Abiturient):

    def __init__(self, surname, date_of_birth, faculty, position, experience):
        super().__init__(surname, date_of_birth, faculty)
        self._position = position
        self._experience = experience

    def print_info(self):
        print(f'Teacher information: Surname: {self._surname}, Date Of Birth: {self._date_of_birth}, '
              f'Faculty: {self._faculty}, Position: {self._position}, Experience: {self._experience}')

    def __str__(self):
        return f'Teacher information: Surname: {self._surname}, Date Of Birth: {self._date_of_birth}, '\
               'Faculty: {self._faculty}, Position: {self._position}, Experience: {self._experience}'


person_list = [Teacher('Smith', date(1949, 4, 13), 'Math', 'Senior Teacher', 36),
               Student('Jackson', date(2000, 8, 4), 'History', 4),
               Abiturient('Hopkins', date(1990, 12, 4), 'History'),
               Abiturient('Simpson', date(1995, 10, 14), 'Math'),
               Student('Parkins', date(2003, 8, 4), 'Physics', 1)]

print('***People in the list:***')
for p in person_list:
    p.print_info()

print('\n***People with the age between 25 and 35:***')
for p in person_list:
    if p.get_current_age() >= 25 and p.get_current_age() <= 35:
        p.print_info()
