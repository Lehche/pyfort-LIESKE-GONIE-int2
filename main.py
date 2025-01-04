#this is the main file
#here there is : the executor of the code and the game function
#this file launch the code

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
    Challenge = challenges_menu()
    Player = ListOfPlayers[choose_player(ListOfPlayers)]  #met son prenom uniquement

    print(f"{Player["name"]} it is your turn!")
    if Challenge == 0 :
        Won = math_challenge()
    elif Challenge == 1:
        Won = battleship_game()
    elif Challenge == 2:
        Won = chance_challenge()
    elif Challenge == 3:
        Won = pere_fouras_riddles("PFRiddle.json")

    if Won == True :
        Keys += 1 #faire ajouter les clés aux joueur, mettre la boucle des challenges
        print(f"One more Key for your team, you have {Keys} Keys")
    else:
        print(f"No keys for you this time, you have {Keys} Keys")

    
    #final stage
    if treasure_room("TRClues.json") == True :
        print("\n", "The Game is over congrats you won !")
        print(f"number of keys obtained : {Keys}")
    else :
        print("\n", "The Game is over but you lost")
        print(f"number of keys obtained : {Keys}")
        print("fortunatly you all get the consolation prize witch is a roomba robot aspirator and 2 week of spotify premium !")

game()