import numpy as np
from matplotlib import pyplot as plt
x1 = [1,2,3,0,0,0]
N1 = len(x1)
W = np.linspace(-np.pi, np.pi, 1000)
x1_w = np.array([np.sum(x1 * np.exp(-1j * k * np.arange(N1))) for k in W])
x2=x1[::-1]
x2_w = np.array([np.sum(x2 * np.exp(-1j * k * np.arange(N1))) for k in W])
x3_w =x2_w[::-1]
if (x1_w.all() == x3_w.all()):
	print("reversal done")