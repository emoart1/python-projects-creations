# problem statement: 
    # Largest Palindrome Product 
    # A palindromic number reads the same both ways 
    # The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99 

    # Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):  
    string = str(number) 
    for idx in range(int(len(string) / 2)): 
        if string[idx] != string[-(idx + 1)]: 
            return(False) 
    return(True) 

def largest_palindrome(min,max): 
    final = 0 
    product = 0 
    for x in range(min, max): 
        for y in range(min, max): 
            product = x * y 
            if is_palindrome(product):
                if final < product: 
                    final = product 
    return(final) 

print(largest_palindrome(100,1000))

