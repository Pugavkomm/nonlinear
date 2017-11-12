#Зададим решение в виде стационарной волны, при с = 2
#при этом функция будет кусочно линейной

import numpy as np
import random
import function as f
#создаем функцию, которая будет давать реализацию программы в
#виде матрицы, при этом зададим в ней различные граничные усл

def realize_f_s_p(quant_it, quant_el, d = 0.1, alpha = .2, beta = .1я, bound = 'ring', c = 2):
    elements = np.zeros((2*c, quant_it))

    for i in range(1, quant_it):
        for j in range(2*c - 1):
            elements[j][i] = elements[j + 1][i -1]
        elements[2*c - 1][i] = f.two_c_stat_solve_piecewise(d, alpha, beta,elements[c + 1][i - 1],elements[c][i - 1], elements[0][i - 1], c)





    print(elements)

realize_f_s_p(10, 5)