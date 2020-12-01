stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}
order = ['screws', 'wingnuts', 'clips']


def get_batches(count, size):
    return count // size


results = {}
for name in order:
    _count = stock.get(name, 0)
    batches = get_batches(_count, 8)

    if batches:
        results[name] = batches

print(results)

has_bug = {name: get_batches(stock.get(name, 0), 4)
           for name in order
           if get_batches(stock.get(name, 0), 8)}

print('Found: ', has_bug)

result = {name: tenth for name, count in stock.items() if (tenth := count // 10) > 0}
print(results)

half = [(last := count // 2) for count in stock.values()]
print(f'Last item of {half} is {last}')

for count in stock.values():
    pass
print(f"Last item of {list(stock.values())} is {count}")

half2 = [count // 2 for count in stock.values()]
print(half2)
print(count)


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        result.append(index + 1)
    return result


address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:15])


def index_words_iter(text):
    if text:
        yield 0

    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


it = index_words_iter(address)
print(next(it))
print(next(it))
print(next(it))

result1 = list(index_words_iter(address))
print(result1[:10])
