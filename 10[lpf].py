import matplotlib.pyplot as plt
import numpy as np

fs = 8000
Fc = 2000
N = 16
k = []
H_k = np.zeros(N)
for i in range(0, int(N / 2)):
    k.append(i)
F = []
for i in k:
    F.append(int(fs / N) * i)
kc = int(F.index(Fc))
H_k[:kc] = 1
H_k[kc:int(N / 2)] = 0
H_k[int(N / 2):int(N / 2) + kc] = 0
H_k[int(N / 2) + kc:N] = 1

print(H_k)
x_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 2, 3, 4, 5, 6]
M = len(x_n)
X_k = []
omega = np.arange(0, 2 * np.pi, (2 * np.pi / M))
for i in range(0, M):
    f = []
    for j in range(0, M):
        a = x_n[j] * np.exp(-1j * (2 * np.pi * j * i) / M)
        f.append(a)
    X_k.append(sum(f))
Y = []
print(len(X_k))
for i in range(N):
    Y.append(X_k[i] * H_k[i])

print(len(Y))
