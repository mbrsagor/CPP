
"""
Avoid Striding and Slicing ina Single Expression
"""
x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

x = "Sagor"
y = x[::-1]
print(x)
print(y)

print('\n')
"""
Item 13: Prefer Catch-All Unpacking Over Slicing
"""
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
print(car_ages_descending)

"""
oldest, second_oldest = car_ages_descending
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)

oldest, *others, youngest = car_ages_descending
print(oldest, youngest, others)
"""

# first, *middle, *second_middle, last = [1, 2, 3, 4]

car_inventory = {
    'Downtown': ('Silver Shadow', 'Pinto', 'DMC'),
    'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova'),
}
# print(car_inventory)

short_list = [1, 2, 3, 4, 5]
first, second, *rest = short_list
print(first, second, rest)

it = iter(range(1, 3))
first, second = it
print(f"{first} and {second}")


def generate_csv():
    yield ('Date', 'Make', 'Year', 'Price')


all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print("CSV Header", header)
print("Row Count", len(rows))

it = generate_csv()
header, *rows = it
print('CSV Header:', header)
print('Row count: ', len(rows))

print('\n')

"""
Item 14: Sort by Complex Criteria Using the key Parameter
"""

numbers = [93, 86, 11, 68, 70]
numbers.sort()
print(numbers)


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Tool({self.name!r}, {self.weight})"


tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.35),
    Tool('chisel', 0.25),
]

print('Unsorted:', repr(tools))
tools.sort(key=lambda x: x.name)
print('\nSorted: ', tools)
tools.sort(key=lambda x: x.weight)
print('By weight:', tools)

places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('Case sensitive: ', places)
places.sort(key=lambda p: p.lower())
print('Case insensitive:', places)

power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]
power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)

power_tools.sort(key=lambda x: (x.weight, x.name), reverse=True)
print(power_tools)

print('\n')

"""
Item 15: Be Cautious When Relying on dict Insertion Ordering
"""
# Python 3.5
baby_names = {
    'cat': 'kitten',
    'dog': 'puppy',
}
print(baby_names)

print(list(baby_names.keys()))
print(list(baby_names.values()))
print(list(baby_names.items()))
print(baby_names.popitem())  # Randomly chooses an item


def my_func(**kwargs):
    for key, val in kwargs.items():
        print(f"{key} = {val}")


fun = my_func(name='Sagor', age=26)


class MyClass:
    def __init__(self):
        self.alligator = 'hatchling'
        self.elephant = 'calf'


a = MyClass()
for key, val in a.__dict__.items():
    print(f"{key} = {val}")


def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)

    for i, names in enumerate(names, 1):
        ranks[names] = i


def get_winner(ranks):
    return next(iter(ranks))


# ranks = {}
# # populate_ranks(votes, ranks)
# print(ranks)
# winner = get_winner(ranks)
# print(winner)

from collections.abc import MutableMapping


class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


sorted_ranks = SortedDict()


