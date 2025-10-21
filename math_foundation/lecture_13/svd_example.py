#!/usr/bin/env python
import numpy as np
np.set_printoptions(precision=6, suppress=True)

# A simple 2×3 example
A = np.array([[3., 2.,  2.],
              [2., 3., -2.]])

# Compute SVD: A = U Σ Vᵀ
U, σ, Vᵀ = np.linalg.svd(A, full_matrices=False)  # Vt is Vᵀ
Σ = np.diag(σ)

# Verify orthonormality and reconstruction
I_U = U.T @ U
I_V = Vᵀ@ Vᵀ.T
Ã = U @ Σ @ Vᵀ

print("\nUᵀU ≈ I =\n", I_U)
print("\nVᵀV ≈ I =\n", I_V)
print("\nReconstruction U Σ Vᵀ =\n", Ã)
print("\n‖A − U Σ Vᵀ‖_F =", np.linalg.norm(A - Ã, ord="fro"))

