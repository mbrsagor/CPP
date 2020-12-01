from collections.abc import Iterator
import timeit
import math


class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


path = 'my_number.txt'
visits = ReadVisits(path)
print(visits)


def normalize_defensive(numbers):
    if iter(numbers) is numbers:
        raise TypeError('Must supply container')

    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


num = [1, 2, 3, 4, 5]
_num = normalize_defensive(num)
print(_num)


def normalize_defensive(numbers):
    if isinstance(numbers, Iterator):
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result


visits = [15, 35, 80]
percentages = normalize_defensive(visits)
assert sum(percentages) == 100.0

visits = ReadVisits(path)
percentages = normalize_defensive(visits)
# assert sum(percentages) == 100.0


value = [len(x) for x in open('my_number.txt')]
print(value)

it = (len(x) for x in open('my_number.txt'))
print(it)


def move(period, speed):
    for _ in range(period):
        yield speed


def pause(delay):
    for _ in range(delay):
        yield 0


def animal():
    for delta in move(4, 5.0):
        yield delta

    for delta in pause(3):
        yield delta

    for delta in move(2, 3.0):
        yield delta


def render(delta):
    print(f"Delta: {delta:.if}")


def run(func):
    for delta in func:
        render(delta)


# run(animal())


def animate_composed():
    yield from move(4, 5.0)
    yield from pause(3)
    yield from move(2, 3.0)


# run(animate_composed())

def child():
    for i in range(1_000_000):
        yield i


def show():
    for i in child():
        yield i


def fast():
    yield from child()


baseline = timeit.timeit(stmt='for _ in show(): pass', globals=globals(), number=50)
print(f'Manual nesting {baseline:.2f}s')


def wave(amplitude, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)

        output = amplitude * fraction
        return output


def transmit(output):
    if output is None:
        print("Output is None")
    else:
        print(f"Output is: {output:> 5.1f}")


def _run(it):
    for output in it:
        transmit(output)


_run(wave(3.0, 8))
