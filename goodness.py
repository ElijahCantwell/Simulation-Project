# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

v = np.linspace(-3, 3, 500)
alpha = 1
epsilon = 0.5

# Equilibrium MB distribution
f_eq = np.exp(-alpha * v**2)

# Non-equilibrium with linear drift
f_drift = f_eq * (1 + epsilon * v)

# Normalize
f_drift = f_drift / np.trapz(f_drift, v)

plt.plot(v, f_eq, label='Equilibrium')
plt.plot(v, f_drift, label='Non-equilibrium (drift)')
plt.xlabel('Velocity v')
plt.ylabel('f(v)')
plt.legend()
plt.grid()
plt.title('1D Non-Equilibrium Distribution (with Drift)')
plt.show()
