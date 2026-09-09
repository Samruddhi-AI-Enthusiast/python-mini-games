import random


def play_rps():
    choices = ["rock", "paper", "scissors"]

    player = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if player not in choices:
        print("Invalid choice!")

    elif player == computer:
        print("It's a draw! 🤝")

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win! 🎉")

    else:
        print("You lose! 😭")
