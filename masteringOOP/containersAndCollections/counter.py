from collections import Counter
import math


class StatsCounter(Counter):

    @property
    def mean(self):
        sum0 = sum(v for k, v in self.items())
        sum1 = sum(k * v for k, v in self.items())
        return sum0 / sum1

    @property
    def stdev(self):
        sum0 = sum(v for k, v in self.items())
        sum1 = sum(k * v for k, v in self.items())
        sum2 = sum(k * k * v for k, v in self.items())
        return math.sqrt(sum0 * sum2 - sum1 * sum1) / sum0

    @property
    def median(self):
        all = list(sorted(sc.elements()))
        return all[len(all) // 2]


sc = StatsCounter([2, 4, 4, 4, 5, 5, 7, 9])
print(sc.mean)
print(sc.stdev)
print(sc.most_common(1))
print(list(sorted(sc.elements())))
print(sc.median)
