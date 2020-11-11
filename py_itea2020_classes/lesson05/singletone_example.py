class SingleError(Exception):
    pass

class Singletone:

    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            obj = super().__new__(cls, *args, **kwargs)
            cls._instance = obj
            return obj
        else:
            #raise SingleError(f'The object of class {cls.__name__} already exists')
            return cls._instance


my_singletone1 = Singletone()
my_singletone2 = Singletone()
print(my_singletone1 is my_singletone2)