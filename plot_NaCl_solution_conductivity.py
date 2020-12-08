# Plot data
import matplotlib.pyplot as plt
import numpy as np

dataY = [2.0,3.9,5.7,7.5,9.2,10.9,12.6,14.3,16.0,17.6,19.2,20.8,22.4,24.0,25.6,\
27.1,28.6,30.1,31.6,33.0]
dataX = []
for i in range(len(dataY)):
    dataX.append(0.1*i)

fig, ax = plt.subplots()
ax.plot(dataX, dataY)
ax.set_xlabel(r'$\frac{V}{W}$ of NaCl [%]')
ax.set_ylabel(r'$\sigma$ [mS.cm]')
ax.set_title('Electrical conductivity vs concentration for a NaCl solution')

plt.show()
