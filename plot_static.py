import numpy as np
import matplotlib.pyplot as plt
import statick

# задаем параметры, которые будем подставлять в функцию с префиксом s_
s_a = .5
s_d = .001
s_alpha = .12
s_quant_el, s_quant_it = 10, 10
s_one_rand, s_end_rand = .2, .2

# сохраним реализацию системы в переменной matrix

matrix = statick.static(s_quant_el,s_quant_it,s_a, s_d, s_alpha, s_one_rand, s_end_rand)

print(matrix)