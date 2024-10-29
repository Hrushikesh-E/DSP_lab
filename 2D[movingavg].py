#moving average system
import numpy as np
from matplotlib import pyplot as plt

x=[1,2,3,4,5]
y=[]
n=int(input("Enter the order of the signal"))
l=len(x)
p=l-n
for i in range(0,l):
	d=0
	if(i<n-1):
		a=0
		for j in range(0,i+1):
			a+=x[j]
		y.append(a/n)
	else:
		a=0
		for j in range(i+1-n,i+1):
			
			a+=x[j]
			
				
				
		y.append(a/n)
print(y)

plt.subplot(2,1,1)
plt.stem(x)

plt.subplot(2,1,2)
plt.stem(y)

plt.show()

