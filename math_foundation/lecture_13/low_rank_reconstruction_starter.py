#!/usr/bin/env python
import numpy as np
from numpy.linalg import eig, eigh, norm
np.set_printoptions(suppress=True, precision=4)


def pretty_np_array(m, title=None, end_space=''):
	m = str(m)
	L1 = m.split('\n')
	L1_max_width = len(max(L1, key=len))
	if title is not None:
		t1 = str.center(title, L1_max_width)
		m = t1 + '\n' + m + end_space
	else: m = m + end_space
	print(m, '\n')

# Original matrix A and eigenvalue matrix Λ
A = np.array([
    [2, -2, 0, 0],
    [-2, 2, 0, 0],
    [0, 0, 2.5005, -2.4995],
    [0, 0, -2.4995, 2.5005]
])

# Eigen-decomposition (A should already be symmetric)
λ, V = eigh(A)  # `eigh` guarantees real symmetric output and orthonormal V
Vᵀ = V.T
Λ = np.diag(λ)

# Which eigenvalue is 0? And therefore, which column of V should you remove?
print(Λ, '\n\n')
print(V)

# Now you need to remove the trivial eigenvectors and then reconstruct.
# The syntax for removing column i of V is 
# V̄ = np.delete(V, i, axis=1)


# The syntax for removing column and row i of Λ is 
#Λ̃ = np.delete(Λ, i, axis=1)
#Λ̃ = np.delete(Λ̃, i, axis=0)
#print(Λ̃)


# Now multiply them together V̄Λ̃V̄ᵀ, it should reconstruct the original matrix
