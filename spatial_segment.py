import matplotlib.pyplot as plt
import numpy as np
import segment_function
import time
import progress_bar
start_time = time.time()
quant_it = 500   # количество итераций
quant_el = 100  # количество элементов
quant_start_one = 40 # c этого элемента задаем начальные условия
quant_start_end = 60 # на этом элементе заканчиваем задавать н.у. остальные элементы равны нулю
value_start = .5      # значение начальных условий
alpha = 1
d = .4
a = .2
matrix = segment_function.segmen(quant_el, quant_it,quant_start_one, quant_start_end, value_start, a = a, d = d, alpha = alpha) # вызываем функцию, которая возвращает матрицу с реализацией системы
plt.figure()
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
plt.title('отрезок: ' + str(quant_el) + ' элементов'  + ' начальные условия задаются: \n с ' + str(quant_start_one) +
          ' по ' + str(quant_start_end) + ' элементы  со значением: ' + str(value_start) + '\n параметры: ' + 'd = ' + str(d) + r'$, \alpha = $' + str(alpha) +
          ', a = ' + str(a))
print('time: %f', time.time() - start_time,' second')
print(matrix)
plt.show()

print(matrix[146])