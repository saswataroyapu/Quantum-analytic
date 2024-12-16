# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 17:44:54 2024

@author: 91959
"""

import numpy as np
from scipy.linalg import eig
import pandas as pd

v = 0.997
omega = 1.99995
lmda = 0
tolerance = 1e-12
max_iter = 100
finaleig = []
diff = []

a = [1, 1, 1, 1]


def construct_matrices(omega,v):
    A = np.array([
        [2, 0, 0, v],
        [0, 3, v, 0],
        [0, v, 1, 0],
        [v, 0, 0, 2]
    ])

    B = np.array([
        [0, 0, 0, v],
        [0, 0, v, 0],
        [0, v, 0, 0],
        [v, 0, 0, 0]
    ])

    
    C = np.fliplr(np.diag(a)) * lmda * omega 

    
    D = np.block([
        [np.eye(A.shape[0]), np.zeros_like(A)],
        [np.zeros_like(A), -np.eye(A.shape[0])]
    ])

    E = np.block([
        [A + C, B + C],
        [B + C, A + C]
    ])
    
    return E, D


    
for iteration in range(max_iter):
        
    E, D = construct_matrices(omega,v)
        
        
    eigenvalues = eig(E, D, right=False)
        
        #real_eigenvalues = eigenvalues[np.isreal(eigenvalues)].real
        
    eigs = np.sort(eigenvalues)
        
    new_omega = eigs[5]
    
    if abs(new_omega - omega) < tolerance:
            print(f"Converged after {iteration + 1} iterations.")
            break
        
        
    omega = new_omega
    print(f"Iteration {iteration + 1}: omega = {omega:.10e}")
    
    #diff.append(float(eigenvalues[6]-eigenvalues[5]))

print(f"Final converged  omega = {omega:.10e}")
    
