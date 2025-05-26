# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Creating the space of values for velocity to work with
v = np.linspace(-3, 3, 500)
alpha = 1
epsilon = 0.5

# Here I set up the Maxwellian distribution which is the equilibrium distribution
f_eq = np.exp(-alpha * v**2)

# Here I create the non-equilibrium distribution by including the approximation of epsilon v.
f_drift = f_eq * (1 + epsilon*v)

# This here is normalising the non-equilibrium approximation
f_drift = f_drift / np.trapz(f_drift, v)

plt.plot(v, f_eq, label='Equilibrium')
plt.plot(v, f_drift, label='Non-equilibrium')
plt.xlabel('Velocity v')
plt.ylabel('f(v)')
plt.legend()
plt.grid()
plt.title('1D Non-Equilibrium Distribution')
plt.show()
