
import numpy as np
import matplotlib.pyplot as plt


def diff_f(y, a):
    return -3 * y ** 2 + 2 * y * (1 + a) - a


def mu(sign, a, d, y):
    b = -((1 - 2 * d + diff_f(y, a)) / (1 - d))
    t = -d / (1 - d)
    if sign == '+':
        return -b / 2 + np.sqrt(b ** 2 - 4 * t) / 2
    elif sign == '-':
        return -b / 2 - np.sqrt(b ** 2 - 4 * t) / 2


iteration = np.arange(-10, 10, 0.01)
mem_save_plus = np.zeros(len(iteration))
mem_save_minus = np.zeros(len(iteration))
#y = 1
#y = 0
y = 10
if y == 0:
    plt.title('$O_1(x = y = 0$')
elif y == 1:
    plt.title('$O_2(x = y = 1$')
else:
    plt.title('$O_3(x = y = a)$')
for i in range(9):
    for j in range(len(iteration)):
        y = iteration[j]
        mem_save_plus[j] = mu('+', iteration[j], 0.1 + i / 10, y)
        mem_save_minus[j] = mu('-', iteration[j], 0.1 + i / 10, y)
    plt.plot(iteration, mem_save_plus, label="$\mu_+$, d = " + str(round(0.1 + i / 10, 2)), color = 'black')
    plt.plot(iteration, mem_save_minus, label="$\mu_-$, d = " + str(round(0.1 + i / 10, 2)), color='red')
    plt.plot([-10, 10], [1, 1], color = 'green')
    plt.plot([-10,10], [-1, -1], color = 'green')
    plt.xlabel('a')
    plt.ylabel('$Re(\mu_{+, -}), Im(\mu_{+, -}) = 0$')
    plt.ylim(-2, 2)
    plt.grid(True)
    plt.legend()
plt.show()