from typing import Tuple, List, Union


def is_upper(string: str):
    return string.isupper()


print(is_upper('str'))
print(is_upper('STR'))
print(is_upper(1))

def calculate_cart(cart_tuple: Tuple[str, int, str, int]):
    """(Banana', 35, 'Tomato', 45)"""
    pass

calculate_cart((35, 'Banana', 45, 'Tomato'))
calculate_cart(('Banana', 35, 'Tomato', 45))
calculate_cart(('Banana', 35, 'Tomato', 45, 'fdfd, 454'))

def calculate_cart2(cart_tuple: List[str, int]):
    """(Banana', 35, 'Tomato', 45)"""
    pass


calculate_cart2(['Banana', 35, 'Tomato', 45, 'fdfd', 55])

class A:

    def get(self):
        return 'A'


def work_with_a(obj: A = A()): #default value specified
    obj.get()


def test_func(arg1: Union[str, int, tuple]):
    pass


test_func(1)
test_func('dfdf')
test_func((1,2))
test_func([1,4])

def test_cart(products: Tuple[Union[str,int], float]):
    pass


test_cart((3.45, 4))
test_cart((3, 455))


def q(arg1, arg2):
    """

    :param arg1: int
    :param arg2: str
    :return: int
    """
    return arg1 + int(arg2)

