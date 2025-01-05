-FORT BOYAD SIMULATOR-
Gaspard LIESKE, Louis GONIE

This goal of this project is to create a game on python based on the tv game "Fort Boyard", to help us we have been provided with a document with instrunction to follow.

This project was made using only python. Multiplle libraries were used:<br />
math, random : for the games<br />
time : for visual effects<br />
json, os : to pull data from elsewhere<br />

To launch the game you need to get the code on git hub pull and run main file

The game function with a series of sub game you must win a certain nuber of them in onder to try the final challenge and win the game, the sub games are:

-Maths challenges, Logical challenges, Chance challenges, Pere Fouras riddles and the Final challenge
Each challenge has mutliple game and a one of each game is chosen when you start a challenge, these are the function:
These are the funtions for the random game :

-shell_game() : it runs the shell game <br />
-roll_dice_game() : run the roll dice game<br />
-chance_challenge() : choose and run one of the 2 games randomly<br />

These are the funtions for the battle ship game :

-next_player(player) : #switch to the next player<br />
-empty_grid() #initalize an empty grid of size 3x3<br />
-display_grid(grid, message) #display the grid<br />
-ask_position() #ask a position to the player and ensure that the position is valid<br />
-initialize() # initialize the player grid by creating a empty grip and asking were to place the 2 boats to the player<br />
-turn(player, player_shots_grid, opponent_grid, playerturn) #this function run a turn<br />
-has_won(player_shots_grid) #checks if all the boats in the given grid are sunk<br />
-battleship_game() #main game function, run the game<br />

These are the funtions for the maths game :

-factorial(n) #compute the factorial of n<br />
-math_challenge_factorial() #factorial challenge, execute the challenge<br />
-is_prime(n) #uses a mathematical definition to determine if n is prime<br />
-nearest_prime(n) #determine the nearest prime of n return a tuple<br />
-math_challenge_prime() #prime challenge game function, launch the game<br />
-math_roulette_challenge() #math roulette challenge<br />
-math_challenge() #select randomly a challenge among all<br />

These are the funtions for the Pere Fouras riddles :

-load_riddles(file) #load the riddles<br />
-pere_fouras_gateux() #beaucause Mr Fourras is quite old sometime he forget what he is doing and throws the key at the player<br /> 
-pere_fouras_riddles(file) execute the game<br />

These are the function of utilie, they help the players register and play:

-introduction() #print a welcoming message and the rules<br />
-compose_equipe() #used to create equipes<br />
-challenges_menu() #display a menu to choose a challenge number<br />
-choose_player(team) #display a menu of all the players in the team to choose one<br />
-save_game<br />


This is the function that launches the game:

-game()
