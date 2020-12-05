from functools import reduce
from operator import add


def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial(40)
print(fact)

li = list(map(factorial, filter(lambda n: n % 2, range(6))))
print(li)

rd = reduce(add, range(100))
print(rd)

_add = sum(range(100))
print(_add)
