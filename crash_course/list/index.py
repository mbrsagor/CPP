bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1].upper())
print(bicycles[-1])

message = f"My 1st bicycles is {bicycles[2].title()}"
print(message)

bicycles[2] = "toyota"
print(bicycles)
bicycles.append("Hounda")
print(bicycles)
bicycles.insert(0, 'Hero cycle')
print(bicycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

bicycles.append(motorcycles)
print(bicycles)

bicycles.pop()
print(bicycles)
bicycles.remove('trek')
print(bicycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.reverse()
print(cars)
