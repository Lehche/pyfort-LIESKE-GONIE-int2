#maths challenge file, every function about any maths challenge is here
import random
import time

def factorial(n): #compute the factorial of n and return it
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def math_challenge_factorial(): #factorial challenge, execute the challenge and return True/False if the game was won/lost
    #chooses a random number and welcomes the player
    number = random.randint(1, 10)
    print("Welcome to the factorial challenge")
    print("selecting number ...")
    time.sleep(1)
    print(f"Calculate the factorial of {number}.")

    #loop to manage wrong inputs
    while True:
        try:
            player_answer = int(input("Your answer: "))
            break
        except ValueError:
            print("Invalid input please enter an integer")

    #compute the correct answer
    correct_answer = factorial(number)

    #checks if the answer is True/False and return the result
    if player_answer == correct_answer:
        print("Correct! You win a key.")
        return True
    else:
        print(f"Wrong! The correct answer was {correct_answer}.")
        return False

def is_prime(n): #uses a mathematical definition to determine if n is prime of not (return True or False)
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):   #en gros ici ça fait entre 2 (pr éviter 1) jusqu'a la racine de n +1 (car python)
        if n % i == 0:             #check diviseur
            return False
    return True

def nearest_prime(n): #determine the nearest prime of n return a tuple : (nearest prime, 0) if there is only one nearest prime ; (nearest prime, 2nd nearest prime) if there is 2 nearest prime
    #determine the nearest prime by trying all the value both by increasing value and decreasing value of n
    w = n
    n += 1
    w -= 1
    while not( is_prime(n) or is_prime(w)):
        n += 1
        w -= 1

    #return one or both values in function of the distance of them from n
    if is_prime(n)== True and is_prime(w)== True:
        return (n, w) #retun les 2 (avec un tuple)
        #cas du 11
    elif is_prime(w)== True:
        return (w, 0)

    else :
        return (n, 0)



def math_challenge_prime(): #prime challenge function ,takes no input, launches the game return True/False if the player Won/lost the game
    #initialisation (chooses the random number and ensure that it is not prime)
    number = 11
    while is_prime(number) == True :
        number = random.randint(10, 20)

    #welcomes the player and give the info
    print("Welcome to the prime number challenge")
    time.sleep(0.5)
    print(f"Find the nearest prime number to {number}.")

    #loop handle invalid inputs from the player and ensure the value given is a valid one
    while True:
        try:
            player_answer = int(input("Your answer: "))
            break
        except ValueError:                      #anti erreur (bonus)
            print("Invalid input please enter an integer")

    #compute the correct answer
    correct_answers = nearest_prime(number)

    #checks if the answer given by the player is correct
    if correct_answers[1] == 0:
        correct_answer = correct_answers[0]
        if player_answer == correct_answer:
            print("Correct! You win a key.")
            return True
        else :
            print(f"Wrong! The correct answer was {correct_answer}.")
            return False
    else :
        if player_answer == correct_answers[1]:
            print("Correct! You win a key.")
            return True
        elif player_answer == correct_answers[0]:
            print("Correct! You win a key.")
            return True
        else :
            print(f"Wrong! The correct answer was {correct_answers[0]} or {correct_answers[1]}.")
            return False





def math_roulette_challenge():  #math toulette challenge, no input, launches the game return True/False if the player won/lost the game
    #chooses randomly the number and operation
    numbers = [random.randint(1, 20) for _ in range(5)]
    operation = random.randint(0, 2)

    #print a welcoming message and give the info
    print("welcome to the math roulette game")    #expliquer les regles
    print("rolling the barrel ...")
    time.sleep(1)                   #animation
    print("selecting operation ...")
    time.sleep(0.5)

    if operation == '0':
        correct_answer = sum(numbers)
        operation_name = "addition"
    elif operation == '1':
        correct_answer = numbers[0]
        for num in numbers[1:]:
            correct_answer -= num
        operation_name = "subtraction"
    else:
        correct_answer = 1
        for num in numbers:
            correct_answer *= num
        operation_name = "multiplication"

    print(f"Numbers on the roulette: {numbers}")
    print(f"Calculate the result by combining these numbers with {operation_name}.")

    #checks if the input given by the player is valid and handle errors
    while True:
        try:
            player_answer = int(input("Your answer: "))
            break
        except ValueError:
            print("Invalid input please enter an integer")

    #check if the answer is true/false and return that
    if player_answer == correct_answer:
        print("Correct answer! You've won a key.")

        return True #donne la clé
    else:
        print("BANG !")        #BANG !"
        time.sleep(1)
        print(f"Wrong answer! The correct answer was {correct_answer}.")

        return False

def math_challenge(): #select randomly a challenge among all the math challenges and execute it(with the return) (no input)
    challenges = [math_challenge_factorial, math_challenge_prime, math_roulette_challenge]
    challenge = random.choice(challenges)
    return challenge()
