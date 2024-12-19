import random

def next_player(player):            #[fait]
    if player == 1:
        return 0
    else:
        return 1

def empty_grid():
    return [["  " for _ in range(3)] for _ in range(3)]


def display_grid(grid, message):
    print(message)
    for row in grid:
        for cell in row:
            print("|", cell, end=" ")
        print("|")
    print("----------------")


def ask_position():
    while True:
        try:
            pos = input("Enter the position (row,column) between 1 and 3 (e.g., 1,2): ").strip()  #le .strip() c pr suprimer les espaces
            row, col = map(int, pos.split(","))
            if 1 <= row <= 3 and 1 <= col <= 3:
                return (row - 1, col - 1)
            else:
                print("Position out of bounds. Try again.")
        except ValueError:
            print("Invalid input format. Try again.")

def initialize():
    grid = empty_grid()
    for i in range(2):
        print(f"Place your boat {i + 1}")
        while True:
            row, col = ask_position()
            if grid[row][col] == "  ":
                grid[row][col] = "🚢"
                break                               #kaße
            else:
                print("Position already occupied. Try again.")
    return grid

def turn(player, player_shots_grid, opponent_grid, playerturn):    #ndt : le player et l'opponent change en focntion du tour
    if player == 0:
        print("═" * 10 + " ✧･ﾟ: *✧･ﾟ:* 🚢⚓ BATTLESHIP ⚓🚢 *:･ﾟ✧*:･ﾟ✧ " + "═" * 10)
        print("═" * 10 + f"                   Turn N°{playerturn}                   " + "═" * 10)

        display_grid(player_shots_grid, "History of your previous shots:")

    while True:
        if player == 0:  # player

            print("Player it is your turn to shoot")
            row, col = ask_position()

        else:  # GM
            print("The game MASTER moves")
            a = False
            while a == False:
                row, col = random.randint(0, 2), random.randint(0, 2)
                if opponent_grid[row][col] == "  " or opponent_grid[row][col] == "🚢":
                    a = True

            print(f"The game master shoots at position {row + 1},{col + 1}")





        if player_shots_grid[row][col] == "  ":    #failsafe pr le joueur

            if opponent_grid[row][col] == "🚢":
                print("Hit, sunk!")
                player_shots_grid[row][col] = "💥"
                opponent_grid[row][col] = "💥"
            else:
                print("Splash...")
                player_shots_grid[row][col] = "💦"
                opponent_grid[row][col] = "💦"
            if player == 1:
                display_grid(opponent_grid, "your grid :")
            break

        elif player == 0:
            print("You've already shot there. Try again.")


def has_won(player_shots_grid):
     if sum(row.count("💥") for row in player_shots_grid) == 2 :
         return True
     else:
         return False


def battleship_game():
    print("Each player must place 2 boats on a 3x3 grid.")
    print("Boats are represented by '🚢', missed shots by '💦', and sunk boats by '💥'.")

    #initializafion
    print("Player, place your boats:")
    player_grid = initialize()                      #ajouter option pour placer ses bateau au pif
    display_grid(player_grid, "Here is your game grid with your boats:")

    game_master_grid = empty_grid()
    #les bateau du méchant sont mis au pif
    placed_boats = 0
    while placed_boats < 2:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if game_master_grid[row][col] == "  ":
            game_master_grid[row][col] = "🚢"
            placed_boats += 1

    # 2nd initialisation (les shot grid)
    player_shots_grid = empty_grid()
    game_master_shots_grid = empty_grid()

    current_player = 0  # 0:player, 1:game master
    playerturn = 0
    while True:
        if current_player == 0:
            playerturn += 1
            turn(current_player, player_shots_grid, game_master_grid, playerturn)
            if has_won(player_shots_grid):
                print("Congratulations! You won!")
                return True
        else:
            turn(current_player, game_master_shots_grid, player_grid, playerturn)
            if has_won(game_master_shots_grid):
                print("The game master won! Better luck next time.")
                return False

        current_player = next_player(current_player)




