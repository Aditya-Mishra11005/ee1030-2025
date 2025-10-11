import numpy as np

# Sample symmetric A and skew symm B that commute
A = np.array([[2, 0, 0],
              [0, 2, 0],
              [0, 0, 3]])  # symmetric

B = np.array([[0, 1, 0],
              [-1, 0, 0],
              [0, 0, 0]])  # skew-symmetric

AB = np.dot(A,B)
if np.allclose(AB.T, -AB):
    print("All odd k")
elif np.allclose(AB.T, AB):
    print("All even k")

else:
    print("None")

