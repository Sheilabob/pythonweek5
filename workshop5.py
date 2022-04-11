import random


def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop+1)
    while tries != 0:
        print("Number of tries left:", tries)
        guess = input(f"Guess a number between {start} and {stop}:")
        if int(guess) == random_number:
            print("You guessed the correct number!")
            return
        elif start-1 < int(guess) < random_number:
            print("Guess higher!")
            tries -= 1
        elif stop+1 > int(guess) > random_number:
            print("Guess lower!")
            tries -= 1
        else:
            print("Your number must be between", start, "and", stop)
    print("You have failed to guess the number:", random_number)


guess_random_number(5, 0, 10)
