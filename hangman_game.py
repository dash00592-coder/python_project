import random

word_list = [
    "python", "computer", "programming", "developer", "keyboard",
    "internet", "hangman", "science", "mathematics", "engineering",
    "university", "challenge", "notebook", "software", "hardware",
    "machine", "learning", "artificial", "intelligence", "language"
]

print("Welcome to Hangman game!")

print(r''' _    _          _   _  _____ __  __          
| |  | |   /\   | \ | |/ ____|  \/  |   /\   | \ | |
| |__| |  /  \  |  \| | |  __| \  / |  /  \  |  \| |
|  __  | / /\ \ | . ` | | |_ | |\/| | / /\ \ | . ` |
| |  | |/ ____ \| |\  | |__| | |  | |/ ____ \| |\  |
|_|  |_/_/    \_\_| \_|\_____|_|  |_/_/    \_\_| \_|
''')


a = random.choice(word_list)
b = list(a) 
l = len(b)


display = ["_ "] * l

print("".join(display))  

for i in range(l):  
    choosen = input("Choose a letter: ").lower()
    
    if choosen in b:
        for j in range(l):
            if b[j] == choosen:
                display[j] = choosen
    else:
        print("Wrong guess!")
    
    print("".join(display))
