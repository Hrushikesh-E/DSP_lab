import numpy as np
from matplotlib import pyplot as plt
W = np.linspace(-np.pi, np.pi, 1000)
x1 = [1,2,3,2,3,3]
N1 = len(x1)
x1_w = np.array([np.sum(x1 * np.exp(-1j * k * np.arange(N1))) for k in W])
x2 = [1,2,3,1,3,1]
N2 = len(x2)
x2_w = np.array([np.sum(x2 * np.exp(-1j * k * np.arange(N2))) for k in W])
a=np.convolve(x1,x2)
x3_w=x1_w*x2_w
if (a.all() == x3_w.all()):
	print("success")