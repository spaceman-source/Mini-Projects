


# Initial Variables + Libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


underflow = 1.0
overflow = 1.0
i = 0

# Store overflow values for plotting
oflow = []
i_val = []
uflow =[]

# Finding overflow and tracking values
while underflow/2 > 0:
    overflow = overflow*2
    oflow.append(overflow)
    uflow.append(underflow)
    i_val.append(i)
    i += 1
print("The maximum overflow value is:", underflow)

