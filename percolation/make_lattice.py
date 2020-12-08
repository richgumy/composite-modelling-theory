# Quick program to demonstrate an N-size cube of pseudo-random particle occupancy
import random as rand
import numpy as np
import matplotlib.pyplot as plt

N = 10   # Lattice size

p = 0.2 # Site occupation probability

def percolate(N,p):
    L = np.zeros((N,N,N)) # Lattice matrix (simple 3D cubic)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if rand.random() > p:
                    L[i,j,k] = 0
                else:
                    L[i,j,k] = 1
    return L


Lat = percolate(N,p)
print("Loading voxels... ")

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.voxels(Lat, facecolors='#1f77bfff', edgecolors='black', shade=True)

plt.show()
