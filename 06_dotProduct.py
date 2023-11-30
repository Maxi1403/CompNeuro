# Comp Neuro Sheet 6.2a
#   Team Kurzschluss2000
import numpy as np
import matplotlib.pyplot as plt

def calculate_vectors(d_values):
    vectors = []
    for d in d_values:
        y = d - 2 * np.arange(-2, 2, .5)  # adapt precision
        vectors.extend(list(zip(np.arange(-5, 5, 1), y)))
    return vectors

# adapt precision here
d_values = np.arange(-5, 5, 0.1)
vectors = calculate_vectors(d_values)

for vector in vectors:
    plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=.5, color='b', linewidth=0.5)

closest_vector = min(vectors, key=lambda v: np.linalg.norm(v))

plt.quiver(0, 0, closest_vector[0], closest_vector[1], angles='xy', color='r', scale=.5, linewidth=.5, label=f'closest to coordinate origin {closest_vector}')

plt.xlabel('x')
plt.ylabel('y')

max_x = max([abs(v[0]) for v in vectors + [closest_vector]])
max_y = max([abs(v[1]) for v in vectors + [closest_vector]])

plt.xlim(-max_x, max_x)
plt.ylim(-max_y, max_y)

plt.legend()
plt.show()

