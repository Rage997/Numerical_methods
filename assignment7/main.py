import sympy as sym
import numpy as np
from computation import computeFD_coeff

# ref: https://docs.sympy.org/latest/modules/functions/index.html
x = sym.Symbol('x')
fun = x**(1./3.) + x

def finite_difference(p, h, stencil, points):
    '''
    Evaluate derivative of f at point p given a FD stencil and points
    i.e.
    stencil = [-1/2, 0, 1/2] and points = [-1, 0, 1] is first derivate with second order accuracy 
    '''
    val = 0
    for i in range(len(points)):
        val += stencil[i] * fun.subs(x, p+points[i]*h)
    return val/h

point = 1 # evaluation point
points =[-2, 0, 1, 2]
coeff = computeFD_coeff(points)

solution = fun.diff().subs(x, point)
print('Symbolically derivative of f(x): ', solution)

errors = []
hs = [10**-k for k in range(1, 16)]

for h in hs:
    numerical = finite_difference(point, h, coeff, points)
    error = abs(solution - numerical)
    print('----------------------------------------------------------------')
    print('Evaluating for h = ', h)
    print('The third order non-centered finite difference derivative of f(x) is: {value}\nwith an error of {err} '.format(
        value=numerical, err=error) )
    ('----------------------------------------------------------------')
    errors.append(error)

# Plot error with different h

from matplotlib import pyplot as plt


plt.figure()
plt.suptitle('Error in function of h')
plt.semilogy(errors, hs, 'r', label="error")
# plt.xscale('log')
plt.xlabel('Error')
plt.ylabel('h')
plt.legend()
# plt.savefig('./report/error_plot.png')
# plt.show()

# print(errors)
