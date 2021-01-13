import numpy as np
from matplotlib import pyplot as plt

def function(x):
    ''' parametric circle function [0, 2pi) -> R^2'''
    return np.array([c[0], c[1]]) + c[2] * np.array([np.cos(x), np.sin(x)])

def derivative(x):
    '''derivative of the function'''
    return c[2] * np.array([-np.sin(x), np.cos(x)])

# Data points
P = np.array([[-1, 1],
              [0, 0],
              [1, 0],
              [2, -2]])
# initial t parameter values
t = np.arange(1, 5, dtype='float32')

n = 3 # number model parameters
m = len(P) # number data points
c = np.zeros(n) #unknowns
# Put data poins into a column vector (makes implemenation easier)
b = P.flatten()

err = 1e10 # init value
old_rmse = rmse = 0
k = 0
eps  = 1e-7 # required convergence error
while err > eps:
    A = np.zeros((2*m, n)) #init matrix A. Note that b vector has been flattened
    j = 0 # init value
    for i in range(m): # step 1) matrix A assembly
        A[j] = np.array([1, 0, np.cos(t[i])]) # first coordinate
        A[j+1] = np.array([0, 1, np.sin(t[i])]) # second coordinate
        j += 2

    # step 2) solve normal equation
    c = np.linalg.inv(A.T.dot(A)).dot(A.T.dot(b))

    # step 3) compute rmse
    r = b - A.dot(c) # residual
    rsme = np.linalg.norm(r)/np.sqrt(m)
    # Error computation. Stop condition
    err = abs(old_rmse - rsme)
    old_rmse = rsme
    
    # step 4) update t
    for i in range(len(t)):
        t[i] = t[i] + ((P[i] - function(t[i])).dot(derivative(t[i]))) / (np.linalg.norm(derivative(t[i])**2))

    # counter variable just to report number of iterations to converge
    k = k + 1

# Log information
print("To reach an error of {} it took {:d} iterations".format(str(eps), k))
print("Optimal parameter values : ", t)
print("Model parameters: ", c)

# Plot result
plt.axis('equal') # same scaling on x and y axis
# Plot the function (is a parametric circle)
domain = np.linspace(0, 2*np.pi) # domain of the function
x, y = np.array([function(x) for x in domain]).T # unpack coordinates
plt.plot(x, y, color='r')

# Plot data points
x, y = P.T # unpack coordinates
plt.scatter(x, y, color='b', marker="+")

# plt.show()
# plt.savefig('./ex2plot.png')