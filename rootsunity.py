# Script that plots the roots of polynomials with ceofficeints uniformly chosen from a fixed interval.

import numpy as np
import matplotlib.pyplot as plt

# Specify degree and number of polynomials 
poly = 50
deg = 100
roots = []
realparts = []
imagparts = []

# Pick coefficients randomly from a [-1, 1]. This interval can easily be changed.
# Calculate the roots using numpy's built in methods.
for i in range(poly):
	currpoly = np.random.uniform(-1, 1, deg)
	roots.append(np.roots(currpoly))
	

# Plot the roots

plt.style.use('bmh')
unitcircle = plt.Circle((0, 0), 1, color='k', fill=False, ls = "--", linewidth = 2)
fig, ax = plt.subplots()

ax.add_artist(unitcircle)

for root in roots:
	realparts.append(root.real)
	imagparts.append(root.imag)

plt.plot(realparts, imagparts, ".", color = 'r')
plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))
plt.show()


