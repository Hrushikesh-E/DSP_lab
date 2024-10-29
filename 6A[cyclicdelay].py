import numpy as np
from matplotlib import pyplot as plt
x1=[1,2,3,4]
x2=[-1,0,5,3]
def cycle_delay(x,m):
	N=len(x)
	y=[]
	for n in range(0,N):
		if n-m >= 0:
			idx=(n-m)%N
		else:
			idx=N+n-m
		y.append(x[idx])
	return y
X1=cycle_delay(x1,3)
print(X1)
X2=cycle_delay(x2,5)
print(X2)

def circular_convolution(x1,x2):
	z=[]
	x2_r=x2[::-1]
	a=cycle_delay(x2_r,1)
	for n in range(len(x1)):
		y=cycle_delay(a,n)
		z.append(np.dot(x1,y))
	return z
print(circular_convolution(x1,x2))	