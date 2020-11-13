# a = [1, 4, 6, 7, 2]
#
# for i in a:
#     print(i)
#
# print('*'*10)
# iterator = iter(a)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#print(next(iterator))

import random

class MyRange():

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            value = self.start
            self.start += 1
            return value
        raise StopIteration


# obj = MyRange(0, 4)
# iterable = iter(obj)
#
# print(next(iterable))
# print(next(iterable))
# print(next(iterable))

for i in MyRange(0, 10):
    print(i)

print('*'*10)

class MyRangeIterable:

    def __init__(self, start, end):
        self.start = start
        self.end = end


    def __next__(self):
        if self.start < self.end:
            value = self.start
            self.start += 1
            return value
        raise StopIteration

class MyRangeIterator():

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRangeIterable(self.start, self.end)

for i in MyRangeIterator(0, 10):
    print(i)

print(list(MyRange(10,20)))
print('*'*20)


class RandomIter:

    def __init__(self, numbers):
        self.counter = 0
        self.numbers = numbers
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.numbers:
            value = random.randint(0, 9999)
            self.counter += 1
            return value
        raise StopIteration

for i in RandomIter(10):
    print(i)