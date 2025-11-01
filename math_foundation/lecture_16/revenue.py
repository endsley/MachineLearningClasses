#!/usr/bin/env python
import numpy as np
from numpy import array


# Gradient of R(x): 
def grad_R(a, p):
	ߜp = -2*p - a + 8
	ߜa = -p - 3*a + 10
	return [ߜp, ߜa]

# Gradient ascent
def optimize_revenue(a = 1, p = 1):
	while True:
		[ߜp, ߜa] = grad_R(a, p)
		if ߜp > 0: p = p + 0.00001
		elif ߜp < 0: p = p - 0.00001
#
		if ߜa > 0: a = a + 0.00001
		elif ߜa < 0: a = a - 0.00001
		#print('a = %.3f, p = %.3f, ߜa = %.3f, ߜp = %.3f'%(a, p, ߜa, ߜp))
		if ߜp < 0.0001 and ߜa < 0.0001: 
			print(f"Optimal p = %.3f, ߜp = %.3f"%(p, ߜp))
			print(f"Optimal a = %.3f, ߜa = %.3f"%(a, ߜa))
			break
	return [a,p]

# Run
optimal_advertising, optimal_pricing = optimize_revenue()


