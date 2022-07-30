#Program to numerically solve for temp distribution along bar
"""
Created on Fri Jul 29 13:02:05 2022

@author: stran
"""
#theta(x) = T(x) - Ta

#Import Required Modules
import numpy as np
import matplotlib.pyplot as plt
from math import pi

#Define Problem Constants
L =  1e-3 #mm (wire length)
L_array = 
part = 5   #no. of partitions
d = 5e-6 #um (diameter)
k = 200 #2/mK (thermal conductivity)
hbar = 1000 #W/m^2.K (heat transfer coefficient)
perim = pi*d
area = (pi/4)*d**2
delta_x = L/part

#Define values
beta = (hbar * perim)/(k*area) #beta squared
s = -2-beta*((delta_x)**2)

#Ambient bar temps
Ta = 293.15 #K
T0 = 353.15 #K
T4  = 343.15 #K

#Create coefficient matrix
A = np.array([1,1,1,0])
B = np.array([1,s,s,s,1])
C = np.array([0,1,1,1])

M = np.diag(A, -1) + np.diag(B, 0) + np.diag(C, 1)
print(M)

b = np.array([T0 - Ta, 0, 0, 0, T4 - Ta])
print(b)

x = np.linalg.solve(M, b)
x= x + 293.15
print(x)

#Plot setup
plt.title("Temperature Distributuion of Wire")
plt.xlabel("Distance Along wire [m]")
plt.ylabel("Temperature [K]")

#Plot output of finite difference formulas
plt.plot(L_array, x)
plt.show()
