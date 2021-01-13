import matplotlib.pyplot as plt
from function import function, get_points 
from interpolation import *
import numpy as np
from timeit import default_timer

n = 20 #number interpolation points

m = 10000
domain = get_points(m) #domain points
xs = get_points(n) #interpolation points
ys = np.array([function(x) for x in xs]) #interpolation points

# Compute solution
y_sol = [function(x) for x in domain]

# Solve interpolation problem with different methods
tic = default_timer()
Ns = [neville(xs, ys, x) for x in domain]
print('Neville took {} seconds'.format(round(default_timer() - tic,2) ))

tic = default_timer()
barycentric = barycentric(xs, ys)
barycentric.pre_compute_weights()
Bs = [barycentric.evaluate(x) for x in domain]
print('Barycentric took {} seconds'.format(round(default_timer() - tic,2) ))

tic = default_timer()
newton_solver = newton(xs, ys)
newton_solver.pre_compute_weights()
Nws = [newton_solver.evaluate(x) for x in domain]
print('Newton took {} seconds'.format(round(default_timer() - tic,2) ))

# Plots
inter_func = ['True function',
        'Neville interpolation', 
        'Lagrange interpolation', 
        'Newton interpolatio']
fig, ax = plt.subplots(nrows=2, ncols=2)

def get_coords(coords):
    y = [coord[1] for coord in coords]
    x = [coord[0] for coord in coords]
    return x, y

px, py = get_coords(ys)

x, y = get_coords(y_sol)
ax[0, 0].plot(x, y, 'r')
ax[0, 0].legend(['True function'])

x, y = get_coords(Ns)
ax[1, 0].plot(x, y, 'b')
ax[1, 0].plot(px, py, 'r o')
ax[1, 0].legend(['Neville interpolation', 'Data points'])

x, y = get_coords(Bs)
ax[0, 1].plot(x, y, 'g')
ax[0, 1].plot(px, py, 'r o')
ax[0, 1].legend(['Lagrange interpolation', 'Data points'])

x, y = get_coords(Nws)
ax[1, 1].plot(x, y, 'y')
ax[1, 1].plot(px, py, 'r o')
ax[1, 1].legend(['Newton interpolation', 'Data points'])

plt.title('PLots test')

# plt.show() #Uncomment if you want to show the plot(s)