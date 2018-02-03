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


def realize(alpha, d, beta, N, quant_it):
    return segment(alpha=alpha, d=d, beta=beta, quant_el=N, quant_it=quant_it, nonlinear='piece')


def line_plot(start, alpha, d, beta, N, quant_it):
    matrix = realize(alpha, d, beta, N, quant_it)
    number = np.arange(1, N + 1, 1)
    elemets = np.zeros((N, quant_it - start))
    for i in range(start, quant_it):
        for j in range(N):
            elemets[j][i - start] = matrix[j][i] 
        
    maxim = elemets.max()
    minim = elemets.min()

    mine = maxim - minim
    print(mine)
    #plt.ylabel([-.001,.001])
    return mine


N = 100
alpha = 0.6
d = .2
beta = 0
start, quant_it = 80000, 90000
var_d = np.arange(0.2, .35, 0.001)
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
    
