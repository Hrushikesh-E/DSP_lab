import numpy as np

def circular_convolution(x, h):
    N = len(x)
    result = np.zeros(N)
    for n in range(N):
        for m in range(N):
            result[n] += x[m] * h[(n - m) % N]
    return result
def overlap_add(X, H, L):
    M = len(H)
    H_padded = np.pad(H, (0, L + M - 1 - len(H)), 'constant')
    results = []
    for i in range(0, len(X), L):
        segment = X[i:i + L]
        padded_segment = np.pad(segment, (0, L + M - 1 - len(segment)), 'constant')
        convolved = circular_convolution(padded_segment, H_padded)
        results.append(convolved)
    output_length = len(X) + len(H) - 1
    output_signal = np.zeros(output_length)
    for i, res in enumerate(results):
        overlap_size = M - 1
        output_signal[i * L:i * L + len(res)] += res
    return output_signal

X =[1,2,3,1,2,3,1,2,3,1,2,3]
H =[1,-1,1]
L =4

final_output = overlap_add(X, H, L)
print("Final Output:", final_output)