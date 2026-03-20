
# Computational Lab 2 
# James Ward 1/29/2026
# This code finds the precision of my floating numbers in python by finding the smallest eps that can be added to 1.0 and the computer can still tell the difference

# Import Libraries
import numpy as np  
import math 
import matplotlib.pyplot as plt
from matplotlib import style


# Initial Variables
eps = 1.0
almostone = 2.0
i = 0

# store the values in array for plotting 
epsilon = []
di = []
# Append initial conditions
epsilon.append(eps)
di.append(i)    

#Loop until computer can't tell the difference
while(almostone != 1.0):
 eps = eps/2.0 # Gets smaller and smaller each iteration
 almostone = 1.0+eps # gets closer to one each iteration until loop stops and computer cant tell difference between 1+eps and 1

 i = i +1
 epsilon.append(eps) 
 di.append(i)    

  # Print the machine epsilon
print("The machine epsilon is:", eps)

# Plotting Epsilon Values
plt.figure()
plt.style.use('classic')
plt.plot(di, epsilon, marker='o', color='black')
plt.xlabel("Iterations (i)")
plt.ylabel("Epsilon Value")
plt.grid(True)
plt.autoscale()
plt.xlim(0, max(di))    
plt.show()