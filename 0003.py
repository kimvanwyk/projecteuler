import sys

TARGET = 600851475143
# TARGET = 13195 

i = 2
while i < ((TARGET/2)+1):
    if not TARGET % i:
        # check if larger divisor is prime
        t = TARGET/i
        print 'large:small: ', t, i
        j = 2
        while j < ((t/2)+1):
            if not (t % j):
                # found a divisor, t not prime
                j = t
            else:
                j += 1
        if j < t:
            print t
            sys.exit()
    i += 1
