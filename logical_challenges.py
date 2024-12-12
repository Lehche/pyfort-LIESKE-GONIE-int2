def empty_grid():
    return [[" " for _ in range(3)] for _ in range(3)]

def display_grid(grid, message):
    print(message)
    for row in grid:
        print("|".join(row))
        print("-" * 5)

def ask_position():
    while True:
        try:
            position = input("Enter the position (row,column) between 1 and 3 (e.g., 1,2): ")
            row, col = map(int, position.split(","))
            if 1 <= row <= 3 and 1 <= col <= 3:
                return row - 1, col - 1
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid format. Please enter in row,column format.")

def initialize():
    grid = empty_grid()
    for i in range(2):
        print(f"Place boat {i + 1}")
        while True:
            row, col = ask_position()
            if grid[row][col] == " ":
                grid[row][col] = "B"
                break
            else:
                print("Position already occupied. Choose another.")
    return grid

def turn(player, player_shots_grid, opponent_grid):
    display_grid(player_shots_grid, "Your shots so far:")
    if player == 0:
        print("It's your turn to shoot!")
        row, col = ask_position()
    else:
        print("The game master is shooting!")
        row, col = random.randint(0, 2), random.randint(0, 2)

    if opponent_grid[row][col] == "B":
        print("Hit!")
        player_shots_grid[row][col] = "X"
        opponent_grid[row][col] = "X"
    else:
        print("Miss!")
        player_shots_grid[row][col] = "."

def has_won(player_shots_grid):
    hits = sum(row.count("X") for row in player_shots_grid)
    return hits == 2

def battleship_game():
    print("Each player must place 2 boats on a 3x3 grid.")
    player_grid = initialize()
    game_master_grid = empty_grid()
    for _ in range(2):
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if game_master_grid[row][col] == " ":
                game_master_grid[row][col] = "B"
                break
    player_shots_grid = empty_grid()
    game_master_shots_grid = empty_grid()

    player = 0
    while True:
        if player == 0:
            turn(player, player_shots_grid, game_master_grid)
            if has_won(player_shots_grid):
                print("You sank all the boats! You win!")
                return True
        else:
            turn(player, game_master_shots_grid, player_grid)
            if has_won(game_master_shots_grid):
                print("The game master sank all your boats! You lose!")
                return False
        player = 1 - player


battleship_game()
