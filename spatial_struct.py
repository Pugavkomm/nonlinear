import matplotlib.pyplot as plt
import numpy as np
import function_start_ring
s_a = .6
s_d = .3
s_alpha = .1
s_quant_it = 2000

quant_it = 2000 # количество итераций
quant_el = 200  # количество элементов

matrix = function_start_ring.model_pereod(quant_el, quant_it, a = s_a, d = s_d, alpha= s_alpha, start = 1) # вызываем функцию, которая возвращает матрицу с реализацией системы
f = open('mass.txt')
matr = np.loadtxt(f)
f.close()
x = np.zeros(len(matr[0]))
y =  np.zeros(len(matr[0]))
for i in range(len(matr[0])):
    x[i] = matr[0][i]
    y[i] = matr[1][i]
    plt.subplot(2,2,1)
for i in range(quant_el):
    plt.scatter(np.arange(quant_it), i*np.ones(quant_it), 4,  c =matrix[i], alpha=0.6)  # строим график, где цветом отображаем амплитуду
cb = plt.colorbar()
print(min, max)
print(np.linspace(np.min(matrix), np.max(matrix), 3))
cb.set_label('значение элемента')
plt.xlim(0, quant_it - 700)
#cb.set_ticklabels('one')

plt.xlabel('k - дискретное время')
plt.ylabel('$U_i$ - номер элемента')
plt.subplot(2,2,2)
plt.title('$u_j(n) = \psi(j+n)$' + ' \n d = ' + str(s_d) + ', a = ' + str(s_a) + r' $, \alpha = $' + str(s_alpha) + '\n нач. усл. x = ' + str(x[0]) + ', y = ' + str(y[0]))
plt.plot (np.arange (len(x)), x, '.', linestyle='-')
plt.xlim([5000, 6000])
plt.xlabel('n - дискретное время')
plt.ylabel('$x_k$')


plt.subplot(2,1,2)
plt.plot (np.arange (len(x)), x, '.', linestyle='-')
plt.xlim([5000, 5400])
plt.xlabel('n - дискретное время')
plt.ylabel('$x_k$')
plt.show()


print(len(matrix[0]))