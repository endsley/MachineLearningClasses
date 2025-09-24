#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.grid(True, linestyle='-', color='lightgray', zorder=0)
ax.set_aspect('equal', adjustable='box')

# Set the limits of the plot for better visualization
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

# Set the axes to be centered at (0,0) for clarity
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Draw the vector from (0,0) to (1,1) with a bold line and a label
# The 'ha' and 'va' parameters adjust the label's position relative to the point
ax.quiver(0, 0, 1, 1, angles='xy', scale_units='xy', scale=1, color='black', linewidth=3, zorder=2)
ax.text(0.5, 0.9, '$\mathit{u}$', fontsize=18, fontweight='bold', ha='left', va='bottom')
ax.text(2.0, 2.7, 'error', fontsize=14, fontweight='bold', ha='left', va='bottom')

# Draw a dashed line from (1,1) to (3,3)
ax.plot([1, 3], [1, 3], 'k--', linewidth=1.5, zorder=1)

# Place a single point at (1.5, 3) and label it 'D'
ax.plot(1.5, 3, 'o', markersize=8, color='blue', zorder=3)
ax.text(1.6, 3, 'D', fontsize=16, ha='left', va='center')

# Draw the dashed projection line from point D to the vector u
ax.plot([1.5, 2.25], [3, 2.25], 'k--', linewidth=1.5, zorder=1)
ax.plot(2.25, 2.25, 'o', markersize=8, color='blue', zorder=3)
ax.text(2.35, 2.25, 'C', fontsize=16, ha='left', va='center')


# Add a title and labels for the axes
ax.set_title('Vector Graph', fontsize=16)
ax.set_xlabel('X-axis', loc='right')
ax.set_ylabel('Y-axis', loc='top')

# Show the plot
plt.show()
