import random
from primePy import primes



def compare(random_number: int, user_guess: int) -> str:
    if random_number > user_guess:
     return(f"{user_guess} ist kleiner als die gesuchte Zahl")
    else:
     return(f"{user_guess} ist grösser als die gesuchte Zahl")

def divide(random_number, **kargs) -> str:
    'function description'

    if primes.check(random_number) == True:
        return("Die gesuche Zahl ist eine Primzahl")
    else:
        teiler = []
        for i in range(2, int(random_number/2)):
            if random_number % i == 0:
                teiler.append(i)
        return(f"Die gesucht Zahl ist durch {random.choice(teiler)} teilbar")   
     
def multiply(random_number, **kargs):
    vielfache = random_number * random.randint(2,10)
    return(f"Ein Vielfaches der gesuchten Zahl ist {vielfache}") 

def main():
    remaining_attempts = 5
    random_number = random.randint(1, 100)
    functions = [compare, multiply, divide]

    print("Dein Ziel ist es eine bestimmte Zahl zwischen 1 und 100 zu erraten. Du hast 5 Versuche")

    while remaining_attempts > 0:
        user_guess = int(input(f"\n{6-remaining_attempts}ter Versuch. Bitte gib eine Zahl ein:\n"))
        if random_number == user_guess:
            print("Glückwunsch. Du hast die Zahl erraten.")
            exit()
        remaining_attempts -= 1
        # my_dict = {
        # 'compare': compare(random_number=random_number, user_guess=user_guess),
        # 'multiply': multiply(random_number=random_number),
        # 'divide': divide(random_number=random_number)
        # }
        # print("Tipp: " + random.choice(list(my_dict.values())))
        print("Tipp: " + random.choice(functions)(random_number=random_number, user_guess=user_guess))

    print(f"du hast verloren. Die Zahl war: {random_number}")


if __name__=="__main__":
    main()
