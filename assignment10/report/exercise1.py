import numpy as np
from matplotlib import pyplot as plt

# Circle centers and radiuses
C = np.array([[-2, 0],
              [2, 1],
              [2, -1],
              [0, 2]], dtype='float32')

R = np.array([2, 1, 1, 1], dtype='float32')
m = len(C) #number circles

w = np.ones(m) #weights initially set to one
P = np.array([.5, .5], dtype='float32') # initial guess

def residual(x, y):
    # Residual || P - C|| - R
    return np.array([np.sqrt((x-C[i][0])**2 + (y-C[i][1])**2) - R[i] for i in range(m)], dtype='float32')

def derivative_residual(x, y):
    # Jacobian of the residual
    return np.array([[(2*x - 2*C[i][0])/(2*np.sqrt((x-C[i][0])**2 + (y-C[i][1])**2)),
                      (2*y - 2*C[i][1])/(2*np.sqrt((x-C[i][0])**2 + (y-C[i][1])**2))] for i in range(m)], dtype='float32')

iterations = [P] # array to keep track of iterations. It will be later used for plotting
convergence = False
tol = 1e-10 # 10 digits of acuracy
max_iters = 10000 # just to avoid looping for ever. No problem for the data given but I've tested the code with different sets of circle
while not convergence and len(iterations) < max_iters: # until convergence
    # Compute P_k - (M^T W M)^{-1} M^T W P_k to get P_{k+1} 
    M = derivative_residual(P[0], P[1])
    # gauss newton (with diagonal matrix containing weights)
    P = P - np.linalg.inv(M.T @ np.diag(w) @ M) @ \
        M.T @ np.diag(w) @ residual(P[0], P[1])
    w = 1/residual(P[0], P[1]) # reset weights

    iterations.append(P) # add new iteration
    # stop condition: P_{k+1} - P_k < tol
    if np.linalg.norm(iterations[-1] - iterations[-2]) < tol:
        convergence = True

ax = plt.gca()
# Plot iterations
iterations = np.array(iterations)
x, y = iterations.T
ax.plot(x, y, 'r')
ax.plot(P[0], P[1], 'b*')
ax.axis('equal')
ax.axis([0, 1, 0.2, 1])

for i in range(m): # plot circles
    circle = plt.Circle(C[i], R[i], color='g')
    ax.add_artist(circle)
# plt.show()
plt.savefig('plot2.png')

# Console logs
abs_norm = sum(np.abs(residual(P[0], P[1])))

print('It took {} iterations to get an error of the residual (abs norm) of {}'.format(
    len(iterations), 
    abs_norm
        )
    )

print('The least squares solution is point P: {}; with the weights: {} '.format(
    iterations[-1],
    w)
    )