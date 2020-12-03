class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """


time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum


start = Time()
start.hours = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0


# done = add_time(start, duration)
# print(done)

def time_to_int(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


_time = time_to_int(45)
print(_time)


