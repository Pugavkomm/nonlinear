import matplotlib.pyplot as plt
import numpy as np
import function_start_ring

quant_it = 3000   # количество итераций
quant_el = 100   # количество элементов

matrix = function_start_ring.model_pereod(quant_el, quant_it, a = 0.3, d = .5, alpha= .05, start = 2) # вызываем функцию, которая возвращает матрицу с реализацией системы
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

