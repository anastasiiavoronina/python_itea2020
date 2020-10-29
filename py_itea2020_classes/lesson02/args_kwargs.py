# def sum1_(arg1, arg2):
#     return arg1 + arg2
#
# def sum_(*args):
#     print(args)
#     result = 0
#     for i in args:
#         result += i
#     return result
#
# r = sum_(18,20)
# print(r)

# def products_sum(**kwargs):
#     print(kwargs)
#
# products_sum(tomato=10,orange=20,carrot=3,meat=2)

#data=[100,200,300,400]

#print(sum_(*data))

#a1, a2, a3, a4 = data[0], data[1], data[2], data[3]

#print(a4)

#a1, a2, a3, a4 = data

#print(a1, a4)

# def sum_(required_value, *args):
#     print(args)
#     result = 0
#     for i in (required_value, ) + args:
#         result += i
#     return result
#
# data=[]
# #result=sum_(*data)
# result=sum_(1,2)
# print(result)

def products_sum(**kwargs):
    print(kwargs)

products = {
    'tomato': 10,
    'orange': 45,
    'banana':13
}

products_sum(**products)

products_sum(tomato=10, orange=45, banana=13)
