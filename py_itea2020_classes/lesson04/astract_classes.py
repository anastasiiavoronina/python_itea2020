from abc import ABC, abstractmethod


class Phone(ABC):

    def __init__(self, model, imei):
        self._model = model
        self._imei = imei

    @abstractmethod
    def call(self):
        pass


class SmartPhone(Phone):

    def __init__(self, model, imei, os_):
        #self._model = model
        #self._imei = imei
        super().__init__(model, imei)
        self._os = os_

    def call(self):
        print(f'Calling form {self._model}')

    def download_application(self):
        print('Downloading application')


SmartPhone('Iphone', '4648948594859', 'ios').call()