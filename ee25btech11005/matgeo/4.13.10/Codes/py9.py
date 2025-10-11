import numpy as np
import matplotlib.pyplot as plt

A = np.array([-1, -7])
B = np.array([5, 1])
C = np.array([1, 10])

D = A - B
E = C - B

eD = D / np.linalg.norm(D)
eE = E / np.linalg.norm(E)

L = eD + eE

plt.plot([A[0], B[0]], [A[1], B[1]], 'k-')
plt.plot([B[0], C[0]], [B[1], C[1]], 'k-')
plt.plot([C[0], A[0]], [C[1], A[1]], 'k-')

plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='blue')

# Label the points
plt.text(A[0], A[1], 'A', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(B[0], B[1], 'B', fontsize=12, verticalalignment='bottom', horizontalalignment='left')
plt.text(C[0], C[1], 'C', fontsize=12, verticalalignment='top', horizontalalignment='left')

lambdas = np.linspace(-5, 5, 100)
bisector_points = B.reshape(2,1) + L.reshape(2,1) * lambdas

plt.plot(bisector_points[0,:], bisector_points[1,:], 'r-')

plt.gca().set_aspect('equal')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triangle and Angle Bisector of angle ∠ABC')
plt.grid(True)
plt.show()

