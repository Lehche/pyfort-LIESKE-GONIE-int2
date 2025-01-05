#this is the main file
#here there is : the executor of the code and the game function
#this file launch the code
import time


from logical_challenges import battleship_game
from math_challenges import math_challenge
from chance_challenges import chance_challenge
from pere_fouras_challenge import pere_fouras_riddles
from  utility_functions import introduction, compose_equipe, challenges_menu, choose_player
from final_challenge import treasure_room

def game(): #function that launches the game just have to execute it
    #introduction and team composition
    introduction()
    ListOfPlayers = compose_equipe()
    Keys = 0

    #event loop
    while Keys < 3:
        Challenge = challenges_menu()
        Player = choose_player(ListOfPlayers)#Player : index#
        Tries = {"Math challenges": 0, "Logic challenges": 0, "Chance challenges": 0, "Fourras riddles": 0}
        attempts = 0

        print(f"{ListOfPlayers[Player]['name']} it is your turn!")
        if Challenge == 0 :
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

        if Won == True :
            Keys += 1 #faire ajouter les clés aux joueur, mettre la boucle des challenges
            ListOfPlayers[Player]["keys_wons"] += 1
            print(f"One more Key for your team, you have {Keys} Keys")
        else:
            print(f"No keys for you this time, you have {Keys} Keys")
        time.sleep(1,5)


    
    #final stage
    if Keys > 2  : #a retirer
        if treasure_room("DATA/TRClues.json") == True :
            print("\n", "The Game is over congrats you won !")
            print("The End")
        else :
            print("\n", "The Game is over but you lost")
            print("The End")
            print("fortunatly you all get the consolation prize witch is a roomba robot aspirator and 2 week of spotify premium !")

    save_game(ListOfPlayers, Keys, Tries, attempts)
