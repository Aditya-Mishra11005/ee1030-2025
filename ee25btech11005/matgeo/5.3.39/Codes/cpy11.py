import numpy as np
import matplotlib.pyplot as plt
from ctypes import cdll, c_double, POINTER

lib = cdll.LoadLibrary('./c11.so')
solve_planes = lib.solve_planes
solve_planes.argtypes = [POINTER(c_double)]
solve_planes.restype = None

res = (c_double * 3)()
solve_planes(res)

x = np.linspace(0, 5, 40)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z1 = 6 - X - Y
Z2 = (7 - X) / 2
Z3 = 12 - 3*X - Y

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z1, alpha=0.5, color='skyblue')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='lightgreen')
ax.plot_surface(X, Y, Z3, alpha=0.5, color='salmon')
ax.scatter(res[0], res[1], res[2], color='red', s=60)
ax.text(res[0], res[1], res[2], f'({res[0]:.0f}, {res[1]:.0f}, {res[2]:.0f})', color='red', fontsize=12)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Intersection of three planes')
plt.tight_layout()
plt.show()

