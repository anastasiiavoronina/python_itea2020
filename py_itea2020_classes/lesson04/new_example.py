class Person:

    def __new__(cls, *args, **kwargs):
        print('Calling new')
        person_object = super().__new__(cls)
        person_object.age = 25
        return person_object

    def __init__(self, first_name, surname):
        print('Calling init')
        self._first_name = first_name
        self._surname = surname

    # @property
    # def first_name(self):
    #     return self._first_name
    #
    # @first_name.setter
    # def first_name(self, value):
    #     print('new value is', value)
    #     self._first_name = value

    def get_first_name(self):
        return  self._first_name

    def set_first_name(self, value):
        self._first_name = value

    first_name = property(get_first_name, set_first_name)

my_person = Person('John', 'Doe')
print(my_person.first_name)
my_person.first_name = 'Trump'
print(my_person.first_name)
