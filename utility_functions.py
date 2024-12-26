from itertools import filterfalse

from bato import battleship_game
from fune import math_challenge
from luck import chanve_challenge


def introduction():
    print("welcomming message") #mettre le message

    #regles
    print("The player must complete challenges to earn keys and unlock the treasure room.")
    print("The aim is to collect three keys to access the treasure room.")

def compose_equipe():

    #imput du nbr de player (gere les cas particuliers)
    numberofplayers = 0
    while numberofplayers < 1 :
        try :
            numberofplayers = int(input("how many players would you like to compose? "))
            if numberofplayers < 1 :
                print("please enter a valid number of players")
            elif numberofplayers > 3 :
                print("the maximum number of players is 3")
                numberofplayers = 0
        except ValueError:
            print("please enter a number")

    #remplissage des info
    leader = False
    listofplayers = []
    for player in range(numberofplayers) :
        identitycard = {} #le dictionnnaire
        print(f"for player {player + 1} :")
        identitycard["name"] = input("please enter your name : ")
        identitycard["profession"] = input("please enter your profession : ")

        if numberofplayers > 1: #si il y a q'un seul joueur, c'est lui le chef
            while True:
                answer = input("are you the team leader? (yes/no): ").lower()
                if answer == "yes":
                    if leader == False:
                        leader = True
                        identitycard["leader"] = True
                    else:
                        print("A leader has already been chosen.")
                    break
                elif answer == "no":
                    identitycard["leader"] = False
                    break
                else:
                    print("please enter yes or no")
        else :
            leader = True
            identitycard["leader"] = True


        identitycard["keys_wons"] = 0
        listofplayers.append(identitycard)

    if leader == False :        #si aucun des player n'a dit etre chef
        print("there is no leader in this team")
        player = -1
        while player == -1 :
            try :
                player = int(input("Please enter the leader number : "))

            except ValueError:
                print("please enter a number")
        listofplayers[player -1]["leader"] = True
    return listofplayers


def challenges_menu():
    print ("greeting adventurer, here are your choices")
    print("pick one challenge you must")
    print("thoses are the avalable challenges")
    print("1. Mathematics challenge")
    print("2. Logic challenge")
    print("3. Chance challenge")
    print("4. Père Fouras' riddle")
    challenge = 0
    while challenge == 0 :
        try:
            challenge = int(input("Please enter your choice : "))
            if challenge > 4 :
                print("please enter a valid number")
                challenge = 0
        except ValueError:
            print("please enter a number")

    if challenge == 1 :
        math_challenge()
    elif challenge == 2 :
        battleship_game()
    elif challenge == 3 :
        chanve_challenge()
    #elif challenge == 4 :
        #pere_fouras_riddles(file)   #verifier la file

def choose_player(team):
    for i in range(len(team)):
        print(f"{i+1}.", end=" ")
        print(team[i]["name"], end=" ")
        print(f"({team[i]["profession"]})", end=" - ")
        if team[i]["leader"] == True:
            print("Leader")
        else:
            print("Member")
    playernumber = -1
    while playernumber == -1 :
        try :
            playernumber = int(input("Enter the player's number: "))
            if playernumber > len(team) :
                playernumber = -1
        except ValueError:
            print("please enter a number")

    return(team[playernumber -1])

#mettre la bonus func ici



