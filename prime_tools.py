# original Eratosthenes prime sieve from http://www.macdevcenter.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html?page=2
# with additions from https://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python

import itertools

def eratosthenes():
    d = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = d.pop(q, None)
        if p is None:
            d[q*q] = q
            yield q
        else:
            x = 2*p + q
            while x in d:
                x += 2*p
            d[x] = p
