import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
z = sp.symbols('z', complex=True)
n = sp.symbols('n', integer=True)

def compute_z_transform(sequence, n_var, L):
    Z = sp.summation(sequence * z**(-n_var), (n_var, 0, L))
    return sp.simplify(Z)  # Simplify the result for a cleaner output
def plot_zeros_poles(zeros,poles):
    zeros = np.array([complex(zero) for zero in zeros], dtype=np.complex128)
    poles = np.array([complex(pole) for pole in poles], dtype=np.complex128)

    plt.figure(figsize=(6, 6))
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)

    plt.scatter(zeros.real, zeros.imag, s=100, c='b', marker='o', label='Zeros')
    
    plt.scatter(poles.real, poles.imag, s=100, c='r', marker='x', label='Poles')
    
    unit_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--')
    plt.gca().add_artist(unit_circle)

    plt.title('Zeros and Poles in the Z-Plane')
    plt.xlabel('Real Part')
    plt.ylabel('Imaginary Part')
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    plt.show()
    

L = sp.oo # infinity
sequence = 1  

z_transform = compute_z_transform(sequence, n, L)
print("Z-transform:", z_transform)
numerator, denominator = z_transform.args[0][0].as_numer_denom()
print('Numerator: ',numerator,' Denominator: ', denominator)


numerator = z**3 + 4*z + 17  #  z^2 + 2z + 1
denominator = z-1         #  z - 1

H_z = numerator / denominator
print("H(z):", H_z)

poles = sp.solve(denominator, z)
print("Poles of the system:", poles)

zeros = sp.solve(numerator, z)
print("Zeros of the system:", zeros)

plot_zeros_poles(zeros,poles)



