#!/usr/bin/env python
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

def draw_box(ax, center, width, height, text, fontsize=14):
	"""Draw a rounded rectangle with centered text."""
	x, y = center
	rect = FancyBboxPatch(
		(x - width/2, y - height/2),
		width, height,
		boxstyle="round,pad=0.02,rounding_size=0.02",
		edgecolor="black",
		facecolor="white",
		linewidth=1.6,
	)
	ax.add_patch(rect)
	ax.text(x, y, text, ha="center", va="center", fontsize=fontsize)
	return rect

def box_anchor(center, width, height, side, offset=0.02):
	x, y = center
	if side == "left":   return (x - width/2 - offset, y)
	if side == "right":  return (x + width/2 + offset, y)
	if side == "bottom": return (x, y - height/2 - offset)
	if side == "top":    return (x, y + height/2 + offset)
	return center

def draw_arrow(ax, start, end, text=None, text_pos=0.5, dy=0.03, fontsize=12):
	arr = FancyArrowPatch(
		posA=start, posB=end, arrowstyle="-|>",
		mutation_scale=15, linewidth=1.5, color="black",
	)
	ax.add_patch(arr)
	if text:
		tx = start[0] + (end[0]-start[0])*text_pos
		ty = start[1] + (end[1]-start[1])*text_pos
		ax.text(tx, ty + dy, text, ha="center", va="bottom", fontsize=fontsize)
	return arr

fig, ax = plt.subplots(figsize=(13, 7))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Positions
title_pos   = (0.5, 0.90)
svd_pos     = (0.25, 0.65)
eigen_pos   = (0.75, 0.65)

col_label_pos= (0.15, 0.45)
row_label_pos= (0.35, 0.45)
col_ortho_pos= (0.15, 0.35)
row_ortho_pos= (0.35, 0.35)

nonsym_pos  = (0.60, 0.45)
sym_pos     = (0.90, 0.45)
nonsym_basis_pos = (0.60, 0.35)
sym_basis_pos    = (0.90, 0.35)

box_w, box_h = 0.20, 0.10
small_w, small_h = 0.12, 0.09

# Boxes
draw_box(ax, title_pos, box_w, box_h, "Finding\nOrthonormal Basis", fontsize=16)
draw_box(ax, svd_pos,   box_w, box_h, "SVD", fontsize=16)
draw_box(ax, eigen_pos, box_w, box_h, "Eigen\nDecomposition", fontsize=16)
draw_box(ax, nonsym_basis_pos, small_w, small_h, "Non-orthonormal\nBasis", fontsize=13)
draw_box(ax, sym_basis_pos,    small_w, small_h, "Orthonormal\nBasis", fontsize=13)
draw_box(ax, col_ortho_pos, small_w, small_h, "Orthonormal\nBasis", fontsize=13)
draw_box(ax, row_ortho_pos, small_w, small_h, "Orthonormal\nBasis", fontsize=13)

# Arrows and labels (outside boxes)
draw_arrow(ax, box_anchor(title_pos, box_w, box_h, "left"),
           box_anchor(svd_pos, box_w, box_h, "top"),
           text="Not square", text_pos=0.55)
draw_arrow(ax, box_anchor(title_pos, box_w, box_h, "right"),
           box_anchor(eigen_pos, box_w, box_h, "top"),
           text="Square", text_pos=0.55)

# Text labels for column and row space
ax.text(col_label_pos[0], col_label_pos[1], "Column Space", ha="center", va="center", fontsize=13)
ax.text(row_label_pos[0], row_label_pos[1], "Row Space", ha="center", va="center", fontsize=13)
ax.text(0.6, 0.45, "Not Symmetric $A = V\Lambda V^{-1}$", ha="center", va="center", fontsize=13)
ax.text(0.9, 0.45, "Symmetric $A = V\Lambda V^{\\top}$", ha="center", va="center", fontsize=13)



# Connectors (arrows remain outside boxes)
draw_arrow(ax, box_anchor(svd_pos, box_w, box_h, "bottom"),
           (col_label_pos[0], col_label_pos[1] + 0.05))
draw_arrow(ax, box_anchor(svd_pos, box_w, box_h, "bottom"),
           (row_label_pos[0], row_label_pos[1] + 0.05))
#draw_arrow(ax, (col_label_pos[0], col_label_pos[1] - 0.05),
#           box_anchor(col_ortho_pos, small_w, small_h, "top"))
#draw_arrow(ax, (row_label_pos[0], row_label_pos[1] - 0.05),
#           box_anchor(row_ortho_pos, small_w, small_h, "top"))

draw_arrow(ax, box_anchor(eigen_pos, box_w, box_h, "bottom"),
           box_anchor(nonsym_pos, small_w, small_h, "top"))
draw_arrow(ax, box_anchor(eigen_pos, box_w, box_h, "bottom"),
           box_anchor(sym_pos, small_w, small_h, "top"))
#draw_arrow(ax, box_anchor(nonsym_pos, small_w, small_h, "bottom"),
#           box_anchor(nonsym_basis_pos, small_w, small_h, "top"))
#draw_arrow(ax, box_anchor(sym_pos, small_w, small_h, "bottom"),
#           box_anchor(sym_basis_pos, small_w, small_h, "top"))

plt.tight_layout()
plt.savefig("orthonormal_flow_clean.png", dpi=220, bbox_inches="tight")
plt.show()

