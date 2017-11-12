import numpy as np
import sympy as sy
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes()

ax.set_aspect(1)
s_a = .3

s_alpha = .4
s_d = 0.1


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
st = ' '
my_file = open ('mult.txt', 'w')
for i in range(9):
    s_d = s_d + .1
    r = kof(s_a, s_d, s_alpha, 1) #незабыть убрать с.р.

    print(i)
    text_for_file = 'Some text here...'
    st = st +  'd = ' + str(s_d) + ', alpha = ' + str(s_alpha) + '\n' + str(r[0]) + '\n' + str(r[1]) + '\n' + str(r[2]) + '\n' + str(r[3])
    st = st + '\n ________________ \n'
    if i == 0:
        col = 'green'
    elif i == 1:
        col = 'black'
    elif i == 2:
        col = 'blue'
    elif i == 3:
        col = 'red'
    elif i == 4:
        col = '#4B0082'
    elif i == 5:
        col = '#FFFF00'
    elif i == 6:
        col = '#00FFFF'
    elif i == 7:
        col = '#808000'
    elif i == 8:
        col = '#2F4F4F'
    elif i == 9:
        col = '#00FFFF'
    print(st)
    for j in range(4):


        if j == 3:
            plt.plot(r[j].real,r[j].imag, '.', color = col, label = 'd  =' + str(round(s_d, 2)) )
        plt.plot (r[j].real, r[j].imag, '.', color=col)
my_file.write(st)
my_file.close ()

#окружность




theta = np.linspace(-np.pi, np.pi, 200)
plt.plot(np.sin(theta), np.cos(theta))

plt.grid(True)
plt.legend()
plt.title(r'$\alpha = $' + str(s_alpha))
plt.show()

s_d = (1 - 2*s_alpha)/2
print(1 - 2*s_d - 2*s_alpha)
r = kof(s_a, s_d, s_alpha, 1) #незабыть убрать с.р.

fig = plt.figure()
ax = plt.axes()

ax.set_aspect(1)

for j in range (4):

    if j == 3:
        plt.plot (r[j].real, r[j].imag, '.', color=col, label='b = 0')
    plt.plot (r[j].real, r[j].imag, '.', color=col)
theta = np.linspace(-np.pi, np.pi, 200)
plt.plot(np.sin(theta), np.cos(theta))

plt.grid(True)
plt.legend()
plt.show()
