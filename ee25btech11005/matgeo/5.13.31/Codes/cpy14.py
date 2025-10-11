import ctypes
import numpy as np

lib = ctypes.CDLL('./c14.so')

lib.check_k.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.check_k.restype = ctypes.c_int

def to_ctypes_array(matrix):
    flat = matrix.flatten()
    return (ctypes.c_double * len(flat))(*flat)

A = np.array([[2, 0, 0],
              [0, 2, 0],
              [0, 0, 3]], dtype=np.double)  # symmetric

B = np.array([[0, 1, 0],
              [-1, 0, 0],
              [0, 0, 0]], dtype=np.double)  # skew-symmetric

A_ct = to_ctypes_array(A)
B_ct = to_ctypes_array(B)

res = lib.check_k(A_ct, B_ct)

if res == 1:
    print("All odd k")
elif res == 2:
    print("All even k")
else:
    print("None")

