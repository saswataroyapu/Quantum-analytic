# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2  9:58:10 2024

@author: 91959
"""

import numpy as np
from scipy.linalg import eig
import pandas as pd

vo = np.linspace(0.95,1,100)
eigval = []

for i in range(len(vo)):
    
    v = vo[i]
    
    A = np.array([
        [2,0,0,v],
        [0,3,v,0],
        [0,v,1,0],
        [v,0,0,2]
    ])
    
    B = np.array([
        [0,0,0,v],
        [0,0,v,0],
        [0,v,0,0],
        [v,0,0,0]
    ])
    
    C = np.block([
        [A, B],
        [B, A]
    ])
    
    D = np.block([
        [np.eye(A.shape[0]), np.zeros_like(A)],
        [np.zeros_like(A), -np.eye(A.shape[0])]
    ])
    
    eigenvalues = eig(C, D, right=False)

    eigval.append(np.real(eigenvalues[1]))
    
dict = {'Eigenvalue':eigval,'v values':vo}
df = pd.DataFrame(dict)
df.to_csv('Eigenvalues.csv')