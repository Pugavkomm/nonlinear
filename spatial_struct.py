import time
import progress_bar
import matplotlib.pyplot as plt
import numpy as np
import function_start_ring
start_time = time.time()
quant_it = 5000   # количество итераций
quant_el = 100  # количество элементов
a = .3
d = .5
alpha = .05
matrix = function_start_ring.model_pereod(quant_el, quant_it, a = a, d = d, alpha= alpha, start = 0) # вызываем функцию, которая возвращает матрицу с реализацией системы
for i in range(quant_el):
    progress_bar.update_progress(i / quant_el, 'построение графика')
    plt.scatter(np.arange(quant_it), i*np.ones(quant_it), 4,  c =matrix[i], alpha=0.6)  # строим график, где цветом отображаем амплитуду
cb = plt.colorbar()
print(min, max)
print(np.linspace(np.min(matrix), np.max(matrix), 3))
cb.set_label('значение элемента')
#cb.set_ticklabels('one')
plt.xlim([0, quant_it - 500])
plt.xlabel('n - дискретное время')
plt.ylabel('$U_j$ - номер элемента')
plt.title('d = ' + str(d) + ', a = ' + str(a) + r', $\alpha$ = ' + str(alpha))
print('time: %f', time.time() - start_time,' second')
plt.show()

