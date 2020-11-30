x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

x = "Sagor"
y = x[::-1]
print(x)
print(y)



"""
Prefer get Over in and KeyError to Handle
Missing Dictionary Keys
"""

counters = {
    'pumpernickel': 2,
    'sourdough': 1,
}

key = "Wheat"

if key in counters:
    count = counters[key]
else:
    count = 0

counters[key] = count + 1

# Short
if key not in counters:
    counters[key] = 0
counters[key] += 1
if key in counters:
    counters[key] += 1
else:
    counters[key] = 1
