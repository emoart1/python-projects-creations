# problem statement: 
    # Smallest Multiple 
    # 2520  is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder 
    # What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 

def isevenlydivisibleby1to20(num):
    if final % 11 != 0:
        return False 
    if final % 12 != 0: 
        return False 
    if final % 13 != 0: 
        return False 
    if final % 14 != 0: 
        return False 
    if final % 15 != 0: 
        return False 
    if final % 16 != 0: 
        return False 
    if final % 17 != 0: 
       return False 
    if final % 18 != 0: 
       return False 
    if final % 19 != 0: 
       return False 
    if final % 20 != 0: 
       return False 
    return True

final = 20 

while not isevenlydivisibleby1to20(final): 
    final = final + 20

print(final)

