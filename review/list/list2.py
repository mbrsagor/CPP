names = ["Sagor", "Ohi", "Meg", "Dhurbo", "Shanto"]

for n, name in enumerate(names):
    print(f"{n + 1}. {name}")
else:
    print("Done")


def myNumbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


for number in myNumbers():
    print(number)
