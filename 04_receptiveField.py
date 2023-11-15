#   Computational Neuroscience, Sheet 04 - Team: Kurzschluss
#   4-2a)

import numpy as np
import matplotlib.pyplot as plt

def excitatory(x):
    return 2 * np.exp(-1/2 * np.square(x))

def inhibitory(x):
    return -np.exp(-1/2 * np.square(x)/np.square(2))

def sum(x):
    return excitatory(x) + inhibitory(x)

x_range = np.linspace(-10, 10, 1000)

excitatory_values = [excitatory(x) for x in x_range]
inhibitory_values = [inhibitory(x) for x in x_range]
sum_values = [sum(x) for x in x_range]

plt.figure(figsize=(10, 6))

plt.plot(x_range, sum_values, label='Sum', color = "green")
plt.plot(x_range, excitatory_values, label='excitatory gaussian', linestyle='dotted', color = "blue")
plt.plot(x_range, inhibitory_values, label='inhibitory gaussian', linestyle='dashed', color = "red")

plt.title("Gaussians (excitatory and inhibitory mechanisms) and their sum")
plt.legend()
plt.xlabel("x")
plt.ylabel("φ(x)")
plt.grid(True)
plt.show()