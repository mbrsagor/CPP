
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
