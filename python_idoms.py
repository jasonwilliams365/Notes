# unpacking

a, b = (1, 2) # a = 1, b = 2
c, d, e, f = (3, 5, 7, 9)

# enumerate

for i, val in enumerate(["apple", "banana"]):
    print(i, val)


# zip

for x, y in zip([1, 2], [3, 4]):
    print(x, y)


# Context Manager (with statement)

with open("test,txt", "w")  as f:
    f.write("Hello")