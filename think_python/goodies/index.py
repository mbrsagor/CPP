def factorial(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * factorial(n - 1)


fac = factorial(5)
print(fac)


def factorial2(n):
    return 1 if n == 0 else n * factorial(n - 1)


fact = factorial2(10)
print(fact)


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


li = ['sagor', 'ohi', 'meg']
capitalize = capitalize_all(li)
print(capitalize)


# comprehension
def capitalize_all_v2(t):
    return [s.capitalize() for s in t]


li2 = ['sagor', 'ohi', 'meg']
capi2 = capitalize_all_v2(li2)
print(capi2)


def only_upper(t):
    return [s for s in t if t.isupper()]


li3 = ['python', 'javascript', 'swift', 'dart']
is_upper = only_upper("li3")
print(is_upper)
