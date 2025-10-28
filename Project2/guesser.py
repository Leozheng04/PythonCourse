import random 

def guess(x:int) -> None:
    num = random.randint(0,x)
    count  = 0
    print(f"Guess a number between 0 to {x}")
    guess = int(input("Enter your guess: "))
    while guess != num:
        if guess < num:
            print(f"The number is too small ! try again")
            guess = int(input("Enter your guess: "))
            count += 1
        else:
            print(f"The number is too large ! try again")
            guess = int(input("Enter your guess: "))
            count += 1
    print(f"congrulation, you win! You took {count} guesses")

def computerGuess(x:int) -> None:
    low = 1
    high = x
    feedback = ' '
    count = 0
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        print(f"The computer just took a guess. Is your number {guess} ?")
        feedback = input("Please enter 'H' is the number is too high, 'L' if the number is too low, and 'C' if the answer is correct: " ).lower()
        if (feedback == 'h'):
            high = guess - 1
        elif (feedback == 'l'):
            low = guess + 1
        count += 1
    print(f"The computer took {count} guesses")

    

computerGuess(50)