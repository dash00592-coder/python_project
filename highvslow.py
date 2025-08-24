celebrities = {
    "Maluma": {
        "description": "Musician",
        "country": "Colombia",
        "followers": 63000000
    },
    "9GAG": {
        "description": "Social media platform", 
        "country": "China",
        "followers": 58000000
    },
    "Cristiano Ronaldo": {
        "description": "Soccer player",
        "country": "Portugal", 
        "followers": 615000000
    },
    "Selena Gomez": {
        "description": "Singer and actress",
        "country": "USA",
        "followers": 429000000
    },
    "Kylie Jenner": {
        "description": "Reality TV star",
        "country": "USA",
        "followers": 399000000
    },
    "Dwayne Johnson": {
        "description": "Actor",
        "country": "USA",
        "followers": 397000000
    },
    "Ariana Grande": {
        "description": "Singer and actress",
        "country": "USA", 
        "followers": 380000000
    },
    "Kim Kardashian": {
        "description": "Reality TV star",
        "country": "USA",
        "followers": 364000000
    },
    "Lionel Messi": {
        "description": "Soccer player",
        "country": "Argentina",
        "followers": 502000000
    },
    "Beyoncé": {
        "description": "Singer",
        "country": "USA",
        "followers": 319000000
    },
    "Neymar": {
        "description": "Soccer player",
        "country": "Brazil",
        "followers": 218000000
    },
    "Justin Bieber": {
        "description": "Singer",
        "country": "Canada",
        "followers": 292000000
    },
    "Taylor Swift": {
        "description": "Singer",
        "country": "USA",
        "followers": 277000000
    },
    "Jennifer Lopez": {
        "description": "Singer and actress",
        "country": "USA",
        "followers": 252000000
    },
    "Nicki Minaj": {
        "description": "Rapper",
        "country": "Trinidad and Tobago",
        "followers": 226000000
    },
    "Kendall Jenner": {
        "description": "Model",
        "country": "USA",
        "followers": 294000000
    },
    "Billie Eilish": {
        "description": "Singer",
        "country": "USA",
        "followers": 110000000
    },
    "Drake": {
        "description": "Rapper",
        "country": "Canada",
        "followers": 144000000
    },
    "Virat Kohli": {
        "description": "Cricketer",
        "country": "India",
        "followers": 266000000
    },
    "Zendaya": {
        "description": "Actress",
        "country": "USA",
        "followers": 184000000
    }
}

import random
name = list (celebrities.keys())
on = 1
while(on):
    a = random.choice(name)
    name.remove(a)
    b = random.choice(name) 
    name.remove(b)
    choice = input (f" who has more followers {a} or {b} -> ").lower()
    if celebrities[a]["followers"] > celebrities[b]["followers"]:
        check = "a"
    else:
        check = "b"

    if choice == check:
        print("you won!")
    
    else:
        print("you lost!")
        exit()
    
    p = input("do you want to play again? y/n ->").lower() 
    if p == "y":
        on = 1
    elif p == "n":
        on = 0
    else:
        print("Invalid input. Please enter 'y' or 'n' .")
