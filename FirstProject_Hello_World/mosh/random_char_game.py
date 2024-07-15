import random
import time


# Function to play the game
def play_game():
    hearts = 3
    correct_count = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while correct_count < 5:
        # Choose a random character from the alphabet
        random_char = random.choice(alphabet)

        # Print the challenge to the user
        print(f"Type '{random_char}'")

        # Get user input within 1 second
        start_time = time.time()
        user_input = input("Press Enter to type the character: ").strip().lower()
        end_time = time.time()

        # Check if user input matches the random character and was entered within 1 second
        if user_input == random_char and end_time - start_time <= 2.5:
            print("Correct!")
            correct_count += 1
        else:
            hearts -= 1
            print(f"Incorrect or timeout! Hearts left: {hearts}")

            # Check if user has lost all hearts
            if hearts == 0:
                print("Game Over! You lost.")
                return

        # Pause for the user to press any key to continue
        input("Press Enter to continue...")

    print("Congratulations! You won.")


# Start the game
play_game()



