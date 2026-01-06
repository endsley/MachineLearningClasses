#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# Heart implicit function:
# f(x,y) = (x^2 + y^2 - 1)^3 - x^2 y^3
def f_xy(x, y):
	r = x*x + y*y
	a = r - 1.0
	return a*a*a - (x*x)*(y*y*y)

# ∂f/∂y = 3(x^2 + y^2 - 1)^2 * 2y - x^2 * 3y^2
#       = 6y(x^2 + y^2 - 1)^2 - 3x^2 y^2
def df_dy(x, y):
	r = x*x + y*y
	a = r - 1.0
	return 6.0*y*(a*a) - 3.0*(x*x)*(y*y)

# We minimize g(y) = f(x,y)^2 for fixed x via gradient descent:
# g'(y) = 2 f(x,y) * ∂f/∂y
def minimize_f2_for_y(x, y0, lr=0.01, steps=4000, tol_f=1e-8, tol_step=1e-10, clip_grad=1e6):
	y = float(y0)
	prev_y = y

	for _ in range(steps):
		fv = f_xy(x, y)
		if abs(fv) < tol_f:
			break

		grad = 2.0 * fv * df_dy(x, y)
		if clip_grad is not None:
			grad = float(np.clip(grad, -clip_grad, clip_grad))

		y = y - lr * grad

		if abs(y - prev_y) < tol_step:
			break
		prev_y = y

	return y, abs(f_xy(x, y))

def unique_by_tolerance(values, tol=1e-4):
	# values: list of (y, err)
	values = sorted(values, key=lambda t: t[0])
	uniq = []
	for y, err in values:
		if len(uniq) == 0:
			uniq.append((y, err))
			continue
		if abs(y - uniq[-1][0]) > tol:
			uniq.append((y, err))
		else:
			# keep the better one (smaller error)
			if err < uniq[-1][1]:
				uniq[-1] = (y, err)
	return uniq

def two_y_solutions_for_x(x,
		inits=(1.5, 1.3, 1, 0.8, 0.6, 0.4, 0.3, 0.2, -0.2, -0.3, -0.4, -0.6, -0.8, -1, -1.3, -1.5),
		lr=0.01,
		steps=4000,
		tol_f=1e-8,
		uniq_tol=1e-3,
		max_err_accept=5e-4):
	candidates = []
	for y0 in inits:
		y, err = minimize_f2_for_y(x, y0, lr=lr, steps=steps, tol_f=tol_f)
		candidates.append((y, err))

	# Deduplicate by y-value (different initializations can converge to same branch)
	candidates = unique_by_tolerance(candidates, tol=uniq_tol)

	# Keep only “good enough” solutions
	candidates = [(y, err) for (y, err) in candidates if err <= max_err_accept]

	# Sort by error then pick up to two distinct solutions
	candidates = sorted(candidates, key=lambda t: t[1])

	sols = []
	for y, err in candidates:
		ok = True
		for yy, _ in sols:
			if abs(y - yy) < uniq_tol:
				ok = False
				break
		if ok:
			sols.append((y, err))
		if len(sols) == 2:
			break

	# Return up to 2 y-values (could be 0/1/2 depending on x and convergence)
	return [y for (y, _) in sols]

def sample_heart_points(num_x=400, x_min=-1.4, x_max=1.4):
	xs = np.linspace(x_min, x_max, num_x)

	top = []
	bot = []

	for x in xs:
		ys = two_y_solutions_for_x(
			x,
			inits=(1.5, 1.3, 1, 0.8, 0.6, 0.4, -0.4, -0.6, -0.8, -1, -1.3, -1.5),
			lr=0.01,
			steps=20000,
			tol_f=1e-10,
			uniq_tol=2e-2,
			max_err_accept=2e-4
		)
		print(x, ys)
		if len(ys) == 0:
			continue

		ys = sorted(ys)
		# Usually bottom is smaller y, top is larger y
		if len(ys) == 1:
			# Fallback: assign to whichever side makes sense
			if ys[0] >= 0:
				top.append((x, ys[0]))
			else:
				bot.append((x, ys[0]))
		else:
			bot.append((x, ys[0]))
			top.append((x, ys[-1]))

	# Convert to arrays
	top = np.array(top, dtype=float) if len(top) else np.zeros((0, 2))
	bot = np.array(bot, dtype=float) if len(bot) else np.zeros((0, 2))

	# Build a single closed path (top left->right, then bottom right->left)
	path = None
	if len(top) and len(bot):
		path = np.vstack([top, bot[::-1]])
	elif len(top):
		path = top
	elif len(bot):
		path = bot

	return top, bot, path

def main():
	top, bot, path = sample_heart_points(num_x=1200, x_min=-1.14, x_max=1.14)

	plt.figure()
	if path is not None and len(path):
		plt.plot(path[:, 0], path[:, 1])
	else:
		if len(top):
			plt.scatter(top[:, 0], top[:, 1], s=5)
		if len(bot):
			plt.scatter(bot[:, 0], bot[:, 1], s=5)

	plt.gca().set_aspect('equal', adjustable='box')
	#plt.axis('off')
	plt.show()

if __name__ == "__main__":
	main()
