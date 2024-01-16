import random

# variables
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

# loop
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    # create random nr from 0-2 to represent random computer pick
    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == options[0] and computer_pick == options[2]:
      print("You won!")
      user_wins = user_wins + 1
    elif user_input == options[1] and computer_pick == options[0]:
        print("You won!")
        user_wins = user_wins + 1
    elif user_input == options[2] and computer_pick == options[1]:
        print("You won!")
        user_wins = user_wins + 1
    else:
        print("You lost!")
        computer_wins = computer_wins + 1



print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")