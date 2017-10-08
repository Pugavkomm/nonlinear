# строим реализацию изначальной системы
import function_start_ring
import matplotlib.pyplot as plt
import numpy

quant_it = 300
quant_el = 100


matrix = function_start_ring.model_pereod(quant_el, quant_it, alpha= 1., d = 0.4, a = .05, one_rand = 0, end_rand= 1)
x = numpy.arange(quant_it)
for i in range(quant_el):
    plt.plot(x, matrix[i], '.', linestyle = '-' )
plt.show()
