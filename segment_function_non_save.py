#  То же, что и сегментталная функция, но не сохраняет не нужные даные в массив и осовбождает память

import numpy as np
import progress_bar
import function


# Создадим программу, которая на вход принимает начальную и количество итераций и сохраняет(возвращает)
# массив только с данными из этого интервала, остальные данные исключаются
# подключен numpy, для работы с массивами, progress bar - при необходимости выводы процентного выполнения прогрммы

# создадим функцию возвращающую реализацию, граничными условиями будет отрезок

def segment_non_save(quant_el=100, quant_it=110, quant_start_one=10, quant_start_end=50, value_start=.2, d=0.4, a=0.5, alpha=1,
            beta=0, nonlinear='piece', start = 0):
    spat = quant_it - start # количество иттерация и данное количество данных сохраняем
    eq = np.zeros(quant_el)
    elements = np.zeros((quant_el, spat))
    for i in range(40, 60):
        eq[i] = .1
    # elements[1][0] = 1


    for i in range(start):

        #progress_bar.update_progress(i / (start), 'вычисление системы')

        for j in range(quant_el):
                if j == 0:
                        eq[j] = function.next_iter(a, d, 0, eq[j], eq[j + 1], alpha, beta,
                                                            nonlinear)
                elif j == quant_el - 1:
                    eq[j] = function.next_iter(a, d, eq[j - 1], eq[j], 0, alpha, beta,
                                                            nonlinear)
                else:
                    eq[j] = function.next_iter(a, d, eq[j - 1], eq[j], eq[j + 1],
                                                            alpha, beta, nonlinear)
    print(eq)

    for k in range(quant_el):
        elements[k][0] = eq[k]
    for i in range(quant_it - start - 1):
        #progress_bar.update_progress(i / (quant_it - start - 1), 'вычисление системы')
        for j in range(quant_el):
            if j == 0:
                elements[j][i + 1] = function.next_iter(a, d, 0, elements[j][i], elements[j + 1][i], alpha, beta,
                                                        nonlinear)
            elif j == quant_el - 1:
                elements[j][i + 1] = function.next_iter(a, d, elements[j - 1][i], elements[j][i], 0, alpha, beta,
                                                        nonlinear)
            else:
                elements[j][i + 1] = function.next_iter(a, d, elements[j - 1][i], elements[j][i], elements[j + 1][i],
                                                        alpha, beta, nonlinear)

    return elements
