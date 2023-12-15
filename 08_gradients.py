# Comp Neuro Sheet 8
#   Team Kurzschluss2000

import numpy as np
import matplotlib.pyplot as plt

def k(x, y):
    return 1 / (x**2 + y**2 + 1)

def k_x(x, y):
    return (-2 * x) / (x**2 + y**2 + 1)**2

def k_y(x, y):
    return (-2 * y) / (x**2 + y**2 + 1)**2

xi_values = [-1, 0, 1, 2]
yj_values = [-1, 0, 1]

vectors = [((xi, yj), k_x(xi, yj), k_y(xi, yj)) for xi in xi_values for yj in yj_values]
print(vectors)

#b)
plt.figure(figsize=(8, 8))
for xi in xi_values:
    for yj in yj_values:
        plt.quiver(xi, yj, k_x(xi, yj), k_y(xi, yj),color='r', angles='xy', scale_units='xy')

def contour(radius):
    phi = np.linspace(0, 2*np.pi, 200)
    r = radius
    x = r*np.cos(phi)
    y = r*np.sin(phi)
    plt.plot(x,y)

contour(1)
contour(np.sqrt(1/2))

plt.xlabel('k_x')
plt.ylabel('k_y')
plt.grid()
plt.show()
