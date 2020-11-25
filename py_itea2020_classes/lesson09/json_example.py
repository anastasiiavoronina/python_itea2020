import json

products = {'Onion':{'price':12, 'in_stock':1000},
            'Tomato':{'price':10, 'in_stock':400}
           }

products_json = json.dumps(products)

print(products)
print(type(products))

print(products_json)
print(type(products_json))

products_new = json.loads(products_json)
print(products_new)
print(type(products_new))

# f = open('myjson.json', 'w')
# json.dump(products, f)
# f.close()

f = open('myjson.json', 'r')
data = json.load(f)
print(data)
f.close()

