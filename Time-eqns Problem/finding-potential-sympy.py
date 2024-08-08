# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:57:33 2024

@author: 91959
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x') 
x1 = np.linspace(-10,10.0,101)
V0 = []
V1 = [] 

# Ground state wavefunction
f0 = (1/((sp.pi)**(1/4)))*(sp.exp(-(x**2)/2))

fd0 = sp.diff(f0,x)
fdd0 = sp.diff(fd0,x)

# First excited state wavefunction
f1 = (1/((sp.pi)**(1/4)))*((2)**(1/2))*x*(sp.exp(-(x**2)/2))

fd1 = sp.diff(f1,x)
fdd1 = sp.diff(fd1,x)


for i in range(len(x1)):
    
    x_val = float(x1[i])
    if f0.subs(x, x_val) > 10^-5:  
       V0.append(0.5 + (fdd0.subs(x, x_val) / (2 * f0.subs(x, x_val))))
    else:
        V0.append(np.nan)  

    if f1.subs(x, x_val) > 10^-5:  
        V1.append(1.5 + (fdd1.subs(x, x_val) / (2 * f1.subs(x, x_val))))
    else:
        V1.append(np.nan)  
    
plt.plot(x1,V0)
plt.plot(x1,V1,'g')