"""
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset

        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset


with open('address.txt', 'r') as f:
    it = index_file(f)
    results = itertools.islice(it, 0, 10)
    print(list(results))

"""


def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


it = read_visits('my_number.txt')
percentages = normalize(it)
# print(percentages)
print(list(it))
print(list(it))


def normalize_copy(numbers):
    numbers_copy = list(numbers)
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result


it = read_visits('my_numbers.txt')
print(percentages)


def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result


path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
