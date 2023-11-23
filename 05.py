#   Computational Neuroscience, Sheet 04 - Team: Kurzschluss
#   4-2a)

import numpy as np

import matplotlib.pyplot as plt


M = np.array([[3, 1], [1, 3]])
data_points = np.random.multivariate_normal([0, 0], M, 500)

var_x = 3
var_y = 3

p_45 = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
p_minus_45 = np.array([1/np.sqrt(2), -1/np.sqrt(2)])

var_z_45 = 3 + 2 * np.cos(np.radians(45)) * np.sin(np.radians(45))
var_z_minus_45 = 3 + 2 * np.cos(np.radians(-45)) * np.sin(np.radians(-45))


plt.scatter(data_points[:, 0], data_points[:, 1], s = 10, color = "black", label='data-points')

plt.axvline(var_x, color = "r", label='var(x)')
plt.axhline(var_y, color = "g", label='var(y)')
plt.axvline(var_z_45, color = "b", label='var(z_45)')
plt.axhline(var_z_minus_45, color = "orange", label='var(z_-45)')

plt.quiver(0, 0, p_45[0], p_45[1], color = "brown", angles='xy', scale_units='xy', scale=1, label='(1/√2, 1/√2)')
plt.quiver(0, 0, p_minus_45[0], p_minus_45[1], color = "grey", angles='xy', scale_units='xy', scale=1, label='(1/√2, -1/√2)')

plt.legend()
plt.title('scatter-plot with vars and the projection vectors')
plt.show()
