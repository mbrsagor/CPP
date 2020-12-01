def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} ({args!r}, {kwargs!r}) -> {result}")
        return result

    return wrapper


@trace
def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


fibonacci = trace(fibonacci)
fibonacci(4)
