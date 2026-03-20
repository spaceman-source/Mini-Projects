
# Lab 2.1.1: Plotting Underflow and Overflow
# James Ward 1/29/2026
# This code finds the max float and minimum float in python by finding the largest number represented before overflow and the smallest number represented before underflow

# Import Libraries
from unicodedata import category
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.pyplot as plt

# Initial Variables
underflow = 1.0
overflow = 1.0
N = 1023
i = 0

# Store values for plotting
uflow = []
oflow = []
di = []

# Loop to calculate underflow and overflow
while i < N:
    uflow.append(underflow)
    oflow.append(overflow)
    di.append(i)

    underflow /= 2
    overflow *= 2
    i += 1
    if overflow == float('inf'):
        break

# Print to know the results
print("The maximum overflow value is:", overflow, "The minimum underflow value is:", underflow)


# Set up plots
plt.figure(figsize=(8, 5))
plt.plot(di, uflow, label="Underflow", color='black', marker='o')
plt.xlabel("Iterations")
plt.ylabel("Floating Point Value")
plt.xlim(min(di), max(di))
plt.yscale('log')
plt.grid(True, which="both", linestyle = '--', linewidth = 0.5)
plt.minorticks_on()
plt.legend()
plt.tight_layout
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(di, oflow, label="Overflow", color = 'black', marker='o')
plt.xlabel("Iterations")
plt.ylabel("Floating PointValue")
plt.xlim(min(di), max(di))
plt.grid(True, which="both", linestyle = '--', linewidth = 0.5)
plt.minorticks_on()
plt.legend()
plt.tight_layout
plt.show()