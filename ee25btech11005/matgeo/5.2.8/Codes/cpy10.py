import numpy as np
from ctypes import cdll, c_double, POINTER, c_int
import matplotlib.pyplot as plt

lib = cdll.LoadLibrary('./c10.so')

lib.row_op.argtypes = [POINTER(c_double), c_int, c_int, c_double]
lib.solve_vars.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]
lib.row_op.restype = None
lib.solve_vars.restype = None

mat = (c_double * 6)(5, -3, 11, -10, 6, -22)

lib.row_op(mat, 1, 0, 2)

x = c_double()
y = c_double()

lib.solve_vars(mat, x, y)

lambd = np.linspace(-2, 2, 100)
x_vals = x.value + (3/5) * lambd
y_vals = lambd

plt.plot(x_vals, y_vals)
plt.scatter(x.value, y.value, color='red')
plt.title("Parametric solution")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

