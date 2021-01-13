import numpy as np
from matplotlib import pyplot as plt
from function import function
from solver import thomas_tridiagonal_solver

degree = 3 #the degree of the b-spline

def N(x, i, j, t):  
    # basis functions
    if j == 0:
        if (x == len(t) - (2*degree + 1) and i == len(t) - (2*degree - 1)) or (x >= t[i] and x < t[i+1]):
            return 1
        else:
            return 0
    else:
        left = 0 if t[i+j] == t[i] \
            else N(x, i, j-1, t) * (x - t[i])/(t[i+j]-t[i])
        right = 0 if t[i+j+1] == t[i + 1] \
            else N(x, i+1, j-1, t) * (t[i+j+1] - x)/(t[i+j+1]-t[i+1])
        return left + right

def de_boor(s):  
    # De Boor algorithm to evaluate b-spline

    k = 0
    while t[degree+k+1] < s:
        k += 1
    E = np.empty((0, 2))
    for i in range(degree+1):
        E = np.vstack((E, D[i+k]))
    for j in range(1, degree+1):
        for i in range(degree-j+1):
            E[i] = (t[degree+i+k+1]-s)/(t[degree+i+k+1]-t[i+k+j])*E[i] + \
                (s-t[i+k+j])/(t[degree+i+k+1]-t[i+k+j])*E[i+1]
    return E[0]


fig, ax = plt.subplots(nrows=2, ncols=1)

for n in [10, 20, 40]:
    # Init for plotting
    plt.figure(n)
    plt.suptitle("B-Spline n=" + str(n))

    m = n - 1
    # Crate the knot vector
    t = np.arange(n+1)
    t = np.append([0]*degree, t)
    t = np.append(t, [n]*degree)

    domain = np.linspace(-1, 1, n+1)
    P = np.array([function(x) for x in domain]) #the interpolation points
    # Matrix M containing basis functions
    M = np.empty((m+degree-1, m+degree+1))
    for i in range(m+degree-1):
        for j in range(m+degree+1):
            M[i][j] = N(t[i+degree], j, degree, t)
    # Solve linear system and obtain the control points
    D = np.linalg.lstsq(M, P, rcond=-1)[0]
    x, y = D.T
    plt.plot(x, y, 'g', label="Control points")

    # Evaluation
    evaluate = np.linspace(0, n, num=10000)
    bspline = np.empty((0, 2))
    for s in evaluate:
        F = de_boor(s)
        bspline = np.vstack((bspline, F))

    x, y = bspline.T
    plt.plot(x, y, 'r', label="B-Spline")
    plt.legend()
    # plt.savefig("/home/rage/Desktop/code/" + 'result' + str(n) + '.jpg')
