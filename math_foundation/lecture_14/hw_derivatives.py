#!/usr/bin/env python
import autograd.numpy as np
from autograd import grad

# (a)
f_a = lambda x: 2*x**2 + 1
fᑊ_a = lambda x: 4*x

# (b)
f_b = lambda x: np.exp(x**2)
fᑊ_b = lambda x: 2*x*np.exp(x**2)

# (c)
f_c = lambda x: (3*x - 2)**2
fᑊ_c = lambda x: 6*(3*x - 2)

# (d) choose your own n, y_i for verification
y = np.array([1.0, 4.0, -2.0, 3.0])   # n=4 example
f_d = lambda x: np.sum((3*x - y)**2)
fᑊ_d = lambda x: 6*np.sum((3*x - y))

# (e)
f_e = lambda x: np.log(1/x) / np.log(2.0)
fᑊ_e = lambda x: (1/x)*(1/np.log(2))

# (f)
f_f = lambda x: np.log((x - 2)**2) / np.log(2.0)
fᑊ_f = lambda x: 2/((x-2)*np.log(2))

for name, f, fᑊ, x0 in [
	("a", f_a, fᑊ_a, 2.0),
	("b", f_b, fᑊ_b, 2.0),
	("c", f_c, fᑊ_c, 2.0),
	("d", f_d, fᑊ_d, 2.0),
	("e", f_e, fᑊ_e, 2.0),
	("f", f_f, fᑊ_f, 3.0),   # avoid x=2
]:
	df = grad(f)
	print(name, "x0=", x0, "autograd f'=", df(x0), "Theoretical f'=", fᑊ(x0))
