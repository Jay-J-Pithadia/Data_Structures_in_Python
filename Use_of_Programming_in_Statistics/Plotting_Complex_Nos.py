# This program is for zeroes and poles of a Transfer function

import matplotlib.pyplot as plt
import numpy as np

# create data of complex numbers
data1 = np.array([1-3j, 1+3j, -2])

x1 = data1.real
y1 = data1.imag

# plot the Poles of Transfer function
plt.plot(x1, y1,"bx", label="Poles")


data2 = np.array([1j, -1j, 2-3j,-3])

x2 = data2.real
y2 = data2.imag

# plot the Zeroes of Transfer function
plt.plot(x2, y2, "ro", label="Zeroes")

plt.ylabel('Imaginary Axis')
plt.xlabel('Real Axis')
plt.legend()
plt.title("Plotting For Zeroes and Poles")
plt.show()
