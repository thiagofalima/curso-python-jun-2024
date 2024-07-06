import numpy as np

# l1 = [1, 2, 3, 4, 5]
# l2 = [6, 7, 8, 9, 0]
# a = np.array(l1)
# b = np.array(l2)
#
# print(l1 + l2)
# print(a)
# print(b)
# print(a + b)
# print(l1 * 2)
# print(a * 5)
#
# print(a * b)
#
# m = np.array([[1, 2, 3],
#               [4, 5, 6]])
#
# n = np.array([[5, 7, 2],
#               [4, 3, 9]])
#
# print(m * n)
#
A = np.array([[3, 2],
             [5, -1]])

B = np.array([[6, 4, -2],
              [0, 7, 1]])

# Produto Matricial
# Opção 1
print(A @ B)

# Opção 2
print(A.dot(B))

c = np.arange(1, 50, 2)
print(c)
print(type(c))
print(c.ndim)
print(c.shape)
print(c.size)
print(c.dtype)

print(np.sin(c))
print(np.cos(c))
print(np.tan(c))
print(np.exp(c))
print(np.log(c))
print(np.log10(c))

# Outra forma

d = np.linspace(0, 100, 101)

print(d)

