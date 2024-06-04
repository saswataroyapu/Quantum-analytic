#This is to plot the 2D energy profile as the function of the width and the depth of the
#Gaussian as the trial wavefunction of the perturbed Hamiltonian.
#Credit: Analytical work done by Nishanth S S.
import numpy as np


C1 = 0.0 ##This is the depth of the perturbed Gaussian wf
C2 = 1.0 ## This width of the perturbed Gaussian wf
A = 5.0
sigma = 0.25


def energy(C1,C2):



#The Final energy is being decomposed as terms from Eq 5 in HO-PT-VP.pdf 
#(version a61905b4c6b8a9407d63b51472783d7654de90b7)

    normalization = ( 1.0 + C1*C1*np.sqrt(np.pi/C2) - 2*C1*(np.pi)**(0.25)*np.sqrt(2.0/C2))
    
    E1 = 0.5
    
    E2 = A*np.sqrt(2.0*sigma*sigma/(1.0+2.0*sigma*sigma))
    
    E3prefactor = -C1*np.pi**(0.25)
    E3_1 = C2*np.sqrt(2.0)/((1+C2)**(3.0/2.0))
    E3_2 = 1.0/(1.0*(1+C2**(3.0/2.0)))
    E3_3 = 2.0*A*np.sqrt(2.0/(C2 + 1.0 + 1.0/(sigma*sigma)))
    
    E3 = E3prefactor*(E3_1 + E3_2 + E3_3)
    
    E4prefactor= C1*C1*np.sqrt(np.pi)
    
    E4_1 = np.sqrt(C2)/4.0
    E4_2 = 1.0/(4.0*C2**(3.0/2.0))
    E4_3 = A*np.sqrt(1.0/(C2 + 1.0/(2.0*sigma*sigma)))
    
    E4 = E4prefactor*(E4_1 + E4_2 + E4_3)
    
    total_energy = (E1 + E2 + E3 + E4)/normalization

    return total_energy

for C1 in np.arange(0.3, 0.6, 0.01):
    for C2 in np.arange(5.5,12.0,0.005):
        e = energy(C1,C2)
        print(C1, C2, e)
    print(" ")
