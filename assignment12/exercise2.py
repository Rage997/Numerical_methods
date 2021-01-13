#!/usr/bin/env python2.7
import numpy as np

# Read links
links = []
with open('links.txt') as file:
    for line in file.readlines():
        x, y = line.split(' ')
        x, y = int(x), int(y)
        links.append([x, y])
links = np.array(links) 

# Get number pages (n) and links (m). First line gives it
n, m = links[0]
A = np.zeros((n, n))

# All the reaming lines give wheter there s link betwen node i and j
# Because of indexing you need to subtract one from each (i.e. matrix start at 0 not 1)
for k in range(1, m+1):
    # A_ij = 1 if page j links to page i
    # The txt gives i links j therefore swap indexes i, j
    j, i = links[k]
    A[i-1, j-1] = 1

# Add page 14 self-loop
A[13, 13] = 1

# Divide each entry by sum (sort of normalization)
for i in range(n):
    n_j = sum(A[:, i])
    A[:, i] = A[:, i]/n_j

# Constant
x = np.ones(n)/n
prev_x = x * 100 # just to be sure the norm is large
e = np.ones(n)
mu = 0.15
tol = 10e-9
k = 0

# Pretty ugly but useful flags to print logs only once in the next for loop
norm_flag = True
equal_flag = True
while(norm_flag or equal_flag):
    prev_x = x # save previous iteration (just used for convergence check)
    x = (1 - mu) * np.dot(A, x) + mu/n * e
    k += 1

    if np.linalg.norm(x - prev_x, ord=np.inf) < tol and norm_flag:
        norm_flag = False
        print('The norm L_inf(x, prev_x) took {} iterations to converge'.format(k))
    
    if np.all(np.argsort(x) == np.argsort(prev_x)) and equal_flag:
        equal_flag = False
        print('The results do not change after {} iterations'.format(k))

rank = np.argsort(x) + 1 # add one back (as mentioned before matrix start at 0)
print('The result ranking of the web pages is: \n {}'.format(rank))

