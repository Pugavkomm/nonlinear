
import stat_function_ring
import numpy as np
import matplotlib.pyplot as plt
f = open ('mass.txt')
matr = np.loadtxt (f)


y = np.zeros(int(len(matr[0])/2))
x = np.zeros(int(len(matr[0])/2))
for i in range(0, len(y), 1):
    y[i] = matr[1][2*i-1]
    x[i] = 2*i-1

plt.scatter(x, y, .4)
plt.xlim([1000, len(y)])
plt.ylim([.995, 1.005])
plt.grid(True)
plt.show()