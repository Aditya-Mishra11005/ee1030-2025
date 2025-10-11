import ctypes
import numpy as np

lib = ctypes.CDLL('./c4.so')
find_unit_vector = lib.find_unit_vector
find_unit_vector.argtypes = [ctypes.POINTER(ctypes.c_double)]
find_unit_vector.restype = None

result_arr = (ctypes.c_double * 3)()
find_unit_vector(result_arr)
d_unit = np.array([result_arr[0], result_arr[1], result_arr[2]])

opts = [
    np.array([1, 1, -2]) / np.sqrt(6),
    np.array([1, 1, 1]) / np.sqrt(3),
    np.array([1, 1, -1]) / np.sqrt(3),
    np.array([1, 1, -1]) / np.linalg.norm([1, 1, -1])
]

def match_option(vec, options):
    for idx, opt in enumerate(options):
        if np.allclose(vec, opt) or np.allclose(vec, -opt):
            return idx + 1
    return -1

idx = match_option(d_unit, opts)

print("Unit vector d is:")
print(f"d = {d_unit[0]:.4f}i + {d_unit[1]:.4f}j + {d_unit[2]:.4f}k")
print(f"Option: {idx} (matches option {'abcd'[idx-1]})")

