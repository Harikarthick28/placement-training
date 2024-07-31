import random
def guess_number():
    number = random.randint(1, 10)
    guess = None
    while guess != number:
        guess = int(input("Guess the number (1-10): "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed it.")
guess_number()
