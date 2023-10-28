# A simple memory test game using python
# You have to remember a series of strings and repeat them until you make a mistake
# The game will increase the difficulty by adding more strings as you progress

import random

# Define the possible strings
strings = ["Shakib", "Tamim", "Tanjim", "Mahmudullah", "Mostafiz", "Taskin", "Riyad", "Shanto"]

# Define the initial level and score
level = 1
score = 0

# Start the game loop
while True:
    # Print the level and score
    print(f"Level: {level}")
    print(f"Score: {score}")

    # Generate a random sequence of strings
    sequence = [random.choice(strings) for _ in range(level)]

    # Show the sequence to the user
    print("Remember this sequence:")
    print(" ".join(sequence))

    # Wait for a few seconds
    input("Press enter to continue...")

    # Clear the screen
    print("\n" * 50)

    # Ask the user to repeat the sequence
    print("Repeat the sequence:")
    answer = input().split()

    # Check if the answer is correct
    if answer == sequence:
        # Increase the level and score
        level += 1
        score += 10

        # Print a positive feedback
        print("Well done!")

    else:
        # End the game
        print("Sorry, that's wrong.")
        print(f"Your final score is {score}.")
        break
