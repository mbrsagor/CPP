class ApiClass:
    def __init__(self):
        self._value = 5

    def get(self):
        return self._value


api = ApiClass()
print(api.get())


class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # Conflicts


a = Child()
print(f'{a.get()} and {a._value} should be different')


class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts


foo = FrequencyList(['a', 'b', 'c', 'a', 'b'])
print("Length is ", len(foo))
