print("welcome to the treasure island")
print(r"""
                🏴‍☠️  TREASURE ISLAND 🏝️

                        ~ ~ ~ ~ ~ ~ ~
                     ~ ~             ~ ~
                  ~ ~      ^^^^        ~ ~
                ~ ~      ^^^^^^^^        ~ ~
              ~ ~       ^^^^^^^^^^         ~ ~
             ~ ~         ^^^^^^^^            ~ ~
              ~ ~         ^^^^^^            ~ ~
                ~ ~         ^^            ~ ~
                   ~ ~      (X)       ~ ~
                      ~ ~   /|\    ~ ~
                         ~ ~ | ~ ~
                            ~~~~~
                         ~~~~~~~~~~~
                      ~~~~~~~~~~~~~~~~~
                   ~~~~~~~~~~~~~~~~~~~~~~~
                       🌴        🌴
                     Palm Trees Protecting
""")

on = True
while(on):
    c_1 = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
    if c_1 == "left":
        c_2 = input("you are at river bank. There is an island in the middle of the river. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
        if c_2 == "wait":
            c_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
            if c_3 == "red":
                print("It's a room full of fire. Game Over.")
                on = False
            elif c_3 == "blue":
                print("You enter a room of beasts. Game Over.")
                on = False
            elif c_3 == "yellow":
                print("You found the treasure! You Win!")
                on = False
            else:
                print("You chose a door that doesn't exist. Game Over.")
                on = False
        else:
            print("You get attacked by an angry trout. Game Over.")
            on = False
