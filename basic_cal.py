operator = {
    "+": "sum",
    "-": "subtract",
    "*": "multiply",
    "/": "divide"
}


def sum(a, b):
    return a + b
def substract (a,b):
    return a - b
def multiply (a,b):
    return a*b
def divide(a,b):
    return a/b

print(r''' 
  _____________________
 |  _________________  |
 | |                 | |
 | |_________________| |
 |  ___ ___ ___   ___  |
 | | 7 | 8 | 9 | | + | |
 | |___|___|___| |___| |
 | | 4 | 5 | 6 | | - | |
 | |___|___|___| |___| |
 | | 1 | 2 | 3 | | x | |
 | |___|___|___| |___| |
 | | . | 0 | = | | / | |
 | |___|___|___| |___| |
 |_____________________| ''')

on  = 1
n1 = int(input("select a number -> "))
    
while(on):
    
    for i in operator:
        print (i)

    choice = input("select an operation : ")
    n2 = int(input("select another number -> "))
    if choice == "+" and choice in operator.keys():
        result = sum(n1,n2)
    elif choice == "-" and choice in operator.keys():
        result = substract(n1,n2)
    elif choice == "*" and choice in operator.keys():
        result = multiply(n1,n2)
    elif choice == "/" and choice in operator.keys():
        result = divide(n1,n2)
    else :
        print("invalid operation")

    print("Result:", result)

    select = input("do you want to continue?(y/n)").lower()
    if select == "y":
        n1 = result
    else:
        on = 0
