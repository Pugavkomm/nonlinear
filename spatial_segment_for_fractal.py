import matplotlib.pyplot as plt
import numpy as np
import segment_function
import time
import progress_bar
import matplotlib.cm as cm
from func_for_mult_spectr import mutipl_all

start_time = time.time()
quant_it = 500 + 2000  # количество итераций
quant_el = 100  # количество элементов
quant_start_one = 20  # c этого элемента задаем начальные условия
quant_start_end = 80  # на этом элементе заканчиваем задавать н.у. остальные элементы равны нулю
value_start = 1.5  # значение начальных условий
alpha = .6
beta = 0.0
#d = .2
a = aa = .2
f = mutipl_all(quant_el, alpha)
start = d = (f[4 + 1] + f[4]) / 2
close = (f[44 + 1] + f[44]) / 2
# nonlinear = 'cube'
nonlinear = 'piece'
# for m in range(5, 44):
m = 0
while d < (f[44 + 1] + f[44]) / 2:
    m += 1
    d += 0.00005
all_m = m
m = 0
d = start 
while d < (f[44 + 1] + f[44]) / 2:
    m += 1
    if d == start:
        t1 = time.time()
    if d == start + 1*0.00005:
        t2 = time.time()
        print('всего потребуется минут', (t2 - t1)/60*all_m)
    progress_bar.update_progress((d - start) / (close - start), 'ПРОГРЕСС')
    # d = (f[m + 1] + f[m]) / 2
    matrix = segment_function.segment(quant_el, quant_it, quant_start_one, quant_start_end, value_start, a=a, d=d,
                                      alpha=alpha, beta=beta,
                                      nonlinear=nonlinear)  # вызываем функцию, которая возвращает матрицу с реализацией

    # f = open ('spatial_segment_info.txt', 'w')
    info = 'd = ' + str(d) + ', alpha = ' + str(alpha) + ', beta = ' + str(beta) + '\n'
    #print(info)
    # f.write (info)
    # f.close ()p
    maxim = matrix.max()
    minim = matrix.min()
    plt.figure(figsize=(10, 6))
    for i in range(quant_el):
        # color = [str (item / 255.) for item in matrix[i]]
        #progress_bar.update_progress(i / quant_el, 'построение графика')
        plt.scatter(np.arange(quant_it), i * np.ones(quant_it), cmap=cm.Greys, s=3, c=matrix[i], vmin=minim,
                    vmax=maxim)  # строим график, где цветом отображаем амплитуду
    plt.axis('off')
    plt.xlim([100 + 2000, quant_it - 30])
    plt.ylim([0, quant_el - 1])
    plt.savefig('/home/mechislav/fractal_test/im_' + str(m + 1))
    plt.close()
    d += .00005
