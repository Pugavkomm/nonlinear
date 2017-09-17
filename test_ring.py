
import numpy as np
import random
import function
import matplotlib.pyplot as plt


def model_stat_eq(quant_el, quant_iter, a = 0.5, d = 0.4, one_rand = 0, end_rand = 1):
    element_x = np.zeros(quant_iter)  # элементы x
    element_y = np.zeros(quant_iter)  # элементы y

    element_x_time = np.zeros(quant_iter) # переменные для хранения всех значений элементов, для построения графика
    element_y_time = np.zeros(quant_iter)


    # заполним массивы случайными значениями от one_rand до end_rand по умолчанию от 0 до 1
    element_x[0] = random.uniform(one_rand, end_rand)
    element_y[0] = random.uniform(one_rand, end_rand)

    element_x_time[0] = element_x[0]
    element_y_time[0] = element_y[0]
        # итерируем систему, учитывая граничные условия типа кольцо Uj+N = Uj
    
    i = 0
    for j in range(quant_iter-1):

        if i == quant_el - 2:
            print('yes')
        element_x[i+1] = element_y[i]
        element_y[i+1] = function.stat_iter(a, d, element_x[i], element_y[i])
        element_y_time[j + 1] = element_x[i+1]
        element_x_time[j + 1] = element_x[i+1]
        i = i + 1

    plt.plot(element_x_time, element_y_time,'.')
    plt.grid(True)
    plt.show()

    plt.plot(np.arange(quant_iter), element_y_time)
    plt.grid(True)
    plt.show()

model_stat_eq(500, 100000)
