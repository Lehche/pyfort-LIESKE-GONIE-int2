import json
import random


def load_clues(file):
    with open(file, "r") as f:
        clues = json.load(f)
    return clues

def treasure_room(file):

    tv_game = load_clues(file)
    year = random.choice(list(tv_game["Fort Boyard"].keys()))
    show = random.choice(list(tv_game["Fort Boyard"][year].keys()))
    clues = tv_game["Fort Boyard"][year][show]["Clues"]
    code_word = tv_game["Fort Boyard"][year][show]["CODE-WORD"]

    print("Clues:", clues[:3])

    attempts = 3
    answer_correct = False

    while attempts > 0:
        player_answer = input(f"Guess the code word (Attempts left: {attempts}): ").strip().upper()

        if player_answer == code_word:
            answer_correct = True
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect. You have {attempts} attempts left.")
                print(f"Hint: {clues[-(4 - attempts)]}")
            else:
                print(f"You failed. The correct code word was: {code_word}")
                return False

    if answer_correct:
        print("Congratulations! You guessed the code word correctly.")
        return True
        #felindra tete de tigre


