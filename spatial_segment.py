import matplotlib.pyplot as plt
import numpy as np
import segment_function
import time
import progress_bar
from matplotlib import rcParams
start_time = time.time()
quant_it = 650 # количество итераций
quant_el = 50  # количество элементов
quant_start_one = 40 # c этого элемента задаем начальные условия
quant_start_end = 60 # на этом элементе заканчиваем задавать н.у. остальные элементы равны нулю
value_start = .5      # значение начальных условий
alpha = 1
d = .1
a = aa = .2
matrix = segment_function.segmen(quant_el, quant_it,quant_start_one, quant_start_end, value_start, a = a, d = d, alpha = alpha) # вызываем функцию, которая возвращает матрицу с реализацией системыc
plt.figure()
plt.subplot(2,1,1)
for i in range(quant_el):
    progress_bar.update_progress(i / quant_el, 'построение графика')
    plt.scatter(np.arange(quant_it), i*np.ones(quant_it), 5,  c =matrix[i], alpha=1)  # строим график, где цветом отображаем амплитуду
cb = plt.colorbar()
print(min, max)
print(np.linspace(np.min(matrix), np.max(matrix), 3))
cb.set_label('значение элемента')
#cb.set_ticklabels('one')

plt.xlabel('n - дискретное время')
plt.xlim(0, quant_it - 50)
plt.ylabel('$U_j$ - номер элемента')
#plt.title('отрезок: ' + str(quant_el) + ' элементов'  + ' начальные условия задаются: \n с ' + str(quant_start_one) +
         # ' по ' + str(quant_start_end) + ' элементы  со значением: ' + str(value_start) + '\n параметры: ' + 'd = ' + str(d) + r'$, \alpha = $' + str(alpha) +
         # ', a = ' + str(a))
plt.title('н.у. $u_1 = 1, u_n = 0 (n > 1)$, \n $f(u) = u(u - a)(1-u)$')
print('time: %f', time.time() - start_time,' second')
fig = plt.subplot(2,1,2)

fig.patch.set_facecolor('w')

# Изменение параметров рисования (смена чёрного по белому на белое по чёрному)

x = np.arange(quant_it)
for i in range(1, quant_el):
    plt.plot(x, matrix[i], '.', linestyle = '-' )
#plt.plot([0, quant_it], [0, 0], linestyle = '-', c = 'black', label = 'н.т.: u = 0')
#plt.plot([0, quant_it], [1, 1], linestyle = '-', c = 'blue', label = 'н.т.: u =  1')
#plt.plot([0, quant_it], [aa, aa], linestyle = '-', c = 'red', label = 'н.т.: u = a = ' + str(aa))
plt.plot (x, matrix[0], '.', linestyle='-', label = 'Первый элемент', color = 'black', alpha = .5)
plt.legend()
plt.xlabel('n - дискретное время')
plt.ylabel('$U_j$ значение элемента')
print(matrix)
plt.grid(True, color='black', alpha = .4, linestyle = '--')
plt.show()

