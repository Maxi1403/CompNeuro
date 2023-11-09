#   Computational Neuroscience, Sheet 03 - Team: Kurzschluss2000
#   Task f)

import numpy as np
import matplotlib.pyplot as plt

def spiking_time(lmbda):
    if lmbda <= 1:
        return
    else:
        return -np.log(1 - 1/lmbda)

def transfer_function(lmbda):
    return 1 / spiking_time(lmbda)

# lambda range
lambda_values = np.linspace(1.01, 10, 50)

# Calculate spiking times and transfer functions for each lambda
ts_lambda = [spiking_time(lmbda) for lmbda in lambda_values]
trans = [transfer_function(lmbda) for lmbda in lambda_values]

# Plotting
plt.figure(figsize=(12, 6))

# Plot spiking times
plt.subplot(121)
plt.plot(lambda_values, ts_lambda, label='ts(λ)', marker = ".")
plt.xlabel('λ')
plt.ylabel('Spiking Time')
plt.legend()

# Plot transfer functions
plt.subplot(122)
plt.plot(lambda_values, trans, label='1/ts(λ)')
plt.xlabel('λ')
plt.ylabel('Transfer Function')
plt.legend()

plt.tight_layout()
plt.show()
