def hello_world(name ):
    return f'Hello world. My name is {name}'

print(hello_world('Nastya'))

hello_world_lambda = lambda x: f'Hello world. My name is {x}'

print(hello_world_lambda('Nastya'))

print(type(hello_world))
hm = hello_world

print(hm('Nastya'))