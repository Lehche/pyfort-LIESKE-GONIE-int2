import random
import json
import time


def load_riddles(file):
    with open(file, "r") as f:
        riddles = json.load(f)
    return riddles


def pere_fouras_gateux():

    x = random.randint(1,10)
    if x == 6 :
        print("uhhhh ?")
        time.sleep(1)
        print("hmmmm", end=", ")
        time.sleep(0.7)
        print("where am I ?")
        time.sleep(0.5)
        print("WHO ARE YOU ?")
        time.sleep(0.63)
        print("GET OUT OF MY HOUSE !")
        time.sleep(1.5)
        print("The pere Fouras is confused and throws the key at your face")
        time.sleep(0.5)
        print("well done you've gotten another key")
        return True
    else :
        return False


def pere_fouras_riddles(file):

    attempts = 3
    riddles = load_riddles(file)
    selected_riddle = random.choice(riddles)

    if pere_fouras_gateux() == True:
        return True

    else:
        print(f"Riddle: ,\n{selected_riddle['question']}")
        correct_answer = selected_riddle['answer'].strip().lower()
        while attempts > 0:
            player_answer = input("Your answer: ").strip().lower()

            if player_answer == correct_answer:
                print("Correct! You've answered the riddle and earned a key.")
                return True
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Incorrect! You have {attempts} attempts remaining. Try again.")
                else:
                    print(f"Out of attempts! The correct answer was: {selected_riddle['answer']}")
                    return False
