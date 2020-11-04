def myFun(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

def target_function(*args,**kwargs):
    if args:
        name = args[0]
    else:
        name = kwargs.get('name','unknown')

    print(f'Hello world, {name}')
    return f'Hello world, {name}'

myFun([1,2,56])
myFun(name='ttt')

target_function(name1='aaa')