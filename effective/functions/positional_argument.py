def log(message, values):
    if not values:
        print(message)
    else:
        value_str = ' '.join(str(x) for x in values)
        print(f"{message}: {value_str}")


log('My number are', [1, 2])
log('Hi there', [])


def log2(message, *values):
    if not values:
        print(message)
    else:
        value_str = ' '.join(str(x) for x in values)
        print(f"{message}: {value_str}")


log2('My numbers are', 1, 2)
log2('Hi there')  # Much better

favorites = [7, 33, 99]
log2('Favorite colors', *favorites)


def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)

