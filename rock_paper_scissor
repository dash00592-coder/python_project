print("welcome to rock paper scissor game")
option = ["rock", "paper", "scissor"]
choices = [
    r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]


print(choices[0])
print(choices[1])
print(choices[2])

import random 
user = int(input("enter 0 for rock, 1 for paper, 2 for scissor: "))
if user in [0,1,2]:
    print(f"you choose option {option[user]}")
    print(choices[user])
    computer = random.randint(0,2)
    print(f"computer chooses {option[computer]}")
    print(f"{choices[computer]}")

    if user == computer:
        print("It's a tie!")
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print("You win!")
    else:
        print("You lose!")
else:
    print("enter valid input")
