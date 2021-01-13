import argparse

# Argument parsers
parser = argparse.ArgumentParser(description='Compute c (Assignment 1)')
parser.add_argument('segments', metavar='N', type=int,
                    help='The total time of the voyage')
parser.add_argument('--time', required=True, type=int,
                    help='The total time of the voyage')
parser.add_argument('--distances', required=True, type=int, nargs='+',
                    help='The distance(s) of each segment of the voyage')
parser.add_argument('--speed', required=True, type=int, nargs='+',
                    help='The speed(s) of each segment of the voyage')

# Read args
args = parser.parse_args()
total_time = args.time
d = args.distances
s = args.speed
n = args.segments
assert n == len(d) == len(s)

def check(c, n, s, d, tot_time):
    ''' 
    Checks for a given parameters if a value of c is too big or too small
    '''
    t = 0
    for i in range(n):
        if c+s[i] <= 0: # the true speed is always positive!
            return 1 #increase c
        else: # add time to traverse each segment
            t+=d[i]/(s[i]+c) # time = distance/speed
    if(t>tot_time): #if the sum of the time for each segment is greater whole journey time
        return 1 #increase c
    else: #if the sum of the time for each segment is less than whole journey time
        return 0 #decrease c

# init variables
# the root has to be inside the interval [low, high]
low = -500
high = 500
max_step = 2200
error = 0.0001 # stop criteria for error

# solve problem
for i in range(max_step):
    # this is bisection method no newton
    mid = (high+low)/2
    # print(mid)
    if check(mid, n, s, d, total_time):
        low=mid
    else:
        high=mid
    if high - low < error:
        break
c = mid

print("It took {} iterations to obtain a c value of {} with an error of {}".format(i, c, error))