#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='-', color='lightgray', zorder=0)

# Define the vectors
vector_u = np.array([5, 2])
vector_v = np.array([2, 3])

# Calculate the projection of vector v onto vector u
# Formula: proj_u(v) = ((v dot u) / ||u||^2) * u
dot_product = np.dot(vector_v, vector_u)
u_norm_squared = np.sum(vector_u**2)
projection_scalar = dot_product / u_norm_squared
projection_vector = projection_scalar * vector_u

# Define the point C and the projection point D
point_c = vector_v
point_d = projection_vector

# Plot the vectors
ax.quiver(0, 0, vector_u[0], vector_u[1], angles='xy', scale_units='xy', scale=1, color='black', linewidth=2, zorder=2)
ax.quiver(0, 0, vector_v[0], vector_v[1], angles='xy', scale_units='xy', scale=1, color='black', linewidth=2, zorder=2)

# Label the vectors
ax.text(vector_u[0] * 0.5 + 2.5, vector_u[1] * 1.0, 'u', fontsize=22, ha='left', va='center')
ax.text(vector_v[0] * 0.5 + 1.3, vector_v[1] * 0.5 + 1.6, 'v', fontsize=22, ha='right', va='center')

# Plot point C and label it
ax.plot(point_c[0], point_c[1], 'o', color='blue', markersize=8, zorder=3)
#ax.text(point_c[0] + 0, point_c[1] + 0.1, 'C', fontsize=16, ha='left', va='bottom', color='blue')

# Draw the dashed projection line from C to D
ax.plot([point_c[0], point_d[0]], [point_c[1], point_d[1]], 'b--', linewidth=1.5, zorder=1)
# Label the dashed line
ax.text((point_c[0] + point_d[0]) / 2 + 0.1, (point_c[1] + point_d[1]) / 2 + 0, 'e', fontsize=16, ha='center', va='bottom', color='blue')

# Plot point D and label it
ax.plot(point_d[0], point_d[1], 'o', color='blue', markersize=8, zorder=3)
ax.text(point_d[0] + 0.2, point_d[1] - 0.3, 'd', fontsize=16, ha='right', va='bottom', color='blue')

# Draw the dashed red line from the origin to D
ax.plot([0, point_d[0]], [0, point_d[1]], 'r--', linewidth=2, zorder=2)

# Label the distance from 0 to D as alpha
# This is a good way to show the distance without drawing a separate vector
ax.text(point_d[0] * 0.5 + 0.4, point_d[1] * 0.5 + 0.1, r'$\alpha$', fontsize=25, ha='right', va='top', color='red')

# Set the limits and labels
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 6)
ax.set_title('Vector Projection', fontsize=14)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')

# Set spines and ticks
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
