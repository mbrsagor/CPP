def factorial(n):
    """returns n!"""
    return 1 if n <= 2 else n * factorial(n - 1)


fact = factorial(42)
print(fact)

_map = map(factorial, range(11))
print(_map)
