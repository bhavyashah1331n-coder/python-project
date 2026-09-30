"""
Numbers Guessing Game
-----------------------
A simple logical game in Python that demonstrates:
- Operators (comparison , arithmetic , logical)
- Conditional statements (if / elif / else)
- Looping structures (while loop , for loop)
- User interaction (input / output)

How to play:
The computer secretly picks a random number between 1 and 100.
The player has a limited number of attempts to guess it.
After every guess, the computer tells the player whether the guess was too high, too low, or correct, using comparison operators.
"""

import random

def get_player_guess():
    """
    Ask the player  to type a number and make sure it is valid.
    This function uses while loop so it keep asking until the player enters a proper whole number between 1 and 100.
    """

    while True:
        guess_text = input("Enter your guess (1-100):")

        if not guess_text.isdigit():
            print("Please enter a whole number,not text or symbols.")
            continue
        
        guess = int(guess_text)

        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.")
            continue

        return guess

def play_round(max_attempts=7):
    """
    Plays one full round of the guessing game.
    Returns True if the player wins, False if they run out of attempts.
    """
    secret_number = random.randint(1,100)
    attempts_used = 0

    print("\n I am thinking of a number between 1 and 100.")
    print(f"\n You have {max_attempts} attempts to guess it. Good luck!!")

    while attempts_used < max_attempts:
        attempts_used += 1
        print(f"--- Attempts {attempts_used} of { max_attempts} ---")
        guess = get_player_guess()

        if guess == secret_number:
            print(f"\n Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts_used} attempt(s). Well done !")
            return True
        elif guess < secret_number:
            difference = secret_number - guess
            if difference > 20:
                print("Too low! And not even close.")
            else:
                print("Too low! But you are getting warm.")

        else:
            difference = guess - secret_number
            if difference > 20:
                print("Too high! Way off.")
            else:
                print("Too hight! You are close though.")

        attempts_left = max_attempts - attempts_used
        if attempts_left > 0:
            print(f"\n Attempts left: {attempts_left}")

    print(f" Out of attempts! The correct number was {secret_number}.")
    return False

def main():
    """
    Main game loop. Lets the player play as many rounds as they like and keeps track of their score using si ple counters.
    """
    print("=" * 50)
    print(" WELCOME TO THE NUMBER GUESSING GAME ")
    print("=" * 50)

    round_played = 0
    round_won = 0

    keep_playing = True
    while keep_playing:
        round_played += 1
        won = play_round()

        if won:
            round_won += 1

        choice = input("\n Do you want to play again? (Yes/No):").strip().lower()
        keep_playing = choice in ("yes","y")

    print("\n" + "=" * 50)
    print("GAME OVER - FINAL SCORE")
    print(f"Round played : {round_played}")
    print(f"Round won : {round_won}")

    if round_played > 0:
        win_rate = (round_won / round_played) * 100
        print(f"Win rate    : {win_rate:.1f}%")

    print("Thanks for playing! Goodbyeee.")
    print("=" * 50)

if __name__=="__main__":
    main()

