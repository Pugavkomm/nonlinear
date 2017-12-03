#  подключим все необходимые элементы и библиотеки
import numpy as np
import matplotlib.pyplot as plt
from homoklinic.solve_multipl import max_mult
from homoklinic.function_uns_sta import linear_unstable, three_stable
from four_solve_stat_piecewise import realize_f_s_p

eps = .001
#   зададим параметры
alpha = .6
d = .25
beta = 1
#   зададим н.т

o1 = beta / 2 / alpha
o2 = 1 + o1

#   для построения одномерного неустойчивого многообразия
#   и трех мерной не устойчивой плоскости нам необходим max
#   по модулю мультипликатор, его нам выдает подгруженная функция
#   max_mult

mu = max_mult(alpha, d)

#   далее нам необходимо задавать н.у., они находятся на одномерном
#   неустойчивом многообразии, поэтому задается только x1
#   желательно задавать в близи н.т.

x1 = 1

#   вычисляем x2, x3, x4, этого одномерного многообразия, все необходимое
#   содержится в файле function_uns_sta

#   вычисляем это для o1

initial = linear_unstable(x1, mu, o1)  # вернули одномерный массив с 4 точками

#   так как мы должны попасть на устойчивую трехмерную плоскость, то
#   изображающая точка должна попадать на устойчивую трехмерную пл.
quan_it = 90  #  берем большое кол-во итераций системы

elements = realize_f_s_p(quan_it, d, alpha, beta, initial)
print(elements)
x = np.linspace(0, quan_it-1, len(elements[0]))

plt.plot(x, elements[0], '.', linestyle = '--')
plt.show()

