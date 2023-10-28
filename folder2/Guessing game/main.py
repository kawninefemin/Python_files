import random

def guess (x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess < random_number:
            print("Sorry, the number is too low. Try again!")
        elif guess > random_number:
            print("Sorry, the number is too high. Try again!")
    print(f"Yay! You got the number {random_number} right! Great Job.")

guess(15)