class MyCustomElement:

    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyCustomDict:

    def __init__(self):
        self._counter = 0
        self._my_container = []

    def __iter__(self):
        self._counter = 0
        return self

    def __next__(self):
        if self._counter < len(self._my_container):
            value = self._my_container[self._counter]
            self._counter += 1
            return value
        raise StopIteration

    def __getitem__(self, item):
        for i in self._my_container:
            if i.key == item:
                return i.value

    def __setitem__(self, key, value):
        key_found = False
        for i in self._my_container:
            if i.key == key:
                i.value = value
                key_found = True
        if key_found == False:
            self._my_container.append(MyCustomElement(key, value))

    def get(self, key, default=None):
        for i in self._my_container:
            if i.key == key:
                return i.value
        return default

    def items(self):
        result = []
        for i in self._my_container:
            result.append((i.key,i.value))
        return result

    def keys(self):
        result = []
        for i in self._my_container:
            result.append(i.key)
        return result

    def values(self):
        result = []
        for i in self._my_container:
            result.append(i.value)
        return result

    def __add__(self, other):
        new_custom_dict = MyCustomDict()
        for i in self._my_container:
            new_custom_dict[i.key] = i.value
        for i in other._my_container:
            new_custom_dict[i.key] = i.value
        return new_custom_dict

    def __str__(self):
        result = 'My Custom Dict: '
        for i in self._my_container:
            result += f'{i.key}/{i.value} '
        return result


d1 = MyCustomDict()
d1['a'] = 15
d1['r'] = 54
d1['l'] = 34
d1['k'] = 2
d1['a'] = 20
print(d1)
print(f'get a: '+str(d1.get('a')))
print('print items')
print(d1.items())
print('print keys')
print(d1.keys())
print('print values')
print(d1.values())
print('new dict')
d2 = MyCustomDict()
d2['a'] = 87
d2['b'] = 60
d2['q'] = 11
print(d2)
print('old + new:')
d3 = d1 + d2
print(d3)