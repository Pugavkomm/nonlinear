#   прогрмма которая возвращает график реализации в виде прямой на которой изображенны
#   элементы, номер которых кодируется цветом, а амплитуда по оси
#   необходимо импортировать программу segment_function
#   сделаем ее в виде функции, чтобы можно было обращаться при не обходимости из
#   других программ
#   цепочка с гр.усл. отрезок
import numpy as np  # импортируем модуль numpy для работы с массивами
from segment_function import segment  # функция возвращающая реализацию цепочки
import progress_bar, time
import matplotlib.pyplot as plt  # для построения графика
import matplotlib.cm as cm
from segment_function_non_save import segment_non_save

def par(alpha, d, beta, N, quant_it):
    return [alpha, d, beta, N, quant_it]


def realize(alpha, d, beta, N, quant_it, start):
    return segment_non_save(alpha=alpha, d=d, beta=beta, quant_el=N, quant_it=quant_it, nonlinear='piece', start = start)


def line_plot(start, alpha, d, beta, N, quant_it):
    elemets = realize(alpha, d, beta, N, quant_it, start)
    number = np.arange(1, N + 1, 1)
    ax = plt.figure(figsize=(8, 6))
    for i in range(0, quant_it - start):
        progress_bar.update_progress((i) / (quant_it - start), 'Построение графика')
        for j in range(N):
            plt.scatter(elemets[j][i], 0, s=1, c=j, vmin=1, vmax=N)
    maxim = elemets.max()
    minim = elemets.min()

    cb = plt.colorbar()
    #plt.ylabel([-.001,.001])
    return maxim - minim
    


N = 100
alpha = 0.6
d = .2
beta = 0
start, quant_it = 60000, 63000
var_d = np.arange(0.2, .45, 0.005)
y = np.zeros(len(var_d))
for i in range(len(var_d)):
    progress_bar.update_progress((i) / (len(var_d)), 'PROGRESS')
    d = var_d[i]
    # var = par(alpha, d, beta, N, quant_it)
    y[i] = line_plot(start, alpha, d, beta, N, quant_it)
plt.plot(var_d, y)
plt.xlabel('d')
plt.ylabel('длинна интервала')
plt.title(r'$\alpha = $' + str(alpha) + r'$\beta = $' + str(beta))
plt.show()
    
