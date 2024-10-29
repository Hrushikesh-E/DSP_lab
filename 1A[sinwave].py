import numpy as np
from matplotlib import pyplot as plt
f = 200  
duration = 0.5   
srate = 8000 
t1 = np.arange(0, duration, 1/srate)
y1 = np.sin(2 * np.pi * f * t1)
plt.plot(t1, y1)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.show()
