# i=0
# while i < 15:
#     print(i)
#     i += 1

list_of_numbers = list(range(0,100))

for i in list_of_numbers:
    print(i)

print('********')

my_dict = {
    1:2,
    5:10,
    10:20
}
for i in my_dict:
    print(i)
print('********')
for i in my_dict.values():
    print(i)
print('********')
for k,v in my_dict.items():
    if k == 5:
        continue
    print(k,v)