#  основные функции которые нам необходимы
# 1 зададим неустойчивую одномерную
# 2 зададим устойчивую трехмерную плоскость в виде неявной функции
import numpy as np


def linear_unstable(x1, mu, xl):
    elements = np.zeros(4)
    elements[0] = x1
    elements[1] = mu * (x1 - xl) + xl
    elements[2] = mu ** 2 * (x1 - xl) + xl
    elements[3] = mu ** 3 * (x1 - xl) + xl
    return elements


def three_stable(x1, x2, x3, x4, xl, alpha, d, mu):
    b = 1 - 2 * d - 2 * alpha
    return mu ** 2 * (x1 - xl) + mu * (x2 - xl) + (1 + b * mu ** 2 / d) * (
        x3 - xl) - mu ** 3 * (x4 - xl)
