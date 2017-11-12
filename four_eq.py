import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

s_a = .3

s_alpha = .4
s_d = (1 - 2*s_alpha)/2


#def b_cof(s_a, s_alpha, s_d, o):
   # return 1 - 2*s_d + s_alpha*(-3*o**2 + 2*o*(1 + s_a) - s_a)

def b_cof(s_a, s_alpha, s_d, o):
   return 1 - 2 * s_d - 2 * s_alpha


def kof(s_a, s_d, s_alpha, o):
    k4 = s_d
    k3 = -1
    k2 = b_cof (s_a, s_alpha, s_d, o)
    k1 = 0
    k0 = s_d
    print (k4, k3, k2, k1, k0)
    y = sy.Symbol ('y')
    return np.roots([k0,k1,k2,k3,k4])


print ('d = ', s_d, ', a = ', s_a, ', alpha = ', s_alpha)
k = 0
for i in range (0, 3):

    if i == 0:
        point = 'O1'
        k = 0
    elif i == 1:
        point = 'O2'
        k = s_a
    elif i == 2:
        k = 1
        point = 'O3'
    r = kof (s_a, s_d, s_alpha, k)
    print (point + '\n', r'$\mu_1$ ', r[0], '\n', '$\mu_2$ ', r[1], '\n', r'$\mu_3$ ', r[2], '\n', r'$\mu_4$ ', r[3],
           '\n -------------------')
k2 = b_cof (s_a, s_alpha, s_d, k)
mi = 0.601128711886766


k4 = s_d
k3 = -1
k2 = 0.063
k1 = 0
k0 = s_d



x = np.arange (-10, 13, .01)
# print(x)
y = np.zeros (len (x))

for i in range (len (x)):
    mi = x[i]
    # print (mi)
    y[i] = k4 * mi ** 4 + k3 * mi ** 3 + k2 * mi ** 2 + k1 * mi + k0
    if mi == 99.0:
        print (y[i], mi)
plt.plot (x, y)
plt.grid (True)
plt.title('F - кубическая' + ', d = ' + str(s_d) + r' $\alpha$ = ' +
          str(s_alpha) + ', a = ' + str(s_a))
plt.xlabel('u')
plt.ylabel('F(u)')
plt.show ()
e = r[1]
print(e.real)
print(np.sqrt(0.965471779918136**2 + 0.207206165000081**2   ))