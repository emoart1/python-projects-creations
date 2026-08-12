# problem statement: 
    # Power Digit Sum 
    # 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26 
    # What is the sum of the digits of the number 2^1000? 

temp = 2 ** 1000 
temp = str(temp) 
final = 0 
for idx in range(len(temp)): 
    final += int(temp[idx]) 

print(final) 

