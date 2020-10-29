class Phone:

    type_ = 'Mobile phone'

    def __init__(self, model, imei, phone_number):
        self.model = model
        self.imei = imei
        self.phone_number = phone_number

    def call(self, to_number):
        print(f'Calling from {self.phone_number} to {to_number}')


class Satellitephone:

    # def make_satellite_call(self):
    #     print('Making a satellite call')

    def call(self):
        print('Making a satellite call')

class Smartphone(Phone, Satellitephone):

    type_ = 'Smartphone'

    # def call(self, to_number):
    #     print(f'Ding. Calling from {self.model} {self.phone_number} to {to_number}')

    def download_application(self):
        print('Downloading application from market')


phone1 = Phone('Nokia', '5789gjdklj234', '0957830209')
phone1.call('0635114918')
print(phone1.model, phone1.imei, phone1.phone_number)
phone1.model = 'Motorola'
print(phone1.model, phone1.imei, phone1.phone_number)

print('-'*37)
phone2 = Phone('Siemens', 'kljk6jkl456', '0630569880')
phone2.call('0445681252')
print(phone2.model, phone2.imei, phone2.phone_number)

print('-'*37)
smartphone = Smartphone('Iphone', 'io5656kl345454lk', '0508796000')
#smartphone.call('0448701545')
#smartphone.call()
print(smartphone.model, smartphone.imei, smartphone.phone_number)
smartphone.download_application()

print('-'*37)
print(Phone.type_)
print(Smartphone.type_)
Smartphone.type_ = 'High-tech smartphone'
print(smartphone.type_)
#smartphone.make_satellite_call()