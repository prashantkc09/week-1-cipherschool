#exercise , number guessing game
win=14
choice=0
while choice!= win:
    choice=int(input("Guess between 1 to 20: "))
    if choice<win:
        print("guess is low")
    elif choice>win:
        print("guess is high")
    else:
        print("Correct guess")