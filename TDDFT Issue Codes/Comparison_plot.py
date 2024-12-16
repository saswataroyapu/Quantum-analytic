# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 16:06:45 2024

@author: 91959
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

vo = []
eig = []

vos = []
eigs = []

with open('Eigenvalues.csv', 'r') as csvfile:
    lines = csv.reader(csvfile,delimiter=',')
    next(lines)
    for row in lines:
        vos.append(float(row[2]))
        eigs.append(float(row[1]))
        
with open('NL_Eigenvalues.csv', 'r') as csvfile:
    lines = csv.reader(csvfile,delimiter=',')
    next(lines)
    for row in lines:
        vo.append(float(row[2]))
        eig.append(float(row[1]))
        
plt.plot(vo,eig, label = 'Non-linear plot')
plt.plot(vos,eigs, label = 'Linear plot')
plt.legend()
plt.xlabel('v values')
plt.ylabel('Eigenvalues')
plt.title('variation of eigenvalues with v')
        