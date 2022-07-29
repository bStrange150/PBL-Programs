#Program to numerically solve for temp distribution along bar
"""
Created on Fri Jul 29 13:02:05 2022

@author: stran
"""

#Import Required Modules
import numpy as np
import matplotlib.pyplot as plt
from math import pi

#Define Problem Constants
L =  1 #mm (wire length)
d = 5 #um (diameter)
k = 200 #2/mK (thermal conductivity)
hbar = 1000 #W/m^2.K (heat transfer coefficient)
perim = pi*d
area = (pi/4)*d**2

#Ambient bar temps
Ta = 293.15 #K
T0 = 353.15 #K
T4  = 343.15 #K

#Define values
beta = (hbar * perim)/(k*area)


