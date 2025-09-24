#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='-', color='lightgray', zorder=0)

# Define the vectors
vector_your_basis = np.array([2, 1])
vector_event = np.array([3, 4])
vector_another_basis = np.array([-2, 2])

# Plot the vectors with labels
ax.quiver(0, 0, vector_your_basis[0], vector_your_basis[1], angles='xy', scale_units='xy', scale=1, color='red', linewidth=2, zorder=2)
ax.text(vector_your_basis[0] - 0.8, vector_your_basis[1] - 0.8, 'your basis', fontsize=14, ha='left', va='bottom', color='red')

ax.quiver(0, 0, vector_event[0], vector_event[1], angles='xy', scale_units='xy', scale=1, color='black', linewidth=2, zorder=2)
ax.text(vector_event[0] + 0.2, vector_event[1] + 0.2, 'event', fontsize=14, ha='left', va='bottom', color='black')

ax.quiver(0, 0, vector_another_basis[0], vector_another_basis[1], angles='xy', scale_units='xy', scale=1, color='blue', linewidth=2, zorder=2)
ax.text(vector_another_basis[0] + 1, vector_another_basis[1] + 0.3, "another's basis", fontsize=14, ha='right', va='bottom', color='blue')


ax.text(-0.6, 0.3, "another's \n perception", fontsize=9, ha='right', va='bottom', color='green')
ax.text(3.8, 2, "your \n perception", fontsize=9, ha='right', va='bottom', color='green')

# --- Projection onto 'your basis' ---
dot_product_your = np.dot(vector_event, vector_your_basis)
norm_squared_your = np.sum(vector_your_basis**2)
projection_scalar_your = dot_product_your / norm_squared_your
projection_vector_your = projection_scalar_your * vector_your_basis

# Draw the light gray projection line
ax.plot([vector_event[0], projection_vector_your[0]], [vector_event[1], projection_vector_your[1]], 'lightgray', linestyle='--', linewidth=1.5, zorder=1)

# Extend the red basis line with a gray dashed line
ax.plot([0, projection_vector_your[0]], [0, projection_vector_your[1]], 'lightgray', linestyle='--', linewidth=1.5, zorder=1)
ax.plot([projection_vector_your[0], vector_your_basis[0]], [projection_vector_your[1], vector_your_basis[1]], 'lightgray', linestyle='--', linewidth=1.5, zorder=1)

# Add blue dot at the intersection
ax.plot(projection_vector_your[0], projection_vector_your[1], 'o', color='green', markersize=8, zorder=3)


# --- Projection onto 'another's basis' ---
dot_product_another = np.dot(vector_event, vector_another_basis)
norm_squared_another = np.sum(vector_another_basis**2)
projection_scalar_another = dot_product_another / norm_squared_another
projection_vector_another = projection_scalar_another * vector_another_basis

# Draw the light gray projection line
ax.plot([vector_event[0], projection_vector_another[0]], [vector_event[1], projection_vector_another[1]], 'lightgray', linestyle='--', linewidth=1.5, zorder=1)

# Add blue dot at the intersection
ax.plot(projection_vector_another[0], projection_vector_another[1], 'o', color='green', markersize=8, zorder=3)


# Set the limits and labels
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 5)
ax.set_title('Plot of Misunderstanding', fontsize=16)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')

# Set spines and ticks for a clean look
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
