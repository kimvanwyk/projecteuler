MAX_DIV = 20

i = MAX_DIV
while True:
    if all((not i % d) for d in xrange(2,MAX_DIV+1)):
        print i
        break
    i += 1
