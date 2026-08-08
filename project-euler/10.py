# problem statement: 
    # Summation of Primes 
    # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17 
    # Find the sum of all the primes below two million 

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2 
    return True

def SummationOfPrimes(limit): 
    num = 1 
    final = 0 
    while num < limit: 
        if is_prime(num): 
            final += num 
        num += 1 
    return(final) 

print(SummationOfPrimes(2000000))

