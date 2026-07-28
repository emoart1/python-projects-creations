# number guessing game in python 
import random 
number =  random.randint(1, 100) 
print(number) 
tries = 1 
guess = int(input("I'm thinking of a number try to guess it in ten tries\n")) 
while tries != 11 :
    if 0 <= guess <= 100 : 
        if guess == number : 
            if tries == 1 : 
                print("congrats, you guessed right on the first try") 
                break 
            else : 
                print("you guessed corect") 
                print(f"it took you {tries} tries") 
                break
        elif guess != number : 
            if tries == 10 : 
                print("you have failed to guess the number") 
                print("better luck next time :)")
                tries += 1 
            elif tries == 9 : 
                tries += 1 
                guess = int(input("last guess\n")) 
            else : 
                if number < guess : 
                    print("too high, try lower")
                elif number > guess :  
                    print("too low, try higher")
                tries += 1 
                guess = int(input("guess again\n"))
    elif guess < 0 or guess > 100 :
        print("the number is between 0 and 100 btw") 
        guess = int(input("try guessing again, right this time\n")) 
      