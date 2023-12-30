choices = ["rock", "paper", "scissor"]

import hello
import random
from users_choice import user_choice
from com_choice import computer_choice

hello.greeting()
you = user_choice()
opp = computer_choice(choices)
print(f"you chose: {you}")
print(f"computer chose: {opp}")
if you == "rock" and opp == "scissor" or you == "paper" and opp == "rock" or you == "scissor" and opp == "paper":
    print("You win!")
elif you == "rock" and opp == "paper" or you == "paper" and opp == "scissor" or you == "scissor" and opp == "rock":
    print("You lose!")
else:
    print("It's a draw!")
