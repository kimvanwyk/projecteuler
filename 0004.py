MAX = 999

import sys

def is_palindrome(s):
    return all((s[d] == s[-d-1]) for d in xrange(len(s)/2))

pals = []
for x in xrange(MAX,0,-1):
    for y in xrange(MAX,0,-1):
        v = x*y
        # print x,y,v
        if is_palindrome(str(v)):
            pals.append(v)

print max(pals)
