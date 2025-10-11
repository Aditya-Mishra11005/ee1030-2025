import numpy as np
import matplotlib.pyplot as plt

lambda_vals = np.linspace(-2, 2, 100)
x = (11/5) + (3/5)*lambda_vals
y = lambda_vals

plt.plot(x, y, label='Solution Line')
plt.scatter(11/5, 0, color='red', s=50, label='Point (11/5, 0)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of the system: x=(11+3λ)/5, y=λ')
plt.legend()
plt.grid(True)
plt.show()

