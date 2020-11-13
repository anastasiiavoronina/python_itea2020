class MyCustomList:

    def __init__(self, *args):
        self._counter = 0
        self._my_container = []
        for i in args:
            self._my_container.append(i)

    def __iter__(self):
        self._counter = 0
        return self

    def __next__(self):
        if self._counter < len(self._my_container):
            value = self._my_container[self._counter]
            self._counter += 1
            return value
        raise StopIteration

    def append(self, elem):
        self._my_container.append((elem))

    def insert(self, position, elem):
        self._my_container.insert(position, elem)

    def remove(self, elem):
        self._my_container.remove(elem)

    def clear(self):
        self._my_container.clear()

    def pop(self, position=-1):
        return self._my_container.pop(position)

    def __add__(self, other):
        return MyCustomList(*(self._my_container + other._my_container))

    def __str__(self):
        return str(self._my_container)

my_list = MyCustomList(2,6,8,9)
print(my_list)
item = my_list.pop()
print(f'pop item {item}')
print(my_list)
item = 89
my_list.append(item)
print(f'append item {item}')
print(my_list)
item = 8
my_list.remove(item)
print(f'remove item {item}')
print(my_list)
item = 58
my_list.insert(2,item)
print(f'insert item {item}')
print(my_list)
print('***Printing elements in a loop***')
for e in my_list:
    print(e)
print('******')
my_list2 = MyCustomList(45, 13, 5, 45)
print('List 2')
print(my_list2)
my_list3 = my_list + my_list2
print('New list:')
print(my_list3)