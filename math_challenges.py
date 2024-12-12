import random

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def math_challenge_factorial():
    number = random.randint(1, 10)
    print(f"Math Challenge: Calculate the factorial of {number}.")
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
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
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
        return w
    elif yn == yw:
        return f"{n}, {w}" #la il faut mettre les 2 pr que ça marche a corriger plus tard pr que le joueur n'aie qu'a mettre qi'un des 1
        #cas du 11
    else :
        return n



def math_challenge_prime():
    number = 11
    while is_prime(number) == True :
        number = random.randint(10, 20)

    print(f"Math Challenge: Find the nearest prime number to {number}.")
    player_answer = int(input("Your answer: "))
    correct_answer = nearest_prime(number)

    if player_answer == correct_answer:
        print("Correct! You win a key.(faire le retun key+1)")
        return True #donne la clé (a faire)
    else:
        print(f"Wrong! The correct answer was {correct_answer}.")
        return False

def math_roulette_challenge():
    numbers = [random.randint(1, 20) for _ in range(5)]
    operation = random.choice(['+', '-', '*'])

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
        print(f"Wrong answer! The correct answer was {correct_answer}.")
        return False

def math_challenge():
    challenges = [math_challenge_factorial, math_challenge_prime, math_roulette_challenge]
    challenge = random.choice(challenges)
    return challenge()

math_challenge()
