# cars = ['bmw','mercedes', 'volkswagen']
# print (cars.count('bmw'))
# cars[0] = 'audi'
# print(cars)
# cars.append('lamborghini')
# print(cars)
#
# cars.append(['porsche','renault','chevrolet'])
# print(cars)
# print(cars[4])

# products = {
#     ('banana','fruits') : 5,
#     'orange' : 9
# }
#
# print(products)
# updated_products = {'carrot': 10, 'milk':2, 'orange':10}
# products.update(updated_products)
# print(products)
#
# num_of_bananas = products[('banana','fruits')]
# num_of_oranges = products['orange']
# num_of_potato = products.get('potato')
#
# print(num_of_bananas, num_of_oranges, num_of_potato)
#
# print(products)
# #products['banana'] = 9
# products['tomato'] = 15
# print(products)

cars = {
    'mercedes' : {
        'g63' : 333,
        'e500': 999
    }
}

my_set = {1,2,3,4,5,1,2,5,6}
print(my_set)
my_set2 = {'1','2','3','4','5','1','2','5','6'}
print(my_set2)

products_set_1 = {'fish', 'meat', 'carrot'}
products_set_2 = {'chicken', 'fish', 'carrot'}
diff = products_set_1 - products_set_2
print(diff)
intersect = products_set_1 & products_set_2
print(intersect)
sum_ = products_set_1 | products_set_2
print(sum_)
print(sum([1,2]))