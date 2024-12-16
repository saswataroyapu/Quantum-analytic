# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:49:46 2024

@author: Nishanth S S
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import time

start_time = time.time()

an = np.linspace(0.01,0.5,30)
sig = 0.25
#A = 3
point = []
energy = []

def E(x, y):
    try:
        N = 1 / (1 + (x**2) * (math.pi / y)**(1/2) - 2 * x * (math.pi**(1/4)) * (2 / y)**(1/2))
        T = 1 / 4 - (x * y * (2**0.5) * (math.pi**0.25) / ((1 + y)**(3/2))) + (x**2) * (y * math.pi)**0.5 / 4
        V = (
            1 / 4
            + A * (2 * (sig**2) / (1 + 2 * sig**2))**0.5
            - x * (math.pi**0.25) / (2 * ((1 + y) / 2)**(3/2))
            - 2 * x * A * (math.pi**0.25) * (2 / (y + 1 / (sig**2) + 1))**0.5
            + (x**2) * (math.pi**0.5 / (4 * y**(3/2)) + A * (math.pi / (y + 1 / (2 * sig**2)))**0.5)
        )
        return (T + V) * N
    except (ZeroDivisionError) as e:
        return None  


x_vals = np.linspace(0.0,0.65, 300)
y_vals = np.linspace(2.89, 18, 300)
x, y = np.meshgrid(x_vals, y_vals)

for i in range(30):
    A = an[i]
    z = np.array([[E(x, y) for x in x_vals] for y in y_vals])
    energy.append(np.min(z))

fig = plt.figure()
ax = plt.axes(projection='3d')
vmin = np.min(z)

surf = ax.plot_surface(x, y, z, cmap='viridis')
ax.view_init(-140, 60)

ax.set_xlabel('C1')
ax.set_ylabel('C2')
ax.set_zlabel('Energy')
ax.set_title('Plot of Energy for different coefficient values')

plt.show()
#print(vmin)
#print(energy)

dict = {'Varitional Energy':energy}
df = pd.DataFrame(dict)
     
df.to_csv('VP energy.csv')

end_time = time.time()

execution_time = end_time - start_time

print(execution_time)













