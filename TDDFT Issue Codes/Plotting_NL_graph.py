# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:05:16 2024

@author: 91959
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

vo = []
eig = []
        
with open('NL_Eigenvalues.csv', 'r') as csvfile:
    lines = csv.reader(csvfile,delimiter=',')
    next(lines)
    for row in lines:
        vo.append(float(row[2]))
        eig.append(float(row[1]))
        
plt.plot(vo,eig)
plt.xlabel('v values')
plt.ylabel('Eigenvalues')
plt.title('variation of eigenvalues with v')
        



