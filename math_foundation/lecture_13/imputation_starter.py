#!/usr/bin/env python

import numpy as np
from numpy.linalg import eigh
from numpy import genfromtxt

A = genfromtxt('imputation_missing_10.csv', delimiter=',')
#A = genfromtxt('imputation.csv', delimiter=',')
print('A[0,0] original was 0.0736')
A[0, 0] = 0 # setting unknow value to 0



# Step 5: Eigendecomposition
[Ū, σ̄ , V̄ᵀ] = np.linalg.svd(A)  

# Key Steps	
#	Identified that the core singular vectors
#	Keep only the core singular vectors 
# 	Reconstruct B_lowrank = V Σ V^T
# 	Step 8: Print reconstructed A[0,0]




