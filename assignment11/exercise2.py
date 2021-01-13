#!/usr/bin/env python2.7

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import cm

n = 50 # Number of points
iterations = 1000
mod = 50 # plot only for k % mod  == 0
a, b = -1, 1 # the interval on where generate the random polygons

for i in range(3):
    plt.figure(i)
    
    P = (b-a)*np.random.rand(n, 2) + a
    # To impose sum(x) = sum(y) = 0 is equivalent that the centroid of x, y is 0
    # which means to subtract the centroid from all points
    centroid = sum(P)/n
    P = P - centroid
    
    # Generate averaging matrix 
    M = np.eye(n, n) + np.eye(n, n, k=1) 
    M[-1, 0] = 1
    x, y = P.T
    
    # ref: https://stackoverflow.com/questions/14720331/how-to-generate-random-colors-in-matplotlib
    cmap = plt.cm.get_cmap('hsv', iterations / mod + 1)
    # It was not asked to but I think that plotting the initial polygon makes it more clear
    plt.fill(x, y, edgecolor=cmap(1), fill=False)

    for k in range(iterations):
        # Multiply points by averaging matrix
        MP = np.matmul(M, P)
        P =  MP /np.linalg.norm(MP)
        if k % mod == 0 and k != 0: # Do plots for some iterations
            x, y = P.T
            plt.fill(x, y, edgecolor=cmap( iterations/k  + 1), fill=False)

    plt.axis('equal')
    plt.xlabel('Iterations for mod(k, 50) = 0')
    #plt.show()
    plt.savefig('report/plot' + str(i+1) + '.png')
