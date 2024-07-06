import numpy as np
import matplotlib.pyplot as plt

anos = [2000 + x for x in range(20)]
pesos = [50, 51, 52, 48, 50, 55, 57, 55, 59, 60,
         62, 64, 65, 66, 59, 55, 60, 70, 65, 69]

plt.plot(anos, pesos, c='#667BC6', lw=5, linestyle=':')
plt.show()

