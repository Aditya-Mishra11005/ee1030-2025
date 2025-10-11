# locus_functional_clean.py
# Aditya Mishra — EE25BTECH11005

import numpy as np
import matplotlib.pyplot as plt

def circle_points(center, radius, n=500):
    """Returns x, y points for a circle."""
    theta = np.linspace(0, 2*np.pi, n)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    return x, y

def locus_bounds(R, r):
    """Returns inner and outer radius of the locus."""
    return R - r, R + r

def plot_locus(R, r):
    """Plots the locus region for circles of radius r with centers on circle radius R."""
    r_in, r_out = locus_bounds(R, r)
    
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_aspect('equal')

    # Boundary circles
    ax.plot(*circle_points((0,0), r_in), color='blue', linewidth=1.5)
    ax.plot(*circle_points((0,0), r_out), color='blue', linewidth=1.5)

    # Circle of centers
    ax.plot(*circle_points((0,0), R), color='gray', linewidth=1.2)

    # Important points
    ax.plot(0, 0, 'ko'); ax.text(0.2, 0.3, 'O(0,0)', fontsize=9)
    ax.plot([r_in, r_out], [0, 0], 'bo')
    ax.text(r_in+0.1, 0.3, f'T₁({r_in},0)', color='blue', fontsize=9)
    ax.text(r_out+0.1, 0.3, f'T₂({r_out},0)', color='blue', fontsize=9)

    # Shaded annulus
    xo, yo = circle_points((0,0), r_out)
    xi, yi = circle_points((0,0), r_in)
    x_ring = np.concatenate([xo, xi[::-1]])
    y_ring = np.concatenate([yo, yi[::-1]])
    ax.fill(x_ring, y_ring, color='lightblue', alpha=0.2)

    ax.set_xlim(-(R+r+1), R+r+1)
    ax.set_ylim(-(R+r+1), R+r+1)
    ax.set_title(f'Locus: {(r_in)**2:.0f} ≤ x² + y² ≤ {(r_out)**2:.0f}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True, linestyle='--', linewidth=0.5)
    plt.show()

if __name__ == "__main__":
    R = 5   # circle of centers radius
    r = 3   # each small circle radius
    plot_locus(R, r)

