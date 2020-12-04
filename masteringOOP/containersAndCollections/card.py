import math


class Statslist(list):

    @property
    def mean(self):
        return sum(self) / len(self)

    @property
    def stdev(self):
        n = len(self)


class StatsList2(list):
    """Eager Stats."""

    def __init__(self, *args, **kw):
        self.sum0 = 0  # len(self)
        self.sum1 = 0  # sum(self)
        self.sum2 = 0  # sum(x**2 for x in self)
        super().__init__(*args, **kw)

        for x in self:
            self._new(x)

    def _new(self, value):
        self.sum0 += 1
        self.sum1 += value
        self.sum2 += value * value

    def _rmv(self, value):
        self.sum0 -= 1
        self.sum1 -= value
        self.sum2 -= value * value

    def insert(self, index, value):
        super().insert(index, value)
        self._new(value)

    def pop(self, index=0):
        value = super().pop(index)
        self._rmv(value)
        return value

    @property
    def mean(self):
        return self.sum1 / self.sum0

    @property
    def stdev(self):
        return math.sqrt(self.sum0 * self.sum2 - self.sum1 * self.sum1) / self.sum0


sl2 = StatsList2([2, 4, 3, 4, 5, 5, 7, 9, 10])
result = sl2.sum0, sl2.sum1, sl2.sum2
print(result)

sl2[2] = 4
print(result)
del sl2[-1]
print(result)
sl2.insert(0, -1)
print(result)
sl2.pop()
print(result)

print(sl2.mean)
print(sl2.stdev)
