my_dict = {}
print('''  ██████╗ ██╗██████╗ ██████╗ ██╗███╗   ██╗ ██████╗                                    
  ██╔══██╗██║██╔══██╗██╔══██╗██║████╗  ██║██╔════╝                                    
  ██████╔╝██║██║  ██║██║  ██║██║██╔██╗ ██║██║  ███╗                                   
  ██╔══██╗██║██║  ██║██║  ██║██║██║╚██╗██║██║   ██║                                   
  ██████╔╝██║██████╔╝██████╔╝██║██║ ╚████║╚██████╔╝                                   
  ╚═════╝ ╚═╝╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝   ''')


on = 1
while (on):
    a = input("what is your name ? ")
    b =int(input("enter the amount $"))
    my_dict[a] = b
    choice  = input("are there any other bidder type yes or no ").lower()
    if choice == "yes":
        on = 1
    elif choice == "no":
        on = 0
        
    else:
        print("enter a valid option")
        on = 0

highest = 0
for value in my_dict.values():
    if value > highest:
        highest = value
    else:
        pass

winner = None
for k , v in my_dict.items():
    if v == highest:
        winner = k

print(f"the winner is {winner} with bidding ${highest}")
my_dict.clear()
