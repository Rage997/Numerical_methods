import numpy as np


class bezier():
    def __init__(self, points):
        self.points = points
        self.n = len(self.points) - 1

    def compute_coeff(self):
        '''
        Solve linear system B u = P as explained in the latex report
        to compute the handlers A, B
        '''
        n = self.n #size of the problem
        points = self.points
        
        # B matrix assembly
        # Tridiagonal matrix with 4 main diagonal and 1, 1 in other two
        B = 4 * np.identity(n) 
        np.fill_diagonal(B[1:], 1)
        np.fill_diagonal(B[:, 1:], 1)
        #  RHS vector P assembly
        P = [ 4 * points[i] + 2* points[i + 1] for i in range(n)]
        
        # Boundary conditions
        # TEST
        # B[0, 0] = 1
        # B[n-1, n-1] = -1
        # B[n-1, n-2] = 2
        # P[0] = 2* points[0] + 2 * points[1]
        # P[n-1] =  points[n-1]
        B[0, 0] = 2
        B[n - 1, n - 1] = 7
        B[n - 1, n - 2] = 2
        P[0] = points[0] + 2 * points[1]
        P[n-1] = 8 * points[n-1] + points[n]

        # Solve system with any method
        # I did not care about performance here
        # Matrix B is tridiagonal so many methods could be used here
        A = np.linalg.solve(B, P)
        # We now have A. We can get B by employing the relation.
        # Look at the latex report, first equation last system of equations
        B = [0] * n # init
        for i in range(n - 1):
            B[i] = 2 * points[i+1] - A[i+1]
        # Remember: the preios relation is not valid for n-1
        # we have:  b_{n-1} = - 2 b_{n-2} + a_{n-2} + 2 a_{n-1}
        B[n - 1] = -2 * B[n - 2] + A[n - 2] + 2 * A[n - 1]

        # Store and return variables
        self.A = A
        self.B = B
        return A, B

    def compute_spline(self):
        '''Computes a spline composed of piecewise cubic bezier curves'''

        def cubic_bezier(a, b, c, d):
                '''Evaluates a cubic bezier over 4 points (a, b, c, d)'''
                return lambda t: np.power(1 - t, 3) * a + 3 * np.power(1 - t, 2) * t * b + 3 * (1 - t) * np.power(t, 2) * c + np.power(t, 3) * d
        
        # TODO check that A, B are not none
        spline = []
        for i in range(self.n):
            spline.append(cubic_bezier(
                        self.points[i], self.A[i], 
                        self.B[i], self.points[i + 1]))
    
        return spline

    def evaluate_bezier(self, n):
        '''Evalute the bezier curve by sampling n points over interval [0, 1]'''
        spline = self.compute_spline()
        # return np.array of evaluation of the spline
        return np.array([bezier(t) for bezier in spline for t in np.linspace(0, 1, n)])