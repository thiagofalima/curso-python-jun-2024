import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.random(50) * 100
y = np.random.random(50) * 100

# plt.scatter(x, y, c='red', marker='d')
plt.scatter(x, y, c='#36BA98', s=300, marker='d', alpha=0.9)
plt.show()
