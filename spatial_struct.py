import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np
import function_start_ring

quant_it = 400
quant_el = 100
elements_one = np.zeros(quant_it)

matrix = function_start_ring.model_pereod(quant_el, quant_it, a = 0.05, d = .4, alpha= 1)
for i in range(quant_el):
    plt.scatter(np.arange(quant_it), i*np.ones(quant_it), 4,  c =matrix[i], alpha=0.6)
cb = plt.colorbar()
print(min, max)
print(np.linspace(np.min(matrix), np.max(matrix), 3))
cb.set_label('значение элемента')
#cb.set_ticklabels('one')

plt.xlabel('k - дискретное время')
plt.ylabel('$U_i$ - номер элемента')


plt.show()

