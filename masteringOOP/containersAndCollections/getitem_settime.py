import math


class Explore:
    def __getitem__(self, index):
        print(index, index.indices(len(self)))
        return super().__getitem__(index)


# x = Explore('abcdefg')
# a = x[:]
# print(a)


class StatsList3:
    def __init__(self):
        self._list = list()
        self.sum0 = 0  # len(self), sometimes called "N"
        self.sum1 = 0  # sum(self)
        self.sum2 = 0  # sum(x**2 for x in self)

    def append(self, value):
        self._list.append(value)
        self.sum0 += 1
        self.sum1 += value
        self.sum2 += value * value

    def __getitem__(self, index):
        return self._list.__getitem__(index)

    @property
    def mean(self):
        return self.sum1 / self.sum0

    @property
    def stdev(self):
        return math.sqrt(self.sum0 * self.sum2 - self.sum1 * self.sum1) / self.sum0


sl3 = StatsList3()
for data in 2, 4, 4, 4, 5, 5, 7, 9:
    sl3.append(data)

for x in sl3:
    print(x)
