# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Compute entropy using S = -k_B * multiplicity

k_B = 1.0  # Boltzmann constant (normalized)

entropy = -k_B
    
# Parameters
n_particles = 1000  # Number of particles
box_size = 10       # Box size
grid_size = 20      # Grid for entropy estimation
num_iterations = 100  # Monte Carlo iterations