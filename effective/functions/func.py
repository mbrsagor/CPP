def get_states(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum


lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]
minimum, maximum = get_states(lengths)
print(f"Min: {minimum}, Max: {maximum}")


def get_avg_ratio(number):
    average = sum(number) / len(number)
    scaled = [x / average for x in number]
    scaled.sort(reverse=True)


# longest, *middle, shortest = get_avg_ratio(lengths)

