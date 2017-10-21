MULTS = [3,5]
MAX = 1000

sum = 0
for i in xrange(MAX):
    if any((not i % m for m in MULTS)):
        sum += i

print sum
