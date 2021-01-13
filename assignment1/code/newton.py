import argparse

parser = argparse.ArgumentParser(description='Compute s (Assignment 1)')
parser.add_argument('segments', metavar='N', type=int,
                    help='The total time of the voyage')
parser.add_argument('--time', required=True, type=int,
                    help='The total time of the voyage')
parser.add_argument('--distances', required=True, type=int, nargs='+',
                    help='The distance(s) of each segment of the voyage')
parser.add_argument('--speed', required=True, type=int, nargs='+',
                    help='The speed(s) of each segment of the voyage')

args = parser.parse_args()

total_time = args.time
d = args.distances
s = args.speed
n = args.segments
assert n == len(d) == len(s)

def function(c):
    t = 0
    for i in range(n):
        t += d[i]/(s[i]+c)
    return t - total_time

def derivative(c):
    val = 0
    for i in range(n):
        val += -d[i]/(s[i]+c)**2
    return val

def newton_method(x0:int, n:int, error)->int:
    '''
    Computes the root of a function using Newton Method
    args:
        x0 (int): initial guess
        n (int): number of steps
    '''

    prev = curr = x0
    for i in range(1,n):
        curr = prev - function(prev)/derivative(prev)
        if abs(function(curr)) < error:
            return curr, i
        prev = curr
    return curr, i

error = 0.0001
c, i = newton_method(0, 1000, error)
print("It took {} iterations to obtain a c value of {} with an error of {}".format(i, c, error))
# print('The value of f(c) is:', function(c)) #should be zero, or really close to zero

# The value s + c has to be positive for each should
for i in range(n):
    assert s[i] + c > 0