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


def model_cube_ring(quant_el, quant_iter, a, d, one_rand, end_rand, alpha):
    quant_el = quant_el + 1
    # функция моделирует систему, когда решение ищем в виде стац. волн, возвращает матрицу, 1 строка - x, вторая y
    elements = np.zeros((2, quant_el)) #первая строка x, второя y. Учитываем граничные условия
    elements_time = np.zeros((2, quant_iter))  #первая строка x, второя y. Количество итераций
    #случайные нач. условия в заданном интервале
    elements[0][0] = random.uniform(one_rand, end_rand)
    elements[1][0] = random.uniform(one_rand, end_rand)
    #elements[0][0] = .386
    #elements[1][0] = .351
    print(elements)
    #elements[0][0] = 1.45
    #elements[1][0] = .5
    j = 1
    for i in range(quant_iter):
        if j ==0:
            elements[1][j] = function.stat_iter(a, d, elements[0][quant_el - 1], elements[1][quant_el - 1], alpha)
            elements[0][j] = elements[1][quant_el - 1]

        elif (j == quant_el - 1):
            elements[0][j] = elements[1][j - 1]
            elements[1][j] = elements[1][0]
        else:
            elements[1][j] = function.stat_iter(a, d, elements[0][j - 1], elements[1][j - 1], alpha)
            elements[0][j] = elements[1][j - 1]
        elements_time[0][i] = elements[0][j]
        elements_time[1][i] = elements[1][j]
        j = j + 1
        if j == quant_el:
            j = 0

    return elements_time

