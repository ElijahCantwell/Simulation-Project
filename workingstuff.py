# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# I set all my values here arbitrarily as I just want the shape of this curve not actual discrete values
T = 1
m = 1
t = np.linspace(0, 10, 200)
epsilon0 = 0.1
lambda_decay = 1
kB = 1
a = (kB*T)/m


epsilon_t = epsilon0 * np.exp(-lambda_decay * t)
S_eq = 10  # I chose a random equilibrium entropy to work with
S_t = S_eq - 0.5 * kB * a * epsilon_t**2  # entropy formula derived in video


#creating my plot
plt.plot(t, S_t, label='S(t)')
plt.axhline(S_eq, color='gray', linestyle='--', label='S_eq')
plt.xlabel('Time t')
plt.ylabel('Entropy S(t)')
plt.title('Entropy Increasing According to H-Theorem')
plt.legend()
plt.grid()
plt.show()
