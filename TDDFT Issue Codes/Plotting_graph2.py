# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:32:27 2024

@author: 91959
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

vo = []
eig = []

with open('Eigenvalues2.csv', 'r') as csvfile:
    lines = csv.reader(csvfile,delimiter=',')
    next(lines)
    for row in lines:
        vo.append(float(row[2]))
        eig.append(float(row[1]))
        
plt.plot(vo,eig)
plt.xlabel('v values')
plt.ylabel('Eigenvalue 1 - Eigenvalue 2')
plt.title('E1 - E2 vs v')