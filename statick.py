import numpy as np
import random
import matplotlib.pyplot as plt
import function

#функция реализующая статические решения
def static(quant_el, quant_it, a, d, alpha, one_rand, end_rand):
    #quant_el = quant_el + 1
    elements = np.zeros((2, quant_el))   #первая строка x, вторая строка y
    elements_time = np.zeros((2, quant_it))
    #случайные начальные условия
    elements[0][0] = random.uniform(one_rand, end_rand)
    elements[1][0] = random.uniform(one_rand, end_rand)
    elements_time[0][0] = elements[0][0]
    elements_time[1][0] = elements[1][0]
    #моделируем реализацию системы

    j = 1
    for i in range(quant_it):
        if j == 0:
            elements[1][j] = function.stat_iter (a, d, elements[0][quant_el - 1], elements[1][quant_el - 1], alpha)
            elements[0][j] = elements[1][quant_el - 1]
        elif (j == quant_el - 1):
            elements[0][j] = elements[1][quant_el - 1]
            elements[1][j] = elements[1][0]
        else:
            elements[0][j] = elements[1][j - 1]
            elements[1][j] = function.static_iter(a, d, elements[0][j - 1], elements[1][j - 1],alpha)
        elements_time[0][i] = elements[0][j]
        elements_time[1][i] = elements[1][j]
        j = j + 1
        if j == quant_el:
            j = 0
    print(elements_time[0][100], elements_time[0][200])
    return elements_time

