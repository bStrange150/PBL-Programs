#Program to numerically solve for temp distribution along bar
"""
Created on Fri Jul 29 13:02:05 2022

@author: stran
"""
#theta(x) = T(x) - Ta

#Import Required Modules
import numpy as np
import matplotlib.pyplot as plt

#Define Problem Constants
L =  1e-3 #mm (wire length)
part = 5   #no. of partitions
L_array = np.linspace(0, L, part)
print(f"The nodes in the wire are located at \n{L_array} m along the wire\n")
d = 5e-6 #um (diameter)
k = 200 #2/mK (thermal conductivity)
hbar = 1000 #W/m^2.K (heat transfer coefficient)
perim = np.pi*d
area = (np.pi/4)*d**2
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
print(f"The coefficient matrix M is /n{M}\n")

b = np.array([T0 - Ta, 0, 0, 0, T4 - Ta])
print(f"The vector b is \n{b}\n")

#Solve system of linear eqns
x = np.linalg.solve(M, b)
x= x + 293.15 #add ambient temp to all values
print(f"The solution vector for points along the wire is \n{x} K\n")

#Compute analytical solution
theta_list = []
for i in range(len(L_array)):
    theta_i = (((T4-Ta)*np.sinh(np.sqrt(beta)*L_array[i]))+(T0-Ta)*np.sinh(np.sqrt(beta)*(L-L_array[i])))/(np.sinh(np.sqrt(beta)*L))
    theta_list.append(theta_i)

#Add Ta to all values in list
temp_list = [j + 293.15 for j in theta_list] #K (convert theta to temps)
print(f"The analytical solution for points along the wire is \n{theta_list} K")

#Plot setup
plt.title(f"Temperature Distributuion of Wire for n={part} points")
plt.xlabel("Distance Along wire [m]")
plt.ylabel("Temperature [K]")

#Plot output of finite difference formulas
plt.plot(L_array, x, label = "Numerical Solution")
plt.plot(L_array, temp_list, label = "Analytical Solution")
plt.legend()
plt.show()