# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 10:20:45 2024

@author: 91959
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

start_time = time.time()

omega = 1.00
An = np.linspace(0.01,0.5,30)
#A = 3
sigma = 0.25
vmin = []
pt = []

def V(x):
    return 0.5*omega*omega*x*x + A*np.exp(-(x**2)/(2*sigma**2))

ngrid = 2048
xmax=10.0
xmin=-10.0
qm = []

dx= (xmax-xmin)/ngrid
H=np.zeros((ngrid,ngrid))
pot = np.zeros(ngrid)
onbydx2=1.0/(dx*dx)

for j in range(30): 
    A = An[j]
    
    for i in range(ngrid):

        if i!=0 and i!=ngrid-1:
            H[i-1][i]=-0.5*onbydx2
            H[i+1][i]=-0.5*onbydx2
        elif i==0:
                H[i+1][i]=-0.5*onbydx2
        elif i==ngrid-1:
                H[i-1][i]=-0.5*onbydx2
    
        xval=xmin+i*dx
        pot[i] = V(xval)
        H[i][i]=onbydx2 + V(xval)

    w,v=np.linalg.eigh(H)
        
    vmin.append(np.min(pot))    
    pt.append(0.5 + A*np.sqrt((2*sigma**2)/(1 + 2*sigma**2)))
    qm.append(w[0])
    
#print(np.min(pot))

dict = {'Perturbation Theory Energy':pt,'Potential':vmin,'Quantum Solver Energy':qm}
df = pd.DataFrame(dict)
     
df.to_csv('PT energy.csv')

end_time = time.time()

print(end_time - start_time)

#print(w[0])
#v2 = v.transpose()

#plt.plot(v2[0],'black')
#plt.plot(pot)
#plt.ylim(bottom = -1.0, top=2.0)


