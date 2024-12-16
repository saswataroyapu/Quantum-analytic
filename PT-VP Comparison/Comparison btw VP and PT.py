# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:58:03 2024

@author: 91959
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

A = np.linspace(0.01,0.5,30)

vp = []

pt = []

pot = []

qm = []

with open('VP energy.csv', 'r') as csvfile:
    lines = csv.reader(csvfile,delimiter=',')
    next(lines)
    for row in lines:
        vp.append(float(row[1]))
     
with open('PT energy.csv', 'r') as csvfile:
    lines = csv.reader(csvfile,delimiter=',')
    next(lines)
    for row in lines:
        pt.append(float(row[1]))
        pot.append(float(row[2]))
        qm.append(float(row[3]))
    
vp = np.array(vp)
pot = np.array(pot)
qm = np.array(qm)

actualpt = pt + pot

PT = qm - pt

VP = qm - vp

print(pt)
print()
print(vp)
print()
print(qm)

plt.plot(A,PT,label='Perturbation Theory')
plt.plot(A,VP,'g',label='Variational Principle')
plt.xlabel('A')
plt.ylabel('Deviation from quantum solver value')
plt.title('Comparison btw Perturbation Theory and Variational Principle')
plt.legend(loc='best')

end_time = time.time()

print(end_time - start_time)

#plt.xlim(0.005,0.065)