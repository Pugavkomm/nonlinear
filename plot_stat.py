import stat_function_ring
import numpy as np
import matplotlib.pyplot as plt

def plot_stat(quant_el = 10, quant_it = 100, d = 0.4, a = 0.5, alpha = 1):
    matrix = stat_function_ring.model_cube_ring(quant_el, quant_it, a, d, alpha)
    print(matrix)
    x = np.zeros(quant_it)
    for i in range(quant_it):
        x[i] = matrix[0][i]
    plt.plot(np.arange(quant_it), x, ',')
    plt.show()

plot_stat(quant_el= 1000, quant_it= 10000)


