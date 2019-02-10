import math

n = int(input())
divisors = []

for i in range(2,int(math.sqrt(n))+1):
    if n % i == 0:
        divisors.extend([i,int(n/i)])

if len(divisors) != 0:
    print(sorted(divisors))
print('{} is a prime number'.format(n))
