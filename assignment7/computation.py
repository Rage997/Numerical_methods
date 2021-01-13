import numpy as np
import math
from math import factorial

def computeFD_coeff(stencil: [])-> []:
        '''
        Assembles and solve linear system to compute non-centered four points forward difference
        Args:
                stencil []: An array of arbitrary length reprensenting the sampled points
        Returns:
                []: An array of the same length as stencil which contains the coefficients for each point
        '''

        n = len(stencil)
        d = 1
        assert(d < n)

        # assemble A
        A = np.zeros((n, n))
        for i in range(n):
                A[i,:] = np.power(stencil, i)
        # assemble b
        b = np.zeros(n)
        b[d] = math.factorial(d)

        # inv_A = np.linalg.inv(A)
        # x = inv_A.dot(b)
        x = np.linalg.solve(A, b)
        # print('The finite difference coefficients are: ', str(x))
        return x


# Test
points =[-2, 0, 1, 2]
coeff = computeFD_coeff(points)