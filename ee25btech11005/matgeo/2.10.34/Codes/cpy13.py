import ctypes
import numpy as np

lib = ctypes.CDLL('./c13.so')
compute_d = lib.compute_d
compute_d.argtypes = [ctypes.POINTER(ctypes.c_double)]

d = np.zeros(3, dtype=np.float64)
compute_d(d.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))

print(d)

