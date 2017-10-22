from prime_tools import eratosthenes

MAX = 2000000

total = 0
for p in eratosthenes():
    if p >= MAX:
        print total
        break
    total += p
    
