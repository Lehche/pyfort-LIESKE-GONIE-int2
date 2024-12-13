import random
import time

def shell_game():
    print("Welcome to the Shell Game!")
    print("Guess which shell (A, B, or C) hides the key.")

    shells = ['A', 'B', 'C']
    attempts = 2

    for attempt in range(attempts):
        key_position = random.choice(shells)
        guess = input(f"Attempt {attempt}/{attempts}: Choose a shell (A, B, or C): ").upper()

        if guess not in shells:
            print("Invalid choice. Please select A, B, or C.")
            continue

        if guess == key_position:
            print("Congratulations! You found the key!")
            return True
            break
        else:
            if attempt == attempts-1 :
                print(f"Wrong guess. The key was under the {key_position} shell.")
                print("Game over! Better luck next time.")
                break
            elif attempt < attempts :
                print(f"Wrong guess. The key was under the {key_position} shell.")
                print("reshuffling...")
                time.sleep(1)
                print("Try again!")
