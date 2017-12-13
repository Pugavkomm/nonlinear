import numpy as np
import matplotlib.pylab as plt
from func_for_mult_spectr import mutipl_all

alpha = .2
#d = .2
beta = 0
N = 100 
f = mutipl_all(N, alpha)
def mutiplicator(alpha, d, s, N):
    return 1 - 2 * alpha - 2 * d * (1 + np.cos(s*np.pi/(N + 1)))
def lyapun(alpha, d, s, N):
    return np.log(abs(mutiplicator(alpha, d, s, N)))
#for i in range(1, 50, 1):
    #print(lyapun(alpha, .3, i + 1, N))

def dimm(alpha, d, N):
    sum = 0 # сумма ляпуновских показателей
    sum_earl = 0 # предыдущее значение суммы
    t = 0	
    lamd_for_sort = np.zeros(N)
    for i in range(N):
        lamd_for_sort[i] = lyapun(alpha, d, i + 1, N)
    lamd_for_sort[::-1].sort()
    #print(lamd_for_sort)
    while sum >= 0 and t < N:
        #print(i)
        t += 1
        sum_earl = sum
        #print('1')
        lamd = lamd_for_sort[t - 1]
        #print(t)
        sum += lamd
        #print(sum)
        if sum_earl < 0:
            print('при этом значение сумма уже меньше нуля:', t)
        if sum < 0:
            print('yes: ', d)
            #if sum_earl >= 0:
                #print('yes: ', d)
                #print(i)
                #print('google')
    if sum < 0 and t == N:
        print('t = ', t)
        m = t - 1
        nu = - sum_earl/lamd
        
        #print('nu = ', nu)
    if sum > 0:
        m = N
        nu = 0	
    elif sum < 0 and t != N :
        m = t - 1
        nu = - sum_earl/lamd
    return m + nu

d = d2 = f[0]
d1 = 2
print(d2, d1)
#print(f[99])
print('d1 - d2 = ', d1 - d2)
#d2 = 0 
step = .00001  # step on d
quantity = int((d1 - d2)/step)
x = np.zeros(quantity)
print(quantity)
l = np.zeros(quantity)
teta = np.zeros(quantity)
for i in range(quantity):
    x[i] = d
    teta[i] = dimm(alpha, d, N)/N
    d += step

#teta = teta/N
plt.plot(x, teta, '.', linestyle = '--')
plt.title(r'$\alpha = $' + str(alpha) + 'N = ' + str(N))
plt.xlabel('d')
plt.ylabel(r'$\theta$')
plt.grid(True)
plt.show()

