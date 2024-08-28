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

num_frames = 1000

with open('density_over_time.csv', 'r') as file1, open('density_values.csv', 'r') as file2:
    reader1 = csv.reader(file1, delimiter=',')
    reader2 = csv.reader(file2, delimiter=',')
    
  
    next(reader1)
    next(reader2)
    
    for row1, row2 in zip(reader1, reader2):
        density_direct.append([float(value) for value in row1[1:num_frames+1]])
        density_coeff.append([float(value) for value in row2[1:num_frames+1]])
    
   
    for i in range(num_frames):
        diff.append(np.abs(np.array(density_direct[i]) - np.array(density_coeff[i])))


x = np.linspace(-10, 10, len(diff[0]))  
t1 = np.linspace(0, 10, num_frames)  
fig, ax = plt.subplots()
base, = ax.plot(x, np.zeros_like(x))
ax.set_xlim(-10, 10)
ax.set_ylim(0, np.max(diff)) 
ax.set_xlabel('x-values')
ax.set_ylabel('Difference |Δψ(x)|²')


def update(frame):
    t = t1[frame]
    base.set_ydata(diff[frame])
    ax.set_title(f'Time = {t:.2f}')  
    return base,

anim = FuncAnimation(fig, update, frames=num_frames, blit=True)

anim.save('density_difference.gif', fps=30)
plt.show()

