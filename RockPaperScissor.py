import random
user_choice = input("rock, paper or scissors? ")

computer = ["rock", "paper", "scissors"]
computer_choice = random.choice(computer)

if user_choice == "rock":

    if "rock" == computer_choice:
        print(f"The computer chose {computer_choice}")
        print("It is a draw")

    elif "scissors" == computer_choice:
        print(f"The computer chose {computer_choice}")
        print("You win")
    elif "paper" == computer_choice:
        print(f"The computer chose {computer_choice}")
        print("You Lose")

elif user_choice == "paper":

    if "rock" == computer_choice:
        print(f"The computer chose {computer_choice}")
        print("You win")

    elif "scissors" == computer_choice:
        print(f"The computer chose {computer_choice}")
        print("You Lose")

    elif "paper" == computer_choice:
        print(f"The computer chose {computer_choice}")
        print("it's a Draw")

elif user_choice == "scissors":

    if "rock" == computer_choice:
        print(f"The computer chose {computer_choice}")
        print("You Lose")

    elif "scissors" == computer_choice:
        print(f"The computer chose {computer_choice}")
        print("It's a draw")

    elif "paper" == computer_choice:
        print(f"The computer chose {computer_choice}")
        print("You Win")
else:
    print("Invalid option")