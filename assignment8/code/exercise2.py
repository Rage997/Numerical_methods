import numpy as np

def f(x):
    return np.exp(x)

# real solution, compute analytically: e^2 - e^1
solution = np.exp(2) - np.exp(1)

N = 5 #max_iter / matrix size
a, b = 1, 2 # interval
R = np.zeros((N, N)) #matrix containing all iterations R[j][i]
j = 0 #init value

while True:
    m = 2**(j)
    h = (b-a)/m
    for i in range(1, m-1):
        # Fill in first column
        R[j][0] += f(a+(i-1/2)*h) * h

    K = 4
    for k in range(1, j+1):
        # Richardson extrapolation to fill in remaining columns
        R[j][k] = (K*R[j][k-1] - R[j-1][k-1])/(K-1.0)
        K *= 4
    
    j += 1
    if j >= N:
        print('Iterations: ', j)
        print('Numerical solution: ', R[-1][-1])
        print('Analytical solution: ', solution)
        print('Absolute error: ', abs(solution - R[-1][-1]))
        break
