import numpy as np
import random
import function
import matplotlib.pyplot as plt

# файл function содержит все необходимые функции для данной модели

# параметры задаем согласно теории (пока не проведены ислледования, то
# используем параметры для кусочно линейной функции

# необходимо обработать код таким образом, чтобы выходом было лишь результат в виде массива
# данных, чтобы его передавать на инструменты выводы, для анализа результатов

# d - коэфицент диффузии, N количество элементов
# данная программа будет моделировать активную среду с кубической нелинейностью
# с переодическими граничными условиями

# N - количество элементов в цепочке, quant_it - количество итераций

def plot(number_el, quant_el, quant_it):
    matrix = model_pereod(quant_el, quant_it)
    y = np.zeros(quant_it)
    for i in range(quant_it):
        y[i] = matrix[number_el - 1][i]
    plt.plot(np.arange(quant_it), y, '.', linestyle = '-', label = "$U_" + str(number_el) + "$")
def model_pereod(quant_el, quant_it, d=0.4, a = 0.5, one_rand = 0, end_rand = 1):
    elements= np.zeros((quant_el, quant_it))
    #print(elements)
    for i in range(quant_el):
        elements[i][0] = random.uniform(one_rand, end_rand) # задаем случайные начальные условия
    for i in range(quant_it - 1):
        for j in range(quant_el):
            if j == 0:
                elements[j][i + 1] = function.next_iter(a, d, elements[quant_el - 1][i], elements[j][i], elements[j + 1][i])
            elif j == quant_el - 1:
                elements[j][i + 1] = function.next_iter(a, d, elements[j - 1][i], elements[j][i], elements[0][i])
            else:
                elements[j][i+1] = function.next_iter(a, d, elements[j - 1][i], elements[j][i], elements[j + 1][i])
    return elements

for i in range(10):
    plot(i + 1, 10, 500)

plt.legend()
plt.grid(True)
plt.xlabel("k - дискретное время")
plt.ylabel("$U_i$ - номер элемента цепочки ")
plt.show()


















