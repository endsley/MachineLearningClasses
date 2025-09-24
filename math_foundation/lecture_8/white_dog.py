import matplotlib.pyplot as plt
import numpy as np

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='-', color='lightgray', zorder=0)

# Define the vectors
vector_white = np.array([1, 0])
vector_dog = np.array([0, 1])
vector_idea = np.array([0.5, 1])

# Plot the vectors with labels
ax.quiver(0, 0, vector_white[0], vector_white[1], angles='xy', scale_units='xy', scale=1, color='red', linewidth=2, zorder=2)
ax.text(vector_white[0], vector_white[1] - 0.2, 'white', fontsize=16, ha='right', va='top')

ax.quiver(0, 0, vector_dog[0], vector_dog[1], angles='xy', scale_units='xy', scale=1, color='blue', linewidth=2, zorder=2)
ax.text(vector_dog[0] - 0.2, vector_dog[1], 'dog', fontsize=16, ha='right', va='bottom')

ax.quiver(0, 0, vector_idea[0], vector_idea[1], angles='xy', scale_units='xy', scale=1, color='black', linewidth=2, zorder=2)
ax.text(vector_idea[0] + 0.1, vector_idea[1] + 0.0, 'idea', fontsize=16, ha='center', va='bottom')


# Calculate and plot the projection of "idea" onto "dog"
# Formula: proj_v(u) = ((u dot v) / ||v||^2) * v
dot_product = np.dot(vector_idea, vector_dog)
dog_norm_squared = np.sum(vector_dog**2)
projection_scalar = dot_product / dog_norm_squared
projection_vector = projection_scalar * vector_dog

# Draw the dashed projection line from "idea" to the "dog" vector
ax.plot([vector_idea[0], projection_vector[0]], [vector_idea[1], projection_vector[1]], 'r--', linewidth=1.5, zorder=1)
ax.text((vector_idea[0] + projection_vector[0]) / 2 - 0.1, (vector_idea[1] + projection_vector[1]) / 2 + 0.1, 'error', fontsize=14, ha='left', va='center')


# Set the limits and labels
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_title('Semantic Vectors', fontsize=14)
ax.set_xlabel('x-axis (Adjectives)')
ax.set_ylabel('y-axis (Nouns)')

# Set spines and ticks
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
