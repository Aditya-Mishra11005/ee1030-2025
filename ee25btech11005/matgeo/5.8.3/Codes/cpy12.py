import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./c12.so')
solve_lines = lib.solve_lines
solve_lines.argtypes = [ctypes.POINTER(ctypes.c_double)]
solve_lines.restype = None

result_arr = (ctypes.c_double * 2)()
solve_lines(result_arr)
sol = [result_arr[0], result_arr[1]]

lambda_vals = np.linspace(-2, 10, 100)
x_vals = (50 - 7 * lambda_vals) / 5
y_vals = lambda_vals

plt.plot(x_vals, y_vals)
plt.scatter(sol[0], sol[1], color='red', s=40)
plt.scatter(x_vals[0], y_vals[0], color='blue', s=30)
plt.scatter(x_vals[-1], y_vals[-1], color='green', s=30)
plt.text(sol[0], sol[1], 'A', fontsize=14, color='black', ha='left', va='bottom')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line: 5x + 7y = 50')
plt.grid(True)
plt.show()

