import numpy as np
import sympy as sy

s_a = .3
s_d = .5
s_alpha = .1


def b_cof(s_a, s_alpha, s_d, o):
    return 1 - 2 * s_d + s_alpha * (-3 * o ** 2 + 2 * o * (1 + s_a) - s_a)


def kof(s_a, s_d, s_alpha, k):
    k4 = s_d
    k3 = -1
    k2 = 0
    k1 = b_cof (s_a, s_alpha, s_d, k)
    k0 = s_d
    y = sy.Symbol ('y')
    return sy.solvers.solve (k4 * y ** 4 + k3 * y ** 3 + k2 * y ** 2 + k1 * y + k0, y)


print ('d = ', s_d, ', a = ', s_a, ', alpha = ', s_alpha)
k = 0
for i in range (0, 3):

    if i == 0:
        point = 'O1'
        k = 0
    elif i == 1:
        point = 'O2'
        k = s_a
    elif i == 2:
        k = 1
        point = 'O3'
    r = kof (s_a, s_d, s_alpha, k)
    print (point + '\n', r'$\mu_1$ ', r[0], '\n', '$\mu_2$ ', r[1], '\n', r'$\mu_3$ ', r[2], '\n', r'$\mu_4$ ', r[3],
           '\n -------------------')
