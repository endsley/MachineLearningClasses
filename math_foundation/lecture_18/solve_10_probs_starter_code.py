#!/usr/bin/env python
import numpy as np
from scipy.optimize import minimize

# Problem 1
def f1(x):  # $$ f(x) = x^2 - 4x + 3 $$
    return x[0]**2 - 4*x[0] + 3


# Problem 2
def f2(x):  # $$ f(x) = 2x^2 - 8x + 5 $$
    return 2*x[0]**2 - 8*x[0] + 5


# Problem 3
x_start = [0,0]
def f3(v):  # $$ f(x, y) = x^2 + y^2 - 6x - 4y + 13 $$
    x, y = v
    return x**2 + y**2 - 6*x - 4*y + 13




# Problem 4
x_start = [0,0]
def f4(v):  # $$ f(x, y) = (x-2)^2 + (y+1)^2 $$
    x, y = v
    return (x - 2)**2 + (y + 1)**2

# Problem 5
Q5 = np.array([[2, 0], [0, 2]])
c5 = np.array([4, 6])
x_start = [0,0]
def f5(x):  # $$ f(x) = x^T Q x - c^T x $$
    return x @ Q5 @ x - c5 @ x


# Problem 6
Q6 = np.array([[1, 1], [1, 2]])
c6 = np.array([1, 1])
x_start = [0,0]
def f6(x):  # $$ f(x) = \frac{1}{2} x^T Q x - c^T x $$
    return 0.5 * x @ Q6 @ x - c6 @ x


# Problem 7
A7 = np.array([[3, 0], [0, 1]])
b7 = np.array([6, 2])
x_start = [0,0]
def f7(x):  # $$ f(x) = x^T A x - b^T x $$
    return x @ A7 @ x - b7 @ x


# Problem 8
c8 = np.array([5, -3])
def f8(x):  # $$ f(x) = ||x - c||^2 $$
    return np.sum((x - c8)**2)


# Problem 9
one = np.array([1, 1])
def f9(x):  # $$ f(x) = (x - 1)^T (x - 1) $$
    return np.sum((x - one)**2)


# Problem 10
def f10(v):  # $$ f(x, y, z) = x^2 + y^2 + z^2 - 2x - 4y + 6z $$
    x, y, z = v
    return x**2 + y**2 + z**2 - 2*x - 4*y + 6*z

