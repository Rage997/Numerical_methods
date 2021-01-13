import numpy as np


def neville(xs, ys, xp):
    '''
     Solve the interpolation problem of a f:R -> R^2 using
     neville algorithm
    
    Args:
        xs: array of x interpolation points 
        ys: array of y interpolation points
        xp: the interpolation point
    Returns:
        arr(float, float): the evaluation of the polynomial at xp
    '''
    Q = np.copy(ys) # initialize
    n = len(xs)
    for j in range(1, n):
        for i in range(0, n-j): # Complexity O(n^2)
            coeff1 = (xs[i+j] - xp) / (xs[i+j] - xs[i]) 
            # because affine transfomration i.e. a+b=1
            coeff2 = 1 -coeff1
            Q[i] = coeff1 * Q[i] + coeff2 * Q[i+1]
    return Q[0] # polynomial of degree n
        
class barycentric:
    '''
    A class to solve the interpolation problem of a f:R -> R^2 using
     Lagrange polynomial in barycentric form
    '''
    def __init__(self, xs, ys):
        self.xs = xs #One dimensional array of x coords
        self.ys = np.copy(ys) #Two dimensional array of y coords
        self.n = np.size(self.xs) #The number of interpolation points
    
    def pre_compute_weights(self):
        '''Pre computes the weights W independently of x'''
        # w = np.array([1.0]*self.n)
        w = np.ones(self.n) #init
        eps=1.0e-14
        for i in range(0, self.n):
            # TODO something's wrong here
            for j in range(0, self.n):
                if i != j: # Compute weigths w_i = 1/(xi - xj)
                    w[i] = w[i]/(self.xs[i] - self.xs[j] + eps)
                else:
                    continue
        self.w = w # store weigths

    def evaluate(self, x):
        '''Evaluates the polynomial'''
        N = 0 #numerator
        D = 0 #denominator
        eps=1.0e-14
        # eps = 0
        for i in range(self.n):
            if x == self.xs[i]: # P(xs) = ys
                return self.ys[i]
            else:
                W = self.w[i] / (x - self.xs[i] + eps) 
                N += W * self.ys[i] 
                D += W
        return N/D                
            

class newton:
    '''
    A class to solve the interpolation problem of a f:R -> R^2 using
    newton divided differences
    '''

    def __init__(self,xs, ys):
        self.xs = xs #One dimensional array of x coords
        self.ys = np.copy(ys) #Two dimensional array of y coords
        self.n = np.size(self.xs) #The number of interpolation points

    def pre_compute_weights(self):
        v = np.zeros([self.n, self.n, 2])
        # for i in range(self.n): #init P[t_i] = P_i
        #     v[i, 0] = self.ys[i]
        v[::, 0] = self.ys
        # Fill in triangle B_i = P[t_0 ... t_1]
        for j in range(1, self.n):
            for i in range(self.n-j):
                v[i, j] = (v[i+1, j-1] - v[i, j-1]) / (self.xs[i+j] - self.xs[i])        
       
        self.w = v[0, :] #first entry of each row of triangle are our weigths

    def evaluate(self, x):
        P = 0
        for i in range(self.n):
            # B = self.w[i]
            N= 1
            for j in range(i): #N_0(t) = 1
                N = N * (x - self.xs[j])
            P = P + self.w[i] * N
        return P

