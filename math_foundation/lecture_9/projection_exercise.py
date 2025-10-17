import matplotlib.pyplot as plt
import numpy as np

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='-', color='lightgray', zorder=0)

# Define the new vectors
vector_u = np.array([4, 2])  # Changed from (5, 2)
vector_v = np.array([1, 4])  # Changed from (2, 3)

# --- Recalculate the projection of vector v onto vector u ---
# Formula: proj_u(v) = ((v dot u) / ||u||^2) * u
dot_product = np.dot(vector_v, vector_u)
u_norm_squared = np.sum(vector_u**2)
projection_scalar = dot_product / u_norm_squared
projection_vector = projection_scalar * vector_u

# Define the point C (end of vector v) and the projection point D
point_c = vector_v
point_d = projection_vector

# Plot the primary vectors
ax.quiver(0, 0, vector_u[0], vector_u[1], angles='xy', scale_units='xy', scale=1, color='black', linewidth=2, zorder=2)
ax.quiver(0, 0, vector_v[0], vector_v[1], angles='xy', scale_units='xy', scale=1, color='black', linewidth=2, zorder=2)

# Label the vectors (Adjusted positions for better visibility with new vectors)
ax.text(4.2, 2, 'u', fontsize=18, ha='left', va='center')
ax.text(1, 4.2, 'v', fontsize=18, ha='right', va='center')

# Plot point C and label it
ax.plot(point_c[0], point_c[1], 'o', color='blue', markersize=8, zorder=3)
#ax.text(point_c[0] - 0.2, point_c[1] + 0.2, 'C', fontsize=16, ha='right', va='bottom', color='blue')

# Draw the dashed projection line for 'e' (error vector) from C to D
ax.plot([point_c[0], point_d[0]], [point_c[1], point_d[1]], 'b--', linewidth=1.5, zorder=1)
# Label the dashed line 'e'
ax.text((point_c[0] + point_d[0]) / 2 + 0.3, (point_c[1] + point_d[1]) / 2 - 0.2, 'e', fontsize=16, ha='left', va='top', color='blue')

# Plot point D and label it
ax.plot(point_d[0], point_d[1], 'o', color='blue', markersize=8, zorder=3)
ax.text(point_d[0] + 0.1, point_d[1] - 0.1, 'd', fontsize=16, ha='left', va='top', color='blue')

# Draw the dashed red line for 'α' (projection vector) from the origin to D
ax.plot([0, point_d[0]], [0, point_d[1]], 'r--', linewidth=2, zorder=2)

# Label the distance from 0 to D as alpha
ax.text(point_d[0] * 0.5 + 0.4, point_d[1] * 0.5 - 0.1, r'$\alpha$', fontsize=25, ha='center', va='center', color='red')

# Set the limits and labels
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 6)
ax.set_title('Vector Projection ($v$ onto $u$)', fontsize=14)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')

# Set spines and ticks
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
