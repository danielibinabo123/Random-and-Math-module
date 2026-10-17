import random
while True:
    user_action=input("enter a choice (rock, paper, scissors)")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"You chose {user_action}, computer chose {computer_action}.")

    if user_action == computer_action:
        print("its at tie")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("you win!")
        else:
            print(" you lose.")        

    elif user_action == "paper":
        if computer_action == "rock":
            print("you win!")
        else:
            print("you lose.")

    elif user_action == "scissors":
        if computer_action == "paper":
            print("you win!")
        else:
            print("you lose.")