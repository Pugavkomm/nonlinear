import numpy as np
import matplotlib.pyplot as plt
N =100
alpha = .2
d = .0
m = 0
var_d = np.arange(.96,.97,.0001)

for i in range(0,1):
    d = .9691
    y = np.zeros(N)
    mu = np.zeros(N)
    x = np.zeros(N)
    f = np.zeros(N)
    for i in range(N):
        z = np.cos((i + 1)*np.pi/(N + 1))
        f[i] = (1 - alpha)/(1 + z)
        if i == 74:
            print('cos = ', z, ', mu = ', 1 - 2*d - 2*alpha - 2*z*d)
        y[i] = np.log(abs(1 - 2*d - 2*alpha - 2*z*d))
        mu[i] = (1 - 2*d - 2*alpha - 2*z*d)
        x[i] = i + 1
    sum = 0
    #mu[::-1].sort()
    #y[::-1].sort()
    for i in range(N):
        value = y[i]
        sum += value
        if i == N - 1:
            plt.plot([x[i], x[i]], [0, y[i]], color='black', label = 'ляпуновские показатели')
            plt.plot(x[i], mu[i], '.', color='black', label = 'мультипликаторы')
        plt.plot([x[i], x[i]], [0, y[i]], color = 'black')
        plt.plot(x[i], mu[i], '.', color = 'black')

        #if i == N - 1:
            #plt.plot([x[i], x[i]], [0, np.log(abs(y[i]))], color = 'black', label = 'ляпуновские показатели')
    #plt.plot(x,y,'.', label = 'мультипликаторы')
    plt.legend()
    plt.grid(True)
    #plt.plot([1, N], [0 , 0])

    plt.title('Спектр, d = ' + str(d) + r'$, \alpha = $' + str(alpha) + ', N = ' + str(N) )
    plt.xlabel('Номер')
    plt.ylabel('Значение')
    print(d)
    plt.show()
    m += 1
    #plt.savefig('/home/mechislav/multipl/im_d_' + str(m))
    plt.close()
'''

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


'''