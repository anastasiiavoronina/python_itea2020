t_1=1
t_2='2'

try:
    result=t_1+t_2
except TypeError as e:
    result = 'type error happenned: '+str(e)
    #print(e.args)
except ArithmeticError:
    result = 'arithmetic error happenned'
finally:
    print('work of try')


print(result)