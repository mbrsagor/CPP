a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

items = []

for i in a:
    if i % 2 == 0:
        items.append(i)
print(items)

for j in a:
    items.append(j ** 2)
print(items)

square = [x ** 2 for x in a]
print(square)

even_squares = [x ** 2 for x in a if x % 2 == 0]
print(even_squares)

alt = map(lambda xy: xy ** 2, filter(lambda xy: xy % 2 == 0, a))
assert even_squares == list(alt)
print(alt)

alt_dict = dict(map(lambda x: (x, x ** 2), filter(lambda x: x % 2 == 0, a)))
print(alt_dict)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

squared = [[x ** 2 for x in row] for row in matrix]
print(squared)

my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    ...
]
print(my_lists)

# flat = [x for sublist1 in my_lists for sublist2 in sublist1 for x in sublist2]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
print(b)

c = [x for x in a if x > 4 and x % 2 == 0]
print(c)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# filtered = [[x for x in row if x % 3 == 0] for row in matrix if row >= 10]
# print(filtered)
