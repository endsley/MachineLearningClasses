#!/usr/bin/env python
import numpy as np

A = np.array([
	[ 3.0, -3.0,  0.0,  0.0],
	[-3.0,  3.0,  0.0,  0.0],
	[ 0.0,  0.0,  1.5, -1.5],
	[ 0.0,  0.0, -1.5,  1.5],
])

λ, V = np.linalg.eigh(A)          # columns of V are eigenvectors
Λ = np.diag(λ)
print(λ)
print(V)


#	Full Reconstruction of the original matrix
Ā = V @ Λ @ V.T
print(Ā)

#	Reconstruction While removing trivial eigenvectors
V̄ = V[:, 2:4]
Λ̃ = Λ[2:4, 2:4]
print(V̄)
print(Λ̃)
Ā = V̄ @ Λ̃ @ V̄.T
print(Ā)
