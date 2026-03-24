import random

def play_game():
    print("Rock Paper Scissors Game")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")


    choice = int(input("Enter your choice (1-3): "))

    
    if choice == 1:
        user = "Rock"
    elif choice == 2:
        user = "Paper"
    elif choice == 3:
        user = "Scissors"
    else:
        print("Invalid choice")
        return

    print("You chose:", user)

    
    comp = random.choice(["Rock", "Paper", "Scissors"])
    print("Computer chose:", comp)


    if user == comp:
        print("It's a Draw!")
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissors" and comp == "Paper"):
        print("You Win!")
    else:
        print("Computer Wins!")

play_game()