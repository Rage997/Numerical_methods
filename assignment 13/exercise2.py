import numpy as np
import cmath
from matplotlib import pyplot as plt

def function(x):
    return 10/(1+(10*x - 5)**2)

def reverse_bit(n):
    # ref: https://stackoverflow.com/questions/12681945/reversing-bits-of-python-integer
    return int('{:08b}'.format(n)[::-1], 2)

def fft_helper(f_k):
    ''' Fast Fourier transform'''
    two_n = len(f_k)
    if two_n >= 2:
        # fft(f0, fn, f1, fn+1 ...) = fft(fo, f1 ... fn-1) + exp(-ikpi/n) fft(fn ... f2n-1)
        # see lecture notes
        
        first = fft_helper(f_k[0:two_n//2])
        second = fft_helper(f_k[two_n//2:two_n])

        z = np.array([np.exp(-1j * 2 * np.pi * k / two_n)
                      for k in range(two_n//2)])

        k = z * second
        return np.append((first + k), (first - k))
    else:
        # root of the tree
        return f_k

def fft(data):
    n = len(data)
    # compute recursively each tree node and then scale the result by sqrt(n)
    return np.array(fft_helper(data))/np.sqrt(n)

m = 8
n = 2**m

# Compute function sample points
points = np.array([reverse_bit(x) for x in np.arange(n)])
f_j = np.array([function(x/n) for x in points])

f_hat = fft(f_j)
#f_hat = np.array(fft(f_j))/np.sqrt(n)
# print(f_hat)

# Plot
real = [x.real for x in f_hat]
imag = [x.imag for x in f_hat]
plt.plot(real, label='Real part')
plt.plot(imag, label='Imaginary part')
plt.legend()
# plt.show()
plt.savefig('./plot.png')