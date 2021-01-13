import numpy as np
import matplotlib.pyplot as plt
from bezier import bezier


# The points given in the assignment
points = np.array([
                [200, 200], [200, 500], 
                [600, 500], [600, 300], 
                [900, 500], [400, 800], 
                [900, 800]])

bz1 = bezier(points[:5])
bz2 = bezier(points[4:])

A1, B1 = bz1.compute_coeff()
A2, B2 = bz2.compute_coeff()
handlers = np.concatenate((A1, A2, B1, B2), axis=0)

# Compute the two bezier curves: P0-P4 and P4-P6
path1 = bz1.evaluate_bezier(50)
path2 = bz2.evaluate_bezier(50)
path = np.append(path1, path2, axis=0) # Join bezier
# print((path.shape))

x, y = points[:,0], points[:,1]
px, py = path[:,0], path[:,1]
hx, hy = handlers[:, 0], handlers[:, 1]
# plot
plt.figure()
plt.plot(px, py, 'r-')
plt.plot(x, y, 'bo')
plt.plot(hx, hy, 'go')

# Plot che green convex hull from assignment
convexhull = np.array([ 
                    [200, 200], [146, 446], [270, 570], 
                    [529, 570], [635, 464], [555, 323],
                    [679, 257], [900, 500], [361, 659],
                    [423, 920], [900, 675], [900, 800]
                    ])
cx, cy = convexhull[:, 0], convexhull[:, 1]
plt.plot(cx, cy, 'g-')


plt.gca().invert_yaxis() # to be more similar to assignment image
path = '/Users/rage/Desktop/numerical algortihms/assignment5/'
# plt.savefig(path + 'convex_hull.jpg')
# plt.show()