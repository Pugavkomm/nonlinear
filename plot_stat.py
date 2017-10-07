import stat_function_ring
import numpy as np
import matplotlib.pyplot as plt

def plot_stat(quant_el = 100, quant_it = 500, d = .5, a = 0.3, alpha = .05):
    matrix = stat_function_ring.model_cube_ring(quant_el, quant_it, a, d, alpha)
    print(matrix)
    x = np.zeros(quant_it)
    y =  np.zeros(quant_it)
    for i in range(quant_it):
        x[i] = matrix[0][i]
        y[i] = matrix[1][i]
    plt.plot(np.arange(quant_it), x, '.', linestyle = '-')
    plt.xlabel('n - дискретное время')
    plt.ylabel('$x_k$')
    plt.title('$u_j(n) = \psi(j+n)$' + ' \n d = ' + str(d) + ', a = ' + str(a) + r' $, \alpha = $' + str(alpha) + '\n нач. усл. x = ' + str(x[0]) + ', y = ' + str(y[0]) )
    plt.show()
    plt.plot(x, y, '.', linestyle = '-')
    plt.xlabel('x')
    plt.ylabel('y')


    plt.show()
    f = open('mass.txt', 'wb')
    np.savetxt(f, matrix)
    f.close()
plot_stat(quant_el= 100, quant_it= 50000)


