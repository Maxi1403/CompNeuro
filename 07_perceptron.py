# Comp Neuro Sheet 7.2
#   Team Kurzschluss2000

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

r = np.array([1, 1, 1])
s = np.array([1, 1, 2])
weight_vector = np.array([-2, 1, 1])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(0, 0, 0, r[0], r[1], r[2], color='red', label='r = [1, 1, 1]')
ax.quiver(0, 0, 0, s[0], s[1], s[2], color='blue', label='s = [1, 1, 2]')
ax.quiver(0, 0, 0, weight_vector[0], weight_vector[1], weight_vector[2], color='green', label='weight vector = [-2, 1, 1]')

def calculate_decision_boundary(weight_vector):
    perpendicular_vector = np.array([1, 1, -weight_vector[1]/weight_vector[2]])
    decision_boundary_vector = np.cross(weight_vector, perpendicular_vector)

    return decision_boundary_vector

decision_boundary = calculate_decision_boundary(weight_vector)
ax.quiver(0, 0, 0, decision_boundary[0], decision_boundary[1], decision_boundary[2], color='purple', label='decision_boundary')

ax.set_xlim(-3, 3)
ax.set_ylim(0, 3)
ax.set_zlim(0, 3)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()

plt.show()
