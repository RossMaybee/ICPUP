x = 5
y = 7
z = 10

if x%2 != 0:
    largest = x
if y%2 != 0:
    if y > largest:
        largest = y
if z%2 != 0:
    if z%2 != 0:
        largest = z
print (largest)
