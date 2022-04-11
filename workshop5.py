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


def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop+1)
    print("The number for the program to guess is:", random_number)
    for guess in range(start, stop+1):
        print("Number of tries left:", tries)
        print("The program is guessing", guess)
        if guess == random_number:
            print("The program has guessed the correct number!")
            return
        tries -= 1
        if tries <= 0:
            print("The program has failed to guess the correct number.")
            return


# Driver Code Task 1
# guess_random_number(5, 0, 10)

# Driver Code Task 2
guess_random_num_linear(5, 0, 10)
