# number guessing game in python 
import random 
number =  random.randint(0, 100)  
tries = 1 

def check(guess):
    try:
        guess = int(guess)
        return guess
    except ValueError:
        print("that is not a number")
        return None

def none(guess) : 
    while guess is None : 
        guess = check(input("please input a number\n"))
    return guess 

guess = none(check(input("I'm thinking of a number try to guess it in ten tries\n"))) 

while tries != 11 :
    if 0 <= guess <= 100 : 
        if guess == number : 
            if tries == 1 : 
                print("congrats, you guessed right on the first try") 
                break 
            else : 
                print("you guessed correct") 
                print(f"it took you {tries} tries") 
                break
        elif guess != number : 
            if tries == 10 : 
                print("you have failed to guess the number") 
                print("better luck next time :)")
                tries += 1 
            elif tries == 9 : 
                tries += 1 
                guess = none(check(input("last guess\n"))) 
            else : 
                if number < guess : 
                    print("too high, try lower")
                elif number > guess :  
                    print("too low, try higher")
                tries += 1 
                guess = none(check(input("guess again\n"))) 
    elif guess < 0 or guess > 100 :
        print("the number is between 0 and 100 btw") 
        guess = none(check(input("try guessing again, right this time\n"))) 
