#this is the logical challenge file everything about the battle ship game is here
import random

def next_player(player): #switch to the next player (imput : current turn[1/0]) return the next player index[1/0]
    if player == 1: #Game master
        return 0 #player
    else:
        return 1 #Game master

def empty_grid(): #initalize an empty grid of size 3x3 and return it as a 2D list (no input)
    return [["  " for _ in range(3)] for _ in range(3)]


def display_grid(grid, message): #display the grid (input : the grid list and a message a add[string]) (return nothing)
    #message display
    print(message)
    #grid display
    for row in grid:
        for cell in row:
            print("|", cell, end=" ")
        print("|")
    print("----------------")


def ask_position(): #ask a position to the player and ensure that the position is valid (no input) (return a tuple[row col]with the coordinates)
    #loop with error management code
    while True:
        try: #asking for the positon :
            pos = input("Enter the position (row,column) between 1 and 3 (e.g., 1,2): ").strip()  #.strip() to delete spaces
            row, col = map(int, pos.split(","))
            if 1 <= row <= 3 and 1 <= col <= 3:
                return (row - 1, col - 1)
            else:
                print("Position out of bounds. Try again.")
        except ValueError:
            print("Invalid input format. Try again.")

def initialize(): #(no input) initialize the player grid by creating a empty grip and asking were to place the 2 boats to the player (return the grid)
    # create an empty grid
    grid = empty_grid()

    #loop to ask and place the 2 boats
    for i in range(2):
        print(f"Place your boat {i + 1}")
        while True: #loop to handle cases of "non-cooperative" players (failsafe)
            row, col = ask_position()
            if grid[row][col] == "  ":
                grid[row][col] = "🚢" #ndt : the emojis are part of ascii code so they can work the same way as any other caracter
                break                               #kaße
            else:
                print("Position already occupied. Try again.")
    return grid

def turn(player, player_shots_grid, opponent_grid, playerturn): #this function run a turn(it can be the turn of the player as well as the GM)
    #input : the player index(0 : Player, 1 : GM) , Player_shots_grid : the grid were is displayed all the previous shots and hits but not the opponent boat, opponent_grid : the grid were the opponent boats are, playerturn : (0/1) current player turn
    #output :  nothing ( the list are modified directly in the function)

    if player == 0: #PLayer
        #if the player is the human prints a nice title and the previous shots history
        print("═" * 10 + " ✧･ﾟ: *✧･ﾟ:* 🚢⚓ BATTLESHIP ⚓🚢 *:･ﾟ✧*:･ﾟ✧ " + "═" * 10)
        print("═" * 10 + f"                   Turn N°{playerturn}                   " + "═" * 10)
        display_grid(player_shots_grid, "History of your previous shots:")

    #loop that used to manages cases were the player want to shoot in already tryed positions
    while True:
        if player == 0:  # player
            print("Player it is your turn to shoot")
            row, col = ask_position()

        else:  # GM
            print("The game MASTER moves")
            #randomly select the position for the Game master
            a = False
            while a == False: #ensure that the GM shoot in clear spots
                row, col = random.randint(0, 2), random.randint(0, 2)
                if opponent_grid[row][col] == "  " or opponent_grid[row][col] == "🚢":
                    a = True

            print(f"The game master shoots at position {row + 1},{col + 1}")





        if player_shots_grid[row][col] == "  ":    #checks if the player shooted in a spot he haven't tryed before
            #update the Grid
            if opponent_grid[row][col] == "🚢":
                print("Hit, sunk!")
                player_shots_grid[row][col] = "💥"
                opponent_grid[row][col] = "💥"
            else:
                print("Splash...")
                player_shots_grid[row][col] = "💦"
                opponent_grid[row][col] = "💦"
            if player == 1:
                #display to the player the progression of the GM tries
                display_grid(opponent_grid, "your grid :")
            break

        elif player == 0:
            print("You've already shot there. Try again.")


def has_won(player_shots_grid): #checks if all the boats in the given grid are sunk if they are return True else return False
     if sum(row.count("💥") for row in player_shots_grid) == 2 :
         return True
     else:
         return False


def battleship_game(): #main game function, takes no input, launches the game return True if the game was won, False if the game was lost
    #print welcoming message
    print("Each player must place 2 boats on a 3x3 grid.")
    print("Boats are represented by '🚢', missed shots by '💦', and sunk boats by '💥'.")

    #initialisation of the game
    print("Player, place your boats:")
    player_grid = initialize()
    display_grid(player_grid, "Here is your game grid with your boats:")
    game_master_grid = empty_grid()
    #put randomly the GM boats
    placed_boats = 0
    while placed_boats < 2:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if game_master_grid[row][col] == "  ":
            game_master_grid[row][col] = "🚢"
            placed_boats += 1

    # 2nd initialisation (shot grids)
    player_shots_grid = empty_grid()
    game_master_shots_grid = empty_grid()

    #starts the Game
    current_player = 0  # 0:player, 1:game master
    playerturn = 0 #cunt the number turn of the player
    while True: #game loop continues until the game end
        if current_player == 0: #player
            #execute the turn of the player and check if he won
            playerturn += 1
            turn(current_player, player_shots_grid, game_master_grid, playerturn)
            if has_won(player_shots_grid):
                print("Congratulations! You won!")
                return True
        else: #GM
            #execute the turn and check if the GM won
            turn(current_player, game_master_shots_grid, player_grid, playerturn)
            if has_won(game_master_shots_grid):
                print("The game master won! Better luck next time.")
                return False

        current_player = next_player(current_player)




