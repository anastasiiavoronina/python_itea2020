
my_list = []

for i in range(10):
    my_list.append(i)

print(my_list)

my_list = [i for i in range(10) if i > 1]

print(my_list)

my_list = [i ** 2 if i > 3 else i for i in range(10) if i > 1]

print(my_list)

#the same as above
my_list = []
for i in range(10):
    if i > 1:
        if i > 3:
            my_list.append(i ** 2)
        else:
            my_list.append(i)
print(my_list)

result = {i for i in range(10)}

print(result)

result = {i: i ** 2 for i in range(10)}

print(result)