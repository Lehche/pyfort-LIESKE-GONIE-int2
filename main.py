from bato import battleship_game
from fune import math_challenge
from luck import chanve_challenge
from utility import introduction, compose_equipe, challenges_menu, choose_player


def game():
    #introduction and team composition
    introduction()
    ListOfPlayers = compose_equipe()
    Keys = 0

    #event loop
    Challenge = challenges_menu()
    Player = choose_player(ListOfPlayers)  #met son prenom uniquement

    print(f"{Player} it is your turn!")
    if Challenge == 0 :
        Won = math_challenge()
    elif Challenge == 1:
        Won = battleship_game()
    elif Challenge == 2:
        Won = chanve_challenge()
    elif Challenge == 3:
        #Won = pere_fouras_riddles(file)

    if Won == True :
        Keys += 1
        print(f"One more Key for your team, you have {Keys} Keys")
    else:
        print(f"No keys for you this time, you have {Keys} Keys")

    
    #final stage
    
