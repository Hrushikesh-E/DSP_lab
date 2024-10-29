import numpy as np
from matplotlib import pyplot as plt
x1_n = [1,2,3,0,0,0]
N1 = len(x1_n)
W = np.linspace(-np.pi, np.pi, 1000)
x_w = np.array([np.sum(x1_n * np.exp(-1j * k * np.arange(N1))) for k in W])
X_general = x_w * np.exp(-1j * W * 3)
x_s = np.roll(x1_n, 3)
x_s_w = np.array([np.sum(x_s * np.exp(-1j * k * np.arange(N1))) for k in W])
if (x_s_w.all() == X_general.all()):
	print("shift done")
else:
	print("Error")
