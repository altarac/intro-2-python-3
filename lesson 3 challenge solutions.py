def primeCheck(num):
    factors = []
    for i in range(2, num):
        if num%i == 0:
            factors.append(i)
        else:
            pass
        
    if len(factors) == 0:
        return num
    else:
        return 0


primes = []
n = int(input('number? '))
for i in range(2, n):
    primes.append(primeCheck(i))

print(sum(primes))
