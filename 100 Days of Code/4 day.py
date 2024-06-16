# Day 4 - randomisation and python lists

# coin flipper

import random

row1 = ["0", "0", "0"]
row2 = ["0", "0", "0"]
row3 = ["0", "0", "0"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal_position = int(position[0])
vertical_position = int(position[1])

map[vertical_position-1][horizontal_position-1] = "X"

print(f"{row1}\n{row2}\n{row3}")

# rock paper scissors

rock = "rock"
paper = "paper"
scissors = "scissors"

game_str = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
print(game_str[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose: {game_str[computer_choice]}")

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("You draw!")       