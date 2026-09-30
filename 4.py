import random

CHOICES=["rock","paper","scissors"]

def get_computer_choice():
    return random.choice(CHOICES)

def get_user_choice():
    user_input=input("Enter  your choice (rock/paper/scissors):").strip().lower()
    while user_input not in CHOICES:
        print("Invalid choice! Please type rock,paper, or scissors.")
        user_input=input("Enter your choice(rock/paper/scissors):").strip().lower()
    return user_input

def decide_winner(user,computer):
    if user==computer:
        return "It`s a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

def play_game():
    print("="*40)
    print(" WELCOME TO ROCK , PAPER ,SCISSORS ")
    print("="*40)

    user_score=0
    computer_score=0
    rounds_played=0

    play_again="yes"

    while play_again =="yes":
        rounds_played +=1
        print(f"\n ---Round {rounds_played} ---")

        user_choice=get_user_choice()
        computer_choice=get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result=decide_winner(user_choice,computer_choice)
        print(result)

        if result == "You Win!":
            user_score += 1
        elif result == "Computer Wins!":
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again=input("\n Do you want to play again? (yes/no):").strip().lower()
        while play_again not in ("yes","no"):
            play_again=input("Please type 'yes' or 'no' :").strip().lower()

    print("\n" + "=" * 40)
    print("GAME OVER")
    print(f"Total Round Played: {rounds_played}")
    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations! You are the overall winnerr !!")
    elif user_score < computer_score:
        print("Better luck next time! Computer wins overall.")
    else:
        print("The game ended in an overall tie !")
    print("="*40)


if __name__ == "__main__":
    play_game()


