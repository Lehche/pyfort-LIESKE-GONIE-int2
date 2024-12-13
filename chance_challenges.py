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
                
def roll_dice_game():
    attempts= 3

    for attempt in range(attempts):
        print(f"Attempt {attempt}/{attempts}")

        input("Press 'Enter' to roll the dice.")
        player = (random.randint(1, 6), random.randint(1, 6))
        print("You've rolled:... ")
        time.sleep(1)
        print(player)

        if 6 in player:
            print("Congratulations! You have won the game and found the key.")
            return True

        master = (random.randint(1, 6), random.randint(1, 6))
        print("Game master rolls:... ")
        time.sleep(1)
        print(master)

        if 6 in master:
            print("The game master has won the game.")
            return False

        if attempt < attempts-1:
            print("No one rolled a 6. Moving to the next attempt.\n")

    print("No player scored a 6 after three tries. It's a draw.")

def chanve_challenge():
    challenges = [shell_game, rollin_dice_game]
    challenge = random.choice(challenges)
    return challenge()
