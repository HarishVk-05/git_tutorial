choices = ["rock", "paper", "scissor"]

import random
from users_choice import user_choice
from com_choice import computer_choice


you = user_choice()
opp = computer_choice(choices)
print(f"you chose: {you}")
print(f"computer chose: {opp}")
if you == "rock" and opp == "scissor" or you == "paper" and opp == "rock" or you == "scissor" or opp == "paper":
    print("You win!")
elif you == "paper" and opp == "rock" or you == "rock" and opp == "paper" or you == "scissor" or opp == "rock":
    print("You lose!")
else:
    print("It's a draw!")
