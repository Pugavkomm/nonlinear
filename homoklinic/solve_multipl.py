import numpy as np


def b_cof(s_alpha, s_d):
    return 1 - 2 * s_d - 2 * s_alpha


def solve_mult_c_2(alpha, d):
    k4 = d
    k3 = -1
    k2 = b_cof(alpha, d)
    k1 = 0
    k0 = d
    return np.roots([k4, k3, k2, k1, k0])


def max_mult(alpha, d):
    return max(abs(solve_mult_c_2(alpha, d)))



