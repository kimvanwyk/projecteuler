# initial generator reminder from https://www.python-course.eu/generators.php

MAX = 4000000

def fibonacci():
    (a, b) = (1, 2)
    while True:
        yield a
        (a, b) = (b, a + b)
        if a > MAX:
            raise StopIteration

total = 0
for x in fibonacci():
    if not x % 2:
        total += x

print total
    
