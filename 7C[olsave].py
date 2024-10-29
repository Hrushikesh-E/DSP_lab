import numpy as np

def circular_convolution(x, h):
    N = len(x)
    result = np.zeros(N)
    for n in range(N):
        for m in range(N):
            result[n] += x[m]*h[(n-m)%N]
    return result

def overlap_save(X, H, L):
    M = len(H)  
    N = L+M-1 
    H_padded = np.pad(H, (0, N - len(H)), 'constant')
    output_signal = []
    X_padded = np.pad(X, (M - 1, 0), 'constant')
    for i in range(0, len(X), L):
        segment = X_padded[i:i + N]
        convolved = circular_convolution(segment, H_padded)
        output_signal.extend(convolved[M - 1:])
    return output_signal
X =[1,2,3,1,2,3,1,2,3,1,2,3]
H =[1,-1,1]
L =4 
final_output = overlap_save(X, H, L)
print("Final Output:", final_output)