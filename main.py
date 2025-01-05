#this is the main file
#here there is : the executor of the code and the game function
#this file launch the code
import time


from logical_challenges import battleship_game
from math_challenges import math_challenge
from chance_challenges import chance_challenge
from pere_fouras_challenge import pere_fouras_riddles
from utility_functions import introduction, compose_equipe, challenges_menu, choose_player, save_game
from final_challenge import treasure_room

def game():  # function that launches the game just have to execute it
    # Introduction and team composition
    introduction()
    ListOfPlayers = compose_equipe()
    Keys = 0
    Tries = {"Math challenges": 0, "Logic challenges": 0, "Chance challenges": 0, "Fourras riddles": 0}
    attempts = 0

    # Event loop
    while Keys < 3:
        Challenge = challenges_menu()
        Player = choose_player(ListOfPlayers)  # Player : index#

        print(f"{ListOfPlayers[Player]['name']} it is your turn!")
        if Challenge == 0:
            Won = math_challenge()
            attempts += 1
            Tries["Math challenges"] += 1
        elif Challenge == 1:
            Won = battleship_game()
            attempts += 1
            Tries["Logic challenges"] += 1
        elif Challenge == 2:
            attempts += 1
            Won = chance_challenge()
            Tries["Chance challenges"] += 1
        elif Challenge == 3:
            attempts += 1
            Won = pere_fouras_riddles("DATA/PFRiddles.json")
            Tries["Fourras riddles"] += 1

        if Won:
            Keys += 1  # Add keys to the player
            ListOfPlayers[Player]["keys_wons"] += 1
            print(f"One more Key for your team, you have {Keys} Keys")
        else:
            print(f"No keys for you this time, you have {Keys} Keys")
        time.sleep(1.5)

    # Final stage
    if Keys > 2:
        if treasure_room("DATA/TRClues.json") == True:
            print("\n", "The Game is over congrats you won!")
            print("The End")
        else:
            print("\n", "The Game is over but you lost")
            print("The End")
            print("Fortunately you all get the consolation prize which is a Roomba robot vacuum and 2 weeks of Spotify Premium!")

    save_game(ListOfPlayers, Keys, Tries, attempts)  # Pass dictionary directly



game()
