#!/usr/bin/env python

import sympy as sp

# variables
x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4')

# coefficient matrix and RHS
A = sp.Matrix([
	[1, 1, 0, 0],
	[2, 1, 1, 0],
	[0, 3, 1, 1],
	[0, 0, 2, 1],
])

b = sp.Matrix([3, 6, 10, 8])

# augmented matrix
Aug = A.row_join(b)

print("A =")
sp.pprint(A)
print("\nb =")
sp.pprint(b)

print("\nAugmented matrix [A|b] =")
sp.pprint(Aug)

# RREF of augmented matrix (Gaussian Elimination to RREF)
RREF, pivots = Aug.rref()

print("\nRREF([A|b]) =")
sp.pprint(RREF)
print("\nPivot columns =", pivots)

# solve Ax=b
x = A.LUsolve(b)   # exact rational solution
print("\nSolution x =")
sp.pprint(x)

# (optional) quick verification
print("\nCheck A*x =")
sp.pprint(A * x)

