# problem statement: 
    # 10 001st Prime 
    # By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13 
    # What is the 10001st prime number? 

def is_prime_1(n): 
    if n <= 1: 
        return False 
    if n == 2: 
        return True 
    if n % 2 == 0: 
        return False 
    
    limit = int(n ** 0.5) + 1 
    for i in range(3, limit, 2): 
        if n % i == 0: 
            return False 
    return True 

def is_prime_2(n):
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

def prime1(num):
    x = 0 
    temp = 1
    final = 0 
    while x != num: 
        if is_prime_1(temp): 
            final = temp 
            x += 1 
        temp += 1 
    return(final)

def prime2(num):
    x = 0 
    temp = 1
    final = 0 
    while x != num: 
        if is_prime_2(temp): 
            final = temp 
            x += 1 
        temp += 1 
    return(final)

print(prime1(10001)) 
print(prime2(10001)) 

# both are good but prime2 is better for really big numbers 
