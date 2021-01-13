import numpy as np
import math
from matplotlib import pyplot as plt

P = np.array([[-1, 1],
              [0, 0],
              [1, 0],
              [2, -2]])

t = np.array([1, 2, 3, 4], dtype='float32')

c = np.zeros(3)
b = P.reshape(-1)

m = 4
n = 3


def f(x):
    return np.array([c[0], c[1]]) + c[2] * np.array([math.cos(x), math.sin(x)])


def f1(x):
    return c[2] * np.array([-math.sin(x), math.cos(x)])


err = 2
prev_rmse = 0
k = 0
while(err > 10e-8):
    A = np.zeros((2*m, n))
    j = 0
    for i in range(m):
        A[j] = np.array([1, 0, math.cos(t[i])])
        A[j+1] = np.array([0, 1, math.sin(t[i])])
        j += 2

    c = np.linalg.inv(A.T.dot(A)).dot(A.T.dot(b))

    for i in range(len(t)):
        t[i] = t[i] + ((P[i] - f(t[i])).dot(f1(t[i]))) / \
            (np.linalg.norm(f1(t[i])**2))
        t[i] = t[i] % (2*np.pi)

    e = b - A.dot(c)
    rsme = np.linalg.norm(e)/math.sqrt(m)
    err = abs(prev_rmse - rsme)
    prev_rmse = rsme
    k = k + 1

print("Iteration k: %d" % k)
print("t:")
print(t)
print("c:")
print(c)

plt.axis('equal')
space = np.linspace(0, 2*math.pi)
x, y = np.array([f(x) for x in space]).T
plt.plot(x, y)


x, y = P.T
plt.scatter(x, y, color='r', marker=".")

plt.show()
