import numpy as np
import matplotlib.pyplot as plt

def get_complex_location(magnitude, phase):
    return magnitude * np.exp(1j * phase)

num_zeros = int(input("Enter the number of zeros: "))
num_poles = int(input("Enter the number of poles: "))

zeros = []
poles = []

for i in range(num_zeros):
    print(f"\nEnter details for Zero {i+1}:")
    magnitude = float(input("  Magnitude (distance from origin): "))
    frequency = float(input("  Frequency (in radians): "))
    zero_location = get_complex_location(magnitude, frequency)
    zeros.append(zero_location)

for i in range(num_poles):
    print(f"\nEnter details for Pole {i+1}:")
    magnitude = float(input("  Magnitude (distance from origin): "))
    frequency = float(input("  Frequency (in radians): "))
    pole_location = get_complex_location(magnitude, frequency)
    poles.append(pole_location)

W = np.linspace(-np.pi, np.pi, 1000)

# Initialize H(w) to 1 (neutral multiplication value)
Hw = np.ones(len(W), dtype=complex)

for zero in zeros:
    Hw *= (1 - zero * np.exp(-1j * W))

for pole in poles:
    Hw /= (1 - pole * np.exp(-1j * W))

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(W, np.abs(Hw))
plt.title("Magnitude Response of H(w)")
plt.xlabel("Frequency (rad/sample)")
plt.ylabel("Magnitude")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(W, np.angle(Hw))
plt.title("Phase Response of H(w)")
plt.xlabel("Frequency (rad/sample)")
plt.ylabel("Phase (radians)")
plt.grid(True)

plt.tight_layout()
plt.show()
