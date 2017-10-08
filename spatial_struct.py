import matplotlib.pyplot as plt
import numpy as np
import function_start_ring
s_a = .3
s_d = .5
s_alpha = .0005

quant_it = 1000  # количество итераций
quant_el = 100  # количество элементов

matrix = function_start_ring.model_pereod(quant_el, quant_it, a = s_a, d = s_d, alpha= s_alpha, start = 2) # вызываем функцию, которая возвращает матрицу с реализацией системы
for i in range(quant_el):
    plt.scatter(np.arange(quant_it), i*np.ones(quant_it), 4,  c =matrix[i], alpha=0.6)  # строим график, где цветом отображаем амплитуду
cb = plt.colorbar()
print(min, max)
print(np.linspace(np.min(matrix), np.max(matrix), 3))
cb.set_label('значение элемента')
#cb.set_ticklabels('one')
plt.xlabel('k - дискретное время')
plt.ylabel('$U_i$ - номер элемента')


plt.show()

