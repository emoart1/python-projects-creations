# problem statement:
    # Multiples of 3 or 5 
    # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9 
    # The sum of these multiples is 23 
    # Find the sum of all the multiples of 3 or 5 below 1000 

def is_multiple(number0): 
    number2 = 0 
    number3 = 0 
    number2 = number0 % 3 
    number3 = number0 % 5 
    if number2 == 0 or number3 == 0: 
        return(number0) 
    else: 
        return 0 

x = 0 
y = 0 
z = 0 

while x != 1000: 
    y = is_multiple(x) 
    z += y 
    x += 1 

print(z) 

