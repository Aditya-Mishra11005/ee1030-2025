import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./c16.so')
lib.quadratic_roots.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.quadratic_roots.restype = None
lib.evaluate_quadratic.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
lib.evaluate_quadratic.restype = ctypes.c_double

a, b, c = 2.0, 1.0, -4.0
x1 = ctypes.c_double()
x2 = ctypes.c_double()
lib.quadratic_roots(a, b, c, ctypes.byref(x1), ctypes.byref(x2))

x_vals = np.linspace(-3, 3, 400)
y_vals = np.array([lib.evaluate_quadratic(a, b, c, xi) for xi in x_vals])

plt.plot(x_vals, y_vals, 'b', label=r'$2x^2 + x - 4$')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
for root in [x1.value, x2.value]:
    plt.plot(root, 0, 'ro')
    plt.text(root + 0.05, 0.5, f'{root:.3f}', color='red', fontsize=10)

plt.title('Graphical Representation of $2x^2 + x - 4 = 0$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

