import matplotlib.pyplot as plt
import numpy as np
import segment_function
import time
import progress_bar
import matplotlib.cm as cm
from func_for_mult_spectr import mutipl_all
start_time = time.time ()
quant_it = 15000  # количество итераций
quant_el = 50  # количество элементов
quant_start_one =0 # c этого элемента задаем начальные условия
quant_start_end = quant_el # на этом элементе заканчиваем задавать н.у. остальные элементы равны нулю
value_start = 1.5  # значение начальных условий
alpha = .6
beta = .0
d = .20014
a = aa = .2
f = mutipl_all(quant_el, alpha)
for j in range(1):
    for i in range(len(f) - 1):
        d = (f[i + 1] + f[i])/2
        #print('\n', 'alpha = ', alpha, ', d = ', d, ', beta = ', beta)
        print('\n', 'd = ', d,', alpha = ', alpha,  ', beta = ', beta)

        #nonlinear = 'cube'
        nonlinear = 'piece'
        matrix = segment_function.segment (quant_el, quant_it, quant_start_one, quant_start_end, value_start, a=a, d=d,
                                           alpha=alpha, beta=beta,
                                           nonlinear=nonlinear)  # вызываем функцию, которая возвращает матрицу с реализацией
        # системыc

        maxim = matrix.max ()
        minim = matrix.min ()

        plt.figure (figsize=(8, 6))
        plt.subplot (2, 1, 1)
        for i in range (quant_el):
            # color = [str (item / 255.) for item in matrix[i]]
            progress_bar.update_progress (i / quant_el, 'построение графика')
            plt.scatter (np.arange (quant_it), i * np.ones (quant_it), cmap = cm.jet, s=1, c=matrix[i], vmin=minim,
                         vmax=maxim)  # строим график, где цветом отображаем амплитуду

        cb = plt.colorbar ()


        cb.set_label ('значение элемента')
        # cb.set_ticklabels('one')

        plt.xlabel ('n - дискретное время')
        plt.xlim (0, quant_it - 15)
        plt.ylabel ('$U_j$ - номер элемента')
        # plt.title('отрезок: ' + str(quant_el) + ' элементов'  + ' начальные условия задаются: \n с ' + str(quant_start_one)
        #  + ' по ' + str(quant_start_end) + ' элементы  со значением: ' + str(value_start) + '\n параметры: ' + 'd = ' +
        # str(d) + r'$, \alpha = $' + str(alpha) + ', a = ' + str(a))
        if nonlinear == 'cube':
            plt.title ('н.у. $u_1 = 1, u_n = 0 (n > 1)$, \n $f(u) = u(u - a)(1-u)$')
        elif nonlinear == 'piece':
            plt.title ('$f(u) - кусчно-линейная, гр.у. - отрезок$ \n' + r'$\alpha = $' + str (alpha) + r', $d =$' + str (
                d) + r', $\beta = $' + str (beta))
        plt.xlim([0, quant_it])
        plt.ylim ([0, quant_el - 1])
        fig = plt.subplot (2, 1, 2)

        # fig.patch.set_facecolor('w')

        # Изменение параметров рисования (смена чёрного по белому на белое по чёрному)

        x = np.arange (quant_it)
        for i in range (1, quant_el):
            plt.plot (x, matrix[i], '.', linestyle='-')
        # plt.plot([0, quant_it], [0, 0], linestyle = '-', c = 'black', label = 'н.т.: u = 0')
        # plt.plot([0, quant_it], [1, 1], linestyle = '-', c = 'blue', label = 'н.т.: u =  1')
        # plt.plot([0, quant_it], [aa, aa], linestyle = '-', c = 'red', label = 'н.т.: u = a = ' + str(aa))
        plt.plot (x, matrix[0], '.', linestyle='-', label='Первый элемент', color='black', alpha=.5)
        plt.legend ()
        plt.xlabel ('n - дискретное время')
        plt.ylabel ('$U_j$ значение элемента')
        plt.grid (True, color='black', alpha=.4, linestyle='--')
        #plt.show ()
        plt.xlim([0, quant_it])
        plt.savefig('_ d = ' + str(d) + r'alpha = ' + str(alpha) + r'beta = ' + str(beta) + '.png')
        plt.close()

        alpha = round(alpha, 3)
print('\n')
print ('time: %f', time.time () - start_time, ' second')
