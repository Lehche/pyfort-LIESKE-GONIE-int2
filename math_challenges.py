import random
import time

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def math_challenge_factorial():
    number = random.randint(1, 10)
    print("Welcome to the factorial challenge")
    print("selecting number ...")
    time.sleep(1)
    print(f"Calculate the factorial of {number}.")
    player_answer = int(input("Your answer: "))
    correct_answer = factorial(number)

    if player_answer == correct_answer:
        print("Correct! You win a key.(faire le retun key+1)")
        return True #donne la clé (a faire)
    else:
        print(f"Wrong! The correct answer was {correct_answer}.")
        return False

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):   #en gros ici ça fait entre 2 (pr éviter 1) jusqu'a la racine de n +1 (car python)
        if n % i == 0:             #check diviseur
            return False
    return True

def nearest_prime(n):
    w = n
    yn = 0    # compteurs
    yw = 0
    while not is_prime(n):
        n += 1
        yn += 1
    while not is_prime(w):
        w -= 1
        yw += 1
    if yw < yn :
        return (w, 0)
    elif yn == yw:
        return (n, w) #retun les 2 (avec un tuple)
        #cas du 11
    else :
        return (n, 0)



def math_challenge_prime():
    number = 11
    while is_prime(number) == True :
        number = random.randint(10, 20)

    print("Welcome to the prime number challenge")
    time.sleep(0.5)
    print(f"Find the nearest prime number to {number}.")
    player_answer = int(input("Your answer: "))
    correct_answers = nearest_prime(number)

    if correct_answers[1] == 0:
        correct_answer = correct_answers[0]
        if player_answer == correct_answer:
            print("Correct! You win a key.(faire le retun key+1)")
            return True
        else :
            print(f"Wrong! The correct answer was {correct_answer}.")
            return False
    else :
        if player_answer == correct_answers[1]:
            print("Correct! You win a key.(faire le retun key+1)")
            return True
        elif player_answer == correct_answers[0]:
            print("Correct! You win a key.(faire le retun key+1)")
            return True
        else :
            print(f"Wrong! The correct answer was {correct_answers[0]} or {correct_answers[1]}.")
            return False





def math_roulette_challenge():
    numbers = [random.randint(1, 20) for _ in range(5)]
    operation = random.choice(['+', '-', '*'])

    print("welcome to the math roulette game")    #expliquer les regles
    print("rolling the barrel ...")
    time.sleep(1)                   #animation
    print("selecting operation ...")
    time.sleep(0.5)

    if operation == '+':
        correct_answer = sum(numbers)
        operation_name = "addition"
    elif operation == '-':
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
    player_answer = int(input("Your answer: "))

    if player_answer == correct_answer:
        print("Correct answer! You've won a key.(faire le retun key+1)")

        return True #donne la clé
    else:
        print("BANG !")        #BANG !"
        time.sleep(1)
        print(f"Wrong answer! The correct answer was {correct_answer}.")

        return False

def math_challenge():
    challenges = [math_challenge_factorial, math_challenge_prime, math_roulette_challenge]
    challenge = random.choice(challenges)
    return challenge()

math_challenge()
