import numpy as np
import ctypes
import matplotlib.pyplot as plt

lib = ctypes.CDLL("./c9.so")

lib.angle_bisector.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double)
]

A = np.array([-1.0, -7.0], dtype=np.float64)
B = np.array([5.0, 1.0], dtype=np.float64)
C = np.array([1.0, 10.0], dtype=np.float64)
L = np.zeros(2, dtype=np.float64)

lib.angle_bisector(
    A.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    B.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    C.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    L.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
)

lambdas = np.linspace(-5, 5, 100)
bisector_pts = B.reshape(2,1) + L.reshape(2,1) * lambdas

# Triangle vertices
tri_x = [A[0], B[0], C[0], A[0]]
tri_y = [A[1], B[1], C[1], A[1]]

plt.plot(tri_x, tri_y, 'k-')
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='blue')
plt.plot(bisector_pts[0, :], bisector_pts[1, :], 'r-')
plt.gca().set_aspect('equal')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triangle and Angle Bisector of ∠ABC')
plt.grid(True)
plt.show()

