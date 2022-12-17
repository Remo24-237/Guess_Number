import random

def guess(x):
    random_numdber=random.randint(1,x)
    userGuess = 0
    while userGuess != random_numdber:
        userGuess =int(input(f"Guess a number from 1 to {x}: "))
        if userGuess > random_numdber:
            print("Sorry, Incorrect. too high")
        elif userGuess < random_numdber:
            print("Sorry,Incorrect. too low")

    print(f"Congrats you guessed the number {random_numdber} correctly")

def computerGuess(x):
    low =1
    high=x
    feedback=""
    while feedback !="c" and low!=high:
        guess=random.randint(low,high)
        feedback=input(f"Is {guess} too high (H), too low (L), or correct (C)")
        if feedback=="h":
            high=guess -1
        elif feedback=="l":
            low=guess+1

    print(f"Yay The computer guessed your number {guess} correctly")

# guess(10) # running the guess function
# computerGuess(x)
