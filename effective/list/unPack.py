"""
Item 13: Prefer Catch-All Unpacking Over Slicing
"""
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
print(car_ages_descending)

"""
oldest, second_oldest = car_ages_descending
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)

oldest, *others, youngest = car_ages_descending
print(oldest, youngest, others)
"""

# first, *middle, *second_middle, last = [1, 2, 3, 4]

car_inventory = {
    'Downtown': ('Silver Shadow', 'Pinto', 'DMC'),
    'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova'),
}
# print(car_inventory)

short_list = [1, 2, 3, 4, 5]
first, second, *rest = short_list
print(first, second, rest)

it = iter(range(1, 3))
first, second = it
print(f"{first} and {second}")


def generate_csv():
    yield ('Date', 'Make', 'Year', 'Price')


all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print("CSV Header", header)
print("Row Count", len(rows))

it = generate_csv()
header, *rows = it
print('CSV Header:', header)
print('Row count: ', len(rows))

print('\n')
