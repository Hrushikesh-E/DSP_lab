import numpy as np
import matplotlib.pyplot as plt
with open('quantized_signal.bin', 'rb') as f:
    q_signal = np.frombuffer(f.read(), dtype=np.uint8)
q_levels = 16
dq_signal = (q_signal / (q_levels - 1)) * 2 - 1
no_samples = len(dq_signal)
srate = 100 
duration = no_samples / srate
t = np.linspace(0, duration, no_samples)
plt.figure(figsize=(10, 4))
plt.plot(t, dq_signal, label='Dequantized Signal')
plt.title('Dequantized Signal from 4-bit Quantization')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()