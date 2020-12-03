# List comprehensions and generator expressions
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
