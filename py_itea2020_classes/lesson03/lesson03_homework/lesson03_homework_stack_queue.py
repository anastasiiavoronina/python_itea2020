class myStack:

    def __init__(self, *args):
        self._my_container = []
        self._my_container.extend(args)

    def put_item(self, item):
        self._my_container.append(item)

    def get_item(self):
        if len(self._my_container) == 0:
            return None
        else:
            result = self._my_container[len(self._my_container)-1]
            del self._my_container[len(self._my_container)-1]
            return result

    def __str__(self):
        return 'Stack: ' + str(self._my_container)

class myQueue:

    def __init__(self, *args):
        self._my_container = []
        self._my_container.extend(args)

    def put_item(self, item):
        self._my_container.append(item)

    def get_item(self):
        if len(self._my_container) == 0:
            return None
        else:
            result = self._my_container[0]
            del self._my_container[0]
            return result

    def __str__(self):
        return 'Queue: ' + str(self._my_container)

print('**'*10+'Stack example'+'**'*10)
stack1 = myStack(3,8,1)
stack1.put_item(2)
stack1.put_item(5)
stack1.put_item(74)
stack1.put_item(6)
print(stack1)
item = stack1.get_item()
print('get ' + str(item))
print(stack1)
item = stack1.get_item()
print('get ' + str(item))
print(stack1)
item = 5
stack1.put_item(item)
print('put ' + str(item))
print(stack1)

print('**'*10+'Queue example'+'**'*10)
queue1 = myQueue()
queue1.put_item(2)
queue1.put_item(5)
queue1.put_item(6)
print(queue1)
item = queue1.get_item()
print('get ' + str(item))
print(queue1)
item = queue1.get_item()
print('get ' + str(item))
print(queue1)
item = queue1.get_item()
print('get ' + str(item))
print(queue1)
item = queue1.get_item()
print('get ' + str(item))
print(queue1)
item = 5
queue1.put_item(item)
print('put ' + str(item))
print(queue1)
