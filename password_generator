import random
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
             'n','o','p','q','r','s','t','u','v','w','x','y','z']

uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
             'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+',
           '[',']','{','}',';',':',"'",'"','<','>','.',',','?','/','|','\\']

print ("welcome to the password generator ")

print(r"""
  ____                                _     ____                      
 |  _ \ __ _ ___ _____      _____  __| |   / ___| __ _ _ __ ___   ___ 
 | |_) / _` / __/ __\ \ /\ / / _ \/ _` |  | |  _ / _` | '_ ` _ \ / _ \
 |  __/ (_| \__ \__ \\ V  V /  __/ (_| |  | |_| | (_| | | | | | |  __/
 |_|   \__,_|___/___/ \_/\_/ \___|\__,_|   \____|\__,_|_| |_| |_|\___|
                                                                      
             🔑 Secure Password Generator 🔑
""")

a = int(input("how many lowercase letters do you want in your password? "))
b = int(input("how many uppercase letters do you want in your password? "))
c = int(input("how many numbers do you want in your password? "))
d = int(input("how many symbols do you want in your password? "))

password = []

for i in range(a):
    z = random.choice(lowercase)
    password.append(z)
    lowercase.remove(z)

for i in range(b):
    z = random.choice(uppercase)
    password.append(z)
    uppercase.remove(z)

for i in range(c):
    z = random.choice(numbers)
    password.append(z)
    numbers.remove(z)

for i in range(d):
    z = random.choice(symbols)
    password.append(z)
    symbols.remove(z)

random.shuffle(password)

print("".join(password))


