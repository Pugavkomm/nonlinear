# файл function содержит все необходимые функции для данной модели

# параметры задаем согласно теории (пока не проведены ислледования, то
# используем параметры для кусочно линейной функции

# необходимо обработать код таким образом, чтобы выходом было лишь результат в виде массива
# данных, чтобы его передавать на инструменты выводы, для анализа результатов

# d - коэфицент диффузии, N количество элементов
# данная программа будет моделировать активную среду с кубической нелинейностью
# с переодическими граничными условиями

# так же будем моделировать среду сразу с решением в виде стационарных волн
# так как именно эти решения нас интересуют, так же создадим модели стационарных во времени и
# в пространстве волн.

# скорость распространения волн рассматриваем равной 1, т.е. (с = 1)

# quant_iter - количеств о итераций
# quant_el - количество элементов в цепочке
# a, d - параметры модели
# a - характерезует положение корня кубической функции
# d - коэффициент диффузии

# граничное условие типа кольцо

import numpy as np
import random
import function
import matplotlib.pyplot as plt


def model_stat_eq(quant_el, quant_iter, a = 0.5, d = 0.4, one_rand = 0, end_rand = 1):
    element_x = np.zeros(quant_el)  # элементы x
    element_y = np.zeros(quant_el)  # элементы y

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
            i = 0
        element_x[i+1] = element_y[i]
        element_y[i+1] = function.stat_iter(a, d, element_x[i], element_y[i])
        element_y_time[j + 1] = element_x[i+1]
        element_x_time[j + 1] = element_x[i+1]
        i = i + 1

    plt.plot(element_x_time, element_y_time,'.')
    plt.grid(True)
    plt.show()

    plt.plot(np.arange(quant_iter), element_y_time, '.')
    plt.grid(True)
    plt.show()

model_stat_eq(500, 100000)
