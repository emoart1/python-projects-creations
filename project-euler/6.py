# problem statement: 
    # Sum Square Difference 
    # The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385 
    # The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025 
    # Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
    # 3025 - 385 = 2640 
    # Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum 

def SumSquareDifference(limit): 
    x = 1 
    sum = 0 
    squares = 0 
    final = 0 
    while x <= limit :  
        sum += x 
        squares = squares + (x ** 2) 
        x += 1 
    final = (sum ** 2) - squares 
    return(final)

print(SumSquareDifference(100))

