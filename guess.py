print('''+---------------------------------------------------+
|            WELCOME TO THE NUMBER GAME!            |
+---------------------------------------------------+
| I'm thinking of a number between 1 and 100.       |
| Can you guess it in the fewest tries possible?    |
+---------------------------------------------------+
|               HOW TO PLAY:                        |
| - Enter your guess when prompted.                 |
| - I'll tell you if it's HIGHER or LOWER.          |
| - Try to guess the number in as few tries as      |
|   possible!                                       |
+---------------------------------------------------+ ''')

import random

a = 1
b = 100
selected  = random.randint(a,b)
live  = 6

for i in range(1,7):
    guess = int(input("enter the number "))
    if guess == selected:
        print("you won!")
        exit()
    elif guess > selected:
        print("too high!")
    elif guess < selected:
        print("too low")
    live-= 1
    print(f"you have more {live} lives")
