import numpy as np
from matplotlib import pyplot as plt
x1 = np.array([1, 2, 3, 4])
x2 = np.array([4, 3, 2, 1])
x3 = x1 + x2
def dtft(x):
    n = np.arange(len(x))
    W = np.linspace(-np.pi, np.pi, 1000, endpoint=False)
    X = np.array([np.sum(x * np.exp(-1j * w * n)) for w in W])
    return X
X1 = dtft(x1)
X2 = dtft(x2)
X3 = dtft(x3)
is_equal = np.allclose(X3, X1 + X2)
print("X3 is equal to the sum of X1 and X2:", is_equal)