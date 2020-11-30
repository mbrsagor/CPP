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
