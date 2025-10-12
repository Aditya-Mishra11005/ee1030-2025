import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y_sq = 3*x**2 - 8

# Left branch
mask_left = x <= -np.sqrt(8/3)
x_left = x[mask_left]
y_left_pos = np.sqrt(3*x_left**2 - 8)
y_left_neg = -np.sqrt(3*x_left**2 - 8)

# Right branch
mask_right = x >= np.sqrt(8/3)
x_right = x[mask_right]
y_right_pos = np.sqrt(3*x_right**2 - 8)
y_right_neg = -np.sqrt(3*x_right**2 - 8)

k = 26*np.sqrt(3)
y1 = (-x + k)/3
y2 = (-x - k)/3

plt.figure()
# Hyperbola branches
plt.plot(x_left, y_left_pos, 'b')
plt.plot(x_left, y_left_neg, 'b')
plt.plot(x_right, y_right_pos, 'b', label='Hyperbola')
plt.plot(x_right, y_right_neg, 'b')

# Normals
plt.plot(x, y1, 'r--', label='Normals')
plt.plot(x, y2, 'r--')

plt.xlim(-10, 10)
plt.ylim(-30, 30)
plt.gca().set_aspect('equal')
plt.legend()
plt.grid(True)
plt.title('Hyperbola with Normals')
plt.show()

