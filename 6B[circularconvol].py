import numpy as np

def circular_convolution(x, h):
    N = len(x)
    result = np.zeros(N)
    for n in range(N):
        for m in range(N):
            result[n]+=x[m]*h[(n-m)%N]
    return result
x = np.array([1,2,3,4])  
h = np.array([-1,0,5,3])  
output = circular_convolution(x, h)
print("Circular Convolution Output:", output)
