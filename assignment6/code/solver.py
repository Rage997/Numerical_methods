import numpy as np

def thomas_tridiagonal_solver(a, b, c, d):  
    # Solve a tridiagonal linear system using thomson algorithm
    # ref: https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
    n = len(d)
    for i in range(n-1):
        d[i+1] -= 1. * d[i] * a[i] / b[i]
        b[i+1] -= 1. * c[i] * a[i] / b[i]
    for i in range(n-1, 0, -1):
        d[i] -= d[i+1] * c[i] / b[i+1]
    return np.array([d[i] / b[i] for i in range(n)])