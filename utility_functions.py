#some utility functions used in main.py file
#introduction(), compose_equipe(), challenge_menu(), choose_player()

def introduction(): #print a welcoming message and the rules (take no imput, return no imput)
    print("Greeting adventurer here is the start of your glorious adventure !")

    #regles
    print("The player must complete challenges to earn keys and unlock the treasure room.")
    print("The aim is to collect three keys to access the treasure room.")

def compose_equipe(): #used to create equipes, take no input, return a list of dictionnaries ({name, profession, leader[True/False],keys_won})
    #imput of the number of players (gere les cas particuliers/erreurs)
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

    #asking the informations player per player
    leader = False
    listofplayers = []
    for player in range(numberofplayers) :
        identitycard = {} #le dictionnnaire
        print(f"for player {player + 1} :")
        identitycard["name"] = input("please enter your name : ")
        identitycard["profession"] = input("please enter your profession : ")

        if numberofplayers > 1: #si il y a q'un seul joueur, c'est lui le chef
            while True: #loop to handle errors + a check to verify there is only one leader per group
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

        #keys won initalisation (consant)
        identitycard["keys_wons"] = 0
        listofplayers.append(identitycard)

    if leader == False :        #special case : if no player claim the leader title ask who is the leader
        print("there is no leader in this team")
        player = -1
        while player == -1 :
            try :
                player = int(input("Please enter the leader number : "))

            except ValueError:
                print("please enter a number")
        listofplayers[player -1]["leader"] = True
    return listofplayers


def challenges_menu(): #display a menu to choose a challenge number (return : 0(math_challenge) 1(battleship_game) 2(chance_challenge) 3(perefourrasridddle)
    #display the menu for choosing a challenge
    print ("greeting adventurer, here are your choices")
    print("pick one challenge you must")
    print("thoses are the avalable challenges")
    print("1. Mathematics challenge")
    print("2. Logic challenge")
    print("3. Chance challenge")
    print("4. Père Fouras' riddle")

    #loop to compute the imput (handle errors)
    challenge = 0
    while challenge == 0 :
        try:
            challenge = int(input("Please enter your choice : "))
            if challenge > 4 :
                print("please enter a valid number")
                challenge = 0
        except ValueError:
            print("please enter a number")

    #return switch to return the selected challenge in the form of a number
    if challenge == 1:
        return 0  # math_challenge()
    elif challenge == 2:
        return 1  # battleship_game()
    elif challenge == 3:
        return 2  # chanve_challenge()
    elif challenge == 4:
        return 3  # pere_fouras_riddles(file)

def choose_player(team): #display a menu of all the players in the team to choose one, take the list of dictionnary created by compose_equipe and return the index of the selected player
    #loop that print the team composition
    for i in range(len(team)):
        print(f"{i+1}.", end=" ")
        print(team[i]["name"], end=" ")
        print(f"({team[i]["profession"]})", end=" - ")
        if team[i]["leader"] == True:
            print("Leader")
        else:
            print("Member")

    #loop to compute the user selection of player (handle errors)
    playernumber = -1
    while playernumber == -1 :
        try :
            playernumber = int(input("Enter the player's number: "))
            if playernumber > len(team) :
                playernumber = -1
        except ValueError:
            print("please enter a number")

    return(playernumber -1) #ndt the -1 is beacause python doesnt know how to count

def save_game_progress_to_text(progress_file="output/progress.txt"):

    keys = 0
    wins = 0
    losses = 0

    if not os.path.exists(os.path.dirname(progress_file)):
        os.makedirs(os.path.dirname(progress_file))

    with open(progress_file, "w", encoding="utf-8") as file:

        file.write("=== Team Information ===\n")
        for i, player in enumerate(team, start=1):
            leader_status = " (Leader)" if player.get("leader", False) else ""
            file.write(f"{i}. {player['name']} ({player['profession']}){leader_status}\n")
        file.write("\n")

        file.write("=== Challenges ===\n")
        file.write("Played Challenges:\n")
        if math_challenges() == True:
            keys += 1
            wins += 1
            file.write("- Math challenge\n")

        if battleship_game() == True:
            keys += 1
            wins += 1
            file.write("- Logical challenge\n")

        if chance_challenges() == True:
            keys += 1
            wins += 1
            file.write("- Chance challenge\n")


        file.write("\nNot Played Challenges:\n")
        if pere_fouras_riddles("DATA/PFRiddles.json") == True:
            losses += 1
            file.write("- Pere Fouras riddle\n")

        if math_challenges() == False:
            losses += 1
            file.write("- Math challenge\n")

        if battleship_game() == False:
            losses += 1
            file.write("- Logical challenge\n")

        if chance_challenges() == False:
            losses += 1
            file.write("- Chance challenge\n")


        if pere_fouras_riddles("DATA/PFRiddles.json") == False:
            losses += 1
            file.write("- Pere Fouras riddle\n")

        file.write("=== Game Progress ===\n")
        file.write(f"Total Keys Obtained: {keys}\n")
        file.write(f"Total Challenges Won: {wins}\n")
        file.write(f"Total Challenges Lost: {losses}\n")



