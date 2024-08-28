# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:38:02 2024

@author: 91959
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

density_direct = []
density_coeff = []
diff = []

# Assuming the CSV files have at least 1003 columns (1 for time + 1002 for data)
for i in range(1000):
    with open('density_over_time.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        # Ensure that the number of columns in the CSV is sufficient
        density_direct.append([float(row[i+1]) for row in reader])

    with open('density_values.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        # Ensure that the number of columns in the CSV is sufficient
        density_coeff.append([float(row[i+3]) for row in reader])

    # Calculate the difference and store it
    diff.append(np.abs(np.array(density_direct[i]) - np.array(density_coeff[i])))

# Set up the figure and axis for animation
x = np.linspace(-10, 10, len(diff[0]))  # x-values based on the length of diff
t1 = np.linspace(0, 10, 1000)  # Assuming 1000 time steps
fig, ax = plt.subplots()
base, = ax.plot(x, np.zeros_like(x))
ax.set_xlim(-10, 10)
ax.set_ylim(0, np.max(diff))  # Set the y-axis limit based on the maximum difference
ax.set_xlabel('x-values')
ax.set_ylabel('Difference |Δψ(x)|²')

# Update function for the animation
def update(frame):
    t = t1[frame]
    base.set_ydata(diff[frame])
    ax.set_title(f'Time = {t:.2f}')  # Display the current time in the title
    return base,

# Create the animation
anim = FuncAnimation(fig, update, frames=len(diff), blit=True)

# Save the animation as a GIF
anim.save('density_difference.gif', fps=10)
plt.show()



