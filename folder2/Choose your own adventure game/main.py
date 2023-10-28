# A simple choose your own adventure text based python game
# You are a treasure hunter who is exploring an ancient temple
# You have to make choices to survive and find the treasure

# Define the possible choices
choices = ["left", "right", "forward", "back"]

# Define the scenes and their outcomes
scenes = {
    "entrance": {
        "text": "You are standing at the entrance of the Palace. There are two doors, one on the left and one on the "
                "right. Which one do you choose?",
        "left": "hallway",
        "right": "pitfall"
    },
    "hallway": {
        "text": "You enter a long hallway with torches on the walls. There is a door at the end of the hallway. Do you go forward or back?",
        "forward": "treasure",
        "back": "entrance"
    },
    "pitfall": {
        "text": "You open the door and fall into a pit of spikes. You are dead.",
        "end": True
    },
    "treasure": {
        "text": "You open the door and see a room full of diamond and jewels. You have found the treasure. You win!",
        "end": True
    }
}

# Define the current scene
current_scene = "entrance"

# Start the game loop
while True:
    # Print the scene text
    print(scenes[current_scene]["text"])

    # Check if the scene is an ending
    if scenes[current_scene].get("end", False):
        # Break the loop
        break

    # Get the user input
    choice = input("Choose one of these options: " + ", ".join(choices) + "\n").lower()

    # Validate the user input
    if choice not in choices:
        # Print an error message
        print("Invalid choice. Try again.")
        continue

    # Check if the choice is valid for the current scene
    if choice not in scenes[current_scene]:
        # Print an error message
        print("You can't go that way. Try again.")
        continue

    # Update the current scene
    current_scene = scenes[current_scene][choice]
