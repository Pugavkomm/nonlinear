import matplotlib.pyplot as plt
import numpy as np
import segment_function
import time
import progress_bar
import matplotlib.cm as cm
from func_for_mult_spectr import mutipl_all

start_time = time.time()
quant_it = 5000 # количество итераций
quant_el = 100  # количество элементов
quant_start_one = 0  # c этого элемента задаем начальные условия
quant_start_end = quant_el  # на этом элементе заканчиваем задавать н.у. остальные элементы равны нулю
value_start = 1.5  # значение начальных условий
alpha = .4
beta = .0
d = .20014
a = aa = .2
f = mutipl_all(quant_el, alpha)
info = ''
start = 1
stop = 36
el = stop - start
speed_plot = np.zeros(stop - start)
errors = np.zeros(stop - start)
f_plot = np.zeros(stop - start)
for j in range(1):
    for i in range(start, stop):
        d = (f[i + 1] + f[i]) / 2
        f_plot[i -start] = d
        # print('\n', 'alpha = ', alpha, ', d = ', d, ', beta = ', beta)
        print('\n', 'd = ', d, ', alpha = ', alpha, ', beta = ', beta)

        # nonlinear = 'cube'
        nonlinear = 'piece'
        matrix = segment_function.segment(quant_el, quant_it, quant_start_one, quant_start_end, value_start, a=a, d=d,
                                          alpha=alpha, beta=beta,
                                          nonlinear=nonlinear)  # вызываем функцию, которая возвращает матрицу с реализацией

        alpha = round(alpha, 3)

        c = 0
        speed = []
        el = 1
        it = 0
        for m in range(0, 1, 1):
            for l in range(quant_it):
                if abs(matrix[m][l]) >= .01:
                    if l != it and l != 0:
                        speed.append(50/(l))
                        c += 50/l
                        it = l

                        break
                    else:
                        break

        delta_c = .01/it
        print(delta_c)
        errors[i - start] = delta_c
        print(errors    )
        speed_plot[i - start] = c
        info += 'd = ' + str(d) + 'mult out: ' + str(i + 1) + ': c = ' + str(c) + '\n'
        print('mult out: ' + str(i) + ': c = ' + str(c))
    g = open('/home/mechislav/image/info', 'w')
    g.write(info)
    g.close()
    print('\n')
    print('time: %f', time.time() - start_time, ' second')

    s = open('/home/mechislav/image/speed.txt', 'w')
    s.write(str(speed))
    s.close()
    plt.figure(figsize=(8, 6))
    ax = plt.subplot(2, 1, 1)
    plt.title(r'$\alpha = $' + str(alpha) + r'$, \beta = $' + str(beta))
    plt.plot(np.arange(1, len(speed_plot) + 1, 1), speed_plot, '.', color = 'black')
    plt.grid(True)
    plt.xlabel('количество мультипликаторов вне ед. окр.')
    plt.ylabel('скорость')


    fig = plt.subplot(2, 1, 2)
    plt.plot(f_plot, speed_plot, '.', color = 'black')
    plt.grid(True)
    plt.xlabel('d')
    plt.ylabel('скорость')
    plt.show()