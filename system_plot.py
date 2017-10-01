# строим реализацию изначальной системы
import function_start_ring
import matplotlib.pyplot as plt
import numpy

quant_it = 500
quant_el = 100

aa = 0.2
matrix = function_start_ring.model_pereod(quant_el, quant_it, alpha= 1, d = 0.4, a = aa, one_rand = 0, end_rand = 1, start=2)
x = numpy.arange(quant_it)
for i in range(quant_el):
    plt.plot(x, matrix[i], '.', linestyle = '-' )
plt.plot([0, quant_it], [0, 0], linestyle = '-', c = 'black', label = 'н.т.: u = 0')
plt.plot([0, quant_it], [1, 1], linestyle = '-', c = 'blue', label = 'н.т.: u =  1')
plt.plot([0, quant_it], [aa, aa], linestyle = '-', c = 'red', label = 'н.т.: u = a = ' + str(aa))
plt.legend()
plt.xlabel('n - дискретное время')
plt.ylabel('U_j значение элемента')
plt.show()
