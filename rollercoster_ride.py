print ("Welcome to the roller coaster ride")
sum = 0
print(r"""
                     🎢 ROLLER COASTER 🎢

            ___        ___        ___        ___
         __/   \______/   \______/   \______/   \__
       _/                                             \_
     _/                                                 \__
   _/                                                     \_
  /                                                        \
  \                                                        /
   \__      ___                          ___           ___/
      \____/   \________________________/   \_________/   
                  |     [ o==o ]     |   <-- Cart         
                  |_________________|                     
""")
height = int(input("enter your height (in cm): "))
if height >120:
    print("you can have a ride")
    age = int(input("enter your age:"))
    if age >= 18:
        print("you have to pay $12 ")
        sum+=12
    elif age >=12 and age<18 :
        print("you have to pay $7 ")
        sum+=7
    else:
        print("you have to pay $5")
        sum+=5
    pic = input("you want pic ? Y or N : ").upper()
    if pic == "Y":
        sum+=3
        print("you have to pay $3 for pic ")
    else:
        pass
    print(f"your total bill is ${sum}")
    print("enjoy your ride !")
else:
    print("sorry you can't have a ride")
