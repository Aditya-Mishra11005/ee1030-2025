import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x**2 + x - 4

x = np.linspace(-3, 3, 400)
y = f(x)

x1 = (-1 + np.sqrt(33)) / 4
x2 = (-1 - np.sqrt(33)) / 4
roots = [x1, x2]

plt.figure(figsize=(8,6))
plt.plot(x, y, label=r'$y = 2x^2 + x - 4$', color='blue')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

for r in roots:
    plt.plot(r, 0, 'ro')
    plt.text(r + 0.05, 0.5, f'{r:.3f}', color='red', fontsize=10)

plt.title('Graphical Representation of $2x^2 + x - 4 = 0$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

