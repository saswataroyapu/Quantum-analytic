# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:12:56 2025

@author: Nishanth S S
"""

import numpy as np
from scipy.linalg import eig

T = np.array([[0.7600,0.2365],
              [0.2365,0.7600]])

V1 = np.array([[-1.2266,-0.5974],
               [-0.5974,-0.6538]])

V2 = np.array([[-0.6538,-0.5974],
               [-0.5974,-1.2266]])

S = np.array([[1.0, 0.6593],
              [0.6593,1.0]])

H_c = T + V1 + V2

EI = np.array([[0.7746,0.4441,0.4441,0.5697],
               [0.4441,0.2970,0.2970,0.4441],
               [0.4441,0.2970,0.2970,0.4441],
               [0.5697,0.4441,0.4441,0.7746]]) 

def Fock(D):
    
    for p in range(4):
        for q in range(4):
            F[p,q] = H_c + sum(D[p,q]*(EI[p,q] - 0.5*EI[p,q]))
    
    return F

C = np.array()

D = np.zeros((2,2))

def density(C):  
    
    for i in range(2):
        for j in range(2):
            
            D[i,j] = sum(2 * C[i,k] * C[j,k] for k in range(2))
    
    return D

for i in range(100):
    
    F = Fock(density(C))
    
    eigenvalues , eigenvectors = eig(F,S)
    
    C = eigenvectors 
    
    D_new = density(C)
    
    if D_new - D < 1e-6 :
        break
    
    D = D_new 
    

    
            

