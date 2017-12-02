import numpy as np
def mutipl_all(N, alpha):

    f = np.zeros(N)
    for i in range(N):
        z = np.cos((i + 1)*np.pi/(N + 1))
        f[i] = (1 - alpha)/(1 + z)
    return f