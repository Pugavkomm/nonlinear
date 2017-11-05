import numpy as np
import random
import matplotlib.pyplot as plt
import function

#функция реализующая статические решения
def static(quant_el, quant_it, a, d, alpha, one_rand, end_rand):
    #quant_el = quant_el + 1

    elements_time = np.zeros((2, quant_it))
    #случайные начальные условия
    elements_time[0][0] = random.uniform(one_rand, end_rand)
    elements_time[1][0] = random.uniform(one_rand, end_rand)
    #моделируем реализацию системы

    j = 1
    k = 0
    for i in range (1, quant_it):
        if j == quant_el:
            print (i)
            j = 0
            k = k + 1
            elements_time[0][i] = elements_time[1][i - 1]
            elements_time[1][i] = elements_time[1][i - quant_el]
        else:
            elements_time[0][i] = elements_time[1][i - 1]
            elements_time[1][i] = function.static_iter (a, d, elements_time[0][i - 1], elements_time[1][i - 1], alpha)
        j = j + 1
    return elements_time

