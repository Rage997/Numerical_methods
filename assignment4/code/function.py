from math import cos, sin
import numpy as np

def function(t):
    sc = (25.*t**2+2.)/(25.*t**2+1.)
    arr = np.array([sin(np.pi/2. * t), cos(np.pi/2. * t)], dtype=float)
    return  sc*arr


def get_points(n):
    '''Return n+1 points given the formulas in the assignment'''

    def get_point(i):
        return (2.*i)/n - 1.

    return [get_point(i) for i in range(0, n+1)]
    