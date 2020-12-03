def histogram(s):
    d = dict()
    for c in s:
        if c is not d:
            d[c] = 1
        else:
            d[c] += 1
    return d


h = histogram('brontosaurus')
print(h)


def print_hist(h):
    for c in h:
        print(c, ':', h[c])


h = histogram('parrot')
print_hist(h)

