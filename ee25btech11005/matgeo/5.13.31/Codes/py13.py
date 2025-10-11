import numpy as np

i = np.array([1, 0, 0])
j = np.array([0, 1, 0])
k = np.array([0, 0, 1])

a = i - j
b = j - k
c = k - i

b_cross_c = np.cross(b, c)
A = np.vstack((a, b_cross_c))

# Find a vector orthogonal to both a and b_cross_c
d = np.cross(a, b_cross_c)
d =d/np.linalg.norm(d)

print("d:", d)

