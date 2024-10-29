import numpy as np
def fft(x):
    n=len(x)
    if(n==1):
        return x
    else:
        l=[]
        l1=[]
        v=[]
        u=[]
        x_e=x[0::2]
        x_o=x[1::2]
        w_n=np.exp(-1j*np.pi*2*np.arange(0,n/2)/n)
        l.append(x_e)
        l1.append(x_o)
        X_e=fft(x_e)
        v.append(X_e)
        X_o=fft(x_o)
        u.append(X_o)
        X=np.append((X_e+w_n*X_o),(X_e-w_n*X_o))
        print(l,l1,v,u)
        return X
x=[1,2,-1,3]
print(fft(x))
print(len(fft(x)))