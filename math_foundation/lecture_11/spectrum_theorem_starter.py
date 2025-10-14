#!/usr/bin/env python
import numpy as np

# Define the matrix A
A = np.array([[ 3.07, -0.82, -2.23],
              [-0.82,  4.09, -0.31],
              [-2.23, -0.31,  1.84]], dtype=float)

# Define column eigenvectors
v1 = np.array([[ 0.74],
               [-0.49],
               [-0.47]])

v2 = np.array([[-0.29],
               [-0.85],
               [ 0.43]])

v3 = np.array([[ 0.61],
               [ 0.18],
               [ 0.77]])

# Eigenvalues
λ1, λ2, λ3 = 5.0, 4.0, 1e-4

# Stack eigenvectors into V and build diagonal Λ
V = np.hstack([v1, v2, v3])
Λ = np.diag([λ1, λ2, λ3])

# Check orthonormality
#
#	Write your code here



# Full reconstruction using the spectral theorem
#
#	Write you code here


# Partial reconstruction using only 2 core essences
#
#	Write you code here

