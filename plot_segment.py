import segment_function
import matplotlib.pyplot as plt
import numpy

quant_it = 900
quant_el = 200
quant_start = 50
aa = 0.2
matrix = segment_function.segmen(quant_el, quant_it,quant_start, alpha= 1, d = 0.4, a = aa)
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