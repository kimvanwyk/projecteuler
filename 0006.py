MAX = 100

sum_sq = 0
total = 0

for i in xrange(1,MAX+1):
    sum_sq += i**2
    total += i
print total**2 - sum_sq
