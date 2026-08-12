# problem statement: 
    # Longest Collatz Sequence
    # The following iterative sequence is defined for the set of positive integers: n -> n/2 (n is even)    n -> 3n + 1 (n is odd) 
    # Using the rule above and starting with 13 , we generate the following sequence: 
    # 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1 
    # It can be seen that this sequence (starting at 13 and finishing at 1) contains  terms 
    # Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1 
    # Which starting number, under one million, produces the longest chain? 
    # NOTE: Once the chain starts the terms are allowed to go above one million 

def LongestCollatzSequence(): 
    pass 
    limit = 1_000_000 
    cycle = 0 
    countofsequence = 0 
    num = 13 
    n = num
    final = 0 
    while num < limit: 
        while n != 1: 
            if n % 2 == 0: 
                n = n / 2 
            elif n % 2 != 0: 
                n = (3 * n) + 1 
            cycle += 1 
        if cycle > countofsequence: 
            final = num 
            countofsequence = cycle 
        num += 1 
        n = num 
        cycle = 0 
    return(final)

print(LongestCollatzSequence()) 

