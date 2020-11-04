def a(a_):
    print('A')

    def b(b_):
        print('B')

        def c(c_):
            print('C')
            return a_, b_, c_

        return c

    return b

result = a(10)
print (result)
result2 = result(20)
print(result2)
result3 = result2(30)
print(result3)
print(a(10)(20)(30))