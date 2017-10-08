import numpy as np
s_y = 0
s_a = .3
alpha = .12
d = .001
def diff_f(a, y):
    return -3*y**2 +2*y*(1+a) - a
mu1 = 1 - alpha*diff_f(s_a, s_y)/2/d + np.sqrt((1 - alpha*diff_f(s_a, s_y)/2/d)**2 - 1)
mu2 = 1 - alpha*diff_f(s_a, s_y)/2/d - np.sqrt((1 - alpha*diff_f(s_a, s_y)/2/d)**2 - 1)
print('$\mu_1 = $', mu1, ' $\mu_2 = $', mu2)