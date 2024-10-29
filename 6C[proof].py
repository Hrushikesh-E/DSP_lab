import numpy as np
import matplotlib.pyplot as pt
x1=[1,2,3]
x2=[4,5,6]
def cycle_delay(x,m):
    N=len(x)
    y=[]
    for n in range(0,N):
        if (n-m>=0):
            idx=(n-m)%N
        else:
            idx=N+n-m
        y.append(x[idx])
    return y
def circularconv(x1,x2):
    z=[]
    print(x2)
    x2r=[]
    x2r.append(x2[0])
    for i in range(len(x2)):
        if(len(x2)-i-1!=0):
            x2r.append(x2[len(x2)-i-1])
    print(x2r)
    for n in range(len(x1)):
        y=cycle_delay(x2r,n)
        z.append(np.dot(x1,y))
    return z
x3=circularconv(x1,x2)
print("circular convolution =",x3)
def idft(x,N):
    f=[]
    omega=np.arange(0,2*np.pi,(2*np.pi/N))
    for i in range(0,N):
        X=[]
        for k in range(0,N):
            a=(1/N)*x[k]*np.exp(1j*(2*np.pi*k*i)/N)
            X.append(a)
        f.append(sum(X))
    return omega,f
def dft(x,N):
    f=[]
    omega=np.arange(0,2*np.pi,(2*np.pi/N))
    for i in range(0,N):
        X=[]
        for k in range(0,N):
            a=x[k]*np.exp(-1j*(2*np.pi*k*i)/N)
            X.append(a)
        f.append(sum(X))
    return omega,f
w,X1=dft(x1,len(x1))
w,X2=dft(x2,len(x2))
X=np.zeros(len(X2),dtype=complex)
for i in range(0,len(X2)): 
    X[i]=X1[i]*X2[i]
w,a=idft(X,len(X))
pt.figure(figsize=(12,6))
pt.subplot(2,1,1)
pt.stem(w,np.abs(a))
    

pt.subplot(2,1,2)
pt.stem(w,np.abs(x3))
pt.show()
if(np.array(x3).all()==np.array(a).all()):
    print("convolved")
