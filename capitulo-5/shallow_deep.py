import copy

a = [1, 2, 3]
b = a

# print(a)
# print(b)

# b.append(4)

print(a)
print(b)

# print(id(a))
# print(id(b))

c = copy.deepcopy(a)

c.append(4)

print(a)
print(c)

print(id(a))
print(id(c))
