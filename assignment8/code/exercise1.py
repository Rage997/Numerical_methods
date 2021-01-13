import numpy as np
from sympy import Symbol, integrate, sin, N

'''
Python script to numerically integrate a function over an interval [a, b]
using a 4 order open composite newton-cotes method
'''

def function(x):
    return np.sin(x)/x

# Constants
weights = (4/3) * np.array([2, -1, 2]) # the computation are shown in the report

def newton_cotes(a, b):
    sol = 0
    h = (b-a)/4
    # Open newton-cotes of order n
    for i in range(1, 4):
        x = a + i*h
        sol += weights[i-1] * function(x)
    return h*sol

# Split interval a,b into 100 pieces
m = 100
a, b = 0, 1
xs = np.linspace(a, b, 2)

numerical_solution = 0
for i in range(0, xs.size//2, 2):
    numerical_solution += newton_cotes(xs[i], xs[i+1])

# Compute analytical solution by symbolically integration
def symbolically_integrate():
    x = Symbol('x')
    return N(integrate(sin(x)/x, (x, a, b)))
analytical_solution = symbolically_integrate()

print('Numerical solution: ', numerical_solution)
print('Analytical solution: ', analytical_solution)
print('Absolute error: ', abs(analytical_solution - numerical_solution))