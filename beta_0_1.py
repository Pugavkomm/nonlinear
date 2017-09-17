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


def model_pereod(d=0.5, N = 6, quant_it = 10000):
    elements = np.zeros((quant_it, N))
    quantity = np.zeros(quant_it)
    a = 0.1

    for k in range(N):
        elements[0][k] = random.uniform(0, 1) # задаем случайные значения параметра среды
    for i in range(quant_it - 1):
        for j in range(N-1):
            if j == 0:
                elements[i + 1][j] = function.next_iter(a, d, elements[i][N - 1], elements[i][j], elements[i][j+1])
            elif j < N - 1:
                elements[i + 1][j] = function.next_iter(a, d, elements[i][j - 1], elements[i][j], elements[i][j+1])
            elif j == N-1 :
                elements[i + 1][j] = function.next_iter(a, d, elements[i][j - 1], elements[i][j], elements[i][0])



    print(elements)
    return elements
matrix = model_pereod()
x1 = np.zeros(10000)
y1 = np.zeros(10000)
for i in range (10000):
    x1[i] = matrix[i][2]
    y1[i] = matrix[i][3]
plt.plot(x1, y1, '.')
plt.grid(True)
plt.show()










