import numpy as np
from matplotlib import pyplot as plt
def dft(x,N):
    X=[]
    for k in np.arange(0,N):
        s=0
        for n in np.arange(0,N):
            s=s+x[n]*np.exp(-2j*np.pi*k*n/N)
        X.append(s)
    return X
x1=[1,2,3]
N1=len(x1)
X1=dft(x1,N1)
x2=[1,2,3,0,0]
N2=len(x2)
X2=dft(x2,N2)
x3=[1,2,3,0,0,0]
N3=len(x3)
X3=dft(x3,N3)
x4=[1,2,3,0,0,0,0]
N4=len(x4)
X4=dft(x4,N4)
mag1 = np.abs(X1)
mag2 = np.abs(X2)
mag3 = np.abs(X3)
mag4 = np.abs(X4)
plt.subplot(2,2,1)
plt.stem(mag1)
plt.subplot(2,2,2)
plt.stem(mag2)
plt.subplot(2,2,3)
plt.stem(mag3)
plt.subplot(2,2,4)
plt.stem(mag4)

plt.show()


