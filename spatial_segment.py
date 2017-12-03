import matplotlib.pyplot as plt
import numpy as np
import segment_function
import time
import progress_bar
import matplotlib.cm as cm
from func_for_mult_spectr import mutipl_all

start_time = time.time()
quant_it = 600 # количество итераций
quant_el = 300  # количество элементов
quant_start_one = 0  # c этого элемента задаем начальные условия
quant_start_end = quant_el  # на этом элементе заканчиваем задавать н.у. остальные элементы равны нулю
value_start = 1.5  # значение начальных условий
alpha = .6
beta = .0
d = .20014
a = aa = .2
f = mutipl_all(quant_el, alpha)
info = ''
speed = np.zeros(45)
f_plot = np.zeros(45)
for j in range(1):
    for i in range(43, 44):
        d = (f[i + 1] + f[i]) / 2
        f_plot[i] = d
        # print('\n', 'alpha = ', alpha, ', d = ', d, ', beta = ', beta)
        print('\n', 'd = ', d, ', alpha = ', alpha, ', beta = ', beta)

        # nonlinear = 'cube'
        nonlinear = 'piece'
        matrix = segment_function.segment(quant_el, quant_it, quant_start_one, quant_start_end, value_start, a=a, d=d,
                                          alpha=alpha, beta=beta,
                                          nonlinear=nonlinear)  # вызываем функцию, которая возвращает матрицу с реализацией
        # системыc

        maxim = matrix.max()
        minim = matrix.min()

        plt.figure(figsize=(8, 6))
        ax = plt.subplot(2, 1, 1)
        for t in range(quant_el):
            # color = [str (item / 255.) for item in matrix[i]]
            progress_bar.update_progress(t / quant_el, 'построение графика')
            plt.scatter(np.arange(quant_it), t * np.ones(quant_it), cmap=cm.jet, s=1, c=matrix[t], vmin=minim,
                        vmax=maxim)  # строим график, где цветом отображаем амплитуду

        cb = plt.colorbar()

        cb.set_label('значение элемента')
        # cb.set_ticklabels('one')

        plt.xlabel('n - дискретное время')
        plt.xlim(0, quant_it - 15)
        plt.ylabel('$U_j$ - номер элемента')
        # plt.title('отрезок: ' + str(quant_el) + ' элементов'  + ' начальные условия задаются: \n с ' + str(
        # quant_start_one) + ' по ' + str(quant_start_end) + ' элементы  со значением: ' + str(value_start) + '\n
        # параметры: ' + 'd = ' + str(d) + r'$, \alpha = $' + str(alpha) + ', a = ' + str(a))
        if nonlinear == 'cube':
            plt.title('н.у. $u_1 = 1, u_n = 0 (n > 1)$, \n $f(u) = u(u - a)(1-u)$')
        elif nonlinear == 'piece':
            plt.title('$f(u) - кусчно-линейная, гр.у. - отрезок$ \n' + r'$\alpha = $' + str(alpha) + r', $d =$' + str(
                d) + r', $\beta = $' + str(beta))
        plt.xlim([0, quant_it])
        plt.ylim([0, quant_el - 1])
        # xmajor_ticks = np.arange(0, quant_it - 1, 20)
        # xminor_ticks = np.arange(0, quant_it - 1, 5)
        # ymajor_ticks = np.arange(0, quant_el - 1, 5)
        # yminor_ticks = np.arange(0, quant_el - 1, 2)
        # ax.set_xticks(xmajor_ticks)
        # ax.set_xticks(xminor_ticks, minor = True)
        # ax.set_yticks(ymajor_ticks)
        # ax.set_yticks(yminor_ticks, minor = True)
        # ax.grid(which='both')

        # or if you want differnet settings for the grids:
        # ax.grid(which='minor', alpha=1)
        # ax.grid(which='major', alpha=1)
        # plt.grid(True, color = 'black')
        fig = plt.subplot(2, 1, 2)

        # fig.patch.set_facecolor('w')

        # Изменение параметров рисования (смена чёрного по белому на белое по чёрному)

        x = np.arange(quant_it)
        for t in range(1, quant_el):
            plt.plot(x, matrix[t], '.', linestyle='-')
        # plt.plot([0, quant_it], [0, 0], linestyle = '-', c = 'black', label = 'н.т.: u = 0')
        # plt.plot([0, quant_it], [1, 1], linestyle = '-', c = 'blue', label = 'н.т.: u =  1')
        # plt.plot([0, quant_it], [aa, aa], linestyle = '-', c = 'red', label = 'н.т.: u = a = ' + str(aa))
        plt.plot(x, matrix[0], '.', linestyle='-', label='Первый элемент', color='black', alpha=.5)
        plt.legend()
        plt.xlabel('n - дискретное время')
        plt.ylabel('$U_j$ значение элемента')
        # plt.grid (True, color='black', alpha=.4, linestyle='--')
        plt.show ()
        plt.xlim([0, quant_it])
        plt.savefig('/home/mechislav/image/var_ ' + '_ d = ' + str(d) + r'alpha = ' + str(alpha) + r'beta = ' + str(
            beta) + '.png')
        plt.close()
        alpha = round(alpha, 3)
        n = 0
        n1 = 0
        for k in range(quant_it):
            if matrix[30][k] > .5:
                print('yes ', n1)
                n1 = k
                break
            if matrix[48][k] != 0:
                n = k
        if n1 != 0 and n != n1:
            c = abs((19) / (n1))
        else:
            c = 0
        speed[i] = c

        #info += 'd = ' + str(d) + 'mult out: ' + str(i + 1) + ': c = ' + str(c) + '\n'
        #print('mult out: ' + str(i) + ': c = ' + str(c))
#g = open('/home/mechislav/image/info', 'w')
#g.write(info)
#g.close()

