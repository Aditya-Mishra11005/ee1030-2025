import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 5, 30)
y = np.linspace(0, 5, 30)
X, Y = np.meshgrid(x, y)

Z1 = 6 - X - Y       # Plane 1: x + y + z = 6
Z2 = (7 - X)/2       # Plane 2: x + 2z = 7
Z3 = 12 - 3*X - Y    # Plane 3: 3x + y + z = 12

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z1, alpha=0.5, color='skyblue', label='x + y + z = 6')
ax.plot_surface(X, Y, Z2, alpha=0.5, color='lightgreen', label='x + 2z = 7')
ax.plot_surface(X, Y, Z3, alpha=0.5, color='coral', label='3x + y + z = 12')

ax.scatter(3, 1, 2, color='red', s=100)
ax.text(3, 1, 2, '(3, 1, 2)', color='red')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Intersection of Three Planes')
plt.show()

