# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 18:02:15 2024

@author: 91959
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import csv
from scipy.linalg import expm

# Constants
c1 = 3/5 
c2 = 4/5
omega = 1
xmax = 10.0
xmin = -10.0 
ngrid = 1024

# Grid and initial psi
x = np.linspace(xmin, xmax, ngrid)
psi = np.zeros(ngrid)

# Potential and Hamiltonian
def V(x):
    return 0.5 * omega * omega * x * x

dx = (xmax - xmin) / ngrid
H = np.zeros((ngrid, ngrid))
pot = np.zeros(ngrid)
onbydx2 = 1.0 / (dx * dx)

def psi0(x):
    return (1 / (np.pi ** 0.25)) * np.exp(-(x ** 2) / 2)

def psi1(x):
    return (1 / (np.pi ** 0.25)) * (2 ** 0.5) * x * np.exp(-(x ** 2) / 2)

# Initial state and Hamiltonian construction
for i in range(ngrid):
    if i != 0 and i != ngrid - 1:
        H[i-1][i] = -0.5 * onbydx2
        H[i+1][i] = -0.5 * onbydx2
    elif i == 0:
        H[i+1][i] = -0.5 * onbydx2
    elif i == ngrid - 1:
        H[i-1][i] = -0.5 * onbydx2

    psi[i] = c1 * psi0(x[i]) + c2 * psi1(x[i])
    pot[i] = V(x[i])
    H[i][i] = onbydx2 + V(x[i])

# Normalize initial psi
psi = psi / np.sqrt(np.sum(np.abs(np.conj(psi)*psi) * dx))

# Time evolution parameters
time = 0.0
dt = 0.01
tmax = 10
frames = int(tmax / dt)

factor = expm(-1j*H*dt)

# Set up the figure and axis
fig, ax = plt.subplots()
line, = ax.plot(x, np.zeros_like(x))
ax.set_xlim(xmin, xmax)
ax.set_ylim(0,np.max(np.abs(psi)**2))
ax.set_xlabel('x')
ax.set_ylabel('|ψ(x)|²')

# List to store density values for each time step
density_over_time = []

# Update function for animation
def update(frame):
    global psi, time
    psi = factor @ psi 
    psi = psi / np.sqrt(np.sum(np.abs(np.conj(psi)*psi) * dx))
    time += dt
    density = np.abs(np.conj(psi) * psi)  
    density_over_time.append(density.copy())  
    line.set_ydata(density)
    ax.set_title(f'Time = {time:.2f}')
    
    ax.relim()
    ax.autoscale_view()
    
    return line,

# Create animation
anim = FuncAnimation(fig, update, frames=frames, blit=True)

# Save as GIF
anim.save('wavefunction_evolution.gif', fps=30)

# Save density values to CSV
with open('density_over_time.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Time'] + list(x))  # Write header with time and x values
    for i, density_t in enumerate(density_over_time):
        time_step = i * dt
        writer.writerow([time_step] + list(density_t))  # Save density values

