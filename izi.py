import numpy as np
import matplotlib.pyplot as plt
alpha = .2
k = -.2
x = np.arange(0, 2*np.pi, .01)

y1 = y2 = np.zeros(len(x))

for i in range(len(x)):
    y1[i] = (1 - 2*alpha)*(k**4*np.cos(x[i]*2) + 1)/np.cos(x[i])
    y2[i] = -2*k**3

plt.plot(x, y1)
#plt.plot(x, y2)
plt.show()