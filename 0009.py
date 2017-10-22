from math import sqrt
import sys

TARGET = 1000

t = TARGET/2

for c in xrange(t,0,-1):
    for b in xrange(c-1,0,-1):
        for a in xrange(b-1,0,-1):
            # print a,b,c
            if (a**2 + b**2 == c**2) and (a+b+c == TARGET):
                print a*b*c
