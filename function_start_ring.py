import numpy as np
import random
import function
import progress_bar

# файл function содержит все необходимые функции для данной модели

# параметры задаем согласно теории (пока не проведены ислледования, то
# используем параметры для кусочно линейной функции

# необходимо обработать код таким образом, чтобы выходом было лишь результат в виде массива
# данных, чтобы его передавать на инструменты выводы, для анализа результатов

# d - коэфицент диффузии, N количество элементов
# данная программа будет моделировать активную среду с кубической нелинейностью
# с переодическими граничными условиями

# N - количество элементов в цепочке, quant_it - количество итераций


def model_pereod(quant_el, quant_it, d=0.4, a = 0.5, one_rand = 0.3, end_rand = 0.5, alpha = 1, start = 1):
    elements= np.zeros((quant_el, quant_it))
    #print(elements)
    if start == 1:
        for i in range(quant_el):
            elements[i][0] = random.uniform(one_rand, end_rand) # задаем случайные начальные условия
    elif start == 0:
        for i in range(int(quant_el/2 - 10), int(quant_el/2 + 10)): # задаем начальные условия типа "прямоугольник"
            elements[i][0] = .5
    elif start == 2:
        f = open('mass.txt')
        matr = np.loadtxt(f)
        for i in range(14,quant_el + 14):
            elements[i-14][0] = matr[0][i]
    for i in range(quant_it - 1):
        progress_bar.update_progress(i/(quant_it - 1), 'вычисление системы')
        for j in range(quant_el):
            if j == 0:
                elements[j][i + 1] = function.next_iter(a, d, elements[quant_el - 1][i], elements[j][i], elements[j + 1][i], alpha)
            elif j == quant_el - 1:
                elements[j][i + 1] = function.next_iter(a, d, elements[j - 1][i], elements[j][i], elements[0][i], alpha)
            else:
                elements[j][i+1] = function.next_iter(a, d, elements[j - 1][i], elements[j][i], elements[j + 1][i], alpha)
    print('1')
    return elements


















