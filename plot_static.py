import numpy as np
import matplotlib.pyplot as plt
import statick

# задаем параметры, которые будем подставлять в функцию с префиксом s_
s_a = .5
s_d = .4
s_alpha = .1
s_quant_el, s_quant_it = 200, 1000
s_one_rand, s_end_rand = .4, .45

# сохраним реализацию системы в переменной matrix

matrix = statick.static(s_quant_el,s_quant_it,s_a, s_d, s_alpha, s_one_rand, s_end_rand)

x = np.arange(1, s_quant_it+1, 1)
y = np.zeros(s_quant_it)
for i in range(s_quant_it):
    y[i] = matrix[0][i]
print(y)
plt.plot(x,y,'.', linestyle = '-')
plt.xlim([200, s_quant_it])
plt.grid(True)
plt.show()

f = open('mass_static.txt', 'wb')
np.savetxt(f, matrix)
f.close()

print('.', np.sort(y))
#print(matrix)