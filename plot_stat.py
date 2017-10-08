import stat_function_ring
import numpy as np
import matplotlib.pyplot as plt
s_quant_el, s_quant_it = 100, 100000

s_a = .3
s_d = .5
s_alpha = .0005

s_one_rand, s_end_rand = .3, .5


#s_a = .3
#s_d = .5
#s_alpha = .005
#s_quant_el, s_quant_it = 100, 1000
#s_one_rand, s_end_rand = .3, .34
def plot_stat(quant_el, quant_it, a, d,  one_rand, end_rand, alpha):
    matrix = stat_function_ring.model_cube_ring(quant_el, quant_it, a, d,one_rand, end_rand,  alpha)
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

plot_stat(s_quant_el, s_quant_it, s_a, s_d, s_alpha, s_one_rand, s_end_rand)


