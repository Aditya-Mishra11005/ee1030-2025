import numpy as np

a = np.array([1, -1, 0])
b = np.array([0, 1, -1])
c = np.array([-1, 0, 1])

aTc = np.dot(a, c)
aTb = np.dot(a, b)
lam = -aTc / aTb

d = c + lam * b
d_norm = np.linalg.norm(d)
d_unit = d / d_norm

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

