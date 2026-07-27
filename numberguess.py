# number guessing game in python 
import random 
number =  random.randint(1, 100) 

userinput1 = input("I'm thinking of a number try to guess it in ten tries\n")
userinput2 = int(userinput1) 
tries = 0 
while tries != 10 :
    if userinput2 <= 100 & userinput2 >= 0 : 
        if userinput2 == number & tries == 0 : 
            print("congrats, you guessed right on the first try") 
            break 
        elif userinput2 == number & tries != 0 : 
            print("you guessed corect\n") 
            print(f"it took you {tries} tries") 
            break 
        elif userinput2 != number & tries == 8 : 
            tries += 1 
            userinput1 = input("last guess\n") 
            userinput2 = int(userinput1) 
        elif userinput2 != number & tries == 9 :
            print("you have failed to guess the number") 
            print("better luck next time :)")
            tries += 1 
        elif userinput2 != number : 
            print("wrong") 
            tries += 1 
            userinput1 = input("guess again\n") 
            userinput2 = int(userinput1) 
    elif userinput2 < 0 or userinput2 > 100 :
        print("the number is between 0 and 100 btw") 
        userinput1 = input("try guessing again, right this time\n") 
        userinput2 = int(userinput1) 
