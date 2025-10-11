import numpy as np
import ctypes
import matplotlib.pyplot as plt

# Load compiled C library
lib = ctypes.CDLL("./c14.so")

# Define function signatures (tell Python what argument types to expect)
lib.inner_radius.argtypes = [ctypes.c_double, ctypes.c_double]
lib.outer_radius.argtypes = [ctypes.c_double, ctypes.c_double]
lib.circle_points.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_double,
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"),
    ctypes.c_int
]

# Wraps the C functions
def circle_points(center, radius, n=500):
    x = np.zeros(n, dtype=np.float64)
    y = np.zeros(n, dtype=np.float64)
    lib.circle_points(center[0], center[1], radius, x, y, n)
    return x, y

def locus_bounds(R, r):
    r_in = lib.inner_radius(R, r)
    r_out = lib.outer_radius(R, r)
    return r_in, r_out

def plot_locus(R, r):
    r_in, r_out = locus_bounds(R, r)

    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_aspect('equal')

    # Circles
    ax.plot(*circle_points((0,0), r_in), color='blue', linewidth=1.5)
    ax.plot(*circle_points((0,0), r_out), color='blue', linewidth=1.5)
    ax.plot(*circle_points((0,0), R), color='gray', linewidth=1.2)

    # Important points
    ax.plot(0,0,'ko'); ax.text(0.2,0.3,'O(0,0)',fontsize=9)
    ax.plot([r_in, r_out], [0,0], 'bo')
    ax.text(r_in+0.1,0.3,f'T₁({r_in:.1f},0)',color='blue',fontsize=9)
    ax.text(r_out+0.1,0.3,f'T₂({r_out:.1f},0)',color='blue',fontsize=9)

    # Fill annulus
    xo, yo = circle_points((0,0), r_out)
    xi, yi = circle_points((0,0), r_in)
    ax.fill(np.concatenate([xo, xi[::-1]]),
            np.concatenate([yo, yi[::-1]]),
            color='lightblue', alpha=0.2)

    ax.set_xlim(-(R+r+1), R+r+1)
    ax.set_ylim(-(R+r+1), R+r+1)
    ax.set_title(f'Locus: {r_in**2:.0f} ≤ x² + y² ≤ {r_out**2:.0f}')
    ax.grid(True, linestyle='--', linewidth=0.5)
    plt.show()

if __name__ == "__main__":
    R, r = 5.0, 3.0
    plot_locus(R, r)
