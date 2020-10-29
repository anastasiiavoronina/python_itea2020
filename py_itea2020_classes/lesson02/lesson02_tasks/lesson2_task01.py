class Car:

    def __init__(self, mark, model, price):
        self.mark = mark
        self.model = model
        self.price = price

    def drive(self):
        print(f'Car {self.model} is starting to move')

    def stop(self):
        print(f'Car {self.model} is stopping')

    def beep(self):
        print('Beep')

class Truck(Car):

    def beep(self):
        print('BEEP!!!!')


class PassengerCar(Car):

    def add_passenger(self):
        print('New passenger enters the car')

truck = Truck('Kia', 'ACD', '200')
passenger_car = PassengerCar('Suzuki', 'Swift', '50')

print('-'*37)
truck.drive()
truck.beep()
truck.stop()

print('-'*37)
passenger_car.drive()
passenger_car.beep()
passenger_car.add_passenger()
passenger_car.stop()