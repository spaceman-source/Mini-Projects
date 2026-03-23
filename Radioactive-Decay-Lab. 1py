
'''
James Ward
1/18/26
Program to model radioactive decay and compare a numerical solution to the
analytic result. The decay process is simulated by numerically solving the
first-order differential equation

    dN/dt = −N / τ

using the Euler integration method. The analytic solution to this equation is

    N(t) = N₀ e^(−t/τ)

The program evolves the number of nuclei forward in time using discrete time
steps and compares the numerical result to the exact exponential decay curve.

'''
# import math and matlab plot libraries
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import style

# let's first set the initial conditions. These values you can change.
Ninitial = 100  # initial number of nuclei
tinitial = 0.0  # initial starting time--we are just taking to be 0.0
tfinal = 5.0  # final time step for integration
tau = 1  # expected lifetime of a nucleus
deltat = .5 # integration time step


# Now let's think about setting up the integration by setting the start
# point.
Nold = Ninitial  # start the integration at Ninitial
t = tinitial  # set time to be initial time


# ts stores time values, N_Euler stores Euler values, N_analytic stores function value
ts = []
N_Euler = []
N_analytic = [] 
percent_err = []

# Store initial condition
ts.append(t)
N_Euler.append(Nold)
N_analytic.append(Ninitial) 
# Initial analytic value is just Ninitial at t=0

while t < tfinal:
    
    Nnew = Nold * (1.0 - deltat / tau)

    # Increment the time step by deltat. same as t = t + deltat
    t += deltat

    # calculate the analytic number of nuclei for comparison with integrated value
    Ntrue = Ninitial * math.exp(-t / tau)

    # percentage error of the integrated value from the analytic value
    err = abs((Nnew - Ntrue) / Ntrue) * 100.0
    
    # Store the data from this step
    ts.append(t)
    N_Euler.append(Nnew)
    N_analytic.append(Ntrue)
    percent_err.append(err)

    # Do a check to make sure the stepped time is < tfinal
    if t < tfinal:
        # if t < tfinal set Nold = Nnew to loop again and step forward
        Nold = Nnew
        
        
# Set up for the Plot 
plt.style.use('dark_background')
plt.plot(ts, N_Euler, label="Euler Method", color = 'blue')
plt.plot(ts, N_analytic, label="Analytic Solution", color = 'red')
plt.text(1, 80, f'deltat = {deltat}, tau = {tau}' , color='white', fontweight = 'bold')
plt.xlabel("Time (Seconds)")
plt.ylabel("Number of Nuclei N(t)")
plt.ylim(0, 100)
plt.xlim(0, tfinal)

plt.grid(True)
plt.legend()


plt.show()

# Percent error plot settings
plt.figure()
plt.plot(ts[1:], percent_err, color='magenta')  # Skip first time point (no error at t=0)
plt.xlabel("Time (seconds)")
plt.ylabel("Percent error (%)")
plt.grid(True)
plt.show()
# Shows percent error after the plots are closed

print('percent error =', err)
