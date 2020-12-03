a = 4
x = 3

y = (x + a / x) / 2
print(y)

print('\n')

while True:
    print(x)
    y = (x + a / x) / 2
    if y == x:
        break
    x = y
