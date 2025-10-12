import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load shared library
lib = ctypes.CDLL("./c16.so")
lib.find_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                            ctypes.c_double, ctypes.c_double,
                            ctypes.POINTER(ctypes.c_double)]

V11, V22, f = 3.0, -1.0, -8.0
n1, n2 = 1.0, 3.0

out = (ctypes.c_double * 4)()
lib.find_points(V11, V22, f, n1, n2, out)

points = np.array([out[0], out[1], out[2], out[3]]).reshape(2, 2)

x = np.linspace(-10, 10, 1000)
y_sq = 3*x**2 - 8
mask_left = x <= -np.sqrt(8/3)
mask_right = x >= np.sqrt(8/3)

x_left, x_right = x[mask_left], x[mask_right]
y_left_pos, y_left_neg = np.sqrt(3*x_left**2 - 8), -np.sqrt(3*x_left**2 - 8)
y_right_pos, y_right_neg = np.sqrt(3*x_right**2 - 8), -np.sqrt(3*x_right**2 - 8)

k = 26*np.sqrt(3)
y1 = (-x + k)/3
y2 = (-x - k)/3

plt.figure()
plt.plot(x_left, y_left_pos, 'b')
plt.plot(x_left, y_left_neg, 'b')
plt.plot(x_right, y_right_pos, 'b', label='Hyperbola')
plt.plot(x_right, y_right_neg, 'b')
plt.plot(x, y1, 'r--', label='Normals')
plt.plot(x, y2, 'r--')
plt.scatter(points[:,0], points[:,1], color='green', zorder=5, label='Points of contact')

plt.xlim(-10, 10)
plt.ylim(-30, 30)
plt.gca().set_aspect('equal')
plt.legend()
plt.grid(True)
plt.title('Hyperbola with Normals and Contact Points')
plt.show()

