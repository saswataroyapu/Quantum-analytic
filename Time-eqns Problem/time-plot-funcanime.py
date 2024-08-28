# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 15:21:45 2024

@author: 91959
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import csv

c1 = 3/5 
c2 = 4/5
ngrid = 1024

E0 = 0.5
E1 = 1.5

x = np.linspace(-10, 10, ngrid)  
t1 = np.linspace(0, 10, 1000)   

def psi0(x):
    return (1 / (np.pi ** 0.25)) * np.exp(-(x ** 2) / 2)

def psi1(x):
    return (1 / (np.pi ** 0.25)) * (2 ** 0.5) * x * np.exp(-(x ** 2) / 2)

fig, ax = plt.subplots()
base, = ax.plot(x, np.zeros_like(x))
ax.set_xlim(-10, 10)
ax.set_ylim(0, 1)
ax.set_xlabel('x-values')
ax.set_ylabel('Density')


with open('density_values.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Time'] + list(x))  

    def update(frame):
        t = t1[frame]
        density_real = np.zeros_like(x)
        density_imag = np.zeros_like(x)

        for i in range(len(x)):
            p_conj = (np.conj(c1) * np.conj(psi0(x[i])) * np.exp(1j * E0 * t) +
                      np.conj(c2) * np.conj(psi1(x[i])) * np.exp(1j * E1 * t))
            p = (c1 * psi0(x[i]) * np.exp(-1j * E0 * t) +
                 c2 * psi1(x[i]) * np.exp(-1j * E1 * t))
            density_real[i] = (p_conj * p).real  
            density_imag[i] = (p_conj * p).imag

        base.set_ydata(density_real)
        ax.set_title(f'Time = {t:.2f}')

        csvwriter.writerow([t] + list(density_real))

        return base,

    
    anim = FuncAnimation(fig, update, frames=len(t1), blit=True)

    anim.save('d_animation.gif', fps=10)
    plt.show()
