# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 16:12:56 2025

@author: Nishanth S S
"""

import numpy as np
from scipy.linalg import eigh

nmo = 2
nao = 2

nocc = 1


T = np.array([[0.7600, 0.2365],
              [0.2365, 0.7600]])

V1 = np.array([[-1.2266, -0.5974],
               [-0.5974, -0.6538]])

V2 = np.array([[-0.6538, -0.5974],
               [-0.5974, -1.2266]])

S = np.array([[1.0, 0.6593],
              [0.6593, 1.0]])

H_c = T + V1 + V2

ERI = np.array([[0.7746, 0.4441, 0.4441, 0.5697],
               [0.4441, 0.2970, 0.2970, 0.4441],
               [0.4441, 0.2970, 0.2970, 0.4441],
               [0.5697, 0.4441, 0.4441, 0.7746]])


def v_pqrs(p, q, r, s, ERI):

    i = nmo*(p) + q
    j = nmo*(r) + s

    return ERI[i, j]


def Fock_matrix_2e(D, Fock):
    
    for p in range(nmo):
        for q in range(nmo):
            for r in range(nmo):
                for s in range(nmo):
                    Fock[p, q] += D[r, s] * \
                        (1.0*v_pqrs(p, q, r, s, ERI)-0.5*v_pqrs(p, r, q, s, ERI))


def build_density(C,D):
    for i in range(nmo):
        for j in range(nmo):

            D[i, j] = sum(2 * C[i, k] * C[j, k] for k in range(nocc))

    return D



dens_mat = np.zeros((nmo, nmo))

guess_E, guess_V = eigh(H_c, S)

build_density(guess_V, dens_mat)

errorfactor = 0.1

error = errorfactor*np.random.random()
dens_mat[0,0] += error
dens_mat[1,1] -= error

print("guess_dens_mat")
print(dens_mat)
print()

F = np.zeros((nmo,nmo))
F = H_c.copy()
Fock_matrix_2e(dens_mat,F)

print("Fock")
print(F)
print()

for i in range(10):
    
    print(i)
    F = H_c.copy()
    
    Fock_matrix_2e(dens_mat, F)
    print("Fock inside")
    print(F)
    print()
    
    eigenvalues, eigenvectors = eigh(F, S)
    print("orbital energies inside")
    print(eigenvalues)
    print()

    C = eigenvectors
    dens_mat_new = np.zeros((nmo, nmo))
    build_density(C,dens_mat_new)

    if np.linalg.norm(dens_mat_new - dens_mat) < 1e-6:
        break

    dens_mat = dens_mat_new

print("Final density matrix")
print(dens_mat)
print()
print("Fock at end")
print(F)
print()

energy = 0

print("orbital energies")
print(eigenvalues)
print()

for p in range(nmo):
    for q in range(nmo):
        
        energy += (F[p,q] + H_c[p,q])*dens_mat[p,q]*0.5

print("Energy")
print(energy)