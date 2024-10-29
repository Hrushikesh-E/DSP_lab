import numpy as np
import matplotlib.pyplot as plt
x1 = [1, 2, 3, 4, 5]
n = np.arange(len(x1))
omega_0 = np.pi / 4
x_shifted = [x1[i] * np.exp(1j * omega_0 * n[i]) for i in range(len(x1))]
def dtft(x, n):
    w = np.arange(-np.pi, np.pi, 0.01)
    X = np.zeros(len(w), dtype=complex)
    for k in range(len(w)):
        X[k] = np.sum([x[i] * np.exp(-1j * w[k] * i) for i in range(n)])
    return w, X
w, X1 = dtft(x1, len(x1))
plt.plot(w, np.abs(X1), label="Original")
w, X_shifted = dtft(x_shifted, len(x_shifted))
plt.plot(w, np.abs(X_shifted), color='red', label="Frequency Shifted")
plt.legend()
plt.show()
if np.any(np.abs(X_shifted) - np.abs(np.roll(X1, int(omega_0 / 0.01))) < 1e-5):
    print("freq shift done")
