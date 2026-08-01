# problem statement: 
    # Largest Prime Factor 
    # The prime factors of 13195 are 5, 7, 13 and 29 
    # What is the largest prime factor of the number 600851475143? 

def largest_prime_factor(number):
    # Track the largest prime factor found
    max_prime = -1
    
    # Step 1: Remove all factors of 2
    while number % 2 == 0:
        max_prime = 2
        number //= 2  # Integer division to reduce 'number'
        
    # Step 2: Remove odd factors up to the square root of 'number'
    # We increment by 2 to skip even numbers (3, 5, 7, 9...)
    i = 3
    while i * i <= number:
        while number % i == 0:
            max_prime = i
            number //= i
        i += 2
        
    # Step 3: If n is still greater than 2, then 'number' itself is prime
    if number > 2:
        max_prime = number
        
    return max_prime

print(largest_prime_factor(600851475143))
