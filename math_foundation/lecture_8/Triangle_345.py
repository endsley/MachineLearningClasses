#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import math

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='-', color='lightgray', zorder=0)

# Define the original vectors for a 3-4-5 triangle
# Vector 'a' (leg 1)
a_vector_original = np.array([3, 0])
# Vector 'b' (leg 2) - Not plotted as a vector from the origin
b_vector_original = np.array([0, 4])
# Vector 'c' (hypotenuse)
c_vector_original = np.array([3, 4])

# Define the rotation angle in radians
angle_degrees = 60
angle_rad = np.radians(angle_degrees)

# Create the rotation matrix
rotation_matrix = np.array([
    [np.cos(angle_rad), -np.sin(angle_rad)],
    [np.sin(angle_rad), np.cos(angle_rad)]
])

# Apply the rotation to the vectors
a_vector = rotation_matrix @ a_vector_original
c_vector = rotation_matrix @ c_vector_original

# Plot the two vectors from the origin
ax.quiver(0, 0, a_vector[0], a_vector[1], angles='xy', scale_units='xy', scale=1, color='red', linewidth=2, zorder=2)
ax.quiver(0, 0, c_vector[0], c_vector[1], angles='xy', scale_units='xy', scale=1, color='blue', linewidth=2, zorder=2)

# Plot the third leg of the triangle as a dashed line
ax.plot([a_vector[0], c_vector[0]], [a_vector[1], c_vector[1]], 'k--', linewidth=1, zorder=1)

# Label the vectors
ax.text(a_vector[0] / 2 + 0.8, a_vector[1] / 2 - 0.3, r'$||a||_2 = 3$', fontsize=16, ha='center', va='top', color='red')
ax.text(c_vector[0] / 2 - 1.9, c_vector[1] / 2, r'$||c||_2 = 5$', fontsize=16, ha='left', va='center', color='blue')
# Label for the third leg
mid_b = (a_vector + c_vector) / 2
ax.text(mid_b[0] + 0.4, mid_b[1] + 0.3, r'$||b||_2 = 4$', fontsize=16, ha='left', va='center')

# Add a label for the angle theta at the origin
ax.text(0.3 * np.cos(np.radians(20)) - 0.15, 0.3 * np.sin(np.radians(20)) + 0.7, r'$\theta$', fontsize=16, ha='center', va='center', color='red')

# Set the limits and labels
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 5)
ax.set_title('3,4,5 Triangle Formed by Vectors Rotated by 40 Degrees', fontsize=14)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')

# Set spines and ticks
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_xticks(np.arange(-4, 5, 1))
ax.set_yticks(np.arange(-1, 5, 1))

# Show the plot
plt.show()
