def remainder(number, division):
    return number % division


# assert remainder(20, 7) == 7
print(remainder(20, 5))


def print_parameters(**kwargs):
    for key, val in kwargs.items():
        print(f"{key} : {val}")


print_parameters(alpha=1.5, beta=9, gamma=4)


def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff


weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print(f'{flow:.3} kg per second')
