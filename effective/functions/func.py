def get_states(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
minimum, maximum = get_states(lengths)
print(f"Min: {minimum}, Max: {maximum}")

first, second = 1, 3
assert first == 1
assert second == 2


def my_function():
    return 1, 2


assert first == 1
assert second == 2
