from prime_tools import eratosthenes

TARGET = 10001

l = 0
for p in eratosthenes():
    l += 1
    if l == TARGET:
        print p
        break
