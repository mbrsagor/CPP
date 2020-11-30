a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('Middle two: ', a[3:5])
print('All but ends:', a[1:7])

# assert a[:5]

b = a[3:]
print('Before: ', b)
b[1] = 99
print('After: ', b)
print('No change:', a)

print('Before ', a)
a[2:7] = [99, 22, 14]
print('After ', a)

print('Before ', a)
a[2:3] = [47, 11]
print('After ', a)

b = a[:]
print(b)
assert b == a and b is not a
b = a
print("Before a", a)
print("Before b", b)

a[:] = [101, 102, 103]
assert a is b  # Still the same list object
print('After a ', a)  # Now has different contents
print('After b ', b)  # Same list, so same contents as a
