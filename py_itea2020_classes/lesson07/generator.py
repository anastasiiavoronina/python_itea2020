import random
def random_numbers_generator(num):
    start = 0

    while start < num:
        yield random.randint(0,100)
        start += 1

# print(random_numbers_generator(10))
#
# for i in random_numbers_generator(10):
#     print(i)

iterator = iter(random_numbers_generator(4))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))

a = tuple(i for i in range(10))
print(a)
b = [i for i in range(10)]
print(b)