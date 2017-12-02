import numpy as np
import matplotlib.pyplot as plt
N =100
alpha = .6
d = .4
y = np.zeros(N)
x = np.zeros(N)
f = np.zeros(N)
for i in range(N):
    z = np.cos((i + 1)*np.pi/(N + 1))
    f[i] = (1 - alpha)/(1 + z)

    y[i] = 1 - 2*d - 2*alpha - 2*z*d
    x[i] = i
for i in range(N):
    plt.plot([x[i], x[i]], [0, y[i]], color = 'black')
#plt.plot([1, N], [0 , 0])
plt.title('Спектр мультипликаторов, d = ' + str(d) + r'$, \alpha = $' + str(alpha) + ', N = ' + str(N))
plt.xlabel('Номер мультипликатора')
plt.ylabel('Значение мультипликатора')
print(np.cos(np.pi/(N + 1)))
plt.show()


x = np.arange(0, 1, .001)
y = np.zeros(len(x))
z = np.zeros(len(x))
for i in range(len(x)):
    y[i] = (1 - x[i])/(1 + np.cos(np.pi/(N + 1)))


ax = plt.figure()
plt.plot(x,y)
plt.xlabel(r'$\alpha$')
plt.ylabel('d')
plt.yticks([])
plt.text(0.4, 0.4, 'Хаотическая динамика', fontsize=11  ,
         # выравнивание по вертикали и по горизонтали по центру
         horizontalalignment='left', verticalalignment='center',
         bbox=dict(facecolor='pink', alpha=0.5))
plt.text(0.0, 0.1, 'Регулярная динамика', fontsize=11,
         # выравнивание по вертикали и по горизонтали по центру
         horizontalalignment='left', verticalalignment='center',
         bbox=dict(facecolor='pink', alpha=0.5))
plt.text(.6, .2, r'            $\frac{1 - \alpha}{1 + z_1}$', fontsize = 11, rotation=47)

plt.show()


for i in range(N):
    print(round(f[i],6))


