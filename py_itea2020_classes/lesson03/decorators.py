from functools import wraps

def decorator(number=3):
    def actual_decorator(func):

        @wraps(func)
        def wrapper(name):
            print('-'*number)
            result = func(name)
            print('-'*number)
            return result

        return wrapper

    return actual_decorator

@decorator(18)
def target_function(name):
    print(f'Hello world, {name}')
    return f'Hello world, {name}'

@decorator(38)
def target_function2(name):
    print(f'Hello world, {name}')
    return f'Hello world, {name}'

#result = decorator(target_function)()
print(target_function.__name__)
result = target_function('Nastya')
result2 = target_function2('Nastya')
print(result)
print(result2)
target_function.__wrapped__('Anastasiia')