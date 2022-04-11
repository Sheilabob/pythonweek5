import random


def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)
    prev_guesses = []

    while tries != 0:
        print("Number of tries left:", tries)
        guess = input(f"Guess a number between {start} and {stop}:")
        is_prev_guess = False
        if len(prev_guesses) >= 1:
            lower_bound = 0
            upper_bound = len(prev_guesses) - 1

            while lower_bound <= upper_bound:
                pivot = (lower_bound + upper_bound) // 2
                pivot_value = prev_guesses[pivot]

                if pivot_value == guess:
                    is_prev_guess = True
                if pivot_value > guess:
                    upper_bound = pivot - 1
                else:
                    lower_bound = pivot + 1
        if is_prev_guess == True:
            print("You have already guessed that number.  Try again")
            continue

        prev_guesses.append(guess)
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
    random_number = random.randint(start, stop)
    print("The number for the program to guess is:", random_number)
    for guess in range(start, stop+1):
        print("Number of tries left:", tries)
        print("The program is guessing", guess)
        if guess == random_number:
            print("The program has guessed the correct number!")
            return True
        tries -= 1
        if tries <= 0:
            print("The program has failed to guess the correct number.")
            return False


def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(start, stop)
    print("Random number to find:", random_number)

    lower_bound = start
    upper_bound = stop

    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        print("Number of tries left:", tries)
        print("Current guess is:", pivot)

        if pivot == random_number:
            print("Found it!", random_number)
            return pivot
        tries -= 1
        if tries <= 0:
            print("The program has failed to find the number.")
            return

        if pivot > random_number:
            upper_bound = pivot-1
            print("Guessing lower!")
        else:
            lower_bound = pivot+1
            print("Guessing higher!")


def users_choice():
    tries = int(input("How many guesses would you like to allow?\t"))
    start = int(input("What is the lowest number you would like to include?\t"))
    stop = int(input("What is the largest number you would like to include?\t"))

    while True:
        print("\nHow would you like to play?")
        print("\t1. user guesses")
        print("\t2. computer guesses using a linear search")
        print("\t3. Computer guesses using a binary search")
        print("\t4. Exit")
        mode = input("Your Selection:\t")
        if mode == '1':
            guess_random_number(tries, start, stop)
        elif mode == '2':
            guess_random_num_linear(tries, start, stop)
        elif mode == '3':
            guess_random_num_binary(tries, start, stop)
        elif mode == '4':
            print("Goodbye")
            return
        else:
            print("\nSorry, that was not a valid selection.  Please try again")


def gamble_guess():
    money_pot = 10
    round = 1
    print("Gambling Mode")
    while True:
        while True:
            print(f"Round {round}:")
            print(f"Your current balance: {money_pot}")
            bet = input(
                "Do you think the computer can guess the correct number (y/n)?\t")
            if bet == 'y':
                bet = True
                break
            elif bet == 'n':
                bet = False
                break
            else:
                print("Sorry, that is not a valid option.  Please try again.")
        while True:
            if money_pot < 10:
                while True:
                    bet_amt = int(
                        input(f"How much do you want to bet, in whole dollar amounts, up to ${money_pot}?\t$"))
                    if bet_amt > money_pot or bet_amt <= 0:
                        print(
                            f"Your bet must be in whole dollar amounts up to ${money_pot}.  Please try again.")
                    else:
                        break
            elif money_pot >= 10:
                while True:
                    bet_amt = int(
                        input(f"How much do you want to bet, in whole dollar amounts, up to $10?\t$"))
                    if bet_amt > 10 or bet_amt <= 0:
                        print(
                            f"Your bet must be in whole dollar amounts up to $10.  Please try again.")
                    else:
                        break
            break
        round = guess_random_num_linear(5, 0, 10)
        if round == True and bet == True or round == False and bet == False:
            money_pot += bet_amt
        else:
            money_pot -= bet_amt
        if money_pot <= 0:
            print("Sorry, you have lost all your money!")
            break
        elif money_pot >= 50:
            print(
                "You have passed our maximum jackpot of $50: Game Over!  Thank you for playing!")
            break
        else:
            round += 1


# Driver Code Task 1
# guess_random_number(5, 0, 10)

# Driver Code Task 2
# guess_random_num_linear(5, 0, 10)


# Driver Code Task 3
# guess_random_num_binary(5, 0, 100)

# Driver Code Bonus 2
# users_choice()

# Driver Code Bonus 4
gamble_guess()
