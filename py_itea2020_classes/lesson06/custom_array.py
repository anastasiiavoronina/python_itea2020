class CustomArray:

    def __init__(self, size, type_):
        self._list = [0] * size
        self._type = type_

    def __getitem__(self, item):
        return self._list[item]

    def __setitem__(self, key, value):
        if isinstance(key, int) and type(value) == self._type:
            self._list[key] = value
        else:
            raise TypeError('TypeError')


array = CustomArray(10, int)
print(array[0])
#array[0] = '10'
#print(array[0])

for i in CustomArray(10, int):
    print(i)

#openweatherapi