import numpy as np
import matplotlib.pylab as plt
from func_for_mult_spectr import mutipl_all

alpha = .6
# d = .2
beta = 0
N = 100
f = mutipl_all(N, alpha)


def mutiplicator(alpha, d, s, N):
    return 1 - 2 * alpha - 2 * d * (1 + np.cos(s * np.pi / (N + 1)))


def lyapun(alpha, d, s, N):
    return np.log(abs(mutiplicator(alpha, d, s, N)))


# for i in range(1, 50, 1):
# print(lyapun(alpha, .3, i + 1, N))

def dimm(alpha, d, N):
    sum = 0  # сумма ляпуновских показателей
    sum_earl = 0  # предыдущее значение суммы
    t = 0
    while sum >= 0 and t < N:
        # print(i)
        t += 1
        sum_earl = sum
        # print('1')
        lamd = lyapun(alpha, d, t, N)
        # print(t)
        sum += lamd


    if sum < 0 and t != N:
        m = t-1
        nu = - sum_earl / lamd
    elif sum >= 0 and t == N:
        m = t
        nu = 0
    elif sum < 0 and t == N:
        m = t - 1
        nu = u = - sum_earl / lamd

    print('sum = ', sum, ', nu = ', nu, ', m = ', m, ', m + nu = ', m + nu)
dimm(alpha,.5378, 100)