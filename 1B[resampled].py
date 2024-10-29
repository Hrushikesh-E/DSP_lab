import numpy as np
from matplotlib import pyplot as plt

f = 200  
duration = 0.5   
srate = 8000
rrate = 1000  
t1 = np.arange(0, duration, 1/srate)
t2 = np.arange(0, duration, 1/rrate)
y1 = np.sin(2 * np.pi * f * t1)
y2 = np.sin(2 * np.pi * f * t2)
plt.plot(t1, y1)
plt.title('Sampled Sine wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()
plt.plot(t2, y2)
plt.title('ReSampled Sine wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()





