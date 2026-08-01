# Register
    # We are really pleased that you are interested in joining the Project Euler community 
    # Hopefully you have already taken the time to look at problems in the Archives to see what challenges lie ahead 

    # To complete registration, we would like you to get a real taste of Project Euler problems for yourself by solving "Problem Zero" 
    # The problems will certainly become more difficult and you are going to require a growing combination of mathematical knowledge and programming skills as you progress through the problem set 
    # So, if you enjoy being challenged and would like to develop your problem solving skills, then to quote the sentiments of Plato: "Let none but enquiring minds enter" 

# problem statement: 
    # Problem Zero 
    # A number is a perfect square, or a square number, if it is the square of a positive integer 
    # For example, 25 is a square number because 5 ** 2 = 5 * 5 = 25; it is also an odd square 
    
    # The first 5 square numbers are: 1, 4, 9, 16, 25, and the sum of the odd squares is 1 + 9 + 25 = 35 
    # Among the first 993 thousand square numbers, what is the sum of all the odd squares? 

def squares(limit): 
    toSquare = 1 
    total = 0 
    while toSquare != (limit + 1): 
        square = toSquare ** 2 
        if square % 2 != 0: 
            total += square 
        toSquare += 1 

    return(total) 
 
print(squares(993_000)) 

