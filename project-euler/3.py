# problem statement: 
    # Largest Prime Factor 
    # The prime factors of 13195 are 5, 7, 13 and 29 
    # What is the largest prime factor of the number 600851475143? 

def largest_prime_factor(number):
    max_prime = -1
    
    while number % 2 == 0:
        max_prime = 2
        number //= 2  

    i = 3
    while i * i <= number:
        while number % i == 0:
            max_prime = i
            number //= i
        i += 2
        
    if number > 2:
        max_prime = number
        
    return max_prime

print(largest_prime_factor(600851475143))
