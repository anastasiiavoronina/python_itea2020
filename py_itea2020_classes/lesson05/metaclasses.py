even_nums = [2, 4, 6, 8]

print(type(even_nums))
print(type(even_nums[0]))
print(type(type(even_nums)))
metaclass = type(type(even_nums))
print(type(metaclass))

def get_num_of_wheels(self):
    return self.NUM_OF_WHEELS

#Vehicle = type('Vehicle', (), {'NUM_OF_WHEELS': 45, 'get_num_of_wheels': get_num_of_wheels})
Vehicle = type('Vehicle', (), {'NUM_OF_WHEELS': 45, 'get_num_of_wheels': lambda self: self.NUM_OF_WHEELS})

print(Vehicle)
print(Vehicle.NUM_OF_WHEELS)
print(Vehicle())
print(Vehicle().get_num_of_wheels())

print('**********')


class DriveMixin:

    def drive(self):
        print(f'{self.model} is driving')

class CarMetaClass(type):

    def __new__(mcs, name, base, attrs):
        if not attrs.get('NUM_OF_WHEELS'):
            raise NotImplementedError('NUM_OF_WHEELS attribute is mandatory')

        if not attrs.get('f1'):
            raise NotImplementedError('f1 method is mandatory')

        base = (DriveMixin, )
        car_class = super().__new__(mcs, name, base, attrs)
        print(name, base, attrs)
        return car_class


class Car(metaclass=CarMetaClass):

    NUM_OF_WHEELS = 4

    def f1(self):
        pass

    def __init__(self, engine, model):
        self.engine = engine
        self.model = model

    def __call__(self, *args, **kwargs):
        print(f'I am {self.model}')

car = Car('V-8', 'Mercedes')
car.drive()
car()

print('----------')

import time

class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time() - start
        return result, end

@Decorator
def do_nothing(seconds):
    time.sleep(seconds)

print(do_nothing(2))